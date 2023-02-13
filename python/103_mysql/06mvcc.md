##### 参考

[8.0 mvcc 源码解析](https://blog.csdn.net/v123411739/article/details/108379583)

https://segmentfault.com/a/1190000037557620

https://blog.csdn.net/Waves___/article/details/105295060



## 事务

> 当每个事务开启时，都会被分配一个唯一的ID, 这个ID是递增的，所以最新的事务，ID值越大

##### 并发场景

```
读-读：不存在任何问题，也不需要并发控制 
读-写：有线程安全问题，可能会造成事务隔离性问题，可能遇到脏读，幻读，不可重复读 
写-写：有线程安全问题，可能会存在更新丢失问题
```

##### 并发问题

- 脏读

  ```
  Dirty Read: 
  当前事务未提交的数据被其他事务读取了, 如果当前事务回滚或修改了数据, 会导致其他事务数据不正确.
  ```

- 幻读

  ```
  Phantom Read: 在事务内, 同一 SELECT 多次读取范围内数据, 得到结果集不同. 侧重数据增加或减少.
  
  例如: 事务 1 查询了所有的数据, 此时事务 2 插入了新的数据, 事务 1 再次查询所有数据, 发现数据多了.
  ```

  | 事务 1                | 事务 2                                    |
  | --------------------- | ----------------------------------------- |
  | begin;                |                                           |
  | select * from person; |                                           |
  |                       | begin;                                    |
  |                       | insert into person (name) values ('Tom'); |
  |                       | commit;                                   |
  | select * from person; |                                           |
  | commit;               |                                           |

- 不可重复读

  ```
  Nonerepeatable Read: 在一个事务中两次读取同一个数据时，由于在两次读取之间，另一个事务修改了该数据，所以出现两次读取的结果不一致. 侧重数据被修改.
  
  例如: 事务 1 查询一条数据, 得到结果为 100, 此时事务 2 修改了这条数据为 200, 此时事务 1 再次读取时变为了200
  ```

##### 事务特性 ???

```
所有操作要么都成功, 要么什么都不做
事务具有四个特征：ACID
    原子性（ Atomicity ）: 所有操作要么都成功, 要么什么都不做
    一致性（ Consistency ）: 
    隔离性（ Isolation ）: 一个事务执行不能干扰其它事务
    持续性（ Durability）: 事务一旦提交, 对数据库中的数据的改变就应该是永久性的
```

##### 事务隔离级别

> 1. 查看事务隔离级别命令: 
>
> ​	show variables like 'transaction_isolation';
>
> 2. SQL 标准中规定的 RR 并不能消除幻读，但是 MySQL InnoDB 的 RR 可以，靠的就 Gap 锁。在 RR 级别下，Gap 锁是默认开启的，而在 RC 级别下，Gap 锁是关闭的

```
1. Read Uncommitted(读未提交)
最低隔离级别, 会读到其他事务未提交的内容, 查询语句不会加锁

2. Read Committed(读提交)
读取其他事务已提交的内容

3. Repeatable Read(可重复读)
同一事务多次读取同一个范围内的数据, 只返回第一次快照的结果集

4. Serializerable(串行化)
最高隔离级别, 顺序执行事务
```

|          | 脏读 | 不可重复读 | 幻读 |
| -------- | ---- | ---------- | ---- |
| 读未提交 | Y    | Y          | Y    |
| 读提交   | N    | Y          | Y    |
| 可重复读 | N    | N          | Y    |
| 串行化   | N    | N          | N    |

##### 快照读

- 快照读(SnapShot Read): 事务查询到的数据都是事务开始前已存在或事务自身写的数据.

- 快照读的前提是隔离级别不是串行级别，串行级别下的快照读会退化成当前读

- 快照读的实现是基于多版本并发控制

  ```sql
  -- 不加锁的简单的 SELECT 都属于快照读
  SELECT * FROM t WHERE id=1;
  ```

##### 当前读

- 当前读: 查询最新版本的记录，读取时还要保证其他并发事务不能修改当前记录，会对读取的记录进行加锁

  ```sql
  -- 加锁的 SELECT 就属于当前读
  SELECT * FROM t WHERE id=1 LOCK IN SHARE MODE;
  SELECT * FROM t WHERE id=1 FOR UPDATE;
  ```

## 隐藏字段

为了实现 MVCC，InnoDB 向每行记录增加三个字段

|             | 大小 byte |                                                              |
| ----------- | --------- | ------------------------------------------------------------ |
| DB_ROW_ID   | 6         | 自增ID（隐藏主键）, 如果数据表没有主键，InnoDB 会自动用该列产生一个聚簇索引 |
| DB_TRX_ID   | 6         | 记录插入或更新该行的最后一个事务的事务 ID                    |
| DB_ROLL_PTR | 7         | 回滚指针，指向 undo log                                      |
| DELETED_BIT | 1         | 记录被更新或删除并不代表真的删除，而是删除flag变了           |
| . . .       | . . .     | . . .                                                        |

## undo log

### 文件结构

##### Undo Tablespace

> 详细参考 https://zhuanlan.zhihu.com/p/453169285

```

mysql 有独立的表空间存储 undo log
8.0 版本 InnoDB 默认有 2 个 undo tablespace, 也可以使用 CREATE UNDO TABLESPACE 语句动态添加, 最大128个
每个 undo tablespace 至多有 TRX_SYS_N_RSEGS(128) 个回滚段
```

```
有 4 undo log 链表:
普通表 
```

### 基础

##### 是什么

- innoDB 记录每次修改之前的历史值, 用于事务回滚数据和mvcc. 在事务没提交之前，MySQL 会先记录更新前的数据到 undo log日志文件里面，当事务回滚时用 undo log 将数据恢复到事务开始之前的状态
- 最新的旧数据作为链表的表头，插在该行记录的 undo log 最前面
- SELECT 不会修改任何用户记录, 查询时不需要记录相应的undo log
- 分类
  - Insert undo log: 插入记录时, 把这条记录主键值记下来，回滚时把这个主键值对应的记录删除
  - Update undo log: 修改记录时, 把修改这条记录前的旧值都记录下来，回滚时把这条记录更新为旧值
  - Delete undo log: 删除记录时, 把这条记录中的内容都记下来，回滚时把由这些内容组成的记录插入到表中. 删除操作都只是设置记录的DELETED_BIT，并不真正将过时的记录删除。 为了节省磁盘空间，InnoDB 有专门的 purge 线程来清理 DELETED_BIT 为 true 的记录。为了不影响MVCC的正常工作，purge线程自己也维护了一个read view, 如果某个记录的DELETED_BIT为true，并且DB_TRX_ID相对于purge线程的read view可见，那么这条记录一定是可以被安全清除的。

```
undo log实际上就是存在rollback segment中旧记录链，
```

##### 创建数据

新增一条记录, DB_TRX_ID 使用当前的事务 ID, 同样会有 undo log 和 redo log

<img src=".\image\过程1.png" alt="过程1" style="zoom:85%;" />

##### 更新数据

- 事务 1 修改 name 为 Tom 
  1. 事务 1 修改该行数据时, 数据库先对该行加排他锁 

  2. 把该行数据拷贝到 undo log 作为旧记录
  3. 更新行记录, 修改该行 name 为 Tom, DB_ROW_ID  为当前事务 1 的 ID, DB_ROLL_PTR 指向拷贝到 undo log 的副本记录
  4. 事务提交后释放锁

<img src=".\image\过程2.png" alt="过程2" style="zoom:80%;" />

- 事务 2 修改该记录 age 为 30
  1. 在事务 2 修改该行数据时，数据库先对该行加排他锁 

  2. 把该行数据拷贝到 undo log 作为旧记录, 发现该行记录已经有 undo log, 那么最新的旧数据作为链表的表头，插在该行记录的 undo log 最前面
  3. 修改该行 age 为 30, DB_ROW_ID 为当前事务 2 的 ID, DB_ROLL_PTR 指向刚拷贝到 undo log 的副本记录
  4. 事务提交，释放锁

<img src=".\image\过程3.png" alt="过程3" style="zoom:80%;" />

##### 删除数据

```
删除在底层实现中使用更新. 

1. 写 undo log 中, 会通过 type_cmpl 来标识是删除还是更新, 并且不记录列的旧值
2. 这边不会直接删除，只会给行记录的 info_bits 打上删除标识（REC_INFO_DELETED_FLAG）, 之后会由专门的 purge 线程来执行真正的删除操作


???????
InnoDB 在 info_bits 中用一个标记位 delete_flag 标识是否删除。当我们在进行判断时，会检查下 delete_flag 是否被标记，如果是，则会根据情况进行处理：
1）如果索引是聚簇索引，并且具有唯一特性则返回 DB_RECORD_NOT_FOUND；
2）否则，会寻找下一条记录继续流程。
```

## read view

##### 是什么

- 保存事务 ID 的列表, 记录当前事务执行时, 系统中启动了但还没提交的事务. 用来判断当前事务能够看到数据的版本
  
  - RC在每次执行 select 时都会创建一个 read view
  
- RR 只在事务第一个 select 的时候创建一个 read view, 提交前一直使用该 ReadView，而不是事务开始的时候
  
    <img src=".\image\RR与RC区别.png" alt="RR与RC区别" style="zoom:80%;" />
  
    <img src=".\image\RR.png" alt="RR" style="zoom:80%;" />
  
- 属性
  - m_ids: 创建 ReadView 时, 系统当前所有未提交事务 ID 列表. 升序排列
  - m_up_limit_id: m_ids 中最小事务 ID
  - m_low_limit_id: m_ids 中最大事务 ID
  - m_creator_trx_id：创建该 ReadView 的事务的 ID

##### 比较算法

> 在进行判断时, 先拿记录的最新版本来比较, 如果无法被当前事务看到, 则通过记录的 DB_ROLL_PTR 找到上一个版本重新进行比较, 直到找到一个能被当前事务看到的版.

1. 如果行记录的 trx_id 与 m_creator_trx_id 相同, 表示记录是当前事务自己修改的
2. 如果行记录的 trx_id 小于 m_up_limit_id, 表示行记录在生成 read view 前已经提交, 可以被当前事务访问
3. 如果行记录的 trx_id 大于等于 m_low_limit_id, 表示行记录在 read view 后才提交, 不能被当前事务访问.
4. 如果行记录的 trx_id 在 m_up_limit_id 和 m_low_limit_id 之间, 需要判断 trx_id 是否在 m_ids 列表中. 使用二分查找.
   1. 如果在, 说明创建 read view 时, 生成该版本的事务还未提交, 当前事务无法访问
   2. 如果不在, 说明创建 read view 时, 生成该版本的事务已经提交, 当前事务可以访问该版本

```

```





## mvcc

##### 源代码(部分片段)

trx_sys_t: 整个事务的管理系统

```c
struct trx_sys_t {
    MVCC *mvcc;
    volatile trx_id_t max_trx_id;           /* 下一个事务被分配的ID */
    std::atomic<trx_id_t> min_active_id;    /* 最小的活跃事务ID */
    trx_id_t rw_max_trx_id;                 /* 最大的活跃事务ID */
    Rsegs rsegs;                            /* 回滚段 */
}
```

MVCC：MVCC 读取视图管理器

```c
class MVCC {
    public:
    /** 创建一个视图 */
    void view_open(ReadView *&view, trx_t *trx);
    /** 关闭一个视图 */
    void view_close(ReadView *&view, bool own_mutex);
    /** 释放一个视图 */
    void view_release(ReadView *&view);
    /** 判断视图是否处于活动和有效状态 */
    static bool is_view_active(ReadView *view) {
        ut_a(view != reinterpret_cast<ReadView *>(0x1));
        return (view != NULL && !(intptr_t(view) & 0x1));
    }
    private:
    typedef UT_LIST_BASE_NODE_T(ReadView) view_list_t;
    /** 空闲可以被重用的视图*/
    view_list_t m_free;
    /**  活跃或者已经关闭的 Read View 的链表 */
    view_list_t m_views;
};
```

ReadView

```c
class ReadView {
    private:
    trx_id_t m_low_limit_id;      /* 大于这个 ID 的事务均不可见 */
    trx_id_t m_up_limit_id;       /* 小于这个 ID 的事务均可见 */
    trx_id_t m_creator_trx_id;    /* 创建该 Read View 的事务ID */
    trx_id_t m_low_limit_no;      /* 事务 Number, 小于该 Number 的 Undo Logs 均可以被 Purge */
    ids_t m_ids;                  /* 创建 Read View 时的活跃事务列表 */
    m_closed;                     /* 标记 Read View 是否 close */
}
```



##### 解决并发问题方式

```
1. 数据库通常使用锁来实现隔离性, 最原生的锁, 锁住一个资源后会禁止其他任何线程访问同一个资源

2. 但是很多应用读多写少, 所以就使用了一种读写锁的方法. 使读锁和读锁之间不互斥，而写锁和写锁、读锁都互斥。这样就很大提升了系统的并发能力。

3. 并发读还是不够，又提出了读写之间也不冲突的方法. 读取数据时通过一种类似快照的方式将数据保存下来，这样读锁就和写锁不冲突了，不同的事务session会看到自己特定版本的数据.
```

##### 是什么

```
1. 多版本并发控制 Multiversion Concurrency Control, 简称 MVCC. 解决读-写冲突的无锁并发控制, 读指的是快照读, 而非当前读. 通过 3 个隐藏字段, undo log 和 read view 实现 mvcc
2. 通过保存数据在某个时间点的快照实现的.
2. 不管事务执行多长时间，事务内部看到的数据是不受其它事务影响. 根据事务开始的时间不同, 每个事务对同一张表, 同一时刻看到的数据可能是不一样
3. 解决脏读，幻读，不可重复读等事务隔离问题，但不能解决更新丢失问题
4. 只在可重复读和提交读两个隔离级别下工作, 其他两个隔离级别都和 MVCC 不兼容, 因为未提交读总是读取最新的数据行, 不符合当前事务版本的数据行. 串行化会对所有读取的行都加锁
```

```
MVCC + 悲观锁: MVCC解决读写冲突，悲观锁解决写写冲突
MVCC + 乐观锁: MVCC解决读写冲突，乐观锁解决写写冲突

乐观（optimistic）并发控制和悲观（pessimistic）并发控制
```

##### 示例

- 有 4 个事务

| 事务 1   | 事务 2   | 事务 3   | 事务 4       |
| -------- | -------- | -------- | ------------ |
| 事务开始 | 事务开始 | 事务开始 | 事务开始     |
|          |          |          | 修改且已提交 |
| 进行中   | 快照读   | 进行中   |              |

```
1. 事务 2 对某行数据执行快照读, 数据库为该行数据生成一个 Read View 读视图, 假设当前事务 ID 为 2
2. 此时还有事务 1 和 3 在活跃中, 事务 4 在事务 2 快照读前一刻提交更新了. 
3. 所以 Read View 记录了系统当前活跃事务 ID 是 1 和 3的ID
```

<img src=".\image\readview1.png" alt="readview1" style="zoom:80%;" />

```
事务 2 在快照读该行记录时, 会拿该行记录的 DB_TRX_ID 去跟 up_limit_id, low_limit_id 和 trx_list 比较, 判断事务 2 能看到该记录的版本
	1. 用该记录 DB_TRX_ID ID(4) 和 up_limit_id(1) 比较, 4 小于 up_limit_id(1), 不符合条件
2. 4 是否大于等于 low_limit_id(5)，也不符合条件，最后判断4是否处于trx_list中的活跃事务, 最后发现事务ID为4的事务不在当前活跃事务列表中, 符合可见性条件，所以事务4修改后提交的最新结果对事务2快照读时是可见的，所以事务2能读到的最新数据记录是事务4所提交的版本，而事务4提交的版本也是全局角度上最新的版本



```

<img src=".\image\readview2.png" alt="readview2" style="zoom:80%;" />

##### 可重复读隔离级别 InnoDB 的 MVCC 是如何工作

```
查询（SELECT）
InnoDB 会根据以下两个条件检查每行记录：

1. InnoDB只查找版本早于当前事务版本的数据行（也就是，行的系统版本号小于或等于事务的系统版本号），这样可以确保事务读取的行，要么是在事务开始前已经存在的，要么是事务自身插入或者修改过的。
2. 行的删除版本要么未定义，要么大于当前事务版本号 ??????
只有符合上述两个条件的记录，才能返回作为查询结果。


插入（INSERT）
InnoDB为新插入的每一行保存当前系统版本号作为行版本号。

删除（DELETE）
InnoDB为删除的每一行保存当前系统版本号作为行删除标识。
删除在内部被视为更新，行中的一个特殊位会被设置为已删除。

更新（UPDATE）
InnoDB为插入一行新记录，保存当前系统版本号作为行版本号，同时保存当前系统版本号到原来的行作为行删除标识。
```

##### mvcc 问题

```
数据库状态的快照适用于事务中的SELECT语句, 而不一定适用于所有DML语句
如果插入或修改某些行, 然后提交该事务, 则从另一个并发REPEATABLE READ事务发出的DELETE或UPDATE语句就可能会影响那些刚刚提交的行, 即使该事务无法查询它们。 如果事务更新或删除由不同事务提交的行, 则这些更改对当前事务变得可见


表中 id 为主键
事务 1 开始
事务 2 开始
事务 1 插入 id 为 100 的数据, 并 commit
事务 2 插入 id 为 100 的数据, 提示失败
```

## innodb

##### select

##### insert

##### delete

##### update

# 问题

```
mvcc 删除操作

mysql innodb 的 RR 为什么没有幻读



```


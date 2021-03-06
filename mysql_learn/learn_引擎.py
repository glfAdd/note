"""
https://www.cnblogs.com/IT-CPC/p/10883101.html


MyISAM
特点:
    1. 不支持事务
    2. 不支持外键
    3. 查询速度很快
    4. 对表进行加锁

支持3种不同的存储方式，分别是：静态表、动态表、压缩表
    1. 静态表：静态表的字段都是非变常类型的。优点是非常迅速，容易缓存，出现故障容易恢复；缺点是占用空间通常比动态表多（因为存储是会按照宽度定义补足空格）.
            在取数据时，会将数据后面的空格都去掉，如果数据后面本身有空格，那么也会被去掉
    2. 动态表：记录不是固定长度的，这样的优点时空间占用少；缺点：频繁的跟新，删除表易造成碎片，需要定期执行OPTIMIZE TABLE或者myisamchk-r命令来改善性能
    3. 压缩表：因为每个记录都是单独压缩的，所以只有非常小的访问开支


Memory
特点:
1. 使用内存当存储介质, 优点式响应速度快。
2. 当mySql进程崩溃的时数据会丢失
3. 存储的长度不变的数据

Memory索引支持
散列索引：散列索引的使用场景是数据查找时使用 == 匹配，但范围查询（<=, >=, <, >）较慢
B树索引：B树索引可以使用部分查询和通配查询，范围查询较快

Memory使用场景：
    1. 数据量小、访问非常频繁、在内存中存放数据，数据量过大会导致内存溢出。可以通过参数max_heap_table_size控制Memory表的大小，限制Memory表的最大的大小。
    2. 数据是临时数据，而且立即可用到。那么就比较合适存放在内存中。
    3. 存储在表中的数据如果丢失也没太大关系，不会造成损失。


InnoDB
特点:
    1. 更新多的表，适合处理多重并发的更新请求。
    2. 支持事务。
    3. 可以从灾难中恢复（通过bin-log日志等）。
    4. 外键约束。只有他支持外键。
    5. 支持自动增加列属性auto_increment。



Mylsam:
优点：系统兼容性好，属于查询速度贼快的那种。使用表格锁定的机制，来优化多个并发的读写操作。支持索引、字段管理
缺点：不支持事务、外键、如果数据库insert和update的操作比较多的话采用表锁效率低（建议使用innodb）、不能在表损坏后恢复数据
使用场景：想得到更好的系统兼容性，很高效的查询速度。但是这个东东不支持事务、外键、如果更新表较多的话对效率也会有影响。

Memory:
优点：数据访问快（使用内存做媒介），这是最大的特点
缺点：会占用服务器内存，如果内存非常紧张不推荐使用，而且数据可能会发送丢失，数据只能是临时数据，数据量不能太大，不然内存会溢出的。
使用场景：数据量小，访问频繁，数据丢失影响不大，是临时数据，而且立即可以使用，内存空间也比较宽松、

csv:
优点：数据存储为CSV文件格式，不用进行转换，可以对数据文件直接编辑
缺点：不支持索引，不能为空，不能自增
使用场景:适合做为数据交换的中间表（能够在服务器运行的时候，拷贝和拷出文件，可以将电子表格存储为CSV文件再拷贝到MySQL数据目录下，就能够在数据库中打开和使用。同样，如果将数据写入到CSV文件数据表中，其它web程序也可以迅速读取到数据。

Performace_Schema：
特点：系统内部使用，你也用不到。主要用于收集数据库服务器性能参数。



Federated：
优点：针对远程数据库实现、本地虚拟表与远程实体表之间是 TCP 长连接，并且是多个客户端利用的。所以不用担心因频繁建立连接带来的网络开销缺点：远程数据库仅限MySql、不支持： 事务、表结构修改、 alter table 命令
使用场景：针对远程数据库实现。

Archive：
使用场景：如果只有INSERT和SELECT操作，可以选择Archive，Archive支持高并发的插入操作，但是本身不是事务安全的。Archive非常适合存储归档数据，如记录日志信息可以使用Archive】

InnoDB
使用场景：如果要提供提交、回滚、崩溃恢复能力的事务安全（ACID兼容）能力，并要求实现并发控制，InnoDB是一个好的选择

InnoDB 和 MyISAM之间的区别：
    1. InnoDB支持事物，而MyISAM不支持事物
    2. InnoDB支持行级锁，而MyISAM支持表级锁
    3. InnoDB支持MVCC, 而MyISAM不支持
    4. InnoDB支持外键，而MyISAM不支持
    5. InnoDB不支持全文索引，而MyISAM支持。



where条件中避免出现!=,or,between,等东西，否则索引实效
"""

""" 事务
https://www.jianshu.com/p/75187e19faf2


所有操作要么都成功, 要么什么都不做


事务具有四个特征：ACID
原子性（ Atomicity ）: 所有操作要么都成功, 要么什么都不做
一致性（ Consistency ）: 
隔离性（ Isolation ）: 一个事务执行不能干扰其它事务
持续性（ Durability）: 事务一旦提交, 对数据库中的数据的改变就应该是永久性的



Mysql的四种隔离级别
1. Read Uncommitted（读取未提交内容）
    所有事务都可以看到其他未提交事务的执行结果
2. Read Committed（读取提交内容）
    一个事务只能看见已经提交事务所做的改变
3.Repeatable Read（可重读）
    MySQL默认
    同一事务的多个实例在并发读取数据时，会看到同样的数据行
4. Serializable（可串行化）
    在每个读的数据行上加上共享锁。在这个级别，可能导致大量的超时现象和锁竞争


四种隔离级别采取不同的锁类型来实现，若读取的是同一个数据的话，就容易发生问题
1. 脏读(Drity Read)：
    某个事务已更新一份数据，另一个事务在此时读取了同一份数据，由于某些原因，前一个RollBack了操作，则后一个事务所读取的数据就会是不正确的
2. 不可重复读(Non-repeatable read):
    在一个事务的两次查询之中数据不一致，这可能是两次查询过程中间插入了一个事务更新的原有的数据。
3. 幻读(Phantom Read):
    在一个事务的两次查询中数据笔数不一致，例如有一个事务查询了几列(Row)数据，而另一个事务却在此时插入了新的几列数据，先前的事务在接下来的查询中，就会发现有几列数据是它先前所没有的。

                    脏读      不可重复读       幻读
Read Uncommitted    V           V               V
Read Committed      X           V               V               
Repeatable Read     X           X               V
Serializable        X           X               X
"""

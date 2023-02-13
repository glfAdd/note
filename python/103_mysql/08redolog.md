##### 参考

https://blog.csdn.net/weixin_43213517/article/details/117457184

https://blog.csdn.net/mizepeng/article/details/124028904



##### 概念

脏页：修改过的数据页

page cache: 操作系统缓冲区

数据页: innodb 是以页为单位来管理存储空间的，任何的读写操作最终都会操作完整的一个页，会将整个页加载到 buffer pool中, 默认大小 16KB 

##### redo log 是什么

```
1. redo log 重做日志, InnoDB 存储引擎独有的日志, 记录在某个数据页上做了什么修改. 当 mysql 服务异常时确保已提交的事务持久化到磁盘

2. 事务中, 数据页修改都是在内存的 Buffer Pool 中, 事务提交后这些被修改后的脏页并不会立刻刷盘, 而是写入到 redo log 中, 修改数据都会生成 redo log, 保证 redo log 成功写入磁盘, 发生故障时可以根据磁盘上的 redo log 恢复

3. 数据页默认大小是16KB, 可能只修改该其中几 Byte 数据, 而且数据页刷盘是随机写，因为一个数据页对应的位置可能在硬盘文件的随机位置, 速度很慢

4. 如果是写 redo log, 一行记录可能就占几十 Byte，只包含表空间号、数据页号、磁盘文件偏移量、更新值，写入 redo log 是顺序写速度很快。之后再将修改刷盘.

5. 一个事物中可能会发生多次的数据修改，对应多个数据页, 产生多条 redo log, 这些 redo log 不能分开, 称为一个 group

6. redo log 分为多个 redo log buffer, 每个 buffer 默认 16mb, buffer 分为多个 block, 每个 block 512kb
```

##### redo log 刷盘策略

- 提供 3 种 刷盘策略, 参数 innodb_flush_log_at_trx_commit 
  - 设置为 0 的时候，不刷盘, 由后台线程来处理
  - 设置为 1 的时候，每次事务提交时刷盘（默认）
  - 设置为 2 的时候，每次事务提交时都只把 redo log buffer 内容写入 page cache(操作系统缓冲区), 只要操作系统不挂就没事，操作系统挂了，事务就无法保证

- InnoDB 引擎有一个后台线程每隔 1 秒就会把 redo log buffer 中的内容写到page cache, 然后调用 fsync 刷盘
- 当 redo log buffer 占用的空间即将达到 innodb_log_buffer_size 一半的时候，后台线程会主动刷盘

##### 日志文件组

- 硬盘上存储的 redo log 日志文件不只一个，而是以一个日志文件组的形式出现的，每个的redo日志文件大小都是一样的.
- 比如配置为一组 4 个文件，每个文件 1GB，整个 redo log 日志文件组可以记录 4G 的内容,  它采用的是环形数组形式，从头开始写，写到末尾又回到头循环写

<img src=".\image\日志文件组1.png" alt="日志文件组1" style="zoom:100%;" />

- 日志文件组属性
  - write pos: 是当前记录的位置，每次刷盘 redo log 记录到日志文件组中，write pos 位置就会后移更新
  - checkpoint: 是当前要擦除的位置，每次 MySQL 加载日志文件组恢复数据时，会清空加载过的 redo log 记录，并把 checkpoint 后移更新

<img src=".\image\日志文件组2.png" style="zoom:100%;" />

如果 write pos 追上 checkpoint ，表示日志文件组满了，这时候不能再写入新的 redo log 记录，MySQL 得停下来，清空一些记录，把 checkpoint 推进一下

![](.\image\日志文件组3.png)

##### redo log 结构

日志类型

```
简单的redo log 记录哪个表空间中的哪个页面从哪个位置开始的多少个节点要修改为什么

MLOG_1BYTE：在页面的某个偏移量处写入1字节的redo日志
MLOG_2BYTE：在页面的某个偏移量处写入2字节的redo日志
MLOG_4BYTE：在页面的某个偏移量处写入4字节的redo日志
MLOG_8BYTE：在页面的某个偏移量处写入8字节的redo日志
上面这4个类型的redo日志结构相同，只是具体数据的字节数不同
```

# 问题

```
数据页的大小

redo log 物理物理修改点
```


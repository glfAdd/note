"""
https://www.cnblogs.com/f-ck-need-u/archive/2018/05/08/9010872.html#auto_id_0


每一个操作在真正写入数据数据库之前,先写入到日志文件中
如要删除一行数据会先在日志文件中将此行标记为删除,但是数据库中的数据文件并没有发生变化.
只有在(包含多个sql语句)整个事务提交后,再把整个事务中的sql语句批量同步到磁盘上的数据库文件.



事务的隔离性是通过锁实现，
事务的原子性、一致性和持久性则是通过事务日志实现


innodb事务日志包括redo log和undo log
redo log: 重做日志，提供前滚操作
undo log: 回滚日志，提供回滚操作



"""

""" redo log
事务开启时, 事务中的操作, 都会先写入存储引擎的日志缓冲中, 在事务提交之前, 这些缓冲的日志都需要提前刷新到磁盘上持久化, 这就是"日志先行"(Write-Ahead Logging)
当事务提交之后, 在Buffer Pool中映射的数据文件才会慢慢刷新到磁盘. 
此时如果数据库崩溃或者宕机, 那么当系统重启进行恢复时, 就可以根据redo log中记录的日志，把数据库恢复到崩溃前的一个状态。未完成的事务，可以继续提交，也可以选择回滚，这基于恢复的策略而定。


redo log包括两部分
    - 内存中的日志缓冲(redo log buffer)，该部分日志是易失性的
    - 磁盘上的重做日志文件(redo log file)，该部分日志是持久的

innodb通过force log at commit机制实现事务的持久性，即在事务提交的时候，必须先将该事务的所有事务日志写入到磁盘上的redo log file和undo log file中进行持久化。

为了确保每次日志都能写入到事务日志文件中，在每次将log buffer中的日志写入日志文件的过程中都会调用一次操作系统的fsync操作(即fsync()系统调用)。
因为MariaDB/MySQL是工作在用户空间的，MariaDB/MySQL的log buffer处于用户空间的内存中。要写入到磁盘上的log file中(redo:ib_logfileN文件,undo:share tablespace或.ibd文件)，中间还要经过操作系统内核空间的os buffer，调用fsync()的作用就是将OS buffer中的日志刷到磁盘上的log file中。


undo log
记录了数据在每个操作前的状态，如果事务执行过程中需要回滚，就可以根据undo log进行回滚操作




"""







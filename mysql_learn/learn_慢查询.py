"""
学习网址
https://blog.csdn.net/qq_40884473/article/details/89455740


1. MySQL的慢查询，全名是慢查询日志，是MySQL提供的一种日志记录，用来记录在MySQL中响应时间超过阀值的语句。
2. 运行时间超过long_query_time值的SQL语句，则会被记录到慢查询日志中。默认值为10，意思是记录运行10秒以上的语句。
3. 默认情况下，MySQL数据库并不启动慢查询日志，需要手动来设置这个参数。 如果不是调优需要的话，一般不建议启动该参数，因为开启慢查询日志会或多或少带来一定的性能影响。
4. 慢查询日志支持将日志记录写入文件和数据库表。


参数
slow_query_log                  是否开启慢查询日志，1开启，0关闭。
log-slow-queries                旧版（5.6以下版本）MySQL数据库慢查询日志存储路径。可以不设置该参数，系统则会默认给一个缺省的文件host_name-slow.log
slow-query-log-file             新版（5.6及以上版本）MySQL数据库慢查询日志存储路径。可以不设置该参数，系统则会默认给一个缺省的文件host_name-slow.log
long_query_time                 慢查询阈值，当查询时间多于设定的阈值时，记录日志。
log_queries_not_using_indexes   未使用索引的查询也被记录到慢查询日志中（可选项）。
log_output                      日志存储方式。log_output='FILE'表示将日志存入文件，默认值是'FILE'。log_output='TABLE'表示将日志存入数据库。
















"""
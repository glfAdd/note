"""
https://www.cnblogs.com/f-ck-need-u/p/9001061.html#blog5



主要有5种日志文件：
    1. 错误日志(error log)：记录mysql服务的启停时正确和错误的信息，还记录启动、停止、运行过程中的错误信息。
    2. 查询日志(general log)：记录建立的客户端连接和执行的语句。
    3. 二进制日志(bin log)：记录所有更改数据的语句，可用于数据复制。
    4. 慢查询日志(slow log)：记录所有执行时间超过long_query_time的所有查询或不使用索引的查询。
    5. 中继日志(relay log)：主从复制时使用的日志。


"""
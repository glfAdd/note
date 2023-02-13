""" ============================ 正对IPv4的内核配置
追加到Linux /etc/sysctl.conf 文件中


net.core.netdev_max_backlog = 100000
每当网络接口接收数据包的速率毕内核处理这些包的速率快是, 允许发送到队列的数据包最大值.
Linux默认128
Nginx定义NGX_LISTEN_BACKLOG默认511


net.core.somaxconn = 100000
设置系统同时发起TCP连接数, 默认128偏小, 导致连接超时


net.ipv4.tcp_max_orphans = 100000
设置系统中最多允许存在多少TCP套接字不被关联到任何一个用户文件句柄上, 超过后没有与用户文件句柄连接的TCP套接字将复位
防止简单的DoS攻击


net.ipv4.tec_max_syn_backlog  = 123123
记录尚未收到客户端确认信息的连接请求最大数,


net.ipv4.tcp_timestamps = 0
用于设置时间戳, 正对Nginx通常设为0


net.ipv4.tcp_synack_retrise = 1
设置内核放弃TCP连接前向客户端发送SYN+ACK包的数量, 影响第二次握手
通常设为1, 即内核放弃连接之前发送1次SYN+ACK包


net.ipv4.tcp_syn_retrise = 1
内核放弃建立连接前发送SYN包的数量
通常设为1
"""

""" ============================ 针对CPU的Ngins配置优化
工作进程数
worker_processes 4;


设置每个进程分配CPU核心数
如果CUP核心数为4, worder_processes为8, 可以设置为
worker_cpu_affinity 0001 0010 0100 1000 0001 0010 0100 1000;
如果CUP核心数为4, worder_processes为8, 可以设置为
worker_cpu_affinity 00000001 00000010 00000100 00001000 00010000 00100000 01000000 10000000;
"""

""" ============================ 与网络相关Nginx配置
keepalive_timeout 120s 100s;
    

send_timeout 10s;
    Nginx和客户端建立连接之后, 服务器等待客户端超过10s就自动关闭连接.


client_header_buffer_size 4k;
    Nginx允许客户端请求头的缓冲区大小, 默认1KB
    当header过大时, 比如cookie中写入了较大的值, Nginx会返回400的错误


multi_accept on | off;
    每个nginx进程能否同时接收多个连接, 默认off
"""

""" ============================ 事件驱动模型相关配置
use method;
    用哪种事件驱动模型处理消息.select/poll/kqueue/epoll/etsig/eventport



"""

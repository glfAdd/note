""" ============================
不支持持久化
没有安全机制
多线程工作，而redis是单线程工作。
各个memcached服务器之间互不通信，各自独立存取数据，不共享任何信息。
服务器并不具有分布式功能，分布式部署取决于memcache客户端


内存key - value缓存
不支持持久化, 服务器关闭后数据全部丢失
没有安全机制
memcached实例之间没有通信机制
每个命令复杂度为 O(1)



完全基于内存操作的，是一个缓存系统，从本质它不是一个数据库系统，也不支持持久化



"""

""" ============================ 
https://www.runoob.com/memcached/memcached-install.html


安装
yum install memcached




启动参数
-d 是启动一个守护进程；
-m 是分配给Memcache使用的内存数量，单位是MB；默认64MB
-u 是运行Memcache的用户；
-l 是监听的服务器IP地址，可以有多个地址；
-p 设置TCP端口号(默认设置为: 11211)
-U UDP监听端口(默认: 11211, 0 时关闭) 
-c 是最大运行的并发连接数，默认是1024；
-P 是设置保存Memcache的pid文件。


启动命令
memcached -p 11211 -m 64m -d -u root



"""

""" ============================ 
默认端口11211
"""

""" ============================ 命令 
set             添加value, 如果有则替换
add             添加value, 如果有则不更新
replace         替换value, 如果没有则替换失败
append          往已有key的value后面追加
prepend         往已有key的value前面追加
cas             替换, 没有被其它客户端修改的情况下才写入
get             获取value, 没有返回空
gets            获取带有CAS令牌存的value, 没有则返回空
delete          删除key
incr/decr       对以后的value自增/自减
stats           返回PID 版本号 连接数
stats items     
stats slabs     显示各个slab的信息
stats sizes     显示所有item的大小和数量
flush_all       清楚所有内容


set key flags exptime bytes [noreply] 
value 
    key：键
    flags：可以包括键值对的整型参数，客户机使用它存储关于键值对的额外信息 。
    exptime：在缓存中保存键值对的时间长度（以秒为单位，0 表示永远）
    bytes：在缓存中存储的字节数
    noreply（可选）： 该参数告知服务器不需要返回数据
    value：存储的值（始终位于第二行）（可直接理解为key-value结构中的value）


memcached的内存是如何分配的
但是不是一开始就会直接向操作系统申请-m设置的内存。然后将内存分成多个page，一个page为1MB，每个page里面有多个固定大小的内存块chunk，其大小最小为96Bytes，最大为1MB，由增长因子来决定中间内存块的大小，每种大小的chunk对应一个slab class。当其中的一个大小的内存块所申请的page没有空间了，可以申请多一个大小的内存块page。所以最大的一个key+value不能超过1MB。内存分配策略叫做slab allocation
"""

""" ============================ telnet 
安装
yum install telnet

连接
telnet 127.0.0.1 11211


命令
o   open        使用 open hostname 可以建立到主机的 Telnet 连接。
c   close       使用命令 close 命令可以关闭现有的 Telnet 连接。
d   display     使用 display 命令可以查看 Telnet 客户端的当前设置。
sen send        使用 send 命令可以向 Telnet 服务器发送命令。支持以下命令：
ao          放弃输出命令。
ayt         “Are you there”命令。
esc         发送当前的转义字符。
ip          中断进程命令。
synch       执行 Telnet 同步操作。
brk         发送信号。
q   quit        退出telnet。

set         set                      设置选项(键入 'set ?' 获得列表)
st          status                   打印状态信息
u           unset                    解除设置选项(键入 'set ?' 获得列表)
?/h         help                     打印帮助信息
"""

""" ============================ stats
STAT pid 46673                   进程ID
STAT uptime 25336                服务器已运行秒数
STAT time 1494173893             服务器当前unix时间戳
STAT version 1.4.13              memcached版本号
STAT libevent 1.4.13-stable      libevent版本
STAT pointer_size 64             操作系统位数，64位
STAT rusage_user 0.642902        进程累计用户时间
STAT rusage_system 0.303953      进程累计系统时间
STAT curr_connections 10         当前打开连接数
STAT total_connections 25        memcached运行以来连接总数
STAT connection_structures 11    memcached分配的连接结构数
STAT reserved_fds 20             内部使用的FD数
STAT cmd_get 7                   执行get命令总数
STAT cmd_set 3                   执行set命令总数
STAT cmd_flush 0                 执行flush_all命令总数
STAT cmd_touch 0                 touch命令请求总数
STAT get_hits 3                  get命中次数
STAT get_misses 4                get未命中次数
STAT delete_misses 0             delete未命中次数
STAT delete_hits 1               delete命中次数
STAT incr_misses 0               incr未命中次数
STAT incr_hits 0                 incr命中次数
STAT decr_misses 0               decr未命中次数
STAT decr_hits 0                 decr命中次数
STAT cas_misses 0                cas未命中次数
STAT cas_hits 0                  cas命中次数
STAT cas_badval 0                使用擦拭次数
STAT touch_hits 0                touch命中次数
STAT touch_misses 0              touch未命中次数
STAT auth_cmds 0                 认证命令处理次数
STAT auth_errors 0               认证失败数目
STAT bytes_read 358              读取字节总数
STAT bytes_written 160           写入字节总数
STAT limit_maxbytes 16777216     分配的内存总数（字节）
STAT accepting_conns 1           是否已达到连接最大数 1-达到 0-未达到
STAT listen_disabled_num 0       统计当前服务器连接数曾经到达最大连接数的次数，这个数应该为0或者趋近于0，如果这个数不断增长，就要小心了
STAT threads 4                   当前MemCache总进程数
STAT conn_yields 0               连接操作主动放弃数目
STAT hash_power_level 16         hash表等级
STAT hash_bytes 524288           当前hash表大小
STAT hash_is_expanding 0         hash表正在扩展
STAT expired_unfetched 0         已过期但未获取大对象数目
STAT evicted_unfetched 0         一驱逐但未获取大对象数目
STAT bytes 166                   当前存储占用字节数
STAT curr_items 2                当前存储的数据总个数
STAT total_items 3               启动以来存储的数据总数
STAT evictions 0                 LRU释放的对象数目
STAT reclaimed 0                 已过期的数据数目来存储新数据的数目
"""

""" ============================ stats items 
STAT items:1:number 4                 该slab中对象数（不包含过期对象）
STAT items:1:age 1941                 LRU队列中最老对象的过期时间
STAT items:1:evicted 0                LRU释放对象数
STAT items:1:evicted_nonzero 0        设置了非0时间的LRU释放对象数
STAT items:1:evicted_time 0           最后一次LRU释放的对象存在时间
STAT items:1:outofmemory 0            不能存储对象次数
STAT items:1:tailrepairs 0            修复slabs次数
STAT items:1:reclaimed 0              使用过期对象空间存储对象次数
STAT items:1:expired_unfetched 0      已过期但未获取的对象数目
STAT items:1:evicted_unfetched 0      已驱逐但未获取的对象数目
"""

""" ============================ set 
set key flags exptime bytes [noreply] 
value 
    - key：键值 key-value 结构中的 key，用于查找缓存值。
    - flags：可以包括键值对的整型参数，客户机使用它存储关于键值对的额外信息。
    - exptime：在缓存中保存键值对的时间长度（以秒为单位，0 表示永远）
    - bytes：在缓存中存储的字节数
    - noreply（可选）： 该参数告知服务器不需要返回数据
    - value：存储的值（始终位于第二行）（可直接理解为key-value结构中的value）
    
    
set one 0 900 9
tests
    
    
STORED：保存成功
ERROR：保存失败
"""

""" ============================ add


"""

""" ============================ replace 

"""

""" ============================ get 

"""

""" ============================ delete

"""

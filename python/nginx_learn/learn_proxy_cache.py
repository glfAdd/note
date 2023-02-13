"""
Buffer
1. "缓冲", 用户传输效率不同步或优先级别不相同的设备之间床底数据, 一般通过对一方的数据临时存放, 再统一发送的办法发给另一方, 这些数据本身就没有用处了
2. 实现了被代理服务器响应数据的异步传输

Cache
1. "缓存", 用于将硬盘上已有的数据在内存中简历缓存数据, 提高数据的访问效率, 对过期不用的缓存可以随时销毁, 但不会销毁硬盘的数据.
2. 实现了Nginx对客户端请求数据的快速响应

Nginx接收到被代理服务器响应的数据以后, 通过Proxy Buffer机制将数据传输给客户端, 并根据Proxy Cache的配置将这些数据缓存到本地磁盘上.
当客户端下次访问相同的数据时, Nginx直接从磁盘检索响应的数据返回给客户端, 从而减少与被代理服务器之间的交互时间.
Cache依赖于Buffer, 只有打开Buffer配置Cache才能发挥作用.

Proxy Cache开启后会检测被代理服务器的响应数据HTTP头部, 以下情况不被Nginx缓存
Cache-Control: 为no-cache 或 no-store 或 private 或 max-age赋值为0/无意义
Expires: 包含一个过期时间
"""

""" ============================ proxy_cache
配置一块公用的内存内存区域的名称, 该区域可以存放缓存的缩影数据. 这些数据在Nginx服务器启动时由缓存索引重建进程负责建立


porxy_chache zone | off;
    zone: 用于存放缓存索引的内存区域名称
    off: 关机porxy_cache功能, 默认
"""

""" ============================ proxy_cache_bypass
Nginx向客户端发送响应是, 不从缓存中获取的条件
作用: 避免私有的数据被其他客户端得到
proxy_cache_bypass string ... ;
    string: 条件变量, 支持变量, 支持多个. 当至少有一个字符串指令不为空或不等于0是, 响应数据不从缓存获取.
    - proxy_cache_bypass $coolie_nocache $arg_nocache $ arg_comment $http_pragma $http_authorization;
"""

""" ============================ proxy_cache_key
Nginx在内存中为缓存数据建立索引的使用关键字
proxy_cache_key string;
    string: 关键字, 支持变量
    - proxy_cache_key $scheme$proxy_host$request_uri$is_args$args;
"""

""" ============================ proxy_cache_lock
是否开启缓存锁
某些数据可能同时被多个请求返回的响应数据填充, 开启后, 同时只能有一个请求天成缓存的某一数据, 相当于个数据加锁, 必须等到锁被释放
proxy_cache_lock on | off;
"""

""" ============================ proxy_cache_lock_timeout
缓存锁开启以后锁的超时时间. 默认5s
proxy_cahce_lock_timeout time;
"""

""" ============================ proxy_cache_min_uses
当客户端向被代理服务器发送相同的请求达到指定次数后, Nginx才对该请求响应做缓存. 合理设置可以硬盘上缓存数据量. 默认1
proxy_cache_min_uses number;
"""

""" ============================ proxy_cache_path
Nginx存储缓存数据的路径和索引相关的内容
只能放在HTTP模块中
proxy_cache_path path [levels=levels] keys_zone=name:size1 [inactive=time] [max_size=size2] 
                      [loader_files=number] [loader_sleep=time2] [loader_threshold=time3];
    path: 路径
    levels: path的几级目录
    name:size1: 缓存索引内存区域的名称和大小
    time1: 当硬盘上的缓存在设定时间内没有被访问时, Nginx会强制从硬盘上删除, 下次客户端访问重新建立, 默认10s
    size2: 硬盘缓存数据大小上限. 超过了根据最近最少访问的策略删除缓存
??? number: 每次加载的数据元素的数量上限。在重建缓存索引的过程中，进程通过一系列的递归遍历读取硬盘上的缓存数据目录及缓存数据文件,
            对每个数据文件中的缓存数据在内存中建立对应的索引.我们称每建立一个索引为加载一个数据元素。 
            进程在每次遍历过程中可以同时加载多个数据元素,该值限制了每次遍历中同时加载的数据元素的数量。默认设置为100。
    time2: 两次遍历间暂停时间. 默认50ms
    time3: 遍历一次时间上限. 默认200ms
    - proxy_cache_path /nginx/cache/a levels=1 keys_zone=a:10m;
    - proxy_cache_path /nginx/cache/b levels=2:2 keys_zone=b:100m;
    - proxy_cache_path /nginx/cache/c levels=1:1:2 keys_zone=c:1000m;
"""

""" ============================ proxy_cache_use_stale
Nginx在访问被代理服务器过程中出现被代理的服务器无法访问或者访问错误等现象时，
Nginx可以使用历史缓存响应客户端的请求，这些数据不一定和被代理服务器上最新的数据相一致, 但对于更新频率不高的后端服务器, 一定程度上能够为客户端提供不间断访问。
设置一些状态，当后端被代理的服务器处于这些状态时，Nginx 服务器启用该功能

proxy_cache_use_stale error | timeout | invalid_header | updating | http_500 | http_502 | http503 | http_504 | http_404 | off ...;
    updating: 客户端请求时Nginx正好处于更新状态
    error: 建立连接/向被代理服务器发送请求/读取被代理服务器想用头时服务器发僧错误
    timeout: 建立连接/向被代理服务器发送请求/读取被代理服务器想用头时服务器超时
    invalid_header: 被代理服务器返回的响应头为空或无效
    http_500 | http_502 | http_503 | http_504 | http_404: 被代理服务器返回500/502/503/504/404状态码
    off: 无法将请求发送给被代理服务器(默认)
"""

""" ============================ proxy_cache_valid
不同的HTTP响应状态设置不同的缓存时间
proxy_cache_valid [code ... ] time;
    - proxy_cache_valid 200 302 10m;
    - proxy_cache_valid 301 1h;
    - proxy_cache_valid any 1m;         非200 302 301 缓存1分钟
"""

""" ============================ proxy_no_cache
什么情况下不适用cache功能
proxy_no_cache string ... ;
    string: 1个或多个变量, 值不菲0是不启动cache功能
"""

""" ============================ proxy_store
是否在本地磁盘缓存莱斯被代理服务器的响应数据, 毕Proxy Cache简单, 没有过去更新/内存索引建立等功能, 不占用内存空间, 对静态数据效果较好
常用在被代理服务器发生错误的情况下, 用来缓存带服务器的响应数据
proxy_store on | off | string;
    on: 开启, 缓存文件会放到alias或root设置的路径下
    off: 默认
    string: 自定义缓存文件路径, 此时是开启状态
"""

""" ============================ proxy_store_access
用户/用户组对Proxy Store数据访问的权限
proxy_store_access users:permissions ... ;
    users: user/group/all
    permissions: 权限
    - proxy_store_access user:rw group:rw all:r;
"""

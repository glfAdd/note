""" ============================ 域名镜像
镜像服务器, 缓存服务器, 负载均衡

把不需要实时更新的动态页面输出结果转化为静态野蛮形式缓存, 按照静态页面访问

1. 404错误驱动web缓存 和 资源不存在驱动Web缓存 如果不是在内存中保存缓存数据, 则不支持缓存数据清理机制, 会一直保存在磁盘
2. 404错误驱动web缓存 和 资源不存在驱动Web缓存 只能缓存状态码200的请求
3. 404错误驱动web缓存 和 资源不存在驱动Web缓存 不支持动态链请求, 会忽略掉后面的参数, 如: person?age=1
"""

""" ============================ 404错误驱动web缓存
依靠Proxy Store对404错误重定向实现. 当Nginx处理请求时, 发现请求的资源数据不存在, 产生404错误, Nginx该错误再向后端服务器请求数据, 将数据返回给客户端并缓存到本地

# 将404错误重定向, 使用location模块捕获重定向请求, 然后发给后端服务器
location / {
    root /myweb/server/;
    # 404重定向到/errpage目录下
    # 将404状态码改为200
    error_page 404 =200 /errpage$request_uri;
}
location /errpage/ {
    # 该目录不能通过外部链接访问
    internal;
    alias /home/html/;
    proxy_pass http://backend;
}
"""

""" ============================ 资源不存在驱动Web缓存
location / {
    internal;
    alias /myweb/server;
    proxy_store on;
    proxy_temp_path /myweb/server/tmp;
    # 判断资源在Nginx是否存在, 如果不存在去后端服务器请求并在Nginx保存
    if (!-f $request_filename) {
        proxy_pass http://backend/; 
    }
}
"""

""" ============================ memcached
1. 高性能的基于分布式的缓存系统, 可以单独作为后台程序
2. 在内存中开辟一块空间，然后建立一个Hash表，将缓存数据通过键值存储在Hash表
3. 由服务端和客户端两个核心组件组成, 服务端先通过计算“键”的Hash值来确定键值对在服务端所处的位置。
4. 当确定键/值对的位置后,客户端就会发送一个查询请求给对应的服务端，让它来查找并返回确切的数据。


memcached_pass address;
    address: memcached服务器地址. IP端口/域名/upstream服务器组
    
memcached_connect_timeout time;
    time: 连接memcached服务器超时时间. 默认60s
    
memcached_read_timeout time;
    time: Nginx向memcached服务器发出两次read请求间的等待时间, 这段时间内没有数据传输则关闭连接. 默认60s
    
memcached_write_timeout time;
    time: Nginx向memcached服务器发出两次write请求间的等待时间, 这段时间内没有数据传输则关闭连接. 默认60s
    
memcached_buffer_size size;
    size: Nginx接收memcached服务器响应数据的缓存区大小. 4k 或 8k
    
memcache_next_upstream status ... ;
    status: memcached服务器返回的状态, 可以多个. 不包含与memcached服务器传输数据过程中发生的错误
        error: 建立连接/向memcached发送请求/读取响应头时发生连接错误
        timeout: 建立连接/向memcached发送请求/读取响应头时连接超时
        invalid_header: memcached返回的响应头为空或无效
        not_found: memcached服务器未找到键值对
        off: 无法将请求发送到memcached服务器
    
    
# 设置$memcached_key变量的值为$uri$args
# Nginx服务器会调用Hash算法向memcached服务器查询请求
# 如果请求缓存的数据时404 502 504时, 则将错误重新定位请求fallcack数据
server {
    location / {
        set $memcached_key "uri$args";
        memcached_pass 192.168.1.5:8000;
        error_page 404 502 504 = @fallback; 
    }
    location @fallback {
        proxy_pass http://backend; 
    }
}
"""

""" ============================ Proxy Cached缓存机制
Nginx服务器启动后, 生产专门进程对磁盘上的缓存文件进行扫描, 在内存中简历缓存索引提高访问效率, 专门的管理进程对磁盘上的缓存文件过期/更新进行管理
支持对任意响应的数据缓存, 不限于200
没有实现自动清理磁盘缓存源数据的功能
"""

""" ============================ Squid
Web缓存服务器
"""

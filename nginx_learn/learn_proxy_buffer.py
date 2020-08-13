""" 
每个请求都会按照这些指令配置各自的Buffer, Nginx不会生产一个公共的Proxy Buffer供代理服务器使用
Proxy Buffer启用后, Nginx会异步的将代理服务器的响应数据发送个客户端.
1. Nginx从代理服务器获取响应数据, 放置在Proxy Buffer中
2. Proxy Buffer大小由proxy_buffer_size和proxy_buffers决定
3. 接收过程中如果没有足够的大小接收响应数据, Nginx会将部分接收到的数据存放在磁盘的临时文件中, 路径通过proxy_temp_path决定, 大小有proxy_max_temp_file_size和proxy_temp_file_write_size决定
4. 一次响应数据接收完成或Buffer装满以后, Nginx开始向客户端传输数据
5. 每个Proxy Buffer装满数据后, 从开始向客户端发送数据直到数据全部完, 处于BUSY状态, 期间对他进行任何操作都会失败.
6. 处于BUSY状态的Proxy Buffer中大小有proxy_busy_buffer_size决定
7. 当Proxy Buffer关闭时, Nginx只要接收到响应数据就会同步的传递给客户端, 它本身不会读取完成的响应数据. 
"""

""" ============================ proxy_buffer
启用/关闭 Proxy Buffer. 默认on
还可已通过HTTP响应头的X-Accel_Buffering头域设为yes或no实现, 但Nginx配置中的proxy_ignore_headers可能使头域失效
proxy_buffer on | off;
"""

""" ============================ proxy_buffers 
设置接收一次代理代理服务器响应数据的Proxy Buffer个数和每个Buffer大小
proxy_buffers number size;
    number: proxy buffer个数
    size: 每个buffer大小, 一般设置为内存页的大小, 根据不同的平台可能为4KB或8KB

总数: number * size
默认: proxy_buffers 8 4k|8k;
"""

""" ============================ proxy_buffer_size 
设置从代理服务器获取的第一部分响应数据的大小, 一般包含HTTP响应头. 默认4KB或8KB
保持与proxy_buffer指令中的size一样大活着更小
proxy_buffer_size size;
"""

""" ============================ proxy_busy_buffer_size 
限制同时处于BUSY状态的Proxy Buffer的总缓存区大小. 默认8KB或16KB
proxy_busy_buffer_size size;
"""

""" ============================ proxy_temp_path 
1. 配置磁盘上路径, 用于临时存放代理服务器的大体积响应数据. 
2. 如果Proxy Buffer被装满后, 响应数据仍然没有被Nginx服务器完全接收, 响应数据会临时存放在该文件中.
proxy_temp_path path [level1 [level2 [level3]];
    path: 临时文件路径
    levelN: 设置在path变量设置的路径下第几级hash目录存放临时文件
    - proxy_temp_path /doucment/temp 1 2;  保存在目录下的第2级
"""

""" ============================ proxy_max_temp_file_size 
配置所有临时文件的总大小. 默认1024MB
proxy_max_temp_file_size size;
"""

""" ============================ proxy_temp_file_write_size
写入临时文件数据总大小, IO负载过大会降低性能. 默认8KB或16KB
proxy_temp+file_wtire_size size;
"""

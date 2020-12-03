""" ============================
作用: 将响应报⽂发送⾄客户端之前可以启⽤压缩功能, 能够节约带宽，并提⾼响应⾄客户端的速度, 压缩会消耗nginx的cpu性能
http / server / location 配置

"""
""" ============================ ngx_http_gzip_module
负责Gzip的开启和设置
使用的时静态压缩


gzip on | off;
    默认off
    
    
gzip_buffers number size;
    Nginx在响应数据输出数据进行Gzip压缩时需要向系统申请number * size大小的空间用于压缩数据. 默认number * size 128, size为4kb | 8kb
    number: Nginx向系统申请缓存空间个数
    size: 每个缓存空间大小
    - gzip_buffers 32 4k | 16 8k;
    
    
gzip_comp_level level;
    压缩程度. 1 - 9, 默认1 
    1压缩程度最低, 压缩效率最高
    9压缩程度最高, 压缩效率低


gzip_disable regex ... ;
    Nginx响应哪些User-Agent关闭Gzip, 支持正则表达式
    
    
gzip_http_version 1.0 | 1.1;
    客户端使用哪种http版本时使用Gzip. 默认1.1
    
    
gzip_min_length length;
    http响应头的Content-Length大于lenght才开启Gzip. Content-Length不存在是该指令不起作用.
    length: 默认20. 设为0时所有响应都使用Gzip
    gzip_min_length 1024;
    
    
gzip_proxied off | expired | on-cache | no-store | private | no_last_modified | no_etag | auth | any ... ; 
    off: 关闭Gzip. 默认
    expired: 当后端服务器响应头包含"expired"时开启Gzip
    no-cache: 当后端服务器响应头包含"Cache-Control: no-cache"时开启Gzip
    no-store: 当后端服务器响应头包含"Cache-Control: no-store"时开启Gzip
    private: 当后端服务器响应头包含"Cache-Control: private"时开启Gzip
    no_last_modified: 当后端服务器响应头不包含"Last-Modified"时开启Gzip
    no_etag: 当后端服务器响应头不包含"ETag"时开启Gzip
    auth: 当后端服务器响应头包含"Authorization"时开启Gzip
    any: 无条件开启Gzip
    - gzip_proxied expired no-cache no-store private auth;
    

gzip_types mime-type ... ;
    Nginx根据响应的MIME类型开启Gzip
    当gizp为on时, * 表示所有类型
    - gzip_types text/plain text/html application/xml;
    
    
gzip_vary on | off;
    设置在使用Gzip功能时是否发送带有"Vary: Accept-Encoding"头域的响应头.
    开启后的效果是在响应头添加"Accept-Encoding: gzip"
    默认off.
    可以使用add_header实现相同效果
    - add_header Vary Accept-Encoding gzip;
"""

""" ============================ ngx_http_gzip_static_module
负责搜索和发送经过Gzip功能预压缩的数据. 这些数据以".gz"后缀名存储在服务器上, 如果客户端请求的数据之前压缩过, 切客户端支持Gzip, 就直接返回压缩的数据.
默认使用Chunked编码的动态压缩, 主要用于服务器无法确定响应数据长度的情况, 比如大文件下载需要实时生成数据长度.
如果使用该功能, 配置Ngxin时添加--with-http_gzip_static_module

gzip_static on | off | always;
    always: 一直发送Gzip预压缩文件, 且不检测客户算是否支持Gzip
"""

""" ============================ ngx_http_gunzip_module
Nginx服务器支持对响应输出数据流进行Gzip压缩，这对客户端浏览器来说，需要有能力解压和处理Gzip压缩数据，
但如果客户端本身不支持该功能，就需要Nginx服务器在向其发送数据之前先将该数据解压。这些压缩数据可能来自于后端服务器压缩产生或者Nginx服务器预压缩产生
ngx_http_gunzip_module模块便是用来针对不支持Gzip压缩数据处理的客户端浏览器，对压缩数据进行解压处理的
如果使用该功能, Nginx配置时添加--with_http_gunzip_module

gunzip_static on | off;
    默认off
    on: 开启. 如果客户端不支持Gzip, Nginx返回解压后的数据. 如果客户端支持Gzip, Nginx返回压缩后的数据.
    off: 关闭


gunzip_buffers number size;
    Nginx在响应数据输出数据进行Gzip压缩时需要向系统申请number * size大小的空间用于压缩数据. 默认number * size 128, size为4kb | 8kb
    number: Nginx向系统申请缓存空间个数
    size: 每个缓存空间大小
    - gzip_buffers 32 4k | 16 8k;
"""

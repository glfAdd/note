""" ============================ 反向代理
http server location 中设置, 一般在server中

同时接收客户端连接数
worker_processes * worker_connections / 4
"""

""" ============================ proxy_pass
设置被代理服务器地址, 可以是主机名/IP端口号/URI等
proxy_pass URL;
1. 传输协议通常是http或https
2. 如果被代理服务器是一组服务器可以使用upstream设置服务器组
3. 如果使用upstream设置了一组服务器作为被代理服务器, 则按照顺序轮询访问.


# 在upstream中指明协议
upstream proxy_svrs{
    server http://192.168.3.1:8000/;
    server http://192.168.3.2:8000/;
    server http://localhost:8000/uri/;
}
server {
    listen 80;
    server_name www.test1.com;
    location / {
        proxy_pass proxy_svrs;
    }
}


# 在proxy_pass中指明协议
upstream proxy_svrs{
    server 192.168.3.1:8000/;
    server 192.168.3.2:8000/;
    server localhost:8000/uri/;
}
server {
    listen 80;
    server_name www.test1.com;
    location / {
        proxy_pass http://proxy_svrs;
    }
}


# proxy_pass中URL是否带有URI
server {
    server_name www.tests.com
    location /server/ {
        # proxy_pass http://192.168.3.1/;
        # proxy_pass http://192.168.3.1/url/;
    }
}
1. 如果URL中没有URI, 客户端使用 http://www.test.com/server/ 发起请求, 地址会转向 http://192.168.3.1/server/
2. 如果URL中有URI, 客户端使用 http://www.test.com/server/ 发起请求, 地址会转向 http://192.168.3.1/url/


# proxy_pass结尾的 / 
proxy_pass http://192.168.3.1;      URL中包含URI /
proxy_pass http://192.168.3.1/;     URL中不包含URI
"""

""" ============================ proxy_hide_header 
设置HTTP响应隐藏部分header信息
proxy_hide_header field;            header隐藏field信息
"""

""" ============================ proxy_pass_header 
设置HTTP响应header信息
proxy_pass_header field;            header添加field

"""

""" ============================ proxy_pass_request_body on | off 
是否将客户端的请求体发送给被代理服务器. 默认on
proxy_pass_request_body on | off;
"""

""" ============================ proxy_set_header 
更改Nginx收到的请求头, 然后发给被代理服务器
proxy_set_header field value;
    field: 要更改信息头
    value: 更改的值, 支持文本/变量/变量组合
    - proxy_set_header Host $proxy_host;
    - proxy_set_header Connection close;
"""

""" ============================ proxy_set_body 
更改Nginx收到的请求体, 然后发给被代理服务器
proxy_set_body value;
    value: 更改的值, 支持文本/变量/变量组合
"""

""" ============================ proxy_bind 
在设置了多个基于名称或基于IP的主机情况下, 如果希望代理连接有指定的主机处理可以在这里设置
proxy_bind address;
    address: 指定主机IP
"""

""" ============================ proxy_connect_timeout 
Nginx与被代理服务器建立连接的超时时间
proxy_connect_timeout time;
    time: 默认60s
"""

""" ============================ proxy_read_timeout 
Nginx向被代理服务器发送read请求后响应时间
proxy_read_timeout time;
    time: 默认60s
"""

""" ============================ proxy_send_timeout 
Nginx向被代理服务器发送write请求后响应时间
proxy_send_timeout time;
    time: 默认60s

"""

""" ============================ proxy_http_version 
被代理服务器HTTP版本
proxy_http_verson 1.0 | 1.1;
    默认1.0
"""

""" ============================ proxy_method 
Nginx向被代理服务器发送请求的方式, 一般为GET和POST, 设置一会客户端的请求将被忽略
proxy_method GET | POST | ...
"""

""" ============================ proxy_ignore_client_abort 
客户端终端网络连接时, Nginx是否中断与被代理服务器连接
proxy_ignore_client_abort on | off;
    默认off, 中断
"""

""" ============================ proxy_ignore_headers
Nginx接收到被代理服务器后, 哪些请求头不处理
proxy_ignore_headers field ... ;
    field: HTTP响应头域, 例如: X-Accel-Redirect X-Accel-Expires Expires Cache-Control Set-Cookie
"""

""" ============================ proxy_redirect 
把被代理服务器返回的地址信息更改为需要的地址信息, 修改被代理服务器返回的响应头中的Location头域和Refresh头域与proxy_ pass指令配合使用
比如，Nginx通过proxy_ pass指令将客户端的请求地址重写为被代理服务器的地址，那么Nginx服务器返回给客户端的响应头中"Location” 头域显示的地址就应该和客户端发起请求的地址相对应， 而不是被代理服务器直接返回的地址信息。

proxy_redirect redirect replacement;
proxy_redirect default;
proxy_redirect off;
    redirect: 匹配需要替换的Location头域的字符串, 支持变量和正则
    replacement: 替换后的字符串, 支持变量使用
    default: 使用location块的uri变量作为replacement, proxy_pass变量作为redirect
    off: 将当前域下所有proxy_redirect指令这位无效
    - proxy_redirect http://localhost:8081/proxy/some/ http://test1.com/some/;

下面个两个效果相同
location /server/ {
    proxy_pass http://www.test.com/some/;
    proxy_redirect default;
}
location /server/ {
    proxy_pass http://www.test.com/some/;
    proxy_redirect http://www.test.com/some/ /server/;
}
"""

""" ============================ proxy_intercept_errors 
proxy_intercept_errors on | off;
    on: 如果代理服务返回的HTTP状态码为400或大于400, 则Nginx使用自己定义的错误页面
    off: Nginx直接将被代理服务器返回的HTTP状态返回给客户端
"""

""" ============================ proxy_headers_hash_max_size 
proxy_headers_hash_max_size size;
    size: HTTP报文头哈希容量上限, 默认512字节
    - proxy_headers_hash_max_size 512;

Nginx服务器为了能够快速检索HTTP报文头中的各项信息，比如服务器名称、MIME类型、请求头名称等，使用哈希表存储这些信息。
"""

""" ============================ proxy_headers_hash_bucket_size 
proxy_headers_hash_bucket_size size;
    size: 设置服务器名称的字符数长度. 默认64字节
"""

""" ============================ proxy_next_upstream 
Nginx发哪些异常时, 将请求顺次交给下一组内服务器处理
proxy_next_upstream status ... ;
    status: 服务器返回的状态, 可以使多个
    
error: 建立连接/向被代理服务器发送请求/读取被代理服务器想用头时服务器发僧错误
timeout: 建立连接/向被代理服务器发送请求/读取被代理服务器想用头时服务器超时
invalid_header: 被代理服务器返回的响应头为空或无效
http_500 | http_502 | http_503 | http_504 | http_404: 被代理服务器返回500/502/503/504/404状态码
off: 无法将请求发送给被代理服务器
"""

""" ============================ proxy_ssl_session_reuse 
是否使用SSL安全协议回话里阿尼额被代理服务器(https). 默认on
proxy_ssl_session_reuse on | off;
"""


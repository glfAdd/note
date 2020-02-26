"""
/etc/nginx/                         Nginx配置路径
/etc/nginx/nginx.conf
/etc/nginx/conf.d/default.conf
/var/run/nginx.pid                  PID目录
/var/log/nginx/error.log		    错误日志
/var/log/nginx/access.log		    访问日志
/usr/share/nginx/html               默认站点目录


main
events
http
    server
        location


惊群: 当某一时刻只有一个网络简介到来时, 多个睡眠京城被同事唤醒, 但只有一个进程获得连接.
标准URI: 可以是不含正则表达的URI
正则URI: 使用正则表达式的URI
MIME-TYPE: 网络资源媒体类型, 用于前端和后端识别


给网卡设备添加两个IP别名
(系统重启后失效) ifconfig eth0:2 10.211.55.102 netmask 255.255.255.0 up
(永久有效) echo "ifconfig eth0:2 10.211.55.102 netmask 255.255.255.0 up" >> /etc/rc.local
"""

""" ============================ 全局块
从文件开始到events之间


user user [group];
    启动进程的权限, 用户和用户组
    所有用户启动(1) 注释掉 (2) user nobody nobody;


worker_processes number | auto;
    工作进程数
    number: 个数
    auto: 自动判断启动多少个
  

pid file;
    保存主进程号的文件名, 相对路径/绝对路径 
    - pid sbin/web_nginx


error_log file | stderr [debug | info | notice | warn | error | crit | alert | emerg];
    错误日志文件
    file: 输出到文件
    stderr: 输出到标准错误输出stderr
    - error_log logs/error.log error;
  

include file;
    导入配置文件
    
    
auth_basic string | off;
    用户名密码认证
    string: 开启认证功能, 并配置验证提示信息
    off: 关闭认证
    
    
auth_basic_user_file file;
    用户名/密码文件路径
    
加密文件
name1:password1
name2:password2:comment        
"""

""" ============================ events 
影响服务器与用户网络的连接, 性能影响大


include file;


accept_mutex on | off;
    对多个nginx进程序列化, 防止多个进程对连接争抢, 默认on
  

multi_accept on | off;
    每个工作进程能否同时处理多个连接, 默认off
  

use method;
    事件驱动模型 
        select
        poll
        kqueue
        epoll
        etsig
        eventport
  

worker_connections number:
    每个进程同时最大连接数, 不能大于操作系统支持打开文件最大句柄数. 默认512. 一般设置为65535
    最大数量Client = worker_processes * worker_connections / 2
    
    查看
    cat /proc/sys/fs/file-max
    设置
    echo "183045" > /proc/sys/fs/file-max; sysctl -p
    
    
worker_rlimit_sigpending limit;
    影响事件驱动模型rtsig薄脆的最大信号数.
    Nginx每个工作进程都有自己的信号队列暂存客户端请求发生的信号, 如果超过长度限制Nginx自动转用pool处理未处理的客户端请求信号
    limit: Linux平台事件信号队列长度上限
    - worker_rlimit_sigpending 1024;
    
    
devpoll_changes number;
    设置传递给内核事数量, /dev/poll事件驱动模式下
    number: 默认512
    
    
devpol_events nubmer;
    设置从内核获取事件的数量, /dev/poll事件驱动模式下
    number: 默认512


kqueue_changes number;
    设置传递给内核事数量, kqueue事件驱动模式下
    number: 默认512
    
    
kqueue_events number;
    设置从内核获取事件的数量, kqueue事件驱动模式下
    number: 默认512
    
    
epoll number;
    Nginx与内核之间传递事件的数量, epoll事件驱动下Nginx向内核传递事件和从内核传递事件的数量是相同的
    number: 默认512

    
rtsig_signo signo;


rtsig_overflow_* number;        
"""

""" ============================ http
代理/缓存和日志


include file;
error_log file | stderr [debug | info | notice | warn | error | crit | alert | emerg];


include /etc/nginx/mime.types;
    导入配置文件, 用于浏览器识别的MIME类型和后缀名
  

default_type application/octet-stream;
    处理前端请求的MIME类型, 不加此指令默认text/plain
  

access_log path[format[buffer=size]];
    服务器提供服务过程应答前端请求的日志
    path: 日志文件
    format: 日志格式, 在log_format中定义
    size: 临时保存日志内存大小
    - access_log logs/access.log name(日志格式名字);
    
    
access_log off;
    关闭日志


log_format name string;
    日志格式
    name: 日志的名字, 默认combined
    string: 字符串
    

sendfile on | off;
    打开/关闭文件传输, 默认off
    

sendfile_max_chunk size;
    每个工作进程每次传输最大值. 0则不限制. 默认0
    - sendfile_max_chunk 128k;


keepalive_timeout timeout[header_timeout];
    与用户建立连接后, Nginx保持打开连接一段时间, 然后关闭. 
    timeout: 默认75s
    header_timeout: 指定使用Keep-Alive消息头毕保持与客户端浏览器的连接, 超时后客户端关闭连接, 而不需要服务器关闭
    - keepalive_timeout 120s 100s;
    
    
    
keepalive_requests number;
    服务端和用户端建立连接后, 用户通过此连接发送请求次数, 默认100
    

root path;
    资源根目录
    Web服务器收到网络请求以后, 首先在服务器指定目录寻找资源.
    

allow address | CIDR | all;
    address: 允许访问的客户端ip, 不支持同时设置多个, 只能写多个allow
    CIDR: 允许访问的哭护短CIDR, 例如: 202.80.18.23/25, 前面32位表示IP, 后面/25表示该IP地址前25位时网络部分, 其余代表主机部分
    all: 允许所有客户端访问
    allow 2620:100:e00::8001;   支持ipv6
    

deny address | CIDR | all;
    禁止访问
    
location / {
    deny 192.168.1.1;
    allow 192.169.1.2;
    deny all;
}
192.169.1.2可以访问, 遇到deny和allow时按顺序匹配, 匹配到了就停止不再匹配后面的
"""

""" ============================ server 
虚拟主机
每个server相当一个虚拟主机, 使得Nginx服务器可以在同一台服务器上只运行一组Nginx进程, 就可以运行多个网站


include file;
error_log file | stderr [debug | info | notice | warn | error | crit | alert | emerg];
include /etc/nginx/mime.types;
default_type application/octet-stream;
access_log path[format[buffer=size]];
sendfile on | off;
sendfile_max_chunk size;
keepalive_timeout timeout[header_timeout];
keepalive_requests number;
root path;
allow address | CIDR | all;
deny address | CIDR | all;
    

listen配置监听
listen address[:port] [default_server] [setfib=number] [backlog=number] [rcvbuf=size] [sndbuf=size] [deferred] [accept_filter=filter] [bind] [ssl];
listen port [default_server] [setfib=number] [backlog=number] [rcvbuf=size] [sndbuf=size] [accept_filterfilter] [deferred] [bind] [ipv6only=on|off];
listen unix:path [default_server] [backlog=number] [rcvbuf=size] [sndbuf=size] [accept_filter=filter] [deferred] [bind] [ssl];
    address: 如果是ipv6需要使用[], 例如[fe80::1]
    port: 端口
    path: socket文件路径, 如/var/run/nginix.sock
    default_server: 标识符, 将此虚拟机主机设为address:port的默认主机
    setfib: (不常用)
    backlog: 监听函数listen最多允许连接同时处于挂起状态, 默认511
    rcvbuf: 监听socket接收缓存区大小
    sndbuf: 监听socket发送缓存区大小
    deferred: 标识符, 将accept()设置为Deferred默认
    accept_filter: (不常用)
    bind: 标识符, 使用独立的bind()处理此address:port; 一般情况下，对于端口相同而IP地址不同的多个连接，Nginx服务器将只使用一个监听命令，并使用bind()处理端口相同的所有连接
    ssl: 标识符，设置会话连接使用SSL模式进行
    - listen *:80 | *:8080;                               监听所有80和8080端口
    - listen 192.168.1.10:8000;                           
    - listen 192.168.1.10;                                IP的所有端口
    - listen 8080;                                        8080端口的所有IP
    - listen 192.168.1.10 default_server backlog=1024;    192.168.1.10的连接请求默认由此虚拟主机处理, 允许最多1024个网络连接同事处于挂起状态


server_name name ... ;
    主机名称就是域名, 多个之间用空格分隔, 第一个名称作为主要名称
    域名两段/三段组成
    可以使用通配符 * , 只能用于三段字符创的首尾, 或两段的尾部
    可以使用正则表达式, 用~作为表达式的开头
    - server_name test1.com www.test2.com;
    - server_name *.test1.com www.test2.*;
    - server_name ~www\d+\.test1.com$;
    - server_name 10.211.55.3;
"""

""" ============================ location 
include file;
error_log file | stderr [debug | info | notice | warn | error | crit | alert | emerg];
include /etc/nginx/mime.types;
default_type application/octet-stream;
access_log path[format[buffer=size]];
sendfile on | off;
sendfile_max_chunk size;
keepalive_timeout timeout[header_timeout];
keepalive_requests number;
root path;
allow address | CIDR | all;
deny address | CIDR | all;


location [ = | ~ | ^~ | ~* ] URI {...}
    =   用于标注URI前, 请求字符串与URI严格匹配, 如果匹配成功就停止继续搜索, 并立刻处理
    ^~  用于标准URI前, 找到请求字符串匹配度最高的location后立刻用此location处理请求, 不再使用location块中的正则rui匹配. 会对URI做编码处理.
    ~   用于表示URI包含正则表达式, 并区分大小写
    ~*                            不区分
    URI: 待匹配的请求字符串

    (在不添加此选项时)
    - Nginx服务器首先在server块的多个location块中搜索是否有标准URI和请求字符串匹配, 如果有多个可以匹配, 就记录匹配度最高的一个
    - 然后，服务器再用location块中的正则URI和请求字符串匹配，当第一个正则URI匹配成功结束搜索, 并使用这个location块处理此请求
    - 如果正则匹配全部失败，就使用刚才记录的匹配度最高的location块处理此请求
    

alias path;
    更改location的URI, 和root命令类似, 只不多在location里面
    
    
index file ...;
    设置网站默认首页, 可以多个文件中间用空格, 先找到那个就用哪个相应, 默认index.html
    - index index.html index.text1.html;
    

error_page code ... [=[response]] URI;
    错误页面
    code: 错误代码
    response: 将code指定的错误代码转为新的错误代码response
    URI: 错误页面的路径或网址
    - error_page 404 /404.html;l
    - error_page 403 http://mytest.com/test.html;
    - error_page 410 =301 /emtpy.gif;       服务器产生410错误时, 使用empty.gif返回错误码301
    
    
    

    
"""

""" ============================ /etc/nginx/nginx.conf 
user nginx;
worker_processes auto;
error_log /var/log/nginx/error.log;
pid /run/nginx.pid;


include /usr/share/nginx/modules/*.conf;

events {
    worker_connections 1024;
}

http {
    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;

    sendfile            on;
    tcp_nopush          on;
    tcp_nodelay         on;
    keepalive_timeout   65;
    types_hash_max_size 2048;

    include             /etc/nginx/mime.types;
    default_type        application/octet-stream;

    include /etc/nginx/conf.d/*.conf;

    server {
        listen       80 default_server;
        listen       [::]:80 default_server;
        server_name  _;
        root         /usr/share/nginx/html;

        include /etc/nginx/default.d/*.conf;

        location / {
        }

        error_page 404 /404.html;
            location = /40x.html {
        }

        error_page 500 502 503 504 /50x.html;
            location = /50x.html {
        }
    }

# Settings for a TLS enabled server.
#
#    server {
#        listen       443 ssl http2 default_server;
#        listen       [::]:443 ssl http2 default_server;
#        server_name  _;
#        root         /usr/share/nginx/html;
#
#        ssl_certificate "/etc/pki/nginx/server.crt";
#        ssl_certificate_key "/etc/pki/nginx/private/server.key";
#        ssl_session_cache shared:SSL:1m;
#        ssl_session_timeout  10m;
#        ssl_ciphers HIGH:!aNULL:!MD5;
#        ssl_prefer_server_ciphers on;
#
#        # Load configuration files for the default server block.
#        include /etc/nginx/default.d/*.conf;
#
#        location / {
#        }
#
#        error_page 404 /404.html;
#            location = /40x.html {
#        }
#
#        error_page 500 502 503 504 /50x.html;
#            location = /50x.html {
#        }
#    }

}














"""

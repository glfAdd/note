""" ============================ http
重定向服务


后端服务器在负载均衡调度中的状态
1. down: 表示当前的server暂时不参与负载均衡。
2. backup    
3. max_fails
4. fail_timeout                 
5. max_conns: 限制最大的接受的连接数


地址转发
1. 地址转发后客户端浏览器地址栏中显示的地址不变
2. 只产生1次网路请求
3. 同一站点项目内
4. 转发的页面可以不用全路径表示
5. 可以向客户端请求的request属性传递给新页面
6. 速度快


地址重写
1. 地址重写后客户端浏览器得会变为务器选择的地址
2. 2次网路请求
3.
4. 重写的页面必须使用完整路径
5. 不可以向客户端请求的request属性传递给新页面
6. 速度慢

"""

""" ============================ upstream
upstream
1. 设置服务器组
2. 默认情况下, Nginx收到请求后顺序选择组内服务器.  如果在处理过程中服务器发生错误会顺序交给组内下一个服务器, 直到返回正常响应.
3. 如果都出错则返回最后一个服务器的结果


server address [parameters];
    设置组内服务器
    weight: 权. 默认1
    backup: 将服务器标记为备用服务器. 当其他所有的非backup机器down或者busy，才会请求backup机器
    max_fails: 请求失败次数. 在一定时间范围内, 当对组内某台服务器请求失败次数超过该变量是, 认为服务器无效.
               默认1. 设为0则不检测是否无效
    fail_timeout: 1. 指max_fails的时间
                  2. 检测服务器是否有效时, 如果服务器被任务时无效的(down), 则表示无效持续的时间, 在此期间不再检测服务器的状态
                  3. 默认10s
                  
    
ip_hash
1. 将某个客户端的多次请求定向到组内同一台服务器, 只有当前该服务器为down状态时, 客户端才会被下一个服务器处理
2. 避免服务器组内各服务器间回话共享
3. 不能喝weight一起使用
4. 客户端IP地址必须是C类地址
5. 由于根据IP地址分配, Nginx服务器必须醋鱼最前端的服务器, 这样才能获取到前端的IP


least_conn;
最少连接
    least connected负载均衡算法
    选取活跃连接数与权重weight的比值最小者(conns/weigh)为下一个处理请求的server. 
    如果有多个后端的conns/weight值同为最小的，那么对它们采用加权轮询算法
    
    
???
keepalive connections;
    connections: Nginx的每个工作进程允许该服务器组保持空闲网络连接的上限. 如果超过, 工作进程将采用最近最少使用的策略关闭网络连接.

    
upstream tests {
    ip_hash;
    least_conn;
    # 如果30s之内3次请求失败, 则30秒内被认为是无效状态. 
    server 127.0.0.1:5000 max_fails=3 file_timeout=30s backup;
}
"""

""" ============================ if
在server / location中使用
false: 变量名为空字符串或0开头字符串
true:


使用正则表达式, 变量和表达式之间使用符号链接
    ~   区分大小写
    ~*  不区分大小写
    !~  取反
    !~* 取反
    ()  截取匹配的值
    $1  引用截取的值


-f  请求文件存在为true
!-f 
-d  请求目录是否存在true
!-d 请求目录不存在, 但上一次存在true
    目录和上级都不存在为false
    请求目录存在为false
-e  请求文件或目录存在是true, 否则false
!-e 请求文件或目录都不存在是true, 否则false
-x  请求文件可执行true, 否则false
!-x 请求文件不可执行true, 否则false


if ($slow) {
}

if ($request_method = POST) {
}

if ($http_user_agent ~ MSIE) {
    # $http_user_agent是否包含字符串MSIE
}

if ($http_cookie ~* "id=(^;)(?:;|$)") {
    # $1和$2截取匹配的值
    set $id $1;
}

if (-f $request_filename) {
}
"""

""" ============================ break
server / location / if 定义
中断当前作用于的其他Nginx配置, 返回上一层作用域继续向下读取配置

location / {
    if ($slow) {
        set $id $1
        break; 
    }
}
"""

""" ============================ return
server / location / if 定义
直接返回请求

return [text]
return code URL;
return URL;
    code: 状态码, 0~999, 非标准的444代码可以强制关闭服务器与客户端的连接且不返回任何响应信息给客户端
    text: 响应体内容, 支持变量
    URL: 返回URL地址
    
    
301: 永久重定向
302: 临时重定向, 要求是GET请求
303: 当前请求的响应可以在另外URL上找到, 且客户端应当采用GET方式访问    
307: 请求的资源临时从不同的URL响应
"""

""" ============================ rewrite
server / location 定义
通过正则表达式改变URI, 可以同时有多个, 按照顺序对URL匹配
有时rewrite可能会形成循环, Nginx循环10次返回500


URI
scheme:[//] [[ 用户名[:密码] @ 主机名[:端口号]] [/资源路径]

URL, URI的子集
scheme://主机名[:端口号] [/资源路径]


rewrite regex replacement [flag];
    regex: 匹配URI的正则. 匹配不包含host和后面的参数
    replacement: 匹配成功后替换URI被截取的字符串. 如果该字符串以http和https开头则不继续向下对URI处理, 而是直接将重写的URI返回个客户端
    flag: last | break | redirect | permanent 
    
    
http://test.com/source?name=ming&age=2
rewrite接收的URI为/source, 不包含http://text.com和name=ming&age=2


rewrite tests.com http://test.com/home;
# 默认情况下, 接收的URI不包含请求URL后面的参数
# $request_uri? 可以将后面的参数传给新的URI
rewrite tests.com http://test.com/home$requrest_uri? permancent;


last: 
1. 终止在本location块中处理接收的URI
2. 并将重写后的URI重新在server块中执行
location / {
    # 如果第1个匹配成功并处理, 则不会使用第2个匹配, 并且让server中所有location重新处理新的URI
    rewrite ^(/tests/.*)/media/(.*)\..*$ $1/mp3/$2.mp3 last;
    rewrite ^(/tests/.*)/file/(.*)\.*$ $1/mp3/$2.ra last;
}


break:
重写后的URI在location中继续处理, 新URI始终在本location中处理
location / {
    # 如果第1个匹配成功并处理, 新的URI继续在本location中使用第2行匹配
    rewrite ^(/tests/.*)/media/(.*)\..*$ $1/mp3/$2.mp3 break;
    rewrite ^(/tests/.*)/file/(.*)\.*$ $1/mp3/$2.ra break;
}


redirect:
将重写后的URI返回客户端, 状态码302


permanent:
将重写后的URI返回客户端, 状态码301
"""

""" ============================ rewrite_log
是否开启URL从写日志输出功能
rewrite_log on | off;
"""

""" ============================ set
设置新的变量
set variable value
    variable: 变量名. 使用符号$作为变量名第一个字符
    value: 可以是字符串或变量
"""

""" ============================ uninitialized_variable_warn
使用未初始化的变量时, 是否记录警告日志
uninitialized_variable_warn on | off; 
"""

""" ============================ 常用全局变量

"""

""" ============================ 域名跳转
# 客户端访问 http://jump.myweb.com 时, URL被Nginx重写为 http://www.myweb.info/ 数据由它响应
server {
    listen 80;
    server_name jump.myweb.com;
    rewrite ^/ http://www.myweb.info/;
}


# 客户端访问 http://jump.myweb.info/request 时, URL被Nginx重写为 http://jump.myweb.name/request 数据由它响应
server {
    listen 80;
    server_name jump.myweb.info jump.myweb.name;
    if ($hotst ~ myweb\.info){
        rewrite ^(.*) http://jump.myweb.name$1 permanent;
    }
}


# 客户端访问 http://jump1.myweb.name/request 和 http://jump2.myweb.name/request 时, URL被Nginx重写为 http://jump.myweb.name/request
server {
    listen 80;
    server_name jump1.myweb.name jump2.myweb.name;
    if($http_host ~* ^(.*)\.myweb\.name){
        rewrite ^(.*) http://jump.myweb.name$1;
        break;
    }
}
"""

""" ============================ 域名镜像 
讲一个完全的网站分别放置到几个服务器上, 并分别使用独立URL, 其中一个服务器上的网站叫主站, 其他为镜像网站.
    - 进项网站可以保存网页信息/历史数据放置丢失. 
    - 可以通过镜像网站提高网站在不同地区的响应速度. 
    - 平衡网站流量负载, 解决当罗带宽限制


server {
    listen 80;
    server_name mirror1.myweb.name;
    rewrite ^(.*) http://jump1.myweb.name$1 last;
}
server {
    listen 81;
    server_name mirror2.myweb.name;
    rewrite ^(.*) http://jump2.myweb.name$1 last;
}


server {
    listen 80;
    server_name jump.myweb.name;
    location ^~ / source1 {
        rewrite ^/source1(.*) http://jump.myweb.name/websrc2$1 last;
        break;
    }
    location ^~ /source2 {
        rewrite ^/source2(.*)  http://jump.myweb.name/websrc2$1 last;
        break;
    }
}
"""

""" ============================ 独立域名
为某个模块设置单独的域名

server {
    listen 80;
    server_name bbs.myweb.name;
    rewrite ^(.*) http://www.myweb.name/bbs$1 last;
    break;
}
server {
    listen 81;
    server_name home.myweb.name;
    rewrite ^(.*) http://www.myweb.name/home$1 last;
    break;
}
"""

""" ============================ 自动为结尾增加 / 
server {
    server_name www.tests.com;
    location ^~ {
        if (-d $request_filename) {
            rewrite ^/(.*)([^/])$ http://$host/$1$2/ permanent;
        }
    }
}
"""

""" ============================ 防盗链
通过检测HTTP请求头referer是不是自己站点, 但可以被修改

获取请求头referer值, 

valid_referers none | blocked | server_names | string ... ;
    none: 检测referer头域是否存在
    blocked: 检测referer头域的值是否被防火前或代理服务器删除或伪装的情况. 这种情况下该头域值不是 http 或 https 开头
    server_name: 设置一个或多个URL, 检测referer头域的值是否是这些URL中的某个, 支持通配符 * 
    

# 当请求以这些结尾时, 如果检测到referer头域中没有符合valid_referers指令配置的值, 就将URL重写
server {
    server_name www.myweb.com;
    location ~* ^.+\.(gif|jpg|png|swf|flv|rar|zip)$ {
        valid_referers none blocked server_name *. myweb.name;  
        if ($invalid_referer) {
            rewrite ^/ http://www.myweb.com/images/123.png; 
        }
    }
}
"""

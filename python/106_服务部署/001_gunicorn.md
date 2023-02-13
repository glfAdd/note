[中文文档](https://gunicorn.readthedocs.io/en/latest/)

```
Gunicorn: Python WSGI HTTP Server
可以采用不同的后台扩展接口sync, gevent, tornado等
```

##### 安装

```
pip install gunicorn
```

##### 概念

```
WSGI: Web Server Gateway Interface（web服务器网关接口），它是一种规范，web服务器和web应用程序之间的接口
uwsgi: 是一种传输协议，用于定义传输信息的类型
uWSGI: 是实现了uwsgi协议WSGI的web服务器

基于 pre-fork 模型
```

##### 部署方式

```
nginx + gunicorn + flask
```

##### gunicorn.conf

```
# 并行工作进程数
workers = 4
# 指定每个工作者的线程数
threads = 2
# 监听内网端口5000
bind = '127.0.0.1:5000'
# 设置守护进程,将进程交给supervisor管理
daemon = 'false'
# 工作模式协程
worker_class = 'gevent'
# 设置最大并发量
worker_connections = 2000
# 设置进程文件目录
pidfile = '/var/run/gunicorn.pid'
# 设置访问日志和错误信息日志路径
accesslog = '/var/log/gunicorn_acess.log'
errorlog = '/var/log/gunicorn_error.log'
# 设置日志记录水平
loglevel = 'warning'
```

##### 命令

```
gunicorn -w 4 -b 127.0.0.1:5000 运行py文件名称:Flask程序实例名
gunicorn -w 4 -b 127.0.0.1:5000 --access-logfile /log/flask.log app:app
gunicorn -h
通过gunicorn运行flask app
gunicorn test1:app
gunicorn -c ./config/gunicorn.conf main:app &


-c CONFIG                               配置文件的路径
-b ADDRESS                              ip加端口
-w INT, --workers INT                   进程的数量，默认1 
-k STRTING, --worker-class STRTING      工作模式，默认为sync异步，可以下载eventlet和gevent并指定
--threads INT                           线程数，使用指定数量的线程运行每个worker。为正整数，默认为1。
--worker-connections INT                最大客户端并发数量，默认情况下这个值为1000。
--backlog int                           未决连接的最大数量，即等待服务的客户的数量。默认2048个，一般不修改 
-p FILE, --pid FILE                     设置pid文件的文件名，如果不设置将不会创建pid文件
--access-logfile FILE                   访问日志文件
--access-logformat STRING               访问日志格式
--error-logfile FILE, --log-file FILE   错误日志文件
--log-level LEVEL                       错误日志输出等级
--limit-request-line INT                HTTP请求头的行数的最大大小，此参数用于限制HTTP请求行的允许大小，默认情况下，这个值为4094。值是0~8190的数字
--limit-request-fields INT              限制HTTP请求中请求头字段的数量。此字段用于限制请求头字段的数量以防止DDOS攻击，默认情况下，这个值为100，这个值不能超过32768
--limit-request-field-size INT          限制HTTP请求中请求头的大小，默认情况下这个值为8190字节。值是一个整数或者0，当该值为0时，表示将对请求头大小不做限制
-t INT, --timeout INT                   超过这么多秒后工作将被杀掉，并重新启动。一般设定为30秒
-D --daemon                             是否以守护进程启动，默认false
--chdir:                                在加载应用程序之前切换目录 
--graceful-timeout INT                  默认30，在超时(从接收到重启信号开始)之后仍然活着的工作将被强行杀死 一般使用默认 
--keep-alive INT                        在keep-alive连接上等待请求的秒数，默认情况下值为2。一般设定在1~5秒之间。
--reload                                默认为False。此设置用于开发，每当应用程序发生更改时，都会导致工作重新启动。
--spew                                  打印服务器执行过的每一条语句，默认False。此选择为原子性的，即要么全部打印，要么全部不打印 
--check-config                          显示现在的配置，默认值为False，即显示
-e ENV, --env ENV                       设置环境变量
```

##### 源码分析 

> https://blog.csdn.net/qq_33339479/article/details/78431209

```
基于 pre-fork worker 模型
  - 通过单独的进程来处理每条请求, 预先开启大量的进程, 等待并处理接到的请求
  - 服务器不需要等待新的进程启动而消耗时间，因而能够以更快的速度应付多用户请求
  - 服务器在遇到极大的高峰负载时仍能保持良好的性能状态。这是因为不管什么时候，只要预先设定的所有进程都已被用来处理请求时，服务器仍可追加额外的进程。
  - 缺点是，当遇到高峰负载时，由于要启动新的服务器进程，不可避免地会带来响应的延迟。

主控master进程
就是一个简单的循环, 用来不断侦听不同进程信号并作出不同的动作. 它通过一些信号管理worker进程

信号
  - HUP         重启所有的配置和所有的worker进程
  - QUIT        正常关闭，它会等待所有worker进程处理完各自的东西后关闭
  - INT/TERM    立即关闭，强行中止所有的处理
  - TTIN        增加一个worker进程
  - TTOU        减少一个worker进程
  - USR1        重新打开由master和worker所有的日志处理
  - USR2        重新运行master和worker
  - WINCH       正常关闭所有worker进程，保持主控master进程的运行
  - CHLD        在一个子进程已经中止之后，由主控master进程重启这个失效的worker进程。

同步workers
大多数情况下，采用的worker类型是同步方式，也就是说一次仅处理一个请求。这种模型方式是最简单的，因为期间发生的任何错误最多只影响到一个请求

异步worker：
  - 需要长时间阻塞调用的应用，比如外部的web service
  - 直接给internet提供服务
  - 流请求和响应
  - 长轮询
  - Web sockets

启动多少个workers
  - gunicorn只需要启用4–12个workers，就足以每秒钟处理几百甚至上千个请求
  - 在处理请求时，gunicorn依靠操作系统来提供负载均衡。通常我们推荐的worker数量是：(2 x 处理器数量) + 1
  - 应用启动之后，然后再通过TTIN和TTOU这两个信号来调整worker数量。
```

##### gunicorn 启动过程

```
首先回去调用gunicorn/app/wsgiapp中的run方法
```

##### 请求处理过程

```
1. gunicorn 会启动一组 worker进程
2. 所有worker进程公用一组listener，
3. 在每个worker中为每个listener建立一个wsgi server。
4. 每当有HTTP链接到来时，wsgi server创建一个协程来处理该链接，协程处理该链接的时候，先初始化WSGI环境，然后调用用户提供的app对象去处理HTTP请求。

基于 pre-fork worker 模型, 有1个管理进程和几个的工作进程
管理进程:master
工作进程:worker

创建完所有的worker后，worker和master各自进入自己的消息循环
  - master的事件循环就是收收信号，管理管理worker进程
  - worker进程的事件循环就是监听网络事件并处理（如新建连接，断开连接，处理请求发送响应等等），所以真正的连接最终是连到了worker进程上

worker种类
  - ggevent
  - geventlet
  - gtornado
  
ggevent
每个ggevent worker启动的时候会启动多个server对象
worker首先为每个listener创建一个server对象, 每个server对象都运行在一个单独的gevent pool对象中。真正等待链接和处理链接的操作是在server对象中进行的。

WSGI SERVER
真正等待链接和处理链接的操作是在gevent的WSGIServer 和 WSGIHandler中进行的
WSGIServer 实际上是创建一个协程去处理该套接字，在WSGIServer中，一个协程单独负责一个HTTP链接
```

### 问题

##### 部署时问题

```
问题:
gunicorn 部署的flask, 内网可以访问, 但外网不能
解决办法:
gunicorn -w 4 -b 0.0.0.0:9019 main:app --log-level=debug &
    在上线之后，应该不暴露Flask，而是监听127.0.0.1，让代理服务器，比如Nginx，把外部请求，转发给Flask，才是最安全的
    否则暴露的Flask，很容易受到DDOS攻击
```


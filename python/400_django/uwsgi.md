```
pip install uwsgi


```

uwsgi.ini

```ini
[uwsgi]
;项目根目录
chdir = /..../project
;指定wsgi模块下的application对象
module = project.wsgi:application
;对本机8000端口提供服务
socket = 127.0.0.1:8000
;主进程
master = true

;;多站模式
;vhost = true
;;多站模式时不设置入口模块和文件
;no-site = true
;;子进程数
;workers = 2
;;退出、重启时清理文件
;reload-mercy = 10
;vacuum = true
;max-requests = 1000
;limit-as = 512
;buffer-size = 30000
;;pid文件，用于下脚本启动、停止该进程
;pidfile = /var/run/uwsgi9090.pid
;;日志文件
;daemonize = 项目根目录/run.log
;;不记录正常信息，只记录错误信息
;disable-logging = true
```


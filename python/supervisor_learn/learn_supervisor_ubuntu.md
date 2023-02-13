##### 安装

```
文档地址: http://supervisord.org/

aptitude install supervisor

# 查看安装的版本
supervisord -version
```

##### 命令

```bash
# 启动服务
$ systemctl start supervisor

# 设为开机自启动
$ systemctl enable supervisor

$ supervisord -c /etc/supervisord.conf
```

##### 编辑配置文件

```
centos 安装以后是 
3.4.0
[include]
files = supervisord.d/*.ini


ubuntu 安装以后是 
4.2.1
[include]
files = /etc/supervisor/conf.d/*.conf


文件格式相同, 将后后缀修改该即可
```

##### 创建配置文件(没实验)

```
echo_supervisord_conf > /etc/supervisor/supervisord.conf
```

##### 管理员页面

```
修改该配置文件
[inet_http_server]
port=0.0.0.0:9001
username=xxx
password=xxx

如果想所有的ip都能访问ip改为 0.0.0.0
浏览器打开 http://127.0.0.1:9001
```

##### supervisorctl

```
> status    # 查看程序状态
> stop       # 关闭程序
> start       # 启动程序
> restart    # 重启程序
> reread    ＃ 读取有更新（增加）的配置文件，不会启动新添加的程序
> update    ＃ 重启配置文件修改过的程序
```


##### 安装

```
yum install supervisor
apt-get install supervisor


supervisor配置文件叫supervisord.conf，supervisord和supervisorctl共用一个配置文件，
如果应用启动时，没有使用-c选项，应用会按照指定顺序寻找supervisord.conf文件：
$CWD/supervisord.conf
$CWD/etc/supervisord.conf
/etc/supervisord.conf
/etc/supervisor/supervisord.conf (since Supervisor 3.3.0)
../etc/supervisord.conf (Relative to the executable)
../supervisord.conf (Relative to the executable)
```

##### 问题 1: 安装后无法启动

- 启动时报错

  ```
  Traceback (most recent call last):
    File "/usr/bin/supervisorctl", line 5, in <module>
      from pkg_resources import load_entry_point
    File "/usr/local/python38/lib/python3.8/site-packages/pkg_resources/__init__.py", line 3267, in <module>
      def _initialize_master_working_set():
    File "/usr/local/python38/lib/python3.8/site-packages/pkg_resources/__init__.py", line 3241, in _call_aside
      f(*args, **kwargs)
    File "/usr/local/python38/lib/python3.8/site-packages/pkg_resources/__init__.py", line 3279, in _initialize_master_working_set
      working_set = WorkingSet._build_master()
    File "/usr/local/python38/lib/python3.8/site-packages/pkg_resources/__init__.py", line 573, in _build_master
      ws.require(__requires__)
    File "/usr/local/python38/lib/python3.8/site-packages/pkg_resources/__init__.py", line 891, in require
      needed = self.resolve(parse_requirements(requirements))
    File "/usr/local/python38/lib/python3.8/site-packages/pkg_resources/__init__.py", line 777, in resolve
      raise DistributionNotFound(req, requirers)
  pkg_resources.DistributionNotFound: The 'supervisor==3.4.0' distribution was not found and is required by the application
  ```

- 原因

  ```
  supervisor 只支持 python2, python3 会造成启动失败
  ```

- 解决办法: 指定 supervisor 使用的python 版本

  ```
  修改 /usr/bin/supervisord 和 /usr/bin/supervisorctl 
  
  将 
  #!/usr/bin/python
  改为
  #!/usr/bin/python2
  ```

##### 命令

```
    systemctl enable supervisord        # 开机自启动
    systemctl stop supervisord
    systemctl start supervisord
    systemctl status supervisord
    systemctl reload supervisord
    systemctl restart supervisord

supervisord参数:
    -c	--configuration	FILENAME	设置配置文件路径
    -h	--help		打印用法信息并退出
    -i	--interactive		执行命令后进入命令行交互模式
    -s	--serverurl	URL	监控服务器正在监听的URL
    -u	--username	USERNAME	用于服务器身份验证的用户名
    -p	--password	PASSWORD	用于服务器身份验证的密码
    -r	--history-file		保留readline历史记录，若readline可用。


supervisorctl 管理配置的应用
    status theprogramname
    start theprogramname
    stop theprogramname
    stop all
    restart theprogramname
    reload                    加载最新配置文件并重启
    update                    根据最新配置文件启动最新配置或有改动的进程
    shutdown

    restart <name>	        重启名为name的进程
    restart <gname>:*	    重启组名为gname中的所有进程
    restart <name> <name>	重启多个进程或多个组
    restart all	            重启所有进程

启动命令:
    supervisorctl -c /etc/supervisord.conf    指定配置文件
    supervisorctl -s http://localhost:7001    指定端口号
```


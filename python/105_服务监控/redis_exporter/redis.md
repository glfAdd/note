## redis_exporter

##### 安装

```
# github地址: https://github.com/oliver006/redis_exporter/releases
# 默认 redis_exporter 端口为 9121
$ wget https://github.com/oliver006/redis_exporter/releases/download/v1.24.0/redis_exporter-v1.24.0.linux-amd64.tar.gz
```

##### 启动

```
# 帮助
$ ./redis_exporter --help
# 查看版本
$ ./redis_exporter -version
# 启动 redi s_exporter 登陆 redis
$ nohup ./redis_exporter > /dev/null 2>&1 &
$ ./redis_exporter redis//localhost:6379 & -web.listenaddress 192.168.0.103:9121
    -redis.addr string：Redis实例的地址，可以使一个或者多个，多个节点使用逗号分隔，默认为 "redis://localhost:6379"
    -redis.password string：Redis实例的密码		
    -web.listen-address string：服务监听的地址，默认为 0.0.0.0:9121
```

##### redis_exporter_conf.conf 

```
[program:redis_exporter]
directory=/opt/redis_exporter-v1.24.0.linux-amd64
command=/opt/redis_exporter-v1.24.0.linux-amd64/redis_exporter
autostart=false
autorestart=false
user=glfadd
log_stdout=true
log_stderr=true
redirect_stderr = true
stdout_logfile_maxbytes = 20MB
stdout_logfile_backups = 20     
stdout_logfile = /opt/logs/supervisord_redis_exporter.log
```

## prometheus 设置

```
scrape_configs:
  - job_name: Redis
    static_configs:
      - targets:
          - 'localhost:9121'
```

## granfana 设置 dashboard

```
https://grafana.com/grafana/dashboards/763
```




## 安装 redis_exporter

##### 安装

```bash
# github地址: https://github.com/oliver006/redis_exporter/releases
# 默认 redis_exporter 端口为 9121
$ wget https://github.com/oliver006/redis_exporter/releases/download/v1.24.0/redis_exporter-v1.24.0.linux-amd64.tar.gz
```

##### 启动

```bash
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

##### 进程管理

```
参考: https://doc.sensorsdata.cn/pages/viewpage.action?pageId=157329254
或使用其他方式
```

## consul 注册服务

##### 在 redis_exporter 目录下创建 json文件

> 1. 文件名任意, 最好能有一定的意义, 例如: redis_exporter_123.123.123.123.json
>
> 2. app, team, project 根据情况自定义, 
>
> 3. ID 和 Name 在 consul 必须全局唯一, 推荐名称中加入 IP 地址
>
> 4. Tags 里面的 "redis" 不能删除, 如需要可以增加其他的
> 5. HTTP里面的 IP 换成当前服务器的 IP
> 6. Interval 可以根据需要调整

```json
{
  "ID": "redis_id_123.123.123.123",
  "Name": "redis_name_123.123.123.123",
  "Tags": [
    "redis"
  ],
  "Address": "localhost",
  "Port": 9121,
  "Meta": {
    "app": "redis_elk",
    "team": "redis_elk",
    "host": "123.123.123.123"
  },
  "EnableTagOverride": false,
  "Check": {
    "HTTP": "http://123.123.123.123:9121/metrics",
    "Interval": "10s"
  },
  "Weights": {
    "Passing": 10,
    "Warning": 1
  }
}
```

##### 将 json 文件配置注册到 consul 

```bash
redis_exporter_123.123.123.123.json 是 json 文件的名字, 改成实际的名字


$ curl --request PUT --data @redis_exporter_123.123.123.123.json http://consul所在服务器IP:8500/v1/agent/service/register\?replace-existing-checks\=1
```






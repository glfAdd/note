##### 参考

```
https://songjiayang.gitbooks.io/prometheus/content/configuration/scrape_configs.html
https://blog.csdn.net/qq_32486597/article/details/110383388
```

## 安装 go 语言环境(不是必须的)

> 官网: https://golang.google.cn/dl/

```bash
$ wget https://golang.google.cn/dl/go1.16.5.linux-amd64.tar.gz
$ tar zxf go1.16.5.linux-amd64.tar.gz 

# 编辑 /etc/profile.d/my_env.sh 文件, 添加如下内容
export PATH=$PATH:/opt/go/bin

# 使配置文件生效
$ source /etc/profile

# 验证是否成功
$ bin/go version
```

## 安装 prometheus

##### 下载

```bash
官网
https://prometheus.io/download/

wget https://github.com/prometheus/prometheus/releases/download/v2.28.0/prometheus-2.28.0.linux-amd64.tar.gz
```

##### 配置文件分块

| 块             | 作用                                                         |
| -------------- | ------------------------------------------------------------ |
| global         | 全局配置                                                     |
| alerting       | 片段指定报警配置， 这里主要是指定prometheus将报警规则推送到指定的alertmanager实例地址 |
| rule_files     | 指定报警规则文件， prometheus根据这些规则信息，会推送报警信息到alertmanager中 |
| scrape_configs | 定抓取配置，prometheus的数据采集通过此片段配置               |

##### 检测配置文件是否有问题

```bash
$ ./promtool check config prometheus.yml
Checking prometheus.yml
  SUCCESS: 0 rule files found
```

##### 启动

```bash
$ ./prometheus -h
$ ./prometheus --version
$ ./prometheus --config.file=prometheus.yml & 

# 允许热加载
$ ./prometheus --web.enable-admin-api --web.enable-lifecycle --config.file=prometheus.yml
$ /opt/prometheus-2.28.0.linux-amd64/prometheus --web.enable-admin-api --web.enable-lifecycle --config.file=/opt/prometheus-2.28.0.linux-amd64/prometheus.yml



$ ./prometheus --config.file="prometheus.yml" --web.listen-address="0.0.0.0:9090" --storage.tsdb.path="/data/prometheus" --storage.tsdb.retention.time=15d --web.enable-lifecycle &

# --config.file="prometheus.yml"  #指定配置文件路径
# --web.listen-address="0.0.0.0:9090"  #指定服务端口
# --storage.tsdb.path="/data/prometheus"  #指定数据存储路径
# --storage.tsdb.retention.time=15d  #数据保留时间
# --collector.systemd #开启systemd的服务状态监控，开启后在WEB上可以看到多出相关监控项
# --collector.systemd.unit-whitelist=(sshd|nginx).service  #对systemd具体要监控的服务名
# --web.enable-lifecycle  #开启热加载配置
```

##### prometheus_conf.conf

```
[program:prometheus]
directory=/opt/prometheus-2.28.0.linux-amd64
command=/opt/prometheus-2.28.0.linux-amd64/prometheus --web.enable-admin-api --web.enable-lifecycle --config.file=/opt/prometheus-2.28.0.linux-amd64/prometheus.yml
autostart=false
autorestart=false
user=glfadd
log_stdout=true
log_stderr=true
redirect_stderr = true
stdout_logfile_maxbytes = 20MB
stdout_logfile_backups = 20     
stdout_logfile = /opt/logs/supervisord_prometheus.log
```

##### 热加载

- 问题1

  ```
  问题:
  shell 发送热加载请求报错
  Lifecycle API is not enabled.%  
  
  
  解决办法:
  curl -X POST http://127.0.0.1:9090/-/reload
  ```

##### Web UI

```
http://localhost:9090
```

```
[program:prometheus]
directory=/opt/prometheus-2.28.0.linux-amd64
command=/opt/prometheus-2.28.0.linux-amd64/prometheus --web.enable-admin-api --web.enable-lifecycle --config.file=/opt/prometheus-2.28.0.linux-amd64/prometheus.yml
autostart=false
autorestart=false
user=glfadd
log_stdout=true
log_stderr=true
redirect_stderr = true
stdout_logfile_maxbytes = 20MB
stdout_logfile_backups = 20     
stdout_logfile = /opt/logs/supervisord_prometheus.log
```

##### 问题1

```
访问 http://localhost:9090 显示报错
Warning: Error fetching server time: Detected 52.74799990653992 seconds time difference between your browser and the server. Prometheus relies on accurate time and time drift might cause unexpected query results.


原因
需要同步时钟


解决办法
$ ntpdate time3.aliyun.com
```



## 数据查询

> https://yunlzheng.gitbook.io/prometheus-book/parti-prometheus-ji-chu/quickstart/prometheus-quick-start/promql_quickstart

## targets

```

```

## global

> 这里的配置项可以单独配置在某个job中

| 参数                     | 作用                |
| ------------------------ | ------------------- |
| scrape_interval: 15s     | 每15s采集一次数据   |
| evaluation_interval: 15s | 每15s做一次告警检测 |
| scrape_timeout:10s       | 采集数据超时时间    |
| external_labels          |                     |

```yml
global:
  scrape_interval: 15s
  evaluation_interval: 15s
```

## scrape_configs

##### 参数说明

| 参数           | 类型 | 作用                                                   |
| -------------- | ---- | ------------------------------------------------------ |
| job_name       | str  | 任务目标名, 可以理解成分组, 对应 Prometheus 的 Targets |
| static_configs | dict | 静态指定服务job                                        |
| params         |      | 指定url参数                                            |
| scheme         | str  | 指定采集使用的协议，http或者https                      |
| metric_path    | str  | 指定抓取metrics数据的路径，默认是targets+'/metrics'    |
| targets        | list | 监控目标访问地址, 是exporters 的 ip 和 端口            |

##### 静态规则

> 没有设置自动发现, 这种情况下增加主机需要自行修改规则，每次静态规则添加都要重启 prometheus 服务,不利于运维自动化。

```yml
scrape_configs:
  - job_name: prometheus
    static_configs:
      - targets:
          - 'localhost:9090'
```

##### 服务发现(常用)

> 基于文件的服务发现方式, 将要新的target信息以 yaml 或 json 文件格式添加到target文件中 ，prometheus会定期从指定文件中读取target信息并更新

```yml
scrape_configs:
  - job_name: test_node
    metrics_path: /metrics
    scheme: http
    file_sd_configs:
      - files:
          - /opt/prometheus-2.28.0.linux-amd64/custom_config/node.json
```

- json 文件

  ```json
  [
    {
      "targets": [
        "localhost:9100"
      ],
      "labels": {
        "instance": "xubuntu"
      }
    }
  ]
  ```

##### 例子

```yml
global:
  scrape_interval: 15s
  evaluation_interval: 15s


scrape_configs:
  - job_name: test_node
    metrics_path: /metrics
    scheme: http
    file_sd_configs:
      - files:
          - /opt/prometheus-2.28.0.linux-amd64/custom_config/node.json

```

## 插件

> https://www.cnblogs.com/you-men/p/13081972.html

##### 常用

| 范围     | 常用 Exporter                                                |
| :------- | :----------------------------------------------------------- |
| 数据库   | MySQL Exporter, Redis Exporter, MongoDB Exporter, MSSQL Exporter等 |
| 硬件     | Apcupsd Exporter，IoT Edison Exporter， IPMI Exporter, Node Exporter等 |
| 消息队列 | Beanstalkd Exporter, Kafka Exporter, NSQ Exporter, RabbitMQ Exporter等 |
| 存储     | Ceph Exporter, Gluster Exporter, HDFS Exporter, ScaleIO Exporter等 |
| HTTP服务 | Apache Exporter, HAProxy Exporter, Nginx Exporter等          |
| API服务  | AWS ECS Exporter， Docker Cloud Exporter, Docker Hub Exporter, GitHub Exporter等 |
| 日志     | Fluentd Exporter, Grok Exporter等                            |
| 监控系统 | Collectd Exporter, Graphite Exporter, InfluxDB Exporter, Nagios Exporter, SNMP Exporter等 |
| 其他     | Blockbox Exporter, JIRA Exporter, Jenkins Exporter， Confluence Exporter等 |

# 使用中问题

##### 问题 1

- 描述

  ```
  Warning: Error fetching server time: Detected 40.69199991226196 seconds time difference between your browser and the server. Prometheus relies on accurate time and time drift might cause unexpected query results.
  ```

- 解决办法

  ```bash
  $ ntpdate time3.aliyun.com
  ```

##### 问题 2


##### 是什么

```
Blackbox Exporter 是 Prometheus 社区提供的 官方黑盒监控解决方案,其允许用户通过 http\HTTPS\DNS\TCP\ICMP的方式对网络进行探测.

HTTP 测试
定义 Request Header 信息
判断 Http status / Http Respones Header / Http Body 内容
TCP 测试
业务组件端口状态监听
应用层协议定义与监听
ICMP 测试
主机探活机制
POST 测试
接口联通性
SSL 证书过期时间
证书到期时间表达式
```

##### 安装

- 下载 blackbox_exporter

  ```bash
  # githu 地址: 
  	https://github.com/prometheus/blackbox_exporter/releases
  	https://github.com/prometheus/blackbox_exporter/blob/master/CONFIGURATION.md
  # 默认端口 9115
  
  $ wget https://github.com/prometheus/blackbox_exporter/releases/download/v0.19.0/blackbox_exporter-0.19.0.linux-amd64.tar.gz
  ```

- 启动 blackbox_exporter

  ```bash
  $ ./blackbox_exporter --help
  $ ./blackbox_exporter --version
  ```

##### 启动

```bash
$ /opt/blackbox_exporter-0.19.0.linux-amd64/blackbox_exporter --config.file=/opt/blackbox_exporter-0.19.0.linux-amd64/blackbox.yml
```

##### 热加载

```bash
# blackbox_exporter 通过配置文件和命令行标志进行配置, 可以运行时动态的重新加载配置文件，当重新加载配置文件失败时，不影响在运行的配置 
# blackbox_exporter 的超时时间由Prometheus配置中的scrape_timeout自动确定，略微减少以允许网络延迟.默认是10s

$ curl -XPOST http://127.0.0.1:9115/-/reload
```

##### blackbox_exporter.conf

```ini
[program:blackbox_exporter]
directory=/opt/blackbox_exporter-0.19.0.linux-amd64
command=/opt/blackbox_exporter-0.19.0.linux-amd64/blackbox_exporter --config.file=/opt/blackbox_exporter-0.19.0.linux-amd64/blackbox.yml
autostart=false
autorestart=false
user=glfadd
log_stdout=true
log_stderr=true
redirect_stderr = true
stdout_logfile_maxbytes = 20MB
stdout_logfile_backups = 20     
stdout_logfile = /opt/logs/supervisord_blackbox_exporter.log
```

## prometheus 设置

##### blackbox_exporter 参数

```
# 探针的详细配置,最多只能配置其中一个
[ http: <http_probe> ]
[ tcp: <tcp_probe> ]
[ dns: <dns_probe> ]
[ icmp: <icmp_probe> ]

HTTP 测试： 定义 Request Header 信息、判断 Http status / Http Respones Header / Http Body 内容
TCP 测试：   业务组件端口状态监听、应用层协议定义与监听
ICMP 测试： 主机探活机制
POST 测试： 接口联通性
SSL证书过期时间
```

| 参数    | 说明                              |
| ------- | --------------------------------- |
| modules | 每一个 modules 就是一个探针配置   |
| prober  | 探针类型: http https tcp dns icmp |
| timeout | 超时时间, 默认单位秒              |
| http    | http 探针详细配置                 |
| tcp     | tcp 探针详细配置                  |
| dns     | dns 探针详细配置                  |
| icmp    | icmp 探针详细配置                 |



```yml
modules:
  http_2xx:
    prober: http
  http_post_2xx:
    prober: http
    http:
      method: POST
  tcp_connect:
    prober: tcp
  pop3s_banner:
    prober: tcp
    tcp:
      query_response:
      - expect: "^+OK" # 期望
      tls: true
      tls_config:
        insecure_skip_verify: false
  ssh_banner:
    prober: tcp
    tcp:
      query_response:
      - expect: "^SSH-2.0-"
      - send: "SSH-2.0-blackbox-ssh-check"
  irc_banner:
    prober: tcp
    tcp:
      query_response:
      - send: "NICK prober"
      - send: "USER prober prober prober :prober"
      - expect: "PING :([^ ]+)"
        send: "PONG ${1}"
      - expect: "^:[^ ]+ 001"
  icmp:
    prober: icmp
```

##### 测试

- target参数指定探测目标 baidu.com
- 探针的探测结果通过Metrics的形式返回

```bash
$ curl http://localhost:9115/probe?module=http_2xx&target=baidu.com
$ curl http://localhost:9115/probe?module=http_2xx&target=localhost:5000


# HELP probe_dns_lookup_time_seconds Returns the time taken for probe dns lookup in seconds
# TYPE probe_dns_lookup_time_seconds gauge
probe_dns_lookup_time_seconds 0.027555836
# HELP probe_duration_seconds Returns how long the probe took to complete in seconds
# TYPE probe_duration_seconds gauge
probe_duration_seconds 0.068977904
# HELP probe_failed_due_to_regex Indicates if probe failed due to regex
# TYPE probe_failed_due_to_regex gauge
probe_failed_due_to_regex 0
# HELP probe_http_content_length Length of http content response
# TYPE probe_http_content_length gauge
probe_http_content_length 81
# HELP probe_http_duration_seconds Duration of http request by phase, summed over all redirects
# TYPE probe_http_duration_seconds gauge
probe_http_duration_seconds{phase="connect"} 0.011073403
probe_http_duration_seconds{phase="processing"} 0.029884008
probe_http_duration_seconds{phase="resolve"} 0.027555836
probe_http_duration_seconds{phase="tls"} 0
probe_http_duration_seconds{phase="transfer"} 0.000147436
# HELP probe_http_last_modified_timestamp_seconds Returns the Last-Modified HTTP response header in unixtime
# TYPE probe_http_last_modified_timestamp_seconds gauge
probe_http_last_modified_timestamp_seconds 1.26330408e+09
# HELP probe_http_redirects The number of redirects
# TYPE probe_http_redirects gauge
probe_http_redirects 0
# HELP probe_http_ssl Indicates if SSL was used for the final redirect
# TYPE probe_http_ssl gauge
probe_http_ssl 0
# HELP probe_http_status_code Response HTTP status code
# TYPE probe_http_status_code gauge
probe_http_status_code 200
# HELP probe_http_uncompressed_body_length Length of uncompressed response body
# TYPE probe_http_uncompressed_body_length gauge
probe_http_uncompressed_body_length 81
# HELP probe_http_version Returns the version of HTTP of the probe response
# TYPE probe_http_version gauge
probe_http_version 1.1
# HELP probe_ip_addr_hash Specifies the hash of IP address. It's useful to detect if the IP address changes.
# TYPE probe_ip_addr_hash gauge
probe_ip_addr_hash 3.00078313e+09
# HELP probe_ip_protocol Specifies whether probe ip protocol is IP4 or IP6
# TYPE probe_ip_protocol gauge
probe_ip_protocol 4
# HELP probe_success Displays whether or not the probe was a success
# TYPE probe_success gauge
probe_success 1
```

##### 编辑 prometheus.yml

- 指定1 个探针类型,  1 个探测目标

  ```yml
  global:
    scrape_interval: 15s
    evaluation_interval: 15s
  scrape_configs:
    - job_name: server1_http2xx_probe
      params:
        module:
          - http_2xx
        target:
          - localhost:5000
      metrics_path: /probe
      static_configs:
        - targets:
            - 'localhost:9115'
  ```

- 指定多个探针类型

  ```
  探针类型 http_2xx, targets 定义采集任务的探测站点, 在采集样本数据之前通过 relabel_configs 对采集任务进行动态配置
  
  1. 将 target 实例的地址 __address__，写入__param_target标签中
  2. 获取 __param_target 的值，并覆写到 instance 标签中.
  3. 覆写 target 实例的 __address__ 标签值为 BlockBox Exporter实例的访问地址
  
  
  ????
  	__param_<name> 形式的标签表示在采集任务时会在请求目标地址中添加<name>参数，等同于params的设置
  ```

  

  ```yml
  scrape_configs:
    - job_name: blackbox
      metrics_path: /probe
      params:
        module:
          - http_2xx
      static_configs:
        - targets:
            - 'http://localhost:5000'
      relabel_configs: # 采集数据之前可以使用 relabel_configs 进行重新标记
        - source_labels: # 指定需要被action所操作的原标签
            - __address__
          target_label: __param_target # 赋值的目标字段
        - source_labels:
            - __param_target
          target_label: instance
        - target_label: __address__
          replacement: 'localhost:9115'
  ```


- 主机存活状态

  ```yml
  
    - job_name: 'node_status'
      metrics_path: /probe
      params:
        module: [icmp]
      static_configs:
        - targets: ['localhost']
          labels:
            instance: 'node_status'
            group: 'node'
      relabel_configs:
        - source_labels: [__address__]
          target_label: __param_target
        - target_label: __address__
          replacement: 127.0.0.1:9115
  ```
  
- 监控主机端口存活状态

  ```yml
    - job_name: 'port_status'
      metrics_path: /probe
      params:
        module: [tcp_connect]
      static_configs:
        - targets: ['127.0.0.1:9100','127.0.0.1:9090']
          labels:
            instance: 'port_status'
            group: 'tcp'
      relabel_configs:
        - source_labels: [__address__]
          target_label: __param_target
        - target_label: __address__
          replacement: 127.0.0.1:9115
  
  ```
  
- 监控网站状态

  ```yml
    - job_name: web_status
      metrics_path: /probe
      params:
        module: [http_2xx]
      static_configs:
        - targets: ['https://www.baidu.com']
          labels:
            instance: web_status
            group: web
      relabel_configs:
        - source_labels: [__address__]
          target_label: __param_target
        - target_label: __address__
          replacement: 127.0.0.1:9115
  ```


## http 探针

##### HTTP 探针默认设置

- 使用 HTTP GET 的方式对目标服务进行探测
- 只会对HTTP返回状态码进行校验，如果状态码为2XX（200 <= StatusCode < 300）则表示探测成功，并且探针返回的指标probe_success值为1. 否则失败

```yml
modules:
  http_2xx_example:
    prober: http
    http: null
```

##### 自定义设置

- Blockbox Exporter内置了对basic_auth的支持

| http 选项             | 说明                         |
| --------------------- | ---------------------------- |
| tls_config            | 指定 https 相关的证书信息    |
| valid_http_versions   | 指定 http 版本               |
| valid_status_codes    | 指定状态码                   |
| body                  | 指定请求body                 |
| basic_auth            | basic_auth 认证信息          |
| fail_if_ssl           | true / false                 |
| fail_if_not_ssl       | true / false                 |
| preferred_ip_protocol | 指定互联网协议版本 ip4 / ip6 |



```yml
modules:
  http_post_2xx:
    prober: http
    timeout: 5s
    http:
      method: POST
      valid_http_versions: ["HTTP/1.1", "HTTP/2"]
      valid_status_codes: []
      headers:
        Content-Type: application/json
      body: '{}'
      basic_auth:
        username: "username"
        password: "mysecret"
      tls_config:
        ca_file: "/certs/my_cert.crt"

```

## 接口监控

```yml
scrape_configs:
  - job_name: port_status
    metrics_path: /probe
    params:
      module:
        - tcp_connect
    static_configs:
      - targets:
          - 'localhost:5000'
        labels:
          instance: port_status
          group: tcp
    relabel_configs:
      - source_labels:
          - __address__
        target_label: __param_target
      - target_label: __address__
        replacement: 'localhost:9115'

```



## granfana 设置 dashboard

- 安装 granfana 需要的插件到指定路径

  ```bash
  $ ./grafana-cli --pluginsDir=/opt/grafana-8.0.3/data/plugins plugins install grafana-piechart-panel
  
  $ 重启服务
  ```

- 安装 dashboard

  ```
  https://grafana.com/grafana/dashboards/9965
  ```

  



> https://blog.csdn.net/qq_43190337/article/details/100577728

> https://www.cnblogs.com/you-men/p/13081972.html



```
promethues + python + flask监控后端服务状态
https://www.jianshu.com/p/19442595e886


使用Python和Flask编写Prometheus监控
https://www.cnblogs.com/-wenli/p/13973067.html
```

```

blackbox_exporter+grafana+prometheus监控主机存活，端口存活及网站状态
https://blog.csdn.net/qq_43190337/article/details/100577728
```

## 问题

##### 部分 http_2xx 返回的 probe_success 是 0, 但实际接口可以正常返回

```
(base) gong@10-10-167-37 [03:04:25 PM] [/opt/blackbox_exporter-0.19.0.linux-amd64] 
-> % curl http://localhost:9115/probe\?module\=http_2xx\&target\=http://localhost:11469/home
# HELP probe_dns_lookup_time_seconds Returns the time taken for probe dns lookup in seconds
# TYPE probe_dns_lookup_time_seconds gauge
probe_dns_lookup_time_seconds 0.000194603
# HELP probe_duration_seconds Returns how long the probe took to complete in seconds
# TYPE probe_duration_seconds gauge
probe_duration_seconds 0.002226177
# HELP probe_failed_due_to_regex Indicates if probe failed due to regex
# TYPE probe_failed_due_to_regex gauge
probe_failed_due_to_regex 0
# HELP probe_http_content_length Length of http content response
# TYPE probe_http_content_length gauge
probe_http_content_length 4
# HELP probe_http_duration_seconds Duration of http request by phase, summed over all redirects
# TYPE probe_http_duration_seconds gauge
probe_http_duration_seconds{phase="connect"} 8.2587e-05
probe_http_duration_seconds{phase="processing"} 0.001439443
probe_http_duration_seconds{phase="resolve"} 0.000194603
probe_http_duration_seconds{phase="tls"} 0
probe_http_duration_seconds{phase="transfer"} 0.000268001
# HELP probe_http_redirects The number of redirects
# TYPE probe_http_redirects gauge
probe_http_redirects 0
# HELP probe_http_ssl Indicates if SSL was used for the final redirect
# TYPE probe_http_ssl gauge
probe_http_ssl 0
# HELP probe_http_status_code Response HTTP status code
# TYPE probe_http_status_code gauge
probe_http_status_code 401
# HELP probe_http_uncompressed_body_length Length of uncompressed response body
# TYPE probe_http_uncompressed_body_length gauge
probe_http_uncompressed_body_length 4
# HELP probe_http_version Returns the version of HTTP of the probe response
# TYPE probe_http_version gauge
probe_http_version 1
# HELP probe_ip_addr_hash Specifies the hash of IP address. It's useful to detect if the IP address changes.
# TYPE probe_ip_addr_hash gauge
probe_ip_addr_hash 9.9635399e+07
# HELP probe_ip_protocol Specifies whether probe ip protocol is IP4 or IP6
# TYPE probe_ip_protocol gauge
probe_ip_protocol 4
# HELP probe_success Displays whether or not the probe was a success
# TYPE probe_success gauge
probe_success 0
```

- 原因

  ```
  探测时默认使用ipv6，探测不支持ipv6的站点都会显示失败，因此在配置时改成了ipv4
  ```

- 解决办法

  ```yml
  modules:
    http_2xx:
      prober: http
      http:
        method: GET
        preferred_ip_protocol: "ip4"
  ```

  

## http code

##### 指标

```
成功时
probe_success 1
probe_http_status_code 200


失败时
probe_success 0
probe_http_status_code 404
```



## 属性查找

```
每次发送请求时间间隔设置





```








##### 参考

```
https://www.applenice.net/2020/07/20/Kafka-Notes-09/
https://cloud.tencent.com/developer/article/1658936
```

##### 安装

- 下载 blackbox_exporter

  ```bash
  # githu 地址: 
  	https://github.com/danielqsj/kafka_exporter
  # 默认端口 9308
  $ wget https://github.com/danielqsj/kafka_exporter/releases/download/v1.3.1/kafka_exporter-1.3.1.illumos-amd64.tar.gz
  ```
  
- 启动 blackbox_exporter

  ```bash
  $ nohup ./kafka_exporter --kafka.server=localhost:9092 > /dev/null 2>&1 &
  
  # web 页面查看
  http://IP:9308/metrics
  ```

##### 热加载 prometheus

```bash
$ curl -X POST http://127.0.0.1:9090/-/reload
```

##### prometheus 设置

```yml
  - job_name: kafka_exporter
    static_configs:
    - targets: ['localhost:9308']
```

##### grafana dashboard

```
7589
```


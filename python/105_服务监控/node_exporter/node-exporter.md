##### 安装

- 下载 node-exporter

  ```bash
  # github 地址: https://github.com/prometheus/node_exporter/releases
  # 默认node-exporter端口为9100
  $ wget https://github.com/prometheus/node_exporter/releases/download/v1.1.2/node_exporter-1.1.2.linux-amd64.tar.gz
  ```

- 启动 node_exporter

  ```bash
  $ ./node_exporter &
  ```

- 编辑 prometheus 配置文件中加入 mysql 监控并重启

  ```bash
    - job_name: 'mysql'
      static_configs:
      - targets: ['localhost:9100']
        labels:
          instance: mysql
  ```

- granfana dashboard

  ```
  https://grafana.com/grafana/dashboards/12633
  ```

##### node_exporter_conf.conf

```
[program:node_exporter]
directory=/opt/node_exporter-1.1.2.linux-amd64
command=/opt/node_exporter-1.1.2.linux-amd64/node_exporter
autostart=false
autorestart=false
user=glfadd
log_stdout=true
log_stderr=true
redirect_stderr = true
stdout_logfile_maxbytes = 20MB
stdout_logfile_backups = 20     
stdout_logfile = /opt/logs/supervisord_node_exporter.log
```


##### 参考

```
https://www.cnblogs.com/caoweixiong/p/12156590.html
```

##### 安装

```bash
# githu 地址: https://github.com/prometheus-community/elasticsearch_exporter/releases
# 默认端口

$ wget https://github.com/prometheus-community/elasticsearch_exporter/releases/download/v1.2.1/elasticsearch_exporter-1.2.1.linux-amd64.tar.gz
```

##### 运行

```
$ ./elasticsearch_exporter --es.uri http://localhost:9200 


--es.uri         　　　　默认http://localhost:9200，连接到的Elasticsearch节点的地址（主机和端口）
--es.all                默认flase，如果为true，则查询群集中所有节点的统计信息，而不仅仅是查询我们连接到的节点。
--es.cluster_settings   默认flase，如果为true，请在统计信息中查询集群设置
--es.indices            默认flase，如果为true，则查询统计信息以获取集群中的所有索引。
--es.indices_settings   默认flase，如果为true，则查询集群中所有索引的设置统计信息。
--es.shards             默认flase，如果为true，则查询集群中所有索引的统计信息，包括分片级统计信息（意味着es.indices = true）。
--es.snapshots          默认flase，如果为true，则查询集群快照的统计信息。
```

##### elasticsearch_exporter_conf.conf

```
[program:elasticsearch_exporter]
directory=/opt/elasticsearch_exporter-1.2.1.linux-amd64
command=/opt/elasticsearch_exporter-1.2.1.linux-amd64/elasticsearch_exporter --es.uri http://localhost:9200 
autostart=false
autorestart=false
user=glfadd
log_stdout=true
log_stderr=true
redirect_stderr = true
stdout_logfile_maxbytes = 20MB
stdout_logfile_backups = 20     
stdout_logfile = /opt/logs/supervisord_elasticsearch_exporter.log
```


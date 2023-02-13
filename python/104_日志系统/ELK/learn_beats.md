```
参考
https://www.jianshu.com/p/009286216560

```

- Logstash: 是一个灵活的数据传输和处理系统，在beats出来之前，还负责进行数据收集。Logstash的任务，就是将各种各样的数据，经过配置转化规则，统一化存入Elasticsearch。使用Ruby开发的Logstash在灵活性上，非常出色。不过性能一直是被诟病的问题。
- Beats 是 ELK Stack 技术栈中负责单一用途数据采集并推送给 Logstash 或 Elasticsearch 的轻量级产品。 

## Beats 官方集成组件

##### filebeat

- 应用于日志收集场景的实现
- filebeat 异常中断重启后会继续上次停止的位置。（通过${filebeat_home}\data\registry文件来记录日志的偏移量）
- 智能调节传输速度，防止logstash、es 过载. Filebeat 使用压力敏感协议(backpressure-sensitive)来传输数据，在 logstash 忙的时候，Filebeat 会减慢读取-传输速度，一旦 logstash 恢复，则 Filebeat 恢复原来的速度

##### Metricbeat

- Metricbeat 是一个轻量级的系统级性能指标监控工具。收集CPU，内存，磁盘等系统指标和 Redis，nginx等各种服务的指标
- 通过在Linux，Windows，Mac上部署Metricbeat，可以收集cpu，内存，文件系统，磁盘IO，网络IO等统计信息。
- 支持采集 Apache, NGINX, MongoDB, MySQL, PostgreSQL, Redis, and ZooKeeper等服务的指标。零依赖，只需要在配置文件中启用即可
- 如果你使用Docker管理你的服务。可以在该主机上单独起一个Metricbeat容器，他通过从proc文件系统中直接读取cgroups信息来收集有关Docker主机上每个容器的统计信息。不需要特殊权限访问Docker API
- Metricbeats是ELK Stack全家桶中的一员，可以和ELK无缝协同工作。例如使用Logstash二次处理数据，用Elasticsearch分析，或者用Kibana创建和共享仪表盘。

##### Packetbeat

- Packetbeat 是一个轻量级的网络数据包分析工具, 可以通过抓包分析应用程序的网络交互。并且将抓到的数据发送到 Logstash 或者Elasticsearch。 
- Packetbeat 轻松的实时监控并解析像HTTP这样的网络协议。以了解流量是如何经过你的网络。Packetbeat 是被动的，不增加延迟开销，无代码侵入，不干涉其他基础设施。
- Packetbeat是一个库，支持多种应用程序层协议，如 http、dns、mysal、icmp、postgres、redis 等。
- Packetbeat可以让你实时在目标服务器上进行抓包-解码-获取请求和响应-展开字段-将json格式的结果发送到Elasticsearch。
- Packetbeat是ELK Stack全家桶中的一员，可以和ELK无缝协同工作。例如使用Logstash二次处理数据，用Elasticsearch分析，或者用Kibana创建和共享仪表盘。

##### Winlogbeat

- Winlogbeat 是一个轻量级的 Windows 事件日志收集工具。将 Windows 事件发送到 Elasticsearc h或者Logstash
- Winlogbeat是ELK Stack全家桶中的一员，可以和ELK无缝协同工作。例如使用Logstash二次处理数据，用Elasticsearch分析，或者用Kibana创建和共享仪表盘。

##### Heartbeat

- Heartbeat 是一个心跳检测工具，主要监控服务的可用性。监控给定的地址是否可用
- 不管你是测试同主机服务还是其他网络服务，Heartbeat都可以很轻松的生成正常运行时间和响应时间数据。而且修改配置不需要重启Heartbeat
- Heartbeat通过ICMP,TCP,和HTTP进行ping，也支持TLS，身份验证，和代理。由于简单的DNS解析，你可以监控所有负载均衡的服务
- 可以修改配置文件后自动加载
- Heartbeat是ELK Stack全家桶中的一员，可以和ELK无缝协同工作

##### 可以自己创建 beat




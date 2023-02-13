## 概述

##### 优点

```
可扩展性：采用高可扩展性的分布式系统架构设计，可以支持每日 TB 级别的新增数据。
使用简单：通过用户图形界面实现各种统计分析功能，简单易用，上手快。
快速响应：从日志产生到查询可见，能达到秒级完成数据的采集、处理和搜索统计。
界面炫丽：Kibana 界面上，只需要点击鼠标，就可以完成搜索、聚合功能，生成炫丽的仪表板。
强大的搜索: 可以以分布式搜索的方式快速检索
```

##### 缺点

    1、三个独立的系统，没有统一的部署、管理工具，用户需要分别部署及管理这三套系统
    2、复杂业务下权限的分组管理，企业肯定希望每个业务部分看自身的，但又存在矛盾点，企业想看汇总情况。
    3、安全漏洞，之前乌云网站曾爆出Elasticsearch存在严重的安全漏洞。
    4、不进行深度开发的话，数据挖掘能力弱
##### 分类

- ELK
  - ElasticSearch + Logstash + Kibana
- Elastic Stack
  - ElasticSearch + Logstash + Kibana + Beats

## 组件简介

##### Elasticsearch

- 分布式搜索引擎。具有高可伸缩、高可靠、易管理等特点。可以用于全文检索、结构化检索和分析，并能将这三者结合起来

##### Logstash

- 主要作用是收集分布在各处的 log 并进行处理

##### Kibana

- 是为 Elasticsearch 开发的前端 GUI，让用户可以很方便的以图形化的接口查询 Elasticsearch 中存储的数据，同时也提供了各种分析的模块，比如构建 dashboard 的功能

##### Beats

- beats是一组轻量级采集程序的统称, 包含
  - filebeat: 进行文件和目录采集，主要用于收集日志数据。
  - metricbeat: 进行指标采集，指标可以是系统的，也可以是众多中间件产品的，主要用于监控系统和软件的性能。
  - packetbeat: 通过网络抓包、协议分析，对一些请求响应式的系统通信进行监控和数据收集，可以收集到很多常规方式无法收集到的信息。
  - Winlogbeat: 专门针对windows的event log进行的数据采集。
  - Heartbeat: 系统间连通性检测，比如icmp, tcp, http等系统的连通性监控
  - 其他社区的beat

##### Filebeat

- 轻量级数据收集引擎。基于原先 Logstash-fowarder 的源码改造出来。换句话说：Filebeat就是新版的 Logstash-fowarder，也会是 ELK Stack 在 shipper 端的第一选择。
- Filebeat 是构建于 beats 之上的，应用于日志收集场景的实现，用来替代 Logstash Forwarder 的下一代 Logstash 收集器，是为了更快速稳定轻量低耗地进行收集工作，它可以很方便地与 Logstash 还有直接与 Elasticsearch 进行对接
- 特性:
  - filebeat 异常中断重启后会继续上次停止的位置。（通过${filebeat_home}\data\registry文件来记录日志的偏移量）
  - 智能调节传输速度，防止logstash、es 过载
  - 

##### Filebeats 与 Logstash

- Filebeats 功能比较单一，它仅仅只能收集本地的 log，但并不能对收集到的 Log 做什么处理，所以通常 Filebeats 通常需要将收集到的 log 发送到 Logstash 做进一步的处理。

##### Logstash 与 Fluentd

- Filebeats、Logstash、Elasticsearch 和 Kibana 是属于同一家公司的开源项目, Fluentd 则是另一家公司的开源项目

- Logstash 与 Fluentd: Logstash 和 Fluentd 都具有收集并处理 log 的能力，但 Logstash 消耗更多的 memory

## 架构

##### 简单架构

![简单架构](./image_简单架构.png)

- 这种架构下我们把 Logstash 实例与 Elasticsearch 实例直接相连。Logstash 实例直接通过 Input  插件读取数据源数据(比如 Java 日志， Nginx 日志等)，经过 Filter 插件进行过滤日志，最后通过 Output 插件将数据写入到 ElasticSearch 实例中
- 日志的收集、过滤、输出等功能，主要由这三个核心组件组成 Input 、Filter、Output。
  - Input：输入，输入数据可以是 File 、 Stdin（直接从控制台输入） 、TCP、Syslog 、Redis 、Collectd 等
  - Filter：过滤，将日志输出成我们想要的格式
  - Output：输出，输出目标可以是 Stdout （直接从控制台输出）、Elasticsearch 、Redis 、TCP 、File 等

##### 集群架构

![集群架构](./image_集群架构.png)

- 这种架构采用多个 Elasticsearch 节点组成 Elasticsearch 集群，由于 Logstash 与 Elasticsearch 采用集群模式运行，集群模式可以避免单实例压力过重的问题，同时在线上各个服务器上部署 Logstash Agent，来满足数据量不大且可靠性不强的场景。
- 数据收集端：每台服务器上面部署 Logstash Shipper Agent 来收集当前服务器上日志，日志经过 Logstash Shipper 中 Input插件、Filter插件、Output 插件传输到 Elasticsearch 集群。
- 数据存储与搜索：Elasticsearch 配置默认即可满足，同时我们看数据重要性来决定是否添加副本，如果需要的话，最多一个副本即可。
- 数据展示：Kibana 可以根据 Elasticsearch 的数据来做各种各样的图表来直观的展示业务实时状况。
- 架构缺点
  - 消耗服务器资源：Logstash 的收集、过滤都在服务器上完成，这就造成服务器上占用系统资源较高、性能方面不是很好，调试、跟踪困难，异常处理困难；
  - 数据丢失：大并发情况下，由于日志传输峰值比较大，没有消息队列来做缓冲，就会导致 Elasticsearch 集群丢失数据。

##### 引入消息队列

![引入消息队列](./image_引入消息队列.png)

- 这种架构多个数据首先通过 Lostash Shipper Agent 来收集数据，然后经过 Output 插件将数据投递到 Kafka 集群中，这样当遇到 Logstash 接收数据的能力超过 Elasticsearch 集群处理能力的时候，就可以通过队列就能起到削峰填谷的作用， Elasticsearch 集群就不存在丢失数据的问题。
- 这种架构适合较大集群的应用部署，通过消息队列解决了消息丢失、网络堵塞的问题。

- 日志服务场景中，使用比较多的两种消息队列为 Kafka 和 Redis, 建议采用 Kafka 。主要从下面两个方面考虑
  - 数据丢失：Redis 队列多用于实时性较高的消息推送，并不保证可靠。Kafka保证可靠但有点延时；
  - 数据堆积：Redis 队列容量取决于机器内存大小，如果超过设置的Max memory，数据就会抛弃。Kafka 的堆积能力取决于机器硬盘大小。

- 架构缺点
  - Logstash shipper 收集数据同样会消耗 CPU 和内存资源
  - 不支持多机房部署。

##### 引入Filebeat

![引入Filebeat](./image_引入Filebeat.png)

- 如果日志的量很大，Logstash 会遇到资源占用高的问题，为解决这个问题，我们引入了Filebeat。Filebeat 是基于 logstash-forwarder 的源码改造而成，用 Golang 编写，无需依赖 Java 环境，效率高，占用内存和 CPU 比较少，非常适合作为 Agent 跑在服务器上。

  


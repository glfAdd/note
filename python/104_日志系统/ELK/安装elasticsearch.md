

> https://michael728.github.io/2020/04/12/elk-es-install/
>
> 

##### 下载地址

```
官网下载: https://www.elastic.co/cn/downloads/elasticsearch

wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.12.1-linux-x86_64.tar.gz
```

##### 目录结构

```
├── bin # 二进制脚本存放目录
├── config # 配置文件
├── data  # 节点上分配的每个 index/分片 的数据文件
├── jdk
├── lib
├── LICENSE.txt
├── logs
├── modules
├── NOTICE.txt
├── plugins # 插键文件存放的位置
└── README.asciidoc
```

##### 单机运行

```
./bin/elasticsearch 
./bin/elasticsearch -d -p pid
	-d 守护程序运行
	-p 将进程 ID 记录到 pid 文件

4. 检查运行状态
curl -X GET "localhost:9200/?pretty"
```

##### 配置文件分类

```
elasticsearch.yml 			ES 的配置
jvm.options 				ES JVM 配置
log4j2.properties 			ES 日志配置
```

##### elasticsearch.yml

| 属性名                             | 说明                                                         | 默认值                    |
| ---------------------------------- | ------------------------------------------------------------ | ------------------------- |
| cluster.name                       | 集群名称, 一个节点只能加入一个集群中                         | elasticsearch             |
| node.name                          | 节点的名称。用来提供可读性高的 ES 实例名称                   | 机器的 hostname           |
| path.conf                          | 设置配置文件的存储路径，tar或zip包安装默认在es根目录下的config文件夹，rpm安装默认在/etc/ elasticsearch |                           |
| path.data                          | 设置索引数据的存储路径，可以设置多个存储路径，用逗号隔开     | es根目录下的data文件夹    |
| path.logs                          | 设置日志文件的存储路径                                       | es根目录下的logs文件夹    |
| path.plugins                       | 设置插件的存放路径                                           | es根目录下的plugins文件夹 |
| bootstrap.memory_lock              | 设置为true可以锁住ES使用的内存，避免内存进行swap             |                           |
| network.host                       | 访问的地址。默认仅绑定在回环地址 127.0.0.1 和 [::1]。如果需要从其他服务器上访问以及多态机器搭建集群，我们需要设定 ES 运行绑定的 Host，节点需要绑定非回环的地址。建议设置为主机的公网 IP 或 0.0.0.0 |                           |
| http.port                          | 这是指 http 端口，如果采用 REST API 对接 ES，那么就是采用的 http 协议 | 9200                      |
| transport.port                     | 集群结点之间通信端口                                         | 9300-9400                 |
| discovery.seed_hosts               | 用于启动当前节点时，发现其他节点的初始列表                   |                           |
| discovery.zen.ping.timeout         |                                                              | 3                         |
| discovery.zen.minimum_master_nodes |                                                              |                           |
| cluster.initial_master_nodes       |                                                              |                           |

```
ransport.port
REST 客户端通过 HTTP 将请求发送到您的 Elasticsearch 集群，但是接收到客户端请求的节点不能总是单独处理它，通常必须将其传递给其他节点以进行进一步处理。它使用传输网络层（transport networking layer）执行此操作。传输层用于集群中节点之间的所有内部通信，与远程集群节点的所有通信，以及 Elasticsearch Java API 中的 TransportClient。

transport.port 绑定端口范围。默认为 9300-9400




cluster.initial_master_nodes





```





```
# 修改 elasticsearch.yml 文件设置跨域访问
http.cors.enabled: true
http.cors.allow-origin: "*"
#绑定的ip：默认只允许本机访问，修改为0.0.0.0后则可以远程访问
network.host: 0.0.0.0
http.port: 9200
# 数据目录位置
path.data: /home/es/data
# 日志目录位置
path.logs: /home/es/logs
```



##### jvm.options

```
# 修改 jvm.options 文件设置使用内存大小, 默认使用内存多
-Xms1g
-Xmx2g
```


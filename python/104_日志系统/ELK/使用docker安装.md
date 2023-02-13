## 安装问题解决办法

##### 查看docker日志

```
docker logs elasticsearch
docker logs -f elasticsearch
```

##### 容器无法正常启动, 修改容器中的文件()

- 方式1: 将容器中的文件 cp 出来, 修改后, 再 cp 到容器中

- 方式2: 直接修改容器里的文件

```
1. 查看容器的详细信息
docker inspect elasticsearch | grep MergedDir

2. MergedDir 为容器在本机的目录, 需要root用户才能查看, 里面的目录和进入docker后看到的目录结构完全相同
```

##### 查看ip

```
docker inspect centos101|grep IP
```

##### docker不知道文件装在哪里, 使用搜素

```
find / -name kibana.yml
```

##### docker 挂载文件

```
https://blog.csdn.net/weixin_42134094/article/details/112110730
```

## elasticsearch

##### 安装 elasticsearch

```
1. 通过镜像，启动一个容器，并将9200和9300端口映射到本机（ElasticSearch的默认端口是9200，我们把宿主环境9200端口映射到Docker容器中的9200端口）
docker run -d --name elasticsearch --net glfaddnetwork --ip 172.19.0.20 -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" elasticsearch:7.12.0

2. 测试是否可用
curl 172.19.0.20:9200
或
http://172.19.0.20:9200

3. 容器中的安装目录
/usr/share/elasticsearch
```

##### 设置跨域

- 挂载一个文件夹时, 用 vim 或者 cat 修改里面的文件, docker 里面会同步
- 挂载文件时, .................

```
不设置跨域管理页面无法访问容器

1. 进入容器
docker exec -it elasticsearch bash

2. 进入配置文件目录 config 修改配置文件 elasticsearch.yml 在结尾增加
http.cors.enabled: true
http.cors.allow-origin: "*"

3. 重启容器
```

##### 问题1

```
访问报错
{
	"error": "Content-Type header [application/x-www-form-urlencoded] is not supported",
	"status": 406
}


原因: 
此原因时由于ES增加了安全机制，进行严格的内容类型检查，严格检查内容类型也可以作为防止跨站点请求伪造攻击的一层保护


解决办法1:
1. 进入docker head插件安装目录
2. 编辑 /usr/src/app/_site/vendor.js修改共有两处：
    (1) 6886行 /contentType: "application/x-www-form-urlencoded 
    改成 contentType: "application/json;charset=UTF-8" 
    (2) 7574行 var inspectData = s.contentType === "application/x-www-form-urlencoded" && 
    改成 var inspectData = s.contentType === "application/json;charset=UTF-8" &&
    
解决办法2:
curl 增加参数 -H "Content-Type: application/json"
```

##### 安装分词器插件(验证分词器效果)

```
ES自带的分词器对中文分词不友好, 所以我们下载开源的IK分词器来解决这个问题
Elasticsearch的版本和IK分词器的版本需要保持一致, 否则在重启的时候会失败

1. github中找到与 elasticsearch 相同的版本号
https://github.com/medcl/elasticsearch-analysis-ik/releases

2. 进入容器, 安装分词器, 重启
elasticsearch-plugin install https://github.com/medcl/elasticsearch-analysis-ik/releases/download/v7.12.0/elasticsearch-analysis-ik-7.12.0.zip
```

## elasticsearch-head

##### 使用 google chrome 的 ElasticSearch Head 插件

```
浏览器 app store 安装
```

##### 安装

```
1. 拉去镜像启动容器
docker run -d --name elasticsearch_admin --net glfaddnetwork --ip 172.19.0.21 -p 9100:9100 mobz/elasticsearch-head:5

2. 验证安装是否成功
http://172.19.0.21:9100

3. 汉化
修改浏览器的语言选项, 将简体中文调整到顶部


3. 使用教程
https://www.cnblogs.com/tdp0108/p/11105848.html
https://www.cnblogs.com/WinterPasser/p/14203370.html
https://www.cnblogs.com/xuwenjin/p/8792919.html

github地址
https://github.com/mobz/elasticsearch-head


```

## Kibana

##### 安装kibana

```
docker run --net glfaddnetwork --ip 172.19.0.22 --name kibana --link es:elasticsearch -p 5601:5601 -d kibana:7.12.0
其中 --link es:elasticsearch中的es是Docker中Elasticsearch容器名, 你也可以替换成对应的容器ID

# 如果 link 失败，可以启动后在设置
docker run --net glfaddnetwork --ip 172.19.0.22 --name kibana -p 5601:5601 -d kibana:7.12.0

#测试是否成功
http://172.19.0.22:5601
```

##### 问题

```
1. 进入docker不是root用户
docker exec -u 0 -it kibana bash

2. 浏览器访问 http://172.19.0.22:5601 显示 "Kibana server is not ready yet"
修改kibana配置文件kibana.yml, 指定正确的ip地址
elasticsearch.hosts: [ "http://172.19.0.20:9200" ]
```

##### 汉化

```
修改 容器 kibana.yml 配置文件, 在末尾添加(注意冒号后一定要有空格), 重启
i18n.locale: zh-CN
```

## logstash

##### 安装logstash

- logstash.conf 文件

```
input {
    tcp {
        port => 5044
        codec => "json"
    }
}
filter{

}
output {
    # 这个是logstash的控制台打印（进行安装调试的开启，稍后成功后去掉这个配置即可）
    stdout {
        codec => rubydebug
    }
    # elasticsearch配置
    elasticsearch {
        hosts => ["http://172.19.0.20:9200"]
    }
}
```

- 创建 logstash.yml配置文件(暂时不用)

```
path.config: /usr/share/logstash/conf.d/*.conf
path.logs: /var/log/logstash
```

- 启动容器

```
方式1: 直接启动, 启动后进入容器修改配置文件
docker run -d -p 5044:5044 --name logstash --net glfaddnetwork --ip 172.19.0.23 logstash:7.12.0

方式2: 启动的时候导入配置文件(当文件修改以后容器会不会自动重启???)
docker run -d -p 5044:5044 -v logstash.conf:/usr/share/logstash/pipeline/logstash.conf -v logstash.yml:/usr/share/logstash/config/logstash.yml --name logstash --net glfaddnetwork --ip 172.19.0.23 logstash:7.12.0


```

## filebeat

- 配置文件 filebeat.yml

```
# 日志输入配置
filebeat.inputs:
- type: log
  enabled: true
  paths:
  # 需要收集的日志所在的位置，可使用通配符进行配置
  #- /data/elk/*.log
  - /logs/*/*.log

#日志输出配置(采用 logstash 收集日志，5044为logstash端口)
output.logstash:
  hosts: ['172.19.0.23:5044']
```

##### 安装filebeat(docker 环境)

```
docker pull elastic/filebeat:7.12.0


docker run --name filebeat --net glfaddnetwork --ip 172.19.0.24 -d --link logstash -v ~/elk/yaml/filebeat.yml:/usr/share/filebeat/filebeat.yml -v ~/elk/logs/:/home/logs/ elastic/filebeat:7.12.0

docker run --name filebeat --net glfaddnetwork --ip 172.19.0.24 -d -v /home/glfadd/Desktop/logs:/logs/ elastic/filebeat:7.12.0

docker run --name filebeat --net glfaddnetwork --ip 172.19.0.24 -d elastic/filebeat:7.12.0


```










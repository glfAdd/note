##### 查看集群的健康状况

```
http://127.0.0.1:9200 
http://127.0.0.1:9200/_cat
http://127.0.0.1:9200/_cat/health?v

Green 即最佳状态
Yellow  即数据和集群可用，但是集群的备份有的是坏的
Red 数据和集群都不可用

curl -X GET "localhost:9200/?pretty"
```

##### 查看集群的节点

```
http://127.0.0.1:9200/_cat/?v
```

##### 概念

- ElasticSearch是一个高度可扩展的开源搜索引擎并使用REST API

- Elastic 本质上是一个分布式数据库，允许多台服务器协同工作，每台服务器可以运行多个 Elastic 实例。单个 Elastic 实例称为一个节点（node）。一组节点构成一个集群（cluster）。
- Elastic 会索引所有字段，经过处理后写入一个反向索引（Inverted Index）。查找数据的时候，直接查找该索引。每个 Index （即数据库）的名字必须是小写。

- Index 里面单条的记录称为 Document（文档）。许多条 Document 构成了一个 Index。Document 使用 json 格式表示. 同一个 Index 里面的 Document，不要求有相同的结构（scheme），但是最好保持相同，这样有利于提高搜索效率

- url 规则

```
http://localhost:9200/<index>/<type>/[<id>]
```

##### 新建和删除 Index

```
1. 查看当前节点的所有 Index。
返回 "health status index uuid pri rep docs.count docs.deleted store.size pri.store.size" 表示集群中没有索引
$ curl -X GET 'http://localhost:9200/_cat/indices?v'
	
	
2. 新建 Index，可以直接向 Elastic 服务器发出 PUT 请求。下面的例子是新建一个名叫weather的 Index
返回 JSON 对象，里面的acknowledged字段表示操作成功。	
$ curl -X PUT 'localhost:9200/weather'
	服务器返回一个 JSON 对象，里面的acknowledged字段表示操作成功。


3. 发出 DELETE 请求，删除这个 Index
$ curl -X DELETE 'localhost:9200/weather'
```

##### 中文分词设置

```
1. 新建一个名称为accounts的 Index，里面有一个名称为person的 Type。
2. person有三个字段 user, title, desc. 这三个字段都是中文，而且类型都是文本（text），所以需要指定中文分词器，不能使用默认的英文分词器。
3. analyzer是字段文本的分词器，search_analyzer是搜索词的分词器。ik_max_word分词器是插件ik提供的，可以对文本进行最大数量的分词。

curl -X PUT '127.0.0.1:9200/accounts' -d '
{
  "mappings": {
    "person": {
      "properties": {
        "user": {
          "type": "text",
          "analyzer": "ik_max_word",
          "search_analyzer": "ik_max_word"
        },
        "title": {
          "type": "text",
          "analyzer": "ik_max_word",
          "search_analyzer": "ik_max_word"
        },
        "desc": {
          "type": "text",
          "analyzer": "ik_max_word",
          "search_analyzer": "ik_max_word"
        }
      }
    }
  }
}'
```

##### 添加数据

- 如果没有先创建 Index，添加数据，Elastic 也不会报错，而是直接生成指定的 Index
- put: 方式需要指定 id, id 可以是任务字符串

```
curl -H "Content-Type: application/json" -X PUT 'localhost:9200/accounts/person/1' -d '
{
  "user": "张三",
  "title": "工程师",
  "desc": "数据库管理"
}'

{
    "_index": "accounts",
    "_type": "person",
    "_id": "1",
    "_version": 1,
    "result": "created",
    "_shards": {
        "total": 2,
        "successful": 1,
        "failed": 0
    },
    "_seq_no": 1,
    "_primary_term": 1
}
```

- post: 不指定 id, 会随机生成

```
curl -H "Content-Type: application/json" -X POST 'localhost:9200/accounts/person' -d '
{
  "user": "李四",
  "title": "工程师",
  "desc": "系统管理"
}'

{
    "_index": "accounts",
    "_type": "person",
    "_id": "lpq_DXkBFbt9iVSlapYK",
    "_version": 1,
    "result": "created",
    "_shards": {
        "total": 2,
        "successful": 1,
        "failed": 0
    },
    "_seq_no": 0,
    "_primary_term": 1
}
```

##### 查看记录

- 发送 get 请求

```
curl 'localhost:9200/accounts/person/1?pretty=true'

# pretty=true表示以易读的格式返回
# found字段, true表示查询成功, false表示查询失败 
# _source字段返回原始记录
# _version 版本号
# result 操作类型包含: updated, created, deleted

{
    "_index": "accounts",
    "_type": "person",
    "_id": "1",
    "_version": 1,
    "_seq_no": 1,
    "_primary_term": 1,
    "found": true,
    "_source": {
        "user": "张三",
        "title": "工程师",
        "desc": "数据库管理"
    }
}


{
  "_index" : "accounts",
  "_type" : "person",
  "_id" : "3",
  "found" : false
}
```

##### 删除记录

- DELETE

```
curl -X DELETE '127.0.0.1:9200/accounts/person/1'

{
    "_index": "accounts",
    "_type": "person",
    "_id": "1",
    "_version": 6,
    "result": "updated",
    "_shards": {
        "total": 2,
        "successful": 1,
        "failed": 0
    },
    "_seq_no": 8,
    "_primary_term": 1
}
```

##### 更新记录

- PUT

##### 搜素数据

```
curl 'localhost:9200/accounts/person/_search'

# took 该操作的耗时（单位为毫秒）
# timed_out字段表示是否超时
# hits字段表示命中的记录
# total：返回记录数，本例是2条。
max_score：最高的匹配程度，本例是1.0。
hits：返回的记录组成的数组。





{
    "took": 292,
    "timed_out": false,
    "_shards": {
        "total": 1,
        "successful": 1,
        "skipped": 0,
        "failed": 0
    },
    "hits": {
        "total": {
            "value": 4,
            "relation": "eq"
        },
        "max_score": 1.0,
        "hits": [
            {
                "_index": "accounts",
                "_type": "person",
                "_id": "lpq_DXkBFbt9iVSlapYK",
                "_score": 1.0,
                "_source": {
                    "user": "李四",
                    "title": "工程师",
                    "desc": "系统管理"
                }
            }
        ]
    }
}


```






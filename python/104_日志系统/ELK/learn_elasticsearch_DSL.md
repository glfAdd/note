> https://www.cnblogs.com/sddai/p/11061412.html
>
> 

> Elasticsearch提供了基于JSON的完整查询DSL（特定于域的语言）来定义查询

##### 查询数据

```
http://localhost:9200/okr-2021-05/_search

GET
```

##### 查询数量

```
http://localhost:9200/okr-2021-05/_count

GET
```

## match

##### match_all

```
# 查询所有数据
{
  "query": {
    "match_all": {}
  }
}
​```
{
  "query": {
    "match_all": {}
  }
}
```

```json
# 返回的部分数据
...
{
  "_index": "okr-2021-05",
  "_type": "_doc",
  "_id": "EXHOaXkBxObgUrTAxsS8",
  "_score": 1,
  "_source": {
    "host_ip": "123.2.45.1",
    "@timestamp": "2021-05-14T07:37:07.244Z",
    "message": "2021-05-14 15:35:39,182 - INFO - test.py - root - 35 - {'request_id': 1620977739182, 'ip_addr': '127.0.0.1', 'action': 'error', 'url': 'http://test.test.test/1974782'}",
    "deploy_id": "ork_01",
    "ip": "127.0.0.1",
    "app_id": "okr"
  }
}
...
```

##### match

- 查询 @timestamp 包含 2021-05-14 并按 _id 升序

```json
{
  "query": {
    "match": {
      "@timestamp": "2021-05-14"
    }
  },
  "sort": [
    {
      "_id": "asc"
    }
  ]
}
```

##### 分页查询

- from 从第几个开始, 最开始时0
- size 返回几个结果

```JSON
# 从第4个开始, 返回2个
{
  "query": {
    "match_all": {}
  },
  "from": 4,
  "size": 2
}
```

##### 指定查询结果字段

- 默认的字段如何隐藏 ????

```json
# 查询语句
# 指定 _source 只返回 host_ip 和 deploy_id
{
  "query": {
    "match_all": {}
  },
  "_source": [
    "host_ip",
    "deploy_id"
  ],
  "from": 4,
  "size": 2
}
```

```json
# 返回片段
...
{
  "_index": "okr-2021-05",
  "_type": "_doc",
  "_id": "F3HOaXkBxObgUrTAxsTC",
  "_score": 1,
  "_source": {
    "host_ip": "123.2.45.1",
    "deploy_id": "ork_01"
  }
}
...
```

##### match - operator

- match 查询还可以接受 operator 操作符作为输入参数，默认情况下该操作符是 or 。我们可以将它修改成 and 让所有指定词项都必须匹配 (????什么意思)

```json
# 默认情况下 "request_id 1620977761612" 会被拆成两个单词去分别匹配, 匹配上任意一个算匹配上这条数据
# 改成 AND 以后变成了, 拆完的两个单词必须同时都匹配上才算匹配上这条数据
{
  "query": {
    "match": {
      "message": {
        "query": "request_id 1620977761612",
        "operator": "and"
      }
    }
  }
}
```

##### match - minimum_should_match

- (这个半分比是怎么计算的? 四舍五入?)

```json
# "request_id 1620977761612" 被拆分后分别匹配, 必须满足一定的百分比才匹配上这条数据
{
  "query": {
    "match": {
      "message": {
        "query": "request_id 1620977761612",
        "minimum_should_match": "90%"
      }
    }
  }
}
```

##### 运算符

| 符号      | 注释 |
| --------- | ---- |
| range     |      |
| gte       | >=   |
| gt        | >    |
| lte       | <=   |
| lt        | <    |
| boost     |      |
| format    |      |
| relation  |      |
| time_zone |      |

```

```

- 查询 request_id 大于等于 1621407300703 的数据

```json
{
  "query": {
    "range": {
      "request_id": {
        "gte": "1621407300703"
      }
    }
  }
}
```

## multi_match

```




```



## term

```







```



## 布尔查询

> https://www.cnblogs.com/ljhdo/p/5040252.html

- 将多个查询条件组合在一起，还可以将查询的结果和结果的评分组合在一起
- 布尔查询把多个子查询组合（combine）成一个布尔表达式，所有子查询之间的逻辑关系是与 and. 只有当一个文档满足布尔查询中的所有子查询条件时，ElasticSearch引擎才认为该文档满足查询条件
- 布尔查询支持的子查询类型共有四种

| 事件         | 描述                                                         |
| ------------ | ------------------------------------------------------------ |
| must     | 子句（查询）必须出现在匹配的文档中，并将有助于得分。         |
| filter   | 子句（查询）必须出现在匹配的文档中。 然而不像 must 此查询的分数将被忽略。 |
| should   | 子句（查询）应出现在匹配文档中。 在布尔查询中不包含 must 或 filter 子句，一个或多个should 子句必须有相匹配的文件。 匹配 should 条件的最小数目可通过设置minimum_should_match 参数。 |
| must_not | 子句（查询）不能出现在匹配的文档中。 |

- 布尔查询的四个子句，都可以是数组字段
- 建议使用过滤（filter）子句和must_not子句，这两个子句属于过滤上下文（Filter Context），经常使用filter子句，使得ElasticSearch引擎自动缓存数据，当再次搜索已经被缓存的数据时，能够提高查询性能；由于过滤上下文不影响查询的评分，而评分计算让搜索变得复杂，消耗更多CPU资源，因此，filter和must_not查询减轻搜索的工作负载。

##### 评分计算

```
bool 查询会为每个文档计算相关度评分 _score ，再将所有匹配的 must 和 should 语句的分数 _score 求和，最后除以 must 和 should 语句的总数。

must_not 语句不会影响评分；它的作用只是将不相关的文档排除。
```

##### 控制精度

- 默认情况下，没有 should 语句是必须匹配的，只有当没有 must 语句的时候，至少有一个 should 语句必须匹配
- 通过 minimum_should_match 参数控制需要匹配的 should 语句的数量，它既可以是一个绝对的数字，又可以是个百分比

```json
# 必须满足should子句中两个以上的条件
{
  "query": {
    "bool": {
      "should": [
        { "match": { "title": "brown" }},
        { "match": { "title": "fox"   }},
        { "match": { "title": "dog"   }}
      ],
      "minimum_should_match": 2 
    }
  }
}
```






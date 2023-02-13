> 百分比变化 https://blog.csdn.net/Gamer_gyt/article/details/53381279?t=1505398850708&utm_medium=distribute.pc_relevant.none-task-blog-baidujs_title-0&spm=1001.2101.3001.4242
>
> 百分比变化 http://www.voidcn.com/article/p-zqnxyyhn-ev.html
>
> 百分比变化 https://blog.csdn.net/getyouwant/article/details/52299208
>
> 官网文档: https://elastalert.readthedocs.io/en/latest/recipes/writing_filters.html#writingfilters
>
> https://www.cnblogs.com/duanxz/p/11859307.html

##### todo list

```
【ElasticSearch】史上最全最常用工具清单
告警工具可以选择 Alert Management、Elasticsearch watch、elastalert等，各有优缺点，有的是收费的，有的是免费的，这里我们选择 elastalert 
https://zhuanlan.zhihu.com/p/81922802




```

## 安装

##### 安装python环境

> ElastAlert, 是Yelp 公司基于python开发的ELK 日志报警插件，Elastalert 通过查询 ElasticSearch 中的记录进行比对，通过配置报警规则对匹配规则的日志进行警报. 独立于应用程序, 架构耦合性低
>
> 需要安装的命令可以在服务的python环境中可以执行
>
> python 3.6.13

```
# github
https://github.com/Yelp/elastalert
# 文档
https://elastalert.readthedocs.io/en/latest/elastalert.html#overview

1. 下载
git clone https://github.com/Yelp/elastalert.git

2. 创建配置文件
cp config.yaml.example config.yaml 

3. 安装pip环境
pip install -r requirements.txt
pip install elastalert
```

##### config.yaml

| 参数             | 类型                   | 说明                                                         |
| ---------------- | ---------------------- | ------------------------------------------------------------ |
| rules_folder     |                        | 加载规则配置文件的路径，默认是example_rules                  |
| run_every        | seconds, minutes，days | 定时向ES发请求查询 elastalert_status 中数据                  |
| buffer_time      | seconds, minutes，days | 查询 es 匹配 rules 的数据请求里时间字段的范围，默认45分钟,  存放到 elastalert_status 中 |
| timestamp_field  |                        | 设置buffer_time时针对哪个字段，默认是@timestamp              |
| es_host          |                        |                                                              |
| es_port          |                        |                                                              |
| es_username      |                        |                                                              |
| es_password      |                        |                                                              |
| writeback_index  |                        | ElastAlert在 es 中存储数据的索引的名称                       |
| writeback_alias  |                        | 别名                                                         |
| alert_time_limit |                        | 失败警报的重试窗口.(seconds, minutes，days 等等)             |

- 例子

```
rules_folder: example_rules
run_every:
  minutes: 1
buffer_time:
  minutes: 2
es_host: localhost
es_port: 9200
#es_username: ******
#es_password: ******
writeback_index: elastalert_status
writeback_alias: elastalert_alerts
alert_time_limit:
  days: 2
```

##### rule 

- 多个type可以写在一个规则配置文件中，按顺序进行匹配

| 参数        | 类型   | 说明                                             |
| ----------- | ------ | ------------------------------------------------ |
| es_host     | string |                                                  |
| es_port     | string |                                                  |
| name        | string | 规则的唯一名称。如果相同，则elastalert不会启动。 |
| run_every   |        |                                                  |
| buffer_time |        |                                                  |
| type        | string | 数据验证方式(规则类型)                           |
| index       | string | 要查询的索引名称。默认logstash-*                 |
| filter      | list   | 相当于query查询语法，匹配信息                    |
| alter       | list   | 每个匹配项上运行的警报列表。                     |

##### example_rules 范例

```
example_spike.yaml
“峰值”规则类型的示例，它使您可以警告某个时间段内的平均事件发生率增加给定因子的时间。当在过去2个小时内发生与过滤器匹配的事件比前2个小时的事件数多3倍时，此示例将发送电子邮件警报。


example_frequency.yaml
“频率”规则类型的示例，它将在一个时间段内发生给定数量的事件时发出警报。此示例将在4小时内出现50个与给定过滤器匹配的文档时发送电子邮件。


example_change.yaml
“更改”规则类型的示例，当两个文档中的某个字段发生更改时，它将发出警报。在此示例中，当两个文档具有相同的“用户名”字段但“ country_name”字段的值不同时，会在24小时之内发送警报电子邮件。


example_new_term.yaml
“新术语”规则类型的示例，当一个或多个新值出现在一个或多个字段中时，它将发出警报。在此示例中，在示例登录日志中遇到新值（“用户名”，“计算机”）时，将发送一封电子邮件。
```

##### 在 Elasticsearch 创建索引

> ElastAlert 将有关其查询和警报的信息和元数据保存回 Elasticsearch, 它使 ElastAlert 可以重新启动并完全从中断处恢复

- 为ElastAlert 在 es 中创建索引

```
# 默认使用 config.yaml
elastalert-create-index
# 或指定配置文件
elastalert-create-index --config config.yaml

或创建5个索引
    elastalert_status_status
    elastalert_status
    elastalert_status_past
    elastalert_status_silence
    elastalert_status_error  
```

- 查看索引

```
curl 'localhost:9200/_cat/indices?v'
```

##### 索引 elastalert_status 

- ElastAlert 根据elastalert_status去确定首次启动的时候在什么时间范围内去查询，以避免重复查询。对于每个规则，它将从最近的结束时间开始查询。包括：

```
@timestamp：文件上传到Elasticsearch的时间。这是在运行查询并且已经处理结果之后。
rule_name：相应规则的名称。
starttime：查询的开始时间sadsf戳。
endtime：查询结束时间戳。
hits：查询结果的数量。                                                                                                                                                      
matches：处理命中后规则返回的匹配数。请注意，这并不一定意味着警报被触发。
time_taken：此查询运行所需的秒数。
```

##### 测试 rule

```
elastalert-test-rule example_rules/example_frequency.yaml
```

##### 运行

```
python -m elastalert.elastalert --verbose --rule example_frequency.yaml
python -m elastalert.elastalert --verbose --rule any_work_weixin.yaml

python -m elastalert.elastalert --rule example_frequency.yaml

python -m elastalert.elastalert --verbose --config ./config.yaml --rule example_frequency.yaml


#运行命令，加载所有rules
python -m elastalert.elastalert --config ./config.yaml 

参数:
--verbose 表示模式展示日志
--rule example_frequency.yaml表示只运行example_frequency.yaml这一个rule文件，如果不加该选项则会运行rules_folder下所有rule文件，上面配置中的rules_folder为默认的example_rules
```

##### filter 支持的过滤器

- 使用ElasticSearch DSL

```
query
query_string类型遵循Lucene查询格式，可用于对多个字段进行部分或完全匹配
term精确的字段匹配
terms组合多个term过滤器
range
```

## type

##### any

- 任何规则都会匹配， 查询返回的每个命中将生成一个警报

```



```

##### blacklist

- 黑名单, 将某个字段与黑名单进行比较，如果它在黑名单中则匹配

```
compare_key: "request"
blacklist:
    - /index.html        #request字段匹配有请求/index.html就报警
    - "!file /tmp/blacklist1.txt"
    - "!file /tmp/blacklist2.txt"

# compare_key: 用于与黑名单进行比较的字段名称。如果该字段为null,则将忽略这些事件
# blacklist: 列入黑名单的列表，and or
```

##### whitelist

- 白名单, 将某个字段与白名单进行比较，如果列表中不包含该字词则匹配

```
compare_key: "request"
ignore_null: "true"
whitelist:
    - /index.html        #request字段匹配过滤请求/index.html的请求
    - "!file /tmp/blacklist1.txt"
    - "!file /tmp/blacklist2.txt"

# compare_key: 用于与白名单进行比较的字段名称
# ignore_null: 如果为true,则没有compare_key字段的事件不匹配
# whitelist: 列入白名单值列表
```

##### change

- 监视某个字段并匹配该字段是否更改该

```
# compare_key: 要监视更改的字段名称。由于这是一个字符串列表，如果任何一个字段发生更改，将触发报警
# ignore_null: 没有compare_key字段的事件将不计为已更改
# query_key
# timeframe: 更改之间的最长时间，如果超过该时间将忘记旧值。再次发生改变时将不认为change
```

##### frequency

- 给定时间范围内匹配一定数量的事件时。可以基于 query_key 计数
- query_key 时什么???????

```
#Elasticsearch  机器
es_host: localhost
#Elasticsearch  端口
es_port: 9200

#是否使用ssl 链接
use_ssl: false

#如果elasticsearch 有认证，填写用户名和密码的地方
#es_username: username
#es_password: password

#rule name 必须是独一的，不然会报错，这个定义完成之后，会成为报警邮件的标题
name: xx-xx-alert

#配置的是frequency，需要两个条件满足，在相同 query_key条件下，timeframe 范围内有num_events个被过滤出来的异常
#type: frequency
type: any

#指定index，支持正则匹配，支持多个index，(逗号, 分隔)同时如果嫌麻烦直接* 也可以。
index: okr-2021-05

#时间出发的次数
num_events: 100
#和num_events参数关联，也就是说在4分钟内出发5次会报警
timeframe:
  minutes: 1

#用来拼配告警规则，elasticsearch 的query语句，支持 AND&OR等。
filter:
- query:
    query_string: 
      query: "message : * error"

alert:
- "post"

http_post_url: "http://127.0.0.1:5000/test"
http_post_static_payload:
    rule_name: alertfortest
#http_post_url: "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=ebbaa8cf-abbb-4b4e-8a38-bc1b249d741d"
#http_post_static_payload:
#  msgtype: text
#  text: 
#    content: hello
```

##### spike

- 用处比较流量突起
- 前两个timeframe时间段内的比较

```
spike_height: 前两个时间段内相差值
spike_type: up(后一个时间段比前一个时间段高，则触发报警)/down/both
timeframe:
threshold_ref: 前一个时间段内的下限，如果不达标，则不触发报警
threshold_cur: 当前时间段内的下限，如果不达标，则不触发报警



```

##### flatline

- 水平线以下触发报警,  当threshold一段时间内事件总数低于给定时间时，此规则匹配

```
threshold: 不触发报警的最小事件数
timeframe:
use_count_query: 如果为true，elastalert将使用count api轮询elasticsearch,而不是下载所有匹配的文档。如果只关心数据而不关心实际数据。
```

##### new_term

- 字段的值与30天前的数据是否是新出现，如比较后是新值，则触发报警

```
new_term: 此规则匹配新值出现在以前从未见过的字段中。当ElastAlert启动时，它将使用聚合查询来收集字段列表的所有已知术语。
fields: 要监视的字段
```

##### cardinality

- 基线上下的值，触发报警. 当一个时间范围内某个字段的唯一值总数高于或低于阈值时，引规则匹配

```
timeframe:
cardinality_field: 计数基数的字段
max_cardinality: 如查数据的基数大于此数字，则会触发警报。每个提升基数的新事件都会触发警报
min_cardinality: 如果数据的基数低于此数据，将触发警报
```

##### metric_aggregation

- 计算窗口中的度量值高于或低于阈值时，此规则匹配

```
metric_agg_key: 计算度量值的字段。
metric_agg_type: 在metric_agg_key字段上执行聚合操作。聚合类型：min,max,avg,sum,cardinality,value_count
max_threshold: 如果计算度量标准值大于此数字，则会触发报警
min_threshold: 如查计算试题标准值小于此数字，则会触发报警
use_run_every_query_size: 默认情况下，度量值是通过buffer_time大小的窗口计算的。如果此参数为true，则规则将run_every用作计算窗口。
```

##### percentage_match

- 当计算窗口中匹配桶中的文档百分比高于或低于阈值时，此规则匹配。默认情况下，计算窗口为buffer_time

```
match_bucket_filter: 定义桶的过滤器，该过滤器就匹配主查询过滤器返回的文档子集
min_percentage: 如果匹配文档的百分比小于此数字，则会触发警报
max_percentage: 如果匹配文档的百分比大于此数字，则会触发警报
```

##### 返回数据拼接字符串

```
```

##### elastalert-rule-from-kibana

```
```

## 报警方式

##### 预防报警风暴

- 报警风暴: 段时间内发送有成百上千个报警发出

```
# 设置一个时长，在该时间内，相同 query_key 的报警只发一个
realert:
  minutes: 5


# 指数级扩大 realert 时间，中间如果有报警，
# 则按照5>10>20>40>60不断增大报警时间到制定的最大时间，
# 如果之后报警减少，则会慢慢恢复原始realert时间
# 设置一个时长，必须大于realert 设置，则在realert到exponential_realert之间，每次报警之后，realert 自动翻倍
exponential_realert:
  hours: 1
  
  
聚合相同告警
# 根据报警的内容，将相同的报警安装 name 来聚合
aggregation_key: name


# 设置一个时长，则该时长内，所有的报警（同一个配置文件内的报警）最终合并在一起发送一次
aggregation:
  seconds: 10


# 聚合报警的内容，只展示 name 与 message
summary_table_fields:
  - name
  - message
```

##### post

- http_post_static_payload
  - 追加post包中的数据
  - 不能使用 es 中返回数据的变量
- http_post_payload
  - 重写post包中的数据
  - 可以使用 es 中返回数据的变量, 如果变量获取不到值则为 null
  - 变量必须是 es 返回数据中存在的才可以, 否则就是 null
- 先用 http_post_payload 重写, 再用 http_post_static_payload 写入如能使用变量的数据
- 缺点: 格式不够灵活, 无法自定义结构

```
es_host: localhost
es_port: 9200

#是否使用ssl 链接
use_ssl: false

#如果elasticsearch 有认证，填写用户名和密码的地方
#es_username: username
#es_password: password

#rule name 必须是独一的，不然会报错，这个定义完成之后，会成为报警邮件的标题
name: xx-xx-alert

#配置的是frequency，需要两个条件满足，在相同 query_key条件下，timeframe 范围内有num_events个被过滤出来的异常
#type: frequency
type: any

#指定index，支持正则匹配，支持多个index，(逗号, 分隔)同时如果嫌麻烦直接* 也可以。
index: okr-2021-05

# 聚合结果, elastalert只会把一条hit的记录发送给你，如果你想获取多条需要使用聚合功能
aggregation:
#  "* * * * *" means: run as the "run_every" in config.yaml
 #seconds: 10
 schedule: "* * * * *"
aggregate_by_match_time: true


#时间出发的次数
num_events: 100
#和num_events参数关联，也就是说在4分钟内出发5次会报警
timeframe:
  minutes: 1

#用来拼配告警规则，elasticsearch 的query语句，支持 AND&OR等。
filter:
- query:
    query_string: 
      query: "message : * error"

alert:
- "post"

http_post_url: "http://127.0.0.1:5000/test"
http_post_payload:
  request_id: request_id
  elast_alert_type: elast_alert_type

http_post_static_payload:
  index: okr-2021-05
```

##### command

- 命令输出,允许执行任意命令并从匹配中传递参数或stdin
- 发送shell命令
- 必须有 aggregation_key, 如果没有这个参数即使触发错误command模式的报警, 但最终只会执行一次, 选择值是唯一的字段

```
alert:  
- "command"

command: [
  "curl",
  "-d",
  '{"msgtype": "text", "text": {"content": "hello world"}}',
  "http://127.0.0.1:5000/test"   
]
```

- 调用python脚本(any - command)

> 详细参考 https://blog.csdn.net/weixin_34221332/article/details/91417285

```
es_host: localhost
es_port: 9200
#rule name 必须是独一的
name: shanghai_any
type: any
#多个index使用逗号分隔, 没有空格, 可以使用通配符*
index: bpm*,connect*,project*,okr*

aggregation:
  schedule: "* * * * *"
aggregation_key: _id

#用来拼配告警规则，elasticsearch 的query语句，支持 AND&OR等。
filter:
- query:
    query_string: 
      query: "elast_alert_type : any"

alert:
- command

pipe_match_json: true
command: [
  "/home/glfadd/Desktop/elastalert/example_rules/test.py",
  "--request_id=%(request_id)s",
  "--_id=%(_id)s",
  "--app_id=%(app_id)s",
  "--deploy_id=%(deploy_id)s",
  "--host_ip=%(host_ip)s",
  "--index=okr-2021-05",
  "--message=%(message)s"
]
```

- 可以启动python文件
  - 开头必须指定python和编码
  - py文件必须有可执行权限, 否则报错 "[Errno 13] Permission denied"

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
```

- python 文件实例

```
#!/home/glfadd/miniconda3/envs/p3613_elast_alert/bin/python
# -*- coding: UTF-8 -*-

"""
/usr/bin/python
"""

import argparse
import requests
import json

parser = argparse.ArgumentParser(description='企业微信报警')
parser.add_argument('--_id', help='es自动生成的id')
parser.add_argument('--app_id', help='es自动生成的id')
parser.add_argument('--deploy_id', help='es自动生成的id')
parser.add_argument('--host_ip', help='es自动生成的id')
parser.add_argument('--index', help='es自动生成的id')
parser.add_argument('--request_id', help='es自动生成的id')

args = parser.parse_args()
_id = args._id
app_id = args.app_id
deploy_id = args.deploy_id
host_ip = args.host_ip
index = args.index
request_id = args.request_id
message = args.message
url = 'http://127.0.0.1:5000/test'

data = {
    'msgtype': 'markdown',
    'markdown': {
        'content': """错误提醒, 请相关同事注意\n
        >es_id:<font color=\"comment\">{}</font>
        >app_id:<font color=\"comment\">{}</font>
        >deploy_id:<font color=\"comment\">{}</font>
        >host_ip:<font color=\"comment\">{}</font>
        >index:<font color=\"comment\">{}</font>
        >request_id:<font color=\"comment\">{}</font>
        >message:<font color=\"comment\">{}</font>
        """.format(_id, app_id, deploy_id, host_ip, index, request_id, message)
    }
}

url = 'http://127.0.0.1:5000/test'
url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=ebbaa8cf-abbb-4b4e-8a38-bc1b249d741d'
headers = {
    'Content-Type': 'application/json'
}
res = requests.post(url=url, data=json.dumps(data), timeout=3)
```

##### email

- 格式化程序的参数将从与警报相关的匹配对象中提供
- 如果规则匹配索引中多个对象，则仅使用第一个匹配来填充格式化程序的参数
- 如果缺少参数列表中提到的字段，则电子邮件使用alert_missing_value代替

| 参数               | 类型 | 说明                               |
| ------------------ | ---- | ---------------------------------- |
| alert_subject      |      | 邮件主题                           |
| alert_subject_args |      | 主题中可以提供变量，变量值在此定义 |
| alert_text         |      | 正文                               |
| alert_text_args    | list | 正方变量，可从匹配中获取           |
| alert_text_type    |      |                                    |
| alert_text_only    |      | 输出自定义主体                     |
| exclude_fields     |      | 简单输出查询时间段内匹配到几条数据 |

```

alert_subject: "Alter {0} occurred at {1} {2}"
alert_subject_args:
- _index
- "@timestamp"
- request
alert_text: "最近三分钟有三次以上404请求"

```

```
alert:
- "email"

#接受报警邮箱的地址,可以指定多个。email:
email:
- "2239660080@qq.com"

#报警邮箱的smtp server
smtp_host: smtp.exmail.qq.com
#报警邮箱的smtp 端口
smtp_port: 465
#需要把认证信息写到额外配置文件里，需要user和password两个属性
smtp_auth_file: /home/glfadd/Desktop/elastalert/example_rules/smtp_auth.yaml
from_addr: gonglongfei@sensorsdata.cn
```

- smtp_auth.yaml 文件

```
user: xxxx@qq.com
password: xxxxxxxxxx
```

##### 自定义告警内容

```
内部是使用Python的format来实现的
alert_subject: "Error {} @{}"
alert_subject_args:
  - name
  - "@timestamp"

alert_text_type: alert_text_only
alert_text: |
  ### Error frequency exceeds
  > Name: {}
  > Message: {}
  > Host: {} ({})
alert_text_args:
  - name
  - message
  - hostname
  - host
```

## 查询语句

##### elasticsearch 的 query 语句

```
es查询语句

```

##### 

```
Elasticsearch 查询 DSL

```

## 实例

##### any - command - .py

- 

```
```










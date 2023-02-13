## 目录结构

```
├── jvm.options				logstash 的 JVM 配置文件
├── log4j2.properties
├── logstash-sample.conf
├── logstash.yml			logstash 的默认启动配置文件
├── logstash.yml.bak
├── pipelines.yml			logstash 管道配置文件, 可以管理每个管道的 conf 配置文件 
└── startup.options			系统安装脚本的配置文件

管道配置文件
    方式1: 一种方法是在Pipeline.yml文件中设置所有内容，然后运行Logstash，所有输入和输出配置都将在同一文件中
	方式2: 每个管道创建单独的conf文件
```

## input

```
input {
    # file为常用文件插件，插件内选项很多，可根据需求自行判断
    file {
        path => "/var/log/httpd/access_log" # 要导入的文件的位置，可以使用*，例如/var/log/nginx/*.log
        Excude =>”*.gz”                       # 要排除的文件
        start_position => "beginning"         # 从文件开始的位置开始读,默认是end
        ignore_older => 0                # 多久之内没修改过的文件不读取，0为无限制，单位为秒
        sincedb_path => "/dev/null"      # 记录文件上次读取位置；输出到null表示每次都从文件首行开始解析
        add_field=>{"test"="test"}       # 增加一个字段
        type => "apache-log"             # type字段，可表明导入的日志类型
        }   
}
```

##### 多个file

```
input {
  file {
    path => "/var/log/messages"
    type => "syslog"
  }
  
  file {
    path => "/var/log/apache/access.log"
    type => "apache"
  }
}
```

##### 多个文件

```
path => ["/var/log/messages","/var/log/*.log"]
path => ["/data/mysql/mysql.log"]
```

## filter

```
filter{
    grok{
        #match属性是从message 字段中把时间给抠出来，并且赋值给另个一个字段logdate   
         match => ['message','%{TIMESTAMP_ISO8601:logdate}']
        } 
        
        #将message中   ip、访问方法、url、数据量、持续时间提取出来并赋值给 clientip、method、request、bytes、duration 字段
        match => {"message"=>"%{IPORHOST:clientip}\s+%{WORD:method}\s+%{URIPATHPARAM:request}\s+%{NUMBER:bytes}\s+%{NUMBER:duration}"} 
        
        #提取后删除message
        remove_field =>["message"]  
}
```

## output

```
 elasticsearch{  
    hosts=>["10.10.10.11:9200"]        # elasticsearch 地址 端口
    action=>"index"                    # 索引
    index=>"indextemplate-logstash"    # 索引名称
    #document_type=>"%{@type}"  
    document_id=>"ignore"  
      
    template=>"/opt/logstash-conf/es-template.json"    # 模板文件的路径 
    template_name=>"es-template.json"                  # 在es内部模板的名字
    template_overwrite=>true                           # 
    protocol => "http"         #目前支持三种协议    node、http 和tranaport  
}
```

## 数据类型

```
logstash中只有三种类型，string,integer,float。如果不指定类型，默认string
```

## 优化

> https://blog.csdn.net/weixin_43390992/article/details/105232927

##### output关闭调试模式, 影响性能

```
# stdout { codec => rubydebug }
```

##### Logstash持久化到磁盘

当发生异常情况，比如logstash重启，有可能发生数据丢失，可以选择logstash持久化到磁盘

```
# config/logstash.yml

queue.type: persisted
path.queue: /usr/share/logstash/data    #队列存储路径；如果队列类型为persisted，则生效
queue.page_capacity: 250mb         #队列为持久化，单个队列大小
queue.max_events: 0               #当启用持久化队列时，队列中未读事件的最大数量，0为不限制
queue.max_bytes: 1024mb           #队列最大容量
queue.checkpoint.acks: 1024       #在启用持久队列时强制执行检查点的最大数量,0为不限制
queue.checkpoint.writes: 1024     #在启用持久队列时强制执行检查点之前的最大数量的写入事件，0为不限制
queue.checkpoint.interval: 1000   #当启用持久队列时，在头页面上强制一个检查点的时间间隔
```

##### 优化input,filter,output的线程模型

- 增大 filter和output worker 数量. logstash正则解析极其消耗计算资源，而我们的业务要求大量的正则解析，因此filter是我们的瓶颈。
  官方建议线程数设置大于核数，因为存在I/O等待
- 增大logstash 堆内存, logstash是将输入存储在内存之中
- 官方的建议是提高每次批处理的数量，调节传输间歇时间。当batch.size增大，es处理的事件数就会变少，写入也就越快了

```
(可以将这些配置写入到 pipelines.yml 中)
# pipeline线程数，适当增加不超过pipeline 线程数, 如几倍 cpu 内核数
pipeline.workers: 8
# 实际output时的线程数
pipeline.output.workers: 8
# 每次发送的事件数
pipeline.batch.size: 3000
# 发送延时
pipeline.batch.delay: 1
```

```
https://blog.csdn.net/qq330983778/article/details/106179903
https://www.cnblogs.com/dyh004/p/9699813.html


logstash 详细参数
https://www.cnblogs.com/jingmoxukong/p/8118791.html
```

## date

获得时间格式的数据

| 参数           | 作用                               | 参数类型 |
| -------------- | ---------------------------------- | -------- |
| locale         | 指定用于日期解析的区域设置         | string   |
| match          | 如何匹配时间格式                   | array    |
| tag_on_failure | 匹配失败后追加的内容               | array    |
| target         | 匹配成功后的内容需要设置的目标字段 | string   |
| timezone       | 指定用于日期解析的时区规范ID       | string   |

- 例子

```
input {
	redis {
		key => "filebeat_test"
		host => "localhost"
		port => 6379
		db => 0
		data_type => "list"
	}
}
filter {
	date {
		match => [ "message", "yyyy-MM-dd HH:mm:ss" ]
		locale => "Asia/Shanghai"
		timezone => "Europe/Paris"
		target => "messageDate"
	}	
}
output {
	stdout { codec => rubydebug }
}


# 写入日志文件数据
2020-05-07 23:59:59


# 控制台输出结果
{
     "@timestamp" => 2021-05-07T08:28:35.776Z,
          "agent" => {
                "type" => "filebeat",
                "name" => "lg",
                  "id" => "41cac466-f09e-4e31-a9aa-b64a10cd3fdb",
        "ephemeral_id" => "62259311-2d75-4e8a-bae7-08003a74efea",
             "version" => "7.12.1",
            "hostname" => "lg"
    },
            "ecs" => {
        "version" => "1.8.0"
    },
          "input" => {
        "type" => "log"
    },
       "@version" => "1",
     "log_source" => "messages",
        "message" => "2020-05-07 23:59:59",
    "messageDate" => 2020-05-07T21:59:59.000Z
}

# 从原始数据 message 获取指定格式的时间数据, 并赋值给 messageDate
```

## Grok

通过正则表达式获取指定的数据

| Item                                 | Comment                                                      |
| ------------------------------------ | ------------------------------------------------------------ |
| %{USER:user}                         | 以 USER 模式进行正则匹配，结果放在user中                     |
| %{NUMBER: id:int}                    | 以 NUMBER 模式进行正则匹配，为整数型，结果放在id中           |
| %{NUMBER:query_time:float}           | 以 NUMBER 模式进行正则匹配，为浮点型，结果放在query_time中   |
| [[^]]+]                              | 以 [ 开头 以]结尾，内容是由一个或多个不是 ] 的字符填充而成   |
| \n                                   | 匹配换行符                                                   |
| \b                                   | 代表字单词边界不占位置，只用来指示位置                       |
| .*                                   | 尽可能多的任意匹配                                           |
| .*$                                  | 任意匹配直到结尾                                             |
| (?:use\s+%{USER:usedatabase};\s*\n)? | 这个匹配可能有，也可能无，如果有，就是以use开头，若干空字符，以 USER 模式进行正则匹配，结果放在usedatabase中，然后紧接着 ; ，后面是0个或多个空字符，然后是换行，注意：如果有是整体有，如果无，是整体无 |
| (?< query>(?< action>\w+)\b.*)       | 整体匹配，存到query中，以一个或多个字符开头组成的单词，结果存到action中 |
| (?:\n#\s+Time)?                      | 内容可能有，也可能无，如果有，是接在一个换行之后，以 # 开头，隔着一个或多个空字符，然后是Time |

##### 基本用法

```
echo '{"age":10,"name":"张三"}' >> flask.log
```

##### 使用自带的模式匹配

```
filter {
  grok {
    match => { "message" => "%{IP:client} %{WORD:method} %{URIPATHPARAM:request} %{NUMBER:bytes} %{NUMBER:duration}" }
  }
}
```

##### overwrite

```




```

##### index

- elasticsearch 输出参数也支持%{}的动态语法，可以将数据中的某一个字段，设置成目标索引的值，将数据插入其中。索引不能包含大写字符

```
# 输出部分参数
elasticsearch {
     hosts => "http://localhost:9200"
     index => "%{userType}"
     document_id => "%{id}"
	 user => user
	 password => password
}

# 写入 elasticsearch参数
{"age":10,"id":1,"name":"admin","userType":"admin"}
{"age":20,"id":2,"name":"user","userType":"user"}

# 结果
增加了两个索引 "admin" 和 "user"
```

- 使用时间作为索引

```
日志随着时间的积累会越来越多，一般来说在生成日志文件的时候我们会根据时间进行切分，将不同时间的日志文件作为不同的日志文件，所以我们同样可以通过时间按天划分索引。logstash提供了直接使用时间戳数据的方法logstash-%{+yyyy.MM.dd},当然也可以自己格式化数据中的日期来设置索引模板。

output {
   elasticsearch {
     hosts => "http://localhost:9200"
	 index => "%{userType}-%{+yyyy-MM-dd}"
	 document_id => "%{id}"
	 user => user
	 password => password
   }
}
```

##### kibana grok 调试工具

> 位于 kibana 工具中 Grok Debuger

- Sample Data(样例数据 )

```
2021-05-17 16:20:29,532 - INFO - test.py - root - 25 - {'user_name': '小明', 'age': 10, 'address': '中国北京', 'phone': '16666666666', 'number': '800', 'elast_alert_type': 'any', 'request_id': 1621239629532, 'action': 'info', 'url': 'http://test.test.test/114529', 'ip_addr': '127.0.0.1'}
```

- 获取时间

```
# Grok Patterns (表达式)
%{YEAR:year}-%{MONTHNUM:month}-%{MONTHDAY:day} %{TIME:time}

# Structured Data (结果)
{
  "month": "05",
  "year": "2021",
  "time": "16:20:29,532",
  "day": "17"
}
```

- 获取时间 (使用自定义模式)

```
# Grok Patterns
%{CREATETIME:create_time}

# Custom Patterns (自定义模式)
CREATETIME %{YEAR}-%{MONTHNUM}-%{MONTHDAY} %{TIME}

# Structured Data
{
  "create_time": "2021-05-17 16:20:29,532"
}
```

##### 自定义模式 - 使用pattern文件

- 创建文件夹, 并在里面创建模式文件 (例如 ./patterns/elast_alert_type)

```
CREATETIME %{YEAR}-%{MONTHNUM}-%{MONTHDAY} %{TIME}
ALERT ['"]elast_alert_type[\'\"\:\s]+[\w]*['"]
```

- 在 filter 中使用 patterns_dir 指定这个文件的路径

```
filter {
  grok {
    patterns_dir => ["./patterns"]
    match => { "message" => "%{CREATETIME:create_time}" }
  }
}
```

##### 自定义模式 - 使用 Oniguruma 语法

- 格式

```
(?<字段名>正则表达式)
```

```
filter {
  grok {
    match => { "message" => "(?<request_id>[0-9]{13})" }
  }
  grok {
    match => { "message" => "(?<temp_1>elast_alert_type[\'\"\:])(?<temp_2>[\'\"\:\s]+)(?<elast_alert_type>\w+)"}
  }
  mutate {
    # 指定数据的类型
    convert => {
      "elast_alert_type" => "string" 
    }
    # 删除没用的字段
    remove_field => ["temp_1"]
    remove_field => ["temp_2"]
    remove_field => ["log"]
    remove_field => ["agent"]
    remove_field => ["@version"]
    remove_field => ["log_source"]
    remove_field => ["ecs"]
    remove_field => ["input"]
    remove_field => ["host"]
    remove_field => ["tags"]
  } 
}
```


## 文档

> [Alerta CLI](https://docs.alerta.io/cli.html#cli)

## 安装

> version 8.5.1

```bash
$ pip install alerta
```

## configuration

##### 命令

```bash
alerta --help

# 查看版本
$ alerta version

# 显示Alerta API已经运行了多长时间
$ alerta uptime

# 显示配置信息
$ alerta config

# 显示API服务器状态和使用指标
$ alerta status
```

## 常用操作

##### 发送警报

> 可以用中文字符串
>
> severity只能是 security, critical, major, minor, warning, indeterminate, informational, normal, ok, cleared, debug, trace, unknown
>
> severity 为 ok 时没有消息

- help

  ```bash
   $ alerta send --help
  Usage: alerta send [OPTIONS]
  
    Send an alert.
  
  Options:
    -r, --resource RESOURCE        Resource under alarm
    -e, --event EVENT              Event name
    -E, --environment ENVIRONMENT  Environment eg. Production, Development
    -s, --severity SEVERITY        Severity eg. critical, major, minor, warning
    -C, --correlate EVENT          List of related events eg. node_up, node_down
    -S, --service SERVICE          List of affected services eg. app name, Web,
                                   Network, Storage, Database, Security
    -g, --group GROUP              Group event by type eg. OS, Performance
    -v, --value VALUE              Event value
    -t, --text DESCRIPTION         Description of alert
    -T, --tag TAG                  List of tags eg. London, os:linux, AWS/EC2
    -A, --attributes KEY=VALUE     List of attributes eg. priority=high
    -O, --origin ORIGIN            Origin of alert in form app/host
    --type EVENT_TYPE              Event type eg. exceptionAlert,
                                   performanceAlert, nagiosAlert
    --timeout SECONDS              Seconds before an open alert will be expired
    --raw-data STRING              Raw data of orignal alert eg. SNMP trap PDU.
                                   '@' to read from file, '-' to read from stdin
    --customer STRING              Customer
    -h, --help                     Show this message and exit.
  ```

- 示例

  ```bash
  $ alerta send -r 来源002 -e HttpError -g Web -s major
  
  # 指定接收消息 url, 时区
  $ alerta send -r 来源002 -e 事件001 -g Web -s major --attributes region="EU" --endpoint-url http://localhost:8080
  ```

##### 查询警报

- help

  ```bash
   $ alerta query --help
  Usage: alerta query [OPTIONS]
  
    Query for alerts based on search filter criteria.
  
  Options:
    -i, --ids ID         List of alert IDs (can use short 8-char id)
    -q, --query QUERY    severity:"warning" AND resource:web
    -f, --filter FILTER  KEY=VALUE eg. serverity=warning resource=web
    --oneline            Show alerts using table format
    --medium             Show important alert attributes
    --full               Show full alert details
    -h, --help           Show this message and exit.
  ```

- 示例

  ```bash
  # 查询所有
  $ alerta query
  
  # 根据 id 查询
  $ alerta query -i 0080f6bc
  
  # 根据其他条件查询
  $ alerta query -f status=open -f event=event001
  
  # 查看完成信息
  $ alerta query --full
  $ alerta query -i 0080f6bc --full
  ```

##### 查询警报历史

- help

  ```bash
   $ alerta history --help
  Usage: alerta history [OPTIONS]
  
    Show status and severity changes for alerts.
  
  Options:
    -i, --ids ID         List of alert IDs (can use short 8-char id)
    -q, --query QUERY    severity:"warning" AND resource:web
    -f, --filter FILTER  KEY=VALUE eg. serverity=warning resource=web
    -h, --help           Show this message and exit.
  ```

- 示例

  ```bash
  $ alerta history -i 3a1856d5
  ```

##### 更新警报属性

> 可以先用 query 的 --full 查看所有的属性

- help

  ```bash
   $ alerta update --help           
  Usage: alerta update [OPTIONS]
  
    Update alert attributes.
  
  Options:
    -i, --ids ID                List of alert IDs (can use short 8-char id)
    -q, --query QUERY           severity:"warning" AND resource:web
    -f, --filter FILTER         KEY=VALUE eg. serverity=warning resource=web
    -A, --attributes KEY=VALUE  List of attributes eg. priority=high  [required]
    -h, --help                  Show this message and exit.
  ```

- 示例

  ```bash
  $ alerta update -i 3a1856d5 -A priority=high -A resource=aabbcc 
  ```

##### 添加 / 删除标签

- help

  ```bash
   $ alerta tag --help
  Usage: alerta tag [OPTIONS]
  
    Add tags to alerts.
  
  Options:
    -i, --ids ID         List of alert IDs (can use short 8-char id)
    -q, --query QUERY    severity:"warning" AND resource:web
    -f, --filter FILTER  KEY=VALUE eg. serverity=warning resource=web
    -T, --tag TEXT       List of tags  [required]
    -h, --help           Show this message and exit.
  ```

  ```bash
   $ alerta untag --help
  Usage: alerta untag [OPTIONS]
  
    Remove tags from alerts.
  
  Options:
    -i, --ids ID         List of alert IDs (can use short 8-char id)
    -q, --query QUERY    severity:"warning" AND resource:web
    -f, --filter FILTER  KEY=VALUE eg. serverity=warning resource=web
    -T, --tag TEXT       List of tags  [required]
    -h, --help           Show this message and exit.
  ```

- 示例

  ```bash
  # -T 中的参数会生成一组标签
  $ alerta tag -i 3a1856d5 -T abc,123,opq
  
  # -T 删除时必须指定一组标签
  $ alerta untag -i 3a1856d5  -T abc,123 -T abc,123,opq
  ```

##### 删除警报

- help

  ```bash
   $ alerta delete --help
  Usage: alerta delete [OPTIONS]
  
    Delete alerts.
  
  Options:
    -i, --ids ID         List of alert IDs (can use short 8-char id)
    -q, --query QUERY    severity:"warning" AND resource:web
    -f, --filter FILTER  KEY=VALUE eg. serverity=warning resource=web
    -h, --help           Show this message and exit.

- 示例

  ```bash
  # 删除所有报警
  $ alerta delete
  
  # 根据 id 删除
  $ alerta delete -i 0080f6bc
  
  # 根据条件删除
  $ alerta delete -f event=event001 -f severity=warning
  ```

##### 关闭警报

- help

  ```bash
   $ alerta close --help
  Usage: alerta close [OPTIONS]
  
    Set alert status to 'closed'.
  
  Options:
    -i, --ids ID         List of alert IDs (can use short 8-char id)
    -q, --query QUERY    severity:"warning" AND resource:web
    -f, --filter FILTER  KEY=VALUE eg. serverity=warning resource=web
    --text TEXT          Message associated with status change
    -h, --help           Show this message and exit.
  ```

- 示例

  ```bash
  $ alerta close -i 3a1856d5
  ```

##### 搁置 / 非搁置

> shelve 相当于暂时不对报警做任何处理

- help

  ```bash
   $ alerta shelve --help
  Usage: alerta shelve [OPTIONS]
  
    Set alert status to 'shelved'.
  
  Options:
    -i, --ids ID         List of alert IDs (can use short 8-char id)
    -q, --query QUERY    severity:"warning" AND resource:web
    -f, --filter FILTER  KEY=VALUE eg. serverity=warning resource=web
    --timeout SECONDS    Seconds before alert auto-unshelved.  [default: 7200]
    --text TEXT          Message associated with status change
    -h, --help           Show this message and exit.
  ```

  ```bash
   $ alerta unshelve --help
  Usage: alerta unshelve [OPTIONS]
  
    Set alert status to 'open'.
  
  Options:
    -i, --ids ID         List of alert IDs (can use short 8-char id)
    -q, --query QUERY    severity:"warning" AND resource:web
    -f, --filter FILTER  KEY=VALUE eg. serverity=warning resource=web
    --text TEXT          Message associated with status change
    -h, --help           Show this message and exit.
  ```

- 示例

  ```bash
  $ alerta shelve -i 3a1856d5
  $ alerta unshelve -i 3a1856d5
  ```




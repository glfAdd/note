## 邮件

```
文档
https://docs.alerta.io/integrations.html?highlight=email

https://docs.alerta.io/configuration.html?highlight=email

github
https://github.com/alerta/alerta-contrib/tree/master/integrations/mailer


prometheus


alerta --endpoint-url http://192.168.1.228:28880/api send --resource webserver01 --event down --environment Production --service Website01 --severity major --text "Web server 01 is down." --value ERROR





$ alerta --endpoint-url http://127.0.0.1:8000/api send --resource 来源003 --event 事件003 --correlate correlate003 --group group003 --severity debug

--endpoint-url



```

## 丁丁通知

```
https://github.com/alerta/alerta-contrib/blob/master/plugins/dingtalk/dingtalkchatbot/chatbot.py
```

## command line tool (CLI)

##### 安装

```bash
$ pip install alerta
```

##### 命令

```bash
$ alerta send --help
```

##### 示例

> 可以用中文字符串
>
> severity只能是 security, critical, major, minor, warning, indeterminate, informational, normal, ok, cleared, debug, trace, unknown
>
> severity 为 ok 时没有消息
>
> 

```bash
$ alerta send -r web01 -e HttpError -g Web -s major --attributes region="EU"
$ alerta send --resource resource001 --event event001 --correlate correlate001 --group group001 --severity critical
$ alerta send --resource 来源002 --event 事件001 --correlate correlate001 --group group001 --severity debug
# 指定 url
$ alerta --endpoint-url http://localhost:8080 send --resource 来源002 --event 事件001 --correlate correlate001 --group group001 --severity debug
```

```

```



## python sdk

```
>>> from alertaclient.api import Client

>>> client = Client(key='NGLxwf3f4-8LlYN4qLjVEagUPsysn0kb9fAkAs1l')
>>> client.send_alert(environment='Production', service=['Web', 'Application'], resource='web01', event='HttpServerError', value='501', text='Web server unavailable.')
Alert(id='42254ef8-7258-4300-aaec-a9ad7d3a84ff', environment='Production', resource='web01', event='HttpServerError', severity='normal', status='closed', customer=None)

>>> [a.id for a in client.search([('resource','~we.*01'), ('environment!', 'Development')])]
['42254ef8-7258-4300-aaec-a9ad7d3a84ff']

>>> client.heartbeat().serialize()['status']
'ok'
```


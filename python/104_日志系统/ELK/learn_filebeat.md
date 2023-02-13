##### filebeat 进程停止

```
问题: 
运行一段时间后，filebeat自动停止, 日志显示 
2021-05-14T16:55:00.087+0800    INFO    instance/beat.go:474    filebeat stopped.


原因:
待扫描的文件长时间没有新内容写入，收割机停止工作


解决办法:


```

##### 传送多行日志





```
问题:
一条日志多行显示, 但被当作多条日志处理, 应该合并
2021-06-11 12:20:14,852 - INFO - Traceback (most recent call last):
  File "/home/glfadd/Desktop/learn/note/elk_test.py", line 35, in root
    a = b
NameError: name 'b' is not defined


解决办法:
使用曾则匹配特定字符串开头的行
    multiline.pattern: '(^Traceback)|(^[0-9]{4}-[0-9]{2}-[0-9]{2}.{1}[0-9]{2}:[0-9]{2}:[0-9]{2}[\.\,]{1})'
    multiline.negate: true
    multiline.match: after
    #最多合并500行
    multiline.max_lines: 100
    #5s无响应则取消合并
    multiline.timeout: 3s 
   
   
参考 https://www.cnblogs.com/sanduzxcvbnm/p/12941286.html
```


```python
get		获取数据
post	修改
put		保存
delete	删除
option	询问服务器某种支持特性
head	返回报文头

http换行符号 "\r\n"

GET / HTTP/1.1
请求方式 + 路径 + 版本
```

```
https 就是在安全地传输层上发送的http
```

#####

```
HTTPS (HyperText Transfer Protocol over Secure Socket Layer)
一般理解为HTTP+SSL/TLS
https 就是在安全地传输层上发送的 http
```



```
如果URL的方案为http。客户端就会打开一条到服务器端口80的连接，并向其发送http命令。

如果URL的方案为https。客户端就会打开一条到服务器端口443的连接，然后与服务器“握手”以二进制格式与服务器交换一些SSL安全参数，附上加密的http命令。
```


##### 文档

[github](https://github.com/valyala/fasthttp)

```


```

##### install

```bash
$ go get -u github.com/valyala/fasthttp
```



##### 使用

```
fasthttp.AcquireRequest()//获取Request连接池中的连接
fasthttp.ReleaseRequest(req) // 用完需要释放资源
fasthttp.AcquireResponse()//获取Response连接池中的连接
fasthttp.ReleaseResponse(resp) // 用完需要释放资源

```


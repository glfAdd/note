##### 参考

- [ ] https://juejin.cn/post/7195491694052884517
- [ ] https://www.cnblogs.com/88223100/p/Which-is-the-strongest-third-party-package-for-Go-JSON.html
- [ ] https://blog.csdn.net/yzh_1346983557/article/details/130007671 多种介绍
- [ ] https://www.luozhiyun.com/archives/535
- [ ] 

##### 文档



##### 对比

```
go 语言自带的 encoding/json, 解析是通过反射机制实现 json数据的解析的，性能的低

easyjson: 速度最快, 使用时要先生成对应结构体的操作代码，使用起来比较麻烦

sonic: 经常更新, 不使用
```

# easyjson

##### 参考

- [ ] https://www.kancloud.cn/idcpj/python/1486472

##### 文档

[github - easyjson](https://github.com/mailru/easyjson)

##### install

```bash
# 有 go.mod 文件的地方执行
$ go get github.com/mailru/easyjson && go install github.com/mailru/easyjson/...@latest

# 验证是否安装成功
$ easyjson
```

##### 使用

student.go

```go
// easyjson:json
type School struct {
	Name string		`json:"name"`
	Addr string		`json:"addr"`
}

// easyjson:json
type Student struct {
	Id       int       `json:"id"`
	Name     string    `json:"s_name"`
	School   School    `json:"s_chool"`
	Birthday time.Time `json:"birthday"`
}
```

```bash
# 生成easyjson_student.go，为结构体增加了MarshalJSON、UnmarshalJSON方法
$ easyjson  -all student.go  

```



# sonic

##### 文档

[github - sonic](https://github.com/bytedance/sonic)

```

```

# gjson

[github](https://github.com/tidwall/gjson) 12.8k

```

```

# fastjson

```
```



# json-iterator

##### 参考

- [ ] https://liuqh.icu/2021/12/30/go/package/33-jsoniter/
- [ ] 

[github](https://github.com/json-iterator/go) 12.6k

[pkg](https://pkg.go.dev/github.com/json-iterator/go#section-readme)

```
jsoniter
```

##### install

```bash
$ go get github.com/json-iterator/go
```


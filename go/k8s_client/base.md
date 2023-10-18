##### 参考

- [ ] https://jimmysong.io/kubernetes-handbook/develop/client-go-sample.html
- [ ] https://blog.csdn.net/Peerless__/article/details/127814142
- [x] https://xinchen.blog.csdn.net/article/details/113753087 1
- [ ] https://xinchen.blog.csdn.net/article/details/113487087 2
- [ ] https://xinchen.blog.csdn.net/article/details/113788269 3
- [ ] https://xinchen.blog.csdn.net/article/details/113795523 4
- [ ] https://xinchen.blog.csdn.net/article/details/113800054 5
- [ ] https://zhuanlan.zhihu.com/p/524775243
- [ ] https://zhuanlan.zhihu.com/p/466091094
- [ ] 
- [ ] https://juejin.cn/post/6962869412785487909
- [ ] https://zhuanlan.zhihu.com/p/202611841?utm_source=wechat_session
- [ ] 

##### 文档

[github](https://github.com/kubernetes/client-go)

https://pkg.go.dev/k8s.io/kube-openapi/pkg/common

##### 安装



版本 `v0.27.3`

```bash
$ go get k8s.io/client-go@latest
$ go get k8s.io/api@latest
$ go get k8s.io/apimachinery@latest

$ go get k8s.io/client-go@v0.27.3
$ go get k8s.io/api@v0.27.3
$ go get k8s.io/apimachinery@v0.27.3



$ go mod tidy
```

##### 源码目录结构

```
kubernetes: 访问 k8s 集群的 api, 与 apiServer 通信, 对集群的资源对象进行增删改查
discovery: 用于发现 k8s apiServer 支持的 API
dynamic: 包含一个动态客户端, 可以对任意 k8s API对象执行通用操作。
plugin/pkg/client/auth: 包含可选的身份验证插件, 用于从外部源获取凭证。
transport: 用于设置认证并启动连接。
informers: 每种 k8s 资源的 informer 实现。
listers: 为每一个 k8s 资源提供 list 功能, 将数据缓存到本地, 然后 get 和 list 时从本地获取, 减轻 apiServer 的压力。
tools: 提供常用工具, 例如 SharedInformer、Reflector、DeltaFifo已经Indexers等。提供client查询和缓存机制, 主要子目录为cache。
util: 提供常用方法。例如 WorkQueue 工作队列, Certificate 证书管理等。
```

# URL

##### GVR / GVK

```
G（Group组）：资源组，包含一组资源操作的集合，比如apps下面有deployment、demonset等。
V（Version版本）：资源版本，用于区分不同API的稳定程度和兼容性，比如v1、v1alpha1等。
R（Resources资源）：资源信息，用于区别不同的资源API，比如 pod、deployment、ingress 等。
K（Kind类别）：资源对象的类型，每个资源对象都需要Kind来区分它自身代表的资源类型。
```

##### url 规则

```
有组名资源组
	/apis/Group分组/Version版本/Resource资源
	/apis/apps/v1/deployments


无组名资源组
	/apis/Version版本/Resource资源
	/apis/v1/pods
```

##### 例子

```bash
$ curl http://127.0.0.1:8001/api/v1/namespaces/{namespace}/pods/{name}
$ curl http://127.0.0.1:8001/api/v1/namespaces/dev/pods
```

##### 

```

```

##### 

```
```

# client

### RestClient

> RESTClient 是 client-go 最基础客户端，对 HTTP Reqeust 封装，提供 RESTful 风格的 API. 使用灵活但麻烦

##### 包

```bash
$ go get k8s.io/client-go@latest
或
$ go get k8s.io/client-go@v0.27.3
```

### ClientSet

> 封装 RESTClient, 简化使用.



### DynamicClient

> Custom Resource Definition 自定义资源类型 CRD
>
> 操作 CRD 对象



### DiscoveryClient

> 

```
- DiscoveryClient：封装了 RestClient，发现客户端，负责发现 apiServer支持地资源组、资源版本和资源信息，相当于使用 kubectl api-resources
```

### 缩容

- [ ] https://verytoolz.com/blog/0c7e76cba61/
- [ ] https://blog.csdn.net/xujiamin0022016/article/details/123642199
- [ ] 

```
DeploymentConfigScaler
```



# 回滚

##### 参考

```
http://www.5bug.wang/post/106.html
https://blog.csdn.net/MoFengLian/article/details/126746894
```



# Patch

[官网文档](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/update-api-object-kubectl-patch/?spm=a2c6h.12873639.article-detail.5.3d155e6dUeM6pY)

```



strategic merge patch, json-patch, json merge patch 区别
```

https://www.cnblogs.com/xgg123/p/17241805.html

https://developer.aliyun.com/article/703438



# 资源设置

- [ ] https://qa.1r1g.com/sf/ask/3708822141/
- [ ] https://kubernetes.io/zh-cn/docs/reference/kubernetes-api/common-definitions/quantity/
- [ ] 

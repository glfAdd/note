##### 参考

```bash
https://cloud.tencent.com/developer/article/2272172?areaSource=102001.12&traceId=PecfZEF7Y2Nl1DopDxQ0T

https://blog.csdn.net/flq18210105507/article/details/126481999


参数介绍
https://blog.csdn.net/RtxTitanV/article/details/108296789


参数说明
https://blog.csdn.net/2202_76081178/article/details/130690804

```

- [ ] https://linwei.blog.csdn.net/article/details/130939051
- [ ] 

# 更新方式

```
https://blog.csdn.net/qq_36963950/article/details/125128594



```



### Deployment 金丝雀发布（灰度发布）

> 如果您想使用 Deployment 将最新的应用程序版本发布给一部分用户, 可以为每个版本创建一个 Deployment，此时，应用程序的新旧两个版本都可以同时获得生产上的流量

##### 步骤

版本 1 (nginx:1.7.9)

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.7.9
---
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
  labels:
    app: nginx
spec:
  selector:
    app: nginx
  ports:
  - name: nginx-port
    protocol: TCP
    port: 80
    nodePort: 32600
    targetPort: 80
  type: NodePort

```

版本 2 (nginx:1.8.0)

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment-canary
  labels:
    app: nginx
    track: canary
spec:
  replicas: 1
  selector:
    matchLabels:
      app: nginx
      track: canary
  template:
    metadata:
      labels:
        app: nginx
        track: canary
    spec:
      containers:
      - name: nginx
        image: nginx:1.8.0
```

##### 处理过程

- 第 1 个版本的 Deployment 包含了 3 个Pod副本，Service 通过 label selector app: nginx 选择对应的 Pod，nginx 的标签为 1.7.9
- Service 的 LabelSelector 是 app: nginx，由 nginx-deployment 和 nginx-deployment-canary 创建的 Pod 都带有标签 app: nginx，所以，Service 的流量将会在两个 release 之间分配, 流量分配的比例为两个版本副本数的比例，此处为 1: 3
- 当确定新的版本没有问题之后，可以将 nginx-deployment 的镜像标签修改为新版本的镜像标签，并在完成对 nginx-deployment 的滚动更新之后，删除 nginx-deployment-canary 这个 Deployment

##### 局限性

按照 Kubernetes 默认支持的这种方式进行金丝雀发布，有一定的局限性：

1. 不能根据用户注册时间、地区等请求中的内容属性进行流量分配
2. 同一个用户如果多次调用该 Service，有可能第一次请求到了旧版本的 Pod，第二次请求到了新版本的 Pod

在 Kubernetes 中不能解决上述局限性的原因是：Kubernetes Service 只在 TCP 层面解决负载均衡的问题，并不对请求响应的消息内容做任何解析和识别。如果想要更完善地实现金丝雀发布，可以考虑如下三种选择

1. 业务代码编码实现
2. Spring Cloud 灰度发布
3. Istio 灰度发布



# 更新中出现的问题

```
 daemonset 更新阻塞实验
Node 节点与集群网络连接断开，会导致 Node 状态变为 NotReady，此时系统会自动为该 Node 打上污点node.kubernetes.io unreachable:NoExecute与node.kubernetes.io/unreachable:NoSchedule，而 daemonset 创建的 Pod 会自动打上容忍度node.kubernetes.io/unreachable:NoExecute，如果有额外的设置，使得 ds 的 pod 容忍 node 污点时，更新 daemonset 应用负载会出现阻塞情况，主要问题是 daemonset 滚动更新会先删除旧 pod，然后创建新的 pod，而 NotReady 的 Node 的 Pod 处于 Terminating 状态并且无法删除，会被认为是不可用 Pod，当不可用 Pod 数大于maxUnavailable，则直接跳过升级过程。
通过实验复现该问题，主要思路是，创建 Daemonset 应用，然后断开某些 Node 节点网络连接，更新 Daemonset 应用，查看更新状态。
实验环境
```


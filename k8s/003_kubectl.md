##### 参考

[官网文档](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands)

```
https://zhuanlan.zhihu.com/p/85810571
https://blog.csdn.net/A_art_xiang/article/details/125707895

中文文档
http://docs.kubernetes.org.cn/490.html
https://www.tkcnn.com/k8s/k8s-kubectl/kubectl-create-role.html (详细)
https://www.apiref.com/kubernetes-zh/index.html
https://www.kubernetes.org.cn/k8s

https://zhuanlan.zhihu.com/p/564931272?utm_id=0 (完整)



https://blog.csdn.net/LK1024zzZ/article/details/129449791
https://blog.csdn.net/u014676474/article/details/128539106

https://www.bookstack.cn/read/rancher-2.6-zh/8c50333488b287db.md



yaml 里面使用 cmd 和 args
https://www.cnblogs.com/luozhiyun/p/13767866.html


命令技巧大全
http://www.taodudu.cc/news/show-4792835.html?action=onClick



原地升级
https://www.cnblogs.com/duiniwukenaihe/p/15381088.html


内容全
https://www.orchome.com/16680



```

# 安装

##### kubectl

>  [文档](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/#install-kubectl-binary-with-curl-on-linux)

mac

```bash
$ brew install kubectl
或
$ brew install kubernetes-cli
或
$ curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/darwin/amd64/kubectl"
```

linux

```bash
$ curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"

$ sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
```

kubectl 连接文件

> kubectl 默认找 ~/.kube/config 的配置文件

```bash
# clusters 集群
# users 用户
# namespace 命名空间
# contexts 上下文: 用来指定以什么用户连接到那个集群, 切换到对应命名空间下

apiVersion: v1
# 集群信息
clusters:
- cluster:
    server: https://123.123.123.123:64111
    certificate-authority-data: LS0tLS1CRUTiBDRVJUSUZJ.....
  name: kubernetes
# 上下文
contexts:
- context:
    cluster: kubernetes
    user: "242509083547882627"
  name: 2425090832627-c0945672fde23dc552c1e9
# 当前上下文
current-context: 24250908882627-c094567011ae3d22c552c1e9
kind: Config
preferences: {}
# 客户端认证
users:
- name: "242509083547882627"
  user:
    client-certificate-data: LS0tLSRUdJTiBDRVJU............
```

##### kube-shell

[github](https://github.com/cloudnativelabs/kube-shell)

> 交互式带命令提示终端
>
> 只有 python3 支持

```bash
# 安装
$ pip install kube-shell --user -U
$ pip3 install kube-shell --user -U


# 运行提示错误
$ kube-shell
zsh: command not found: kube-shell


# 查找安装的路径
$ find . -name kube-shell


# 再 .zshrc 文件添加
export PATH=~/Library/Python/3.11/bin:$PATH


$ source ~/.zshrc
```

##### kubectx

[github](https://github.com/ahmetb/kubectx)

> 用于切换 kubernetes context

mac

```bash
$ brew install kubectx
```

##### kubens (kubectx 包含这个)

[github]()

> 命名空间切换工具

```bash
# 切换到 glf-test
$ kubens glf-test

# 切换到 default
$ kubens -
```

# 配置文件

> K8s 只支持 stdin, yaml 和 json 格式创建资源对象

##### 有状态与无状态的区别

```
无状态：
1）deployment 认为所有的pod都是一样的
2）不用考虑顺序的要求
3）不用考虑在哪个node节点上运行
4）可以随意扩容和缩容

有状态
1）实例之间有差别，每个实例都有自己的独特性，元数据不同，例如etcd，zookeeper
2）实例之间不对等的关系，以及依靠外部存储的应用。


--- 表示新的yaml文件开始
# 表示标识注释，从这个字符一直到行尾，都会被解释器忽略
```

### kind

> [官网文档](https://kubernetes.io/docs/tasks/run-application/run-stateless-application-deployment/)

##### 所有 kind

```
Deployment：用于定义应用程序的声明式更新。
StatefulSet：用于有状态应用程序的声明式更新和管理。
DaemonSet：用于在集群中运行一个pod的声明式更新和管理。
Job：用于在集群上运行一次性任务的声明式更新和管理。
CronJob：用于在集群上运行定期作业的声明式更新和管理。
Service：用于定义一组pod的逻辑集合，以及访问这些pod的方式。
Pod：一个Kubernetes中最基本的资源类型，它用于定义一个或多个容器的共同运行环境。
ReplicaSet：用于确保在集群中运行指定数量的pod的声明式更新和管理。
ConfigMap：用于存储非敏感数据（如配置文件）的声明式更新和管理。
Secret：用于存储敏感数据（如密码和密钥）的声明式更新和管理。
ServiceAccount：用于定义一个pod的身份验证信息，以及与Kubernetes API Server进行交互的权限。
Ingress：用于定义从外部访问Kubernetes集群中服务的方式。
PersistentVolume：用于定义持久化存储卷，并使它们在Kubernetes集群中可用。
StorageClass：用于定义不同类型的存储，例如云存储、本地存储等，并为这些存储类型指定默认的参数和策略。
Namespace：用于在Kubernetes集群中创建逻辑分区，从而将资源隔离开来，以提高安全性和可维护性。
ServiceMonitor：用于自动发现和监控在Kubernetes集群中运行的服务。
HorizontalPodAutoscaler：用于自动调整Kubernetes集群中的pod副本数量，以根据当前负载需求实现自动扩展或收缩。
NetworkPolicy：用于定义网络访问策略，以控制pod之间的网络流量。
CustomResourceDefinition：用于定义自定义资源，以扩展Kubernetes API和CRD操作。
PodDisruptionBudget：用于定义维护期间可以安全中断的pod的最小数量，以确保Kubernetes集群的高可用性。
Role：用于定义对Kubernetes资源的操作权限，例如读、写、更新、删除等。
ClusterRole：与Role类似，但是可以在整个Kubernetes集群中使用。
```

##### 常见的 kind 类型

- Endpoints：Endpoints可以把外部的链接到k8s系统中（可以理解为引用外部资源，如将一个外部mysql连接到k8s中）
- Service：部署一个内部虚拟IP，其他deployment可以链接。（可以简单理解为K8S的端口映射，如外部3444端口映射到pod应用中80端口）
- Secrets：用于存储和管理一些敏感数据，比如密码，token，密钥等敏感信息。（可以理解为ssh中的密钥）
- Deployment
  - 适合无状态的服务部署
  - 部署一个Pod，内部只能链接service，无法互相链接。（可以简单理解为一个pod应用的部署工具，即使部署的应用挂了还能重启，但只能链接service服务）

##### flask - pod

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: flask01
  labels:
    versions: v1.3
    app_name: flask-glf-test
  namespace: glf-test
  annotations:
    create_user: glfAdd
spec:
  nodeName: cn-shenzhen.172.16.4.128
  containers:
    - name: glf-flask-test #容器名字
      image: 123123123123123123.aliyuncs.com/namespace1/registry1:flask-test-v1.0 #镜像信息
      ports: #容器对外的端口
        - containerPort: 5000
          protocol: TCP
          
```

```
      resources:
        limits:
          cpu: '4'
          memory: 4Gi
        requests:
          cpu: '4'
          memory: 4Gi

```



##### flask - Deployment

```yaml
apiVersion: apps/v1
kind: Deployment #deployment 为副本控制器
metadata:
  name: flask02
  labels:
    versions: v1.3
  namespace: glf-test
  annotations:
    create_user: glfAdd
spec:
  replicas: 2
  selector: #标签选择器
    matchLabels:
      app: flask111
  template:
    metadata:
      labels:
        app: flask111
    spec:
      nodeName: cn-shenzhen.172.16.4.128
      containers:
        - name: glf-flask-test
          image: 123123123123123123.aliyuncs.com/namespace1/registry1:flask-test-v1.0
          ports:
            - containerPort: 5000
              protocol: TCP
```

##### flask - HorizontalPodAutoscaler

水平伸缩

```yaml
apiVersion: autoscaling/v2beta2
kind: HorizontalPodAutoscaler
metadata:
  name: flask02-hpa
  labels:
    versions: v2.0
  namespace: glf-test
  annotations:
    create_user: glfAdd
spec:
  maxReplicas: 5
  minReplicas: 2
  metrics:
    - resource:
        name: memory
        target:
          averageUtilization: 92
          type: Utilization
      type: Resource
    - resource:
        name: cpu
        target:
          averageUtilization: 93
          type: Utilization
      type: Resource
  scaleTargetRef: # 指定要控制的Deployment
    apiVersion: apps/v1
    kind: Deployment
    name: flask02
```





##### 实例

> https://www.cnblogs.com/uestc2007/p/15848995.html

```yaml
apiVersion: v1       #必选，版本号，例如v1
kind: Pod            #必选，Pod
metadata:            #必选，元数据
  name: string       #必选，Pod名称
  namespace: string  #必选，Pod所属的命名空间
  labels:            #自定义标签
    - name: string   #自定义标签名字
  annotations:       #自定义注释列表
    - name: string
spec:                #必选，Pod中容器的详细定义
  containers:        #必选，Pod中容器列表
  - name: string     #必选，容器名称
    image: string    #必选，容器的镜像名称
    imagePullPolicy: Always #获取镜像的策略, Always | Never | IfNotPresent Alawys表示下载镜像 IfnotPresent表示优先使用本地镜像，否则下载镜像，Nerver表示仅使用本地镜像
    command: [string]    #容器的启动命令列表，如不指定，使用打包时使用的启动命令
    args: [string]       #容器的启动命令参数列表
    workingDir: string   #容器的工作目录
    volumeMounts:        #挂载到容器内部的存储卷配置
    - name: string       #引用pod定义的共享存储卷的名称，需用volumes[]部分定义的的卷名
      mountPath: string  #存储卷在容器内mount的绝对路径，应少于512字符
      readOnly: boolean  #是否为只读模式
    ports:               #需要暴露的端口库号列表
    - name: string       #端口号名称
      containerPort: int #容器需要监听的端口号
      hostPort: int      #容器所在主机需要监听的端口号，默认与Container相同
      protocol: string   #端口协议，支持TCP和UDP，默认TCP
    env:                 #容器运行前需设置的环境变量列表
    - name: string       #环境变量名称
      value: string      #环境变量的值
    resources:           #资源限制和请求的设置
      limits:            #资源限制的设置
        cpu: string      #Cpu的限制，单位为core数，将用于docker run --cpu-shares参数
        memory: string   #内存限制，单位可以为Mib/Gib，将用于docker run --memory参数
      requests:          #资源请求的设置
        cpu: string      #Cpu请求，容器启动的初始可用数量
        memory: string   #内存清楚，容器启动的初始可用数量
    livenessProbe:       #对Pod内个容器健康检查的设置，当探测无响应几次后将自动重启该容器，检查方法有exec、httpGet和tcpSocket，对一个容器只需设置其中一种方法即可
      exec:              #对Pod容器内检查方式设置为exec方式
        command: [string]  #exec方式需要制定的命令或脚本
      httpGet:             #对Pod内个容器健康检查方法设置为HttpGet，需要制定Path、port
        path: string
        port: number
        host: string
        scheme: string
        HttpHeaders:
        - name: string
          value: string
      tcpSocket:               #对Pod内个容器健康检查方式设置为tcpSocket方式
         port: number
       initialDelaySeconds: 0  #容器启动完成后首次探测的时间，单位为秒
       timeoutSeconds: 0       #对容器健康检查探测等待响应的超时时间，单位秒，默认1秒
       periodSeconds: 0        #对容器监控检查的定期探测时间设置，单位秒，默认10秒一次
       successThreshold: 0
       failureThreshold: 0
       securityContext:
         privileged:false
    restartPolicy: [Always | Never | OnFailure]#Pod的重启策略，Always表示一旦不管以何种方式终止运行，kubelet都将重启，OnFailure表示只有Pod以非0退出码退出才重启，Nerver表示不再重启该Pod
    nodeSelector: obeject  #设置NodeSelector表示将该Pod调度到包含这个label的node上，以key：value的格式指定
    imagePullSecrets:      #Pull镜像时使用的secret名称，以key：secretkey格式指定
    - name: string
    hostNetwork:false      #是否使用主机网络模式，默认为false，如果设置为true，表示使用宿主机网络
    volumes:               #在该pod上定义共享存储卷列表
    - name: string         #共享存储卷名称 （volumes类型有很多种）
      emptyDir: {}         #类型为emtyDir的存储卷，与Pod同生命周期的一个临时目录。为空值
      hostPath: string     #类型为hostPath的存储卷，表示挂载Pod所在宿主机的目录
        path: string       #Pod所在宿主机的目录，将被用于同期中mount的目录
      secret:              #类型为secret的存储卷，挂载集群与定义的secre对象到容器内部
        scretname: string  
        items:     
        - key: string
          path: string
      configMap:           #类型为configMap的存储卷，挂载预定义的configMap对象到容器内部
        name: string
        items:
        - key: string
          path: string   

```



# 命令

## 命令缩写

```
componentstatuses                 cs                                          false        ComponentStatus
configmaps                        cm                                          true         ConfigMap
endpoints                         ep                                          true         Endpoints
events                            ev                                          true         Event
limitranges                       limits                                      true         LimitRange
namespaces                        ns                                          false        Namespace
nodes                             no                                          false        Node
persistentvolumeclaims            pvc                                         true         PersistentVolumeClaim
persistentvolumes                 pv                                          false        PersistentVolume
pods                              po                                          true         Pod
podtemplates                                                                  true         PodTemplate
replicationcontrollers            rc                                          true         ReplicationController
resourcequotas                    quota                                       true         ResourceQuota
secrets                                                                       true         Secret
serviceaccounts                   sa                                          true         ServiceAccount
services                          svc                                         true         Service
daemonsets                        ds           apps                           true         DaemonSet
deployments                       deploy       apps                           true         Deployment
replicasets                       rs           apps                           true         ReplicaSet
statefulsets                      sts          apps                           true         StatefulSet
horizontalpodautoscalers          hpa          autoscaling                    true         HorizontalPodAutoscaler
cronjobs                          cj           batch                          true         CronJob
jobs                                           batch                          true         Job
certificatesigningrequests        csr          certificates.k8s.io            false        CertificateSigningRequest
events                            ev           events.k8s.io                  true         Event
daemonsets                        ds           extensions                     true         DaemonSet
deployments                       deploy       extensions                     true         Deployment
ingresses                         ing          extensions                     true         Ingress
networkpolicies                   netpol       extensions                     true         NetworkPolicy
podsecuritypolicies               psp          extensions                     false        PodSecurityPolicy
replicasets                       rs           extensions                     true         ReplicaSet
ingresses                         ing          networking.k8s.io              true         Ingress
networkpolicies                   netpol       networking.k8s.io              true         NetworkPolicy
runtimeclasses                                 node.k8s.io                    false        RuntimeClass
poddisruptionbudgets              pdb          policy                         true         PodDisruptionBudget
podsecuritypolicies               psp          policy                         false        PodSecurityPolicy
priorityclasses                   pc           scheduling.k8s.io              false        PriorityClass
storageclasses                    sc           storage.k8s.io                 false        StorageClass
```

```
certificatesigningrequests (缩写 csr)
componentstatuses (缩写 cs)
configmaps (缩写 cm)
customresourcedefinition (缩写 crd)
daemonsets (缩写 ds)
deployments (缩写 deploy)
endpoints (缩写 ep)
events (缩写 ev)
horizontalpodautoautoscalers (缩写 hpa)
ingresses (缩写 ing)
limitranges (缩写 limits)
namespaces (缩写 ns)
networkpolicies (缩写 netpol)
nodes (缩写 no)
persistentvolumeclaims (缩写 pvc)
persistentvolumes (缩写 pv)
poddisruptionbudgets (缩写 pdb)
pods (缩写 po)
podsecuritypolicies (缩写 psp)
replicasets (缩写 rs)
replicationcontrollers (缩写 rc)
resourcequotas (缩写 quota)
serviceaccounts (缩写 sa)
services (缩写 svc)
statefulsets (缩写 sts)
storageclasses (缩写 sc)
```



```bash
# 查看 api 版本
$ kubectl api-versions


$ kubectl version --client
```

##### 重启 pod

无法重启 pod, 可以通过一下方式实现

- 方式 1:

  ```bash
  # 平滑重启, 创建新的 pod, 再释放旧的 pod
  $ kubectl rollout restart deployment flask02
  
  
   $ kubectl get pods
  NAME                       READY   STATUS        RESTARTS   AGE
  flask02-56c66c7777-7sdvm   1/1     Terminating   0          6m19s
  flask02-56c66c7777-nmwlt   1/1     Terminating   0          6m17s
  flask02-685596c7-gcxr6     1/1     Running       0          22s
  flask02-685596c7-smf67     1/1     Running       0          24s
  ```

- 方式 2:

  ```bash
  # 先将副本数改为 0 , 再将副本数改回, 会中断服务
  $ kubectl scale deployment flask02 -n glf-test --replicas=0
  $ kubectl scale deployment flask02 -n glf-test --replicas=2
  
  
   $ kubectl get pod
  NAME                     READY   STATUS              RESTARTS   AGE
  flask02-685596c7-bzmrr   0/1     ContainerCreating   0          2s
  flask02-685596c7-gcxr6   1/1     Terminating         0          11m
  flask02-685596c7-mx9pl   0/1     ContainerCreating   0          2s
  flask02-685596c7-smf67   1/1     Terminating         0          11m
  ```

- 方式 3:

  ```bash
  # 删除 pod, 和方式 1 效果一样
  $ kubectl delete pod flask02-685596c7-mx9pl -n glf-test
  $ kubectl delete pod flask02-685596c7-x112l -n glf-test
  
  
   $ kubectl get pods
  NAME                       READY   STATUS        RESTARTS   AGE
  flask02-56c66c7777-7sdvm   1/1     Terminating   0          6m19s
  flask02-56c66c7777-nmwlt   1/1     Terminating   0          6m17s
  flask02-685596c7-gcxr6     1/1     Running       0          22s
  flask02-685596c7-smf67     1/1     Running       0          24s
  ```

- 方式 4:

  ```bash
  kubectl replace
  
  这种方法是通过更新Pod ，从触发k8s pod 的更新
  
  kubectl get pod <pod_name> -n <namespace> -o yaml | kubectl replace --force
  ```

- 方式 5:

  ```
  kubectl set env
  
  通过 设置环境变量，其实也是更新pod spec 从而触发滚动升级。
  
  kubectl set env deployment <deployment name> -n <namespace> DEPLOY_DATE="$(date)"
  
      1.
  
  只不过这里通过kubectl 命令行，当我们通过API 更新pod spec 后一样会触发滚动升级
  
  
  
  ```

- 方式 6: (不一定成功)

  ```bash
  # 在容器里面 kill 1 号进程, 
  # 有个局限，必须要求你的 1 号进程要 捕获 TERM 信号，否则在容器里面是杀不死自己的
  
  $ kubectl exec -it flask02-685596c7-t2g4k -n glf-test bash -c "kill 1"
  ```

##### 滚动升级

```

```



## node

```
https://www.yii666.com/blog/448360.html

在 Kubernetes 中使用 Node Selector 和 Affinity 机制来实现 Node 划分



Node Selector 是一种将 Pod 调度到符合特定节点标签的节点上的机制


Namespace划分

ResourceQuota划分


```



## config

##### 参数说明

| 选项            | 说明                                                        |      |
| --------------- | ----------------------------------------------------------- | ---- |
| current-context | 显示当前的上下文名称                                        |      |
| delete-cluster  | 从 kubeconfig 中删除指定的集群                              |      |
| delete-context  | 从 kubeconfig 中删除指定的上下文                            |      |
| delete-user     |                                                             |      |
| get-clusters    | 输出所有的集群信息                                          |      |
| get-contexts    | 输出所有的上下文信息，同时会标记哪一个是当前的上下文        |      |
| get-users       |                                                             |      |
| rename-context  | 重命名一个上下文                                            |      |
| set             | 设置 kubeconfig 中一个具体的属性的值                        |      |
| set-cluster     | 设置指定集群的属性                                          |      |
| set-context     | 设置指定上下文的属性                                        |      |
| set-credentials | 设置指定用户的属性                                          |      |
| unset           | 删除 kubeconfig 中一个具体的属性的值                        |      |
| use-context     | 指定某个上下文为当前激活的上下文                            |      |
| view            | 输出合并后的kubeconfig的内容，格式为 YAML，密文内容不会显示 |      |

```bash
$ kubectl config view -o jsonpath='{.clusters[?(@.name == "kubernetes")].cluster.server}'


# 查看命名空间
$ kubectl get namespace
```

##### 生成 yaml / json 文件

```bash
#生成一个以nginx为镜像，名称为nginx、副本数为2的deployment 的 yaml 和 json 文件
$ kubectl create deployment nginx --image=nginx -o json --dry-run=client --replicas=2 >nginx.json
$ kubectl create deployment nginx --image=nginx -o yaml --dry-run=client --replicas=2 >nginx.yaml
    # depolyment：工作负载
    # --dry-run 表示尝试运行,并不会真正执行
    # --image=nginx：这个为对应镜像是nginx,
    # -o yaml ：会把这个操作用yaml的格式生成出来，
```

##### 导出 yaml / json

```bash
$ kubectl get deployment ocean-test-16 -o=yaml -- export 123.yaml

```



## explain

```bash
# 获取 pod 和 svc 的文档
$ kubectl explain pods,svc 
```

## create

> 创建一个集群资源对象, 支持JSON和YAML格式的文件

```bash
# 创建资源
$ kubectl create -f ./my-manifest.yaml
# 使用多个文件创建资源
$ kubectl create -f ./my1.yaml -f ./my2.yaml
# 使用目录下的所有清单文件来创建资源
$ kubectl create -f ./dir
# 使用 url 来创建资源
$ kubectl create -f https://git.io/vPieo
# 从 stdin 输入中创建多个 YAML 对象
$ cat <<EOF | kubectl create -f -
apiVersion: v1
kind: Pod
metadata:
  name: busybox-sleep
spec:
  containers:
  - name: busybox
    image: busybox
    args:
    - sleep
    - "1000000"
---
apiVersion: v1
kind: Pod
metadata:
  name: busybox-sleep-less
spec:
  containers:
  - name: busybox
    image: busybox
    args:
    - sleep
    - "1000"
EOF
# 创建包含几个 key 的 Secret
$ cat <<EOF | kubectl create -f -
apiVersion: v1
kind: Secret
metadata:
  name: mysecret
type: Opaque
data:
  password: $(echo "s33msi4" | base64)
  username: $(echo "jane" | base64)
EOF
```

## apply

## replace

```
```



## exec

```
进入容器
$ kubectl exec -it flask02-685596c7-t2g4k -n glf-test bash

```



## get

```bash
# 列出所有 namespace 中的所有 service
$ kubectl get services            
# 列出所有 namespace 中的所有 pod
$ kubectl get pods --all-namespaces  
# 列出所有 pod 并显示详细信息
$ kubectl get pods -o wide   
# 根据命名空间获取 pod
$ kubectl get pod -n glf-test
# 列出指定 deployment
$ kubectl get deployment my-dep      
# 列出该 namespace 中的所有 pod 包括未初始化的
$ kubectl get pods --include-uninitialized      
# 使用详细输出来描述命令
$ kubectl describe nodes my-node
$ kubectl describe pods my-pod
# List Services Sorted by Name
$ kubectl get services --sort-by=.metadata.name 
# 根据重启次数排序列出 pod
$ kubectl get pods --sort-by='.status.containerStatuses[0].restartCount'
# 获取所有具有 app=cassandra 的 pod 中的 version 标签
$ kubectl get pods --selector=app=cassandra rc -o jsonpath='{.items[*].metadata.labels.version}'
# 获取所有节点的 ExternalIP
$ kubectl get nodes -o jsonpath='{.items[*].status.addresses[?(@.type=="ExternalIP")].address}'
# 列出属于某个 PC 的 Pod 的名字
# “jq”命令用于转换复杂的 jsonpath，参考 https://stedolan.github.io/jq/
$ sel=${$(kubectl get rc my-rc --output=json | jq -j '.spec.selector | to_entries | .[] | "\(.key)=\(.value),"')%?}
$ echo $(kubectl get pods --selector=$sel --output=jsonpath={.items..metadata.name})
# 查看哪些节点已就绪
$ JSONPATH='{range .items[*]}{@.metadata.name}:{range @.status.conditions[*]}{@.type}={@.status};{end}{end}' \
 && kubectl get nodes -o jsonpath="$JSONPATH" | grep "Ready=True"
# 列出当前 Pod 中使用的 Secret
$ kubectl get pods -o json | jq '.items[].spec.containers[].env[]?.valueFrom.secretKeyRef.name' | grep -v null | sort | uniq
```

## describe

```bash
# 查看 node 状态
$ kubectl describe node virtual131321312
# 查看 pod 状态 (要指定命名空间)
$ kubectl describe pod flask01-b4badsf-asdf --namespace=123te
```

## delete

##### 删除 pod

```bash
# 直接删除 pod 会自动启动
$ kubectl get pods -n glf-test
$ kubectl delete pod flask01-b4bcd67f-9qbq4 --namespace glf-test
$ kubectl get pods -n glf-test

# 删除 pod 控制器后 pod 自动删除了
$ kubectl get deploy -n glf-test
$ kubectl delete deploy flask01 -n glf-test


# 批量删除 OutOfcpu 状态的 pod
# 打印指定命名空间下所有OutOfCpu 的 pod
$ kubectl get pods -n  glf-test | grep OutOfcpu | awk '{print $1}'
# 批量删掉pod
$ kubectl get pods -n  glf-test | grep OutOfcpu | awk '{print $1}' | xargs kubectl delete pod -n  namespace
```

## label

##### 标签操作

```bash
# 创建标签
$ kubectl label nodes node01 app_name=flask-glf-test

# 标签已经存在, 覆盖时报错
		error: 'tier' already has a value (frontend), and --overwrite is false
# 更新标签
$ kubectl label nodes node01 app_name=flask-glf-test --overwrite=True



$ kubectl label pod "pod名称" "label信息" "命名空间" --overwrite




# 查看标签
$ kubectl get nodes --show-labels 

# 删除标签, 后面的 - 表示删除标签
$ kubectl label nodes node01 app_name-
```

##### 部署到指定节点

```bash
# 如果需要限制 Pod 到指定的 Node 上运行, 可以给 Node 打标签并给 Pod 配置 NodeSelector

# 查看节点
$ kubectl get nodes
# 节点状态
$ kubectl describe node node01
```

- 使用 nodeName 指定节点

  ```yaml
  spec:
    nodeName: only-worker-node-3
  ```

- 使用 nodeSelector 匹配节点标签

  ```yaml
  # 给 node 设置标签, 
  spec:
    nodeSelector: 
      test-nodeselector: target-node
  ```

## logs

```bash
$ kubectl logs flask02-5d5564f57d-2jfv5 -n glf-test -f
```

## top

```bash
$ kubectl top nodes
$ kubectl top pod -n glf-test

```



# 弹性策略

> https://blog.csdn.net/ling_76539446/article/details/104236851



```
1. 先创建 deployment
2. 再创建 HorizontalPodAutoscaler
	根据 scaleTargetRef 查找
```





```
https://www.cnblogs.com/alisystemsoftware/p/17022897.html



K8s 在应用层面提供了 HPA，围绕 HPA 开源社区延伸出了 KEDA 这样的弹性组件，为微服务应用以业务指标执行弹性策略提供了实现的可能性。但 HPA 正常工作的一个大前提是需要保证集群资源充足，为此用户必须提前对集群扩容或时常保持集群资源冗余

edas
https://help.aliyun.com/apsara/agile-cnstack/v_1_2_0_20220518/edas/edas-apsarastack-user-guide/auto-scaling-k8s.html


https://cloud.tencent.com/developer/article/2038102
```

## HorizontalPodAutoscaler

##### 参考

- [ ] https://www.jianshu.com/p/e4c130dfcd87
- [ ] https://zhuanlan.zhihu.com/p/245208287

```
https://www.scriptjc.com/article/1136
https://blog.csdn.net/m0_50589374/article/details/126422596



horizontal-pod-autoscaler-sync-period 修改
冷却时间, 周期, 稳定期, 要在启动容器的 yaml 里面配置
```



http://www.hzhcontrols.com/new-1016919.html



##### apiVersion

```
HorizontalPodAutoscaler 是 Kubernetes autoscaling API 组的资源
当前稳定版本（autoscaling/v1）中只支持基于 CPU 指标的扩缩

API 的 beta 版本（autoscaling/v2beta2）引入了基于内存和自定义指标的扩缩。 在 autoscaling/v2beta2 版本中新引入的字段在 autoscaling/v1 版本中以注解 的形式得以保留。


```



```
Pod 水平自动扩缩全名是Horizontal Pod Autoscaler简称HPA。它可以基于 CPU 利用率或其他指标自动扩缩 ReplicationController、Deployment 和 ReplicaSet 中的 Pod 数量




根据观察到的CPU利用率（或在支持自定义指标的情况下，根据其他一些应用程序提供的指标）自动伸缩 replication controller, deployment, replica set, stateful set 中的pod数量。注意，Horizontal Pod Autoscaling不适用于无法伸缩的对象，例如DaemonSets。







```

##### 循环周期

```

循环周期由 controller manager 中的--horizontal-pod-autoscaler-sync-period标志指定（默认是 30 秒）



```



```bash
$ kubectl get hpa --all-namespaces
$ kubectl describe hpa -n glf-test
$ kubectl delete hpa a1 -n glf-test



$ kubectl autoscale deployment flask02 -n glf-test --cpu-percent=80 --min=1 --max=4
$ kubectl scale



```

## CronHPA

```
https://help.aliyun.com/document_detail/151557.html?spm=5176.2020520152.help.dexternal.735e16ddXsXgn1#section-ah0-3o3-h28
```

# 升级和回滚

##### 参考

- [ ] https://blog.csdn.net/qq_20042935/article/details/128476388
- [ ] 

##### 滚动升级

```
```





# 启动失败排除问题

##### 启动失败

```
1. 是否指定了运行的节点
2. 镜像地址是否正确, 使用完整镜像地址
3. 容器的网络地址外网是否能访问
4. 容器的端口和里面服务的端口是否一致
```




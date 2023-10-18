```
文档:
https://help.aliyun.com/document_detail/160530.html?spm=a2c4g.167546.0.0.4d8c67f65ODK8Y


参考:
https://www.jb51.net/article/248648.htm
https://www.cnblogs.com/machangwei-8/p/15925358.html#_label4_3



环境变量
https://programtalk.com/python-more-examples/kubernetes.client.V1EnvVar
https://vimsky.com/examples/detail/python-method-kubernetes.client.V1EnvVar.html


V1Lifecycle
https://python.hotexamples.com/examples/kubernetes.client/-/V1Lifecycle/python-v1lifecycle-function-examples.html




https://blog.csdn.net/qq_35447389/article/details/105313052
```

[pip](https://pypi.org/project/kubernetes/)

[github](https://github.com/kubernetes-client/python)

##### client

```
都是 Kubernetes Python 客户端库中的 API, 它们分别用于不同的 Kubernetes API 对象

AppsV1Api：用于管理 Kubernetes 应用程序的 API 对象，如 Deployment、StatefulSet、DaemonSet 和 ReplicaSet 等
BatchV1Api：用于管理 Kubernetes 批处理作业的 API 对象，如 Job 和 CronJob 等。
CoreV1Api：用于管理 Kubernetes 核心 API 对象，如 Pod、Service、Namespace、Node 和 PersistentVolume 等
```

```
# 查看deployment内容
def read_namespaced_deployment

patch_namespaced_deployment ：局部更新YAML (文件里写了哪些, 就更新哪些, 没写的不变)
replace_namespaced_deployment：替换整个YAML (完完全全按照文件更新)


```


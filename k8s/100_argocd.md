```

可以挂历多个 k8s 集群




Kubernetes_部署_k8s的四种部署策略(滚动更新、重新创建、金丝雀部署、蓝绿部署)
http://www.taodudu.cc/news/show-5584545.html?action=onClick


简介
https://blog.csdn.net/ichen820/article/details/126667804
https://blog.csdn.net/xixihahalelehehe/article/details/122238344 (1)
```

##### 参考

[github](https://github.com/argoproj/argo-cd)

##### 说明

```
最新版本 2.7.4
```

##### 安装方式

```
多租户（multi-tenant）、 core 、自定义 、Helm
```



##### 安装 argocd

> 在 k8s 中部署

```bash
# 1. 创建命名空间 (会安装很多服务, 所以单独创建一个命名空间)
$ kubectl create namespace argocd 


# 2. 获取 install.yaml 文件
# No-HA
$ kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/v2.7.4/manifests/install.yaml
# HA
$ kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/v2.7.4/manifests/ha/install.yaml
# 这个是不是最新版本???
$ wget https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
或
$ kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml


# 3. 部署 argo cd
$ kubectl apply -n argocd -f install.yaml


# 暴露 ui 端口供访问
kubectl port-forward --address 0.0.0.0 svc/argocd-server -n argocd 8080:443
# 获取登录用户 admin 密码
kubectl get pods -n argocd -l app.kubernetes.io/name=argocd-server -o name | cut -d'/' -f 2

```

##### 安装 cli

```bash

# https://github.com/argoproj/argo-cd/releases/download/v2.1.2/argocd-linux-amd64
$ cp argocd-linux-amd64 /usr/local/bin/argocd
$ chmod +x /usr/local/bin/argocd


```

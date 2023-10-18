```
快捷搭建kubernetes(k8s)的安装工具，它提供了kubeadm init 以及 kubeadm join这两个命令来快速创建kubernetes集群。
```

##### 安装

- 关闭防火墙

  ```bash
  $ systemctl stop firewalld
  $ systemctl disable firewalld
  $ systemctl status firewalld
  ```

- 关闭 selinux

  ```bash
  # 查看 selinux 状态
  $ sestatus
  # 永久关闭
  $ sed -i 's/enforcing/disabled/' /etc/selinux/config
  # 临时关闭
  $ setenforce												
  # 立即生效
  $ setenforce 0
  ```

- 时间同步(未使用)

  ```bash
  $ yum install ntp chrony
  $ systemctl status chronyd
  $ systemctl start chronyd
  ```

- 创建 kubernetes.repo 源

  ```
  [kubernetes]
  name=kubernetes
  baseurl=https://mirrors.aliyun.com/kubernetes/yum/repos/kubernetes-el7-x86_64/
  enabled=1
  gpgcheck=0
  repo_gpgcheck=0
  gpgkey=https://mirrors.aliyun.com/kubernetes/yum/doc/yum-key.gpg
  https://mirrors.aliyun.com/kubernetes/yum/doc/rpm-package-key.gpg
  ```

- 安装

  ```bash
  $ yum install kubelet kubeadm kubectl
  $ yum install kubelet-1.27.3 kubeadm-1.27.3 kubectl-1.27.3
  ```

- 123

  ```bash
  # 查看需要的镜像
  $ kubeadm config images list
  registry.k8s.io/kube-apiserver:v1.27.3
  registry.k8s.io/kube-controller-manager:v1.27.3
  registry.k8s.io/kube-scheduler:v1.27.3
  registry.k8s.io/kube-proxy:v1.27.3
  registry.k8s.io/pause:3.9
  registry.k8s.io/etcd:3.5.7-0
  registry.k8s.io/coredns/coredns:v1.10.1
  
  
  
  # init kuberlet
  
  
  
  ```

  ```bash
  $ kubeadm init --apiserver-advertise-address=192.168.2.100 \
  --image-repository registry.aliyuncs.com/google_containers \
  --kubernetes-version=v1.18.20 \									#版本号自选
  --service-cidr=10.96.0.0/12 \									#可不改
  --pod-network-cidr=10.244.0.0/16								#可不改
  
  初始化成功后显示：Your Kubernetes control-plane has initialized successfully!
  
  ```

  ```bash
  $ kubeadm init --apiserver-advertise-address=192.168.28.128 \
  --image-repository registry.aliyuncs.com/google_containers \
  --kubernetes-version=1.21.3 \
  --pod-network-cidr=10.0.0.0/24 
  
  
  
  
  ```

  

##### docker 使用 systemctl 命令

```bash
报错
	Failed to get D-Bus connection: No such file or directory


mac
    vim ~/Library/Group\ Containers/group.com.docker/settings.json
    修改"deprecatedCgroupv1"参数为true，默认是false
    然后重启docker环境
```

##### docker 安装 centos

```bash
$ docker pull centos:centos7
$ docker run -tid -p 50001:22 --privileged=true --name centos7 centos:centos7 /usr/sbin/init
$ docker exec -it centos7 bash
```

##### ssh

```bash
$ yum reinstall -y net-tools 
$ yum reinstall -y openssh-server
$ yum reinstall -y passwd
$ systemctl restart sshd
```

##### 阿里源

```bash
$ wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo
$ yum clean all
$ yum makecache
$ yum update -y
```

##### epel-release

```bash
$ yum install epel-release
```

##### 启动后开发端口

```
```

##### commit

```bash
docker commit [OPTIONS] CONTAINER [REPOSITORY[:TAG]]
  -a：提交的镜像作者
  -c：使用Dockerfile指令来创建镜像
  -m：提交时的说明文字
  -p：在commit时，将容器暂停 (默认选项)


# 制作镜像
$ docker commit -a "glfadd" -m "centos7 base" 容器ID/名字 镜像名:标签
$ docker commit -a="glfadd" -m="centos7 base" centos7 centos7:v0.1
$ docker commit -a="glfadd" -m="centos7 base" d2f25733acbe centos7:v0.1

# 查看镜像
$ docker images
$ docker history centos7:v0.1
```

##### save

```bash
将镜像打包为 tar 文件
$ docker save -o centos7_python_3.9.2_image.tar centos7_python:3.9.2
$ docker save -o ~/Downloads/centos7_python_3.9.2_image.tar centos7_python:3.9.2


参数


```
















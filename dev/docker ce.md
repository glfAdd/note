# 安装

##### centos

```bash
安装
# yum -y install yum-utils
# sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
# sudo yum install docker-ce

启动命令
# systemctl start docker
# systemctl enable docker
# systemctl restart docker
# systemctl status docker

国内源
# vim /etc/docker/daemon.json
{
  "registry-mirrors": ["https://docker.mirrors.ustc.edu.cn/"]
}
```

##### debian

```
第1步：卸载旧软件
apt-get remove docker docker-engine docker.io containerd runc

第2步：更新软件仓库索引
apt-get update

第3步：安装相关工具
apt-get install apt-transport-https ca-certificates curl gnupg2 software-properties-common

第4步：安装GPG密钥
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -

第5步：添加Docker仓库
修改/etc/apt/sources.list文件，根据自己的操作系统类型选择Docker官方仓库。
#Debian 9 使用这个Docker仓库
deb https://download.docker.com/linux/debian stretch stable
#Ubuntu 16.04 使用这个Docker仓库
deb https://download.docker.com/linux/ubuntu xenial stable

第6步：更新软件仓库索引
apt-get update

第7步：安装Docker CE
apt-get install docker-ce docker-ce-cli containerd.io


service docker start
service docker restart

```

##### mac

```
官网下载
```


##### 国内源

```
推荐使用阿里加速源
{
  "registry-mirrors" : [
    "http://ovfftd6p.mirror.aliyuncs.com",
    "http://registry.docker-cn.com",
    "http://docker.mirrors.ustc.edu.cn",
    "http://hub-mirror.c.163.com"
  ],
  "insecure-registries" : [
    "registry.docker-cn.com",
    "docker.mirrors.ustc.edu.cn"
  ],
  "debug" : true,
  "experimental" : true
}
```

##### 镜像网站

```
https://hub.docker.com/
```

# Docker

##### apt-get

```
apt-get update
apt-get vim
```

##### 文件拷贝到docker容器

```
docker cp 原文件路径 容器名字:容器里的路径
docker cp /root/init.sh  CS5_AS_EALL1:/home/hundsun/workspace/log
```

##### 常用命令

```python
docker version
systemctl daemon-reload
docker images
docker ps -a
docker ps
docker container ls -a
# 删除已有的image
docker rmi image_id
docker rmi -f 91dadee7afee
# 删除容器
docker rm 69ecad01f6c0
docker start mysql
docker stop 容器ID或容器名
docker stop container_name
# 参数 -t：关闭容器的限时，如果超时未能关闭则用kill强制关闭，默认值10s，这个时间用于容器的自己保存状态 
docker stop -t=60 容器ID或容器名
docker kill 容器ID或容器名
# 搜索
docker starch jumpserver
```

##### mysql

```python
docker pull mysql
docker pull mysql:5.7.25
# 创建并启动一个MySQL容器
docker run --name mysql7 -e MYSQL_ROOT_PASSWORD=123456 -p 3306:3306 -d mysql:5.7.25
docker run --name mysql8 -e MYSQL_ROOT_PASSWORD=123456 -p 3307:3307 -d mysql

# 进入容器
docker exec -it mysql sh
# 登录
mysql -uroot -p123456
```

##### redis

```python
docker pull redis
docker run --name redis -p 6379:6379 -d redis:latest
    
mac客户端
https://github.com/luin/medis
```

##### zookeerper

```
docker pull zookeeper
docker run --privileged=true -d --name zookeeper --publish 2181:2181  -d zookeeper:latest
```

##### nginx

```
docker pull nginx
docker run -d --name nginx nginx
```

##### postgresql

```
docker pull postgres:9.5
docker run --name postgres95 -e POSTGRES_PASSWORD=123456 -p 5432:5432 -d postgres:11.4
run，创建并运行一个容器；
--name，指定创建的容器的名字；
-e POSTGRES_PASSWORD=password，设置环境变量，指定数据库的登录口令为password；
-p 54321:5432，端口映射将容器的5432端口映射到外部机器的54321端口；
-d postgres:9.4，指定使用postgres:9.4作为
```

##### rabbitmq

```
docker pull rabbitmq
docker pull rabbitmq:management  (带web管理页面)

docker run -d --name rabbitmq --publish 5671:5671 --publish 5672:5672 --publish 4369:4369 --publish 25672:25672 --publish 15671:15671 --publish 15672:15672 rabbitmq:management

docker run -d --hostname my-rabbit --name rabbit -e RABBITMQ_DEFAULT_USER=admin -e RABBITMQ_DEFAULT_PASS=admin -p 15672:15672 -p 5672:5672 -p 25672:25672 -p 61613:61613 -p 1883:1883 rabbitmq:management

http://宿主机IP:15672，默认创建了一个 guest 用户，密码也是 guest
```

##### jumpserver

```
参考
https://www.jianshu.com/p/1475ebde6297

docker run --name jms_all -d -p 8030:80 -p 8020:2222 jumpserver/jms_all:latest
8030的意思是Jumpserver 管理的客户端  8020代表的是你堡垒机的端口号
访问:  http://127.0.0.1:8030/users/login/?next=/
默认帐号： Admin  密码：admin
```

##### tensorflow serving

```





```


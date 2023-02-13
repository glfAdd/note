##### 参考

```
docker save和docker export
https://www.cnblogs.com/pekkle/p/8988471.html



python docker
https://www.cnblogs.com/jpfss/p/10941739.html
https://doc.sensorsdata.cn/pages/viewpage.action?pageId=183022417



dockerfile 参数设置
https://blog.csdn.net/u010246789/article/details/54139168



```

## python 基础镜像

##### docker 安装 centos

> [docker hub](https://hub.docker.com/_/centos)

```bash
$ docker pull centos:centos7.9.2009
$ docker run -itd --name centos_python_base centos:centos7.9.2009
$ docker exec -it centos_python_base bash
$ yum update -y
$ yum install vim htop wget git -y

$ yum install zlib-devel gcc make bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel libffi-devel -y
```

##### 安装 python

```bash
$ mkdir -p /usr/local/python/python3
$ wget https://www.python.org/ftp/python/3.9.2/Python-3.9.2.tgz
$ tar zxvf Python-3.9.2.tgz
$ cd Python-3.9.2
$ ./configure --prefix=/usr/local/python/python3
$ make && make install
$ ln -s /usr/local/python/python3/bin/python3.9 /usr/bin/python3
$ ln -s /usr/local/python/python3/bin/pip3 /usr/bin/pip3
$ pip3 install --upgrade pip
$ pip3 --version
$ python3 --version
```

##### 制作镜像

> docker commit <container_id> <image_name>:<tag> 

```bash
$ docker commit ba7f013af38a centos7_python:3.9.2
```

##### 将镜像打包为 tar 文件

```bash
$ docker save -o centos7_python_3.9.2_image.tar centos7_python:3.9.2

$ docker save -o ~/Downloads/centos7_python_3.9.2_image.tar centos7_python:3.9.2
```

##### 问题 1

```
为什么不将python3命令配置成python


在CentOS服务器上，我们可以在 ~/.bash_profile中配置别名的方式将python3命令简化成python。但是通过配置别名的方式无法在容器内部良好的实现。因为服务器或安装CentOS镜像的虚拟机（注意虚拟机镜像不是Docker镜像）带有完整的操作系统，在操作系统启动的过程中，会执行 boot 的所有初始化操作。但 Docker 则不是， Docker 只运行我们设置需要启动运行的脚本，否则不会自己运行。因此每次使用/bin/bash进程进入container内部，不会自动的加载环境变量文件，也就无法使别名生效。除非docker容器自动后，手动source ~/.bash_profile，但这样无疑增加了使用复杂度，没有意义。

但并非无法使用python命令直接调用python3。我们可以在/usr/bin目录下将python3重命名为python即可。但是这个操作并不推荐大家使用，首先会覆盖原有的python文件（原有的python文件是python2版本）。不过这个问题倒容易解决，我们只需要在重命名前备份即可。其次，系统中的一些工具代码依赖python2，如果我们强行将python3重命名为python，会导致一些工具无法使用（比如yum）。以yum为例，解决这个问题需要在/usr/bin/yum文件中把第一行注释修改为 #!/usr/bin/python2 就可以规避。

```

## 打包 python

##### 构建镜像

```bash
$ docker build -t 'testflask' .


	-t: 镜像的名字


```

##### 运行镜像 

- debug

  ```bash
  $ docker run -it --rm -p 10469:10469 testflask
  ```

- production

  ```bash
  $ docker run -d -p 10469:10469 --name test-flask-1 testflask
  ```

  






















































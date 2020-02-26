##### 用户 / 用户组

```bash
# cat /etc/group							所有用户组
# groups glfadd								查看用户所在的组
# groupadd test								新建用户组
# cat /etc/passwd							所用用户
# cat /etc/passwd|grep xxx		查看某个用户

将glfadd用户添加到test组
usermod -s /bin/bash -g test glfadd
```

##### 定时任务

```bash
查看定时任务
# crontab -l

编辑定时任务
# crontab -e

0 1 * * * nohup pyton /sources/LFFlightChange/tools/ak_change.py > /dev/null 2>&1 &
```

##### 目录文件

```bash
查看SL目录大小
# du -sh aaa
将5J、SL目标打包成5j_sl.tar.gz压缩包
# tar zcf 5j_sl.tar.gz aaa/ bbb/ 
查看文件个数
# ll SL|wc -l
查看磁盘空间
# df -h
```



```bash
查看ip
netstat -anp|grep postmaster

查看占用端口的进程
netstat -antup | grep 5432

将引号中内容写入某文件中 echo
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile

访问网址看看返回什么
curl https://www.baidu.com

查看源
yum list | grep postgresql

检查80端口是否被占用
netstat -ano|grep 80
```

##### 环境变量

```bash
查看设置的变量
export

当前窗口临时添加
export PYTHONPATH=$PYTHONPATH:/root/code/Web/website
```

##### 服务器端口

```bash
netstat -anp																			查看开放的端口
firewall-cmd --query-port=666/tcp									查询端口是否开放
firewall-cmd --add-port=123/tcp --permanent				开放的端口
firewall-cmd --permanent --remove-port=123/tcp		移除指定端口


systemctl status firewalld				查看防火墙状态 
systemctl start firewalld  				开启防火墙 
systemctl stop firewalld					关闭防火墙 
firewall-cmd --reload							重载入添加的端口
```

##### linux 查看图片

```bash
1.开放端口

2.在图片目录下启动
python -m SimpleHTTPServer

3.浏览区查看图片
http://10.211.55.3:8000/
```

##### 防火墙

```bash
开启防火墙
# systemctl start firewalld
查看已打开的端口  
# netstat -anp
查看想开的端口是否已开, 提示no表示未开, yes表示成功
# firewall-cmd --query-port=666/tcp
开永久端口号. success表示成功
# firewall-cmd --add-port=666/tcp --permanent
若移除端口 
# firewall-cmd --permanent --remove-port=666/tcp
重新载入
# firewall-cmd --reload
```

##### 文件目录

```bash
/usr：系统级的目录，可以理解为C:/Windows/

/usr/lib理解为C:/Windows/System32

/usr/local：用户级的程序目录，可以理解为C:/Progrem Files/。用户自己编译的软件默认会安装到这个目录下. 里主要存放那些手动安装的软件，即不是通过apt-get安装的软件。它和/usr目录具有相类似的目录结构。让软件包管理器来管理/usr目录，而把自定义的脚本(scripts)放到/usr/local目录下面，我想这应该是个不错的主意。

/usr/src：系统级的源码目录

/usr/local/src：用户级的源码目录

/opt：用户级的程序目录，可以理解为D:/Software，opt有可选的意思，这里可以用于放置第三方大型软件（或游戏），当你不需要时，直接rm -rf掉即可。在硬盘容量不够时，也可将/opt单独挂载到其他磁盘上使用
这里主要存放那些可选的程序。你想尝试最新的firefox测试版吗?那就装到/opt目录下吧，这样，当你尝试完，想删掉firefox的时候，你就可 以直接删除它，而不影响系统其他任何设置。安装到/opt目录下的程序，它所有的数据、库文件等等都是放在同个目录下面。举个例子：刚才装的测试版firefox，就可以装到/opt/firefox_beta目录下，/opt/firefox_beta目录下面就包含了运 行firefox所需要的所有文件、库、数据等等。要删除firefox的时候，你只需删除/opt/firefox_beta

/etc 习惯上存放配置文件的目录，.d 的意思是目录，里面包含了配置文件，前面的名字你可以自己起，这是 linux 的惯例。
```



```
ctrl + c 杀死结束程序
ctrl + z 程序后台运行
bg 查看当前终端后台运行的程序
fg 把当前终端后台后台运行的拿到前台运行
```

##### ssh不输入密码

```
在目标机器的 〜/.ssh/authorized_keys 中添加自己的ssh公钥
```






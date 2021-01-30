##### xxx.app已损坏,打不开.你应该将它移到废纸篓

```
sudo spctl --master-disable

10.15系统 新版本中可能失效使用下面方法
sudo xattr -rd com.apple.quarantine 空格 软件的路径
例如
sudo xattr -rd com.apple.quarantine /Applications/App\ UninstalIer.app
```

##### 加载ntfs

```
sudo vim /etc/fstab
LABEL=xxxxxx none ntfs rw,auto,nobrowse

Command+Shift+G
/Volumes

方式 2
先查看挂载信息
sudo mount
卸载
$ sudo umount /Volumes/新加卷
挂载
sudo mount -t ntfs -o rw,auto,nobrowse /dev/disk2s1 /data/mydisk/
```

##### Mac 发热

```
禁用spotlight服务
sudo mdutil -a -i off 
启动spotlight服务
sudo mdutil -a -i on
```

##### Pycharm卡发热

```
搜索Windows Options > 选中show memmory indicator > OK

help > Find Action > 输入VM Options > 打开 Edit Custom VM Options > 编辑pycharm.vmoptions文件
将   -Xmx750m   改为   -Xmx1024m
```

##### Pycharm破解

```
http://idea.lanyus.com/
hosts文件路径：sudo vim /etc/hosts
将0.0.0.0 account.jetbrains.com添加到hosts文件中

激活前清除hosts中屏蔽的网址, 激活后请加“0.0.0.0 account.jetbrains.com”及“0.0.0.0 www.jetbrains.com”到hosts中屏蔽联网
```

##### 自己写的模块导入时红色波浪线

```
file->settings->project->project structure->点击项目路径->点击Excluded
```

##### 终端vi

```
ctrl + c 杀死结束程序
ctrl + z 程序后台运行
bg 查看当前终端后台运行的程序
fg 把当前终端后台后台运行的拿到前台运行
```

##### 开盖自动开机

```
sudo nvram AutoBoot=%00
```

##### brew切换国内源

```
# 替换brew.git: 
cd "$(brew --repo)" 
git remote set-url origin https://mirrors.ustc.edu.cn/brew.git 

# 替换homebrew-core.git: 
cd "$(brew --repo)/Library/Taps/homebrew/homebrew-core" 
git remote set-url origin https://mirrors.ustc.edu.cn/homebrew-core.git

brew update
```

##### docker

```
brew cask install docker
```

##### frp内网穿透

```
github下载地址
https://github.com/fatedier/frp/releases
服务器和客户端版本要一致


# linux 版本
wget https://github.com/fatedier/frp/releases/download/v0.27.0/frp_0.27.0_linux_amd64.tar.gz
# mac版本
wget https://github.com/fatedier/frp/releases/download/v0.27.0/frp_0.27.0_darwin_amd64.tar.gz
tar -zxvf  frp_0.13.0_linux_amd64.tar.gz

$ vi ./frps.ini
[common]
bind_port = 7000           #与客户端绑定的进行通信的端口
vhost_http_port = 6081     #访问客户端web服务自定义的端口号



$ vi ./frpc.ini
[common]
server_addr = 120.56.37.48   #公网服务器ip
server_port = 7000            #与服务端bind_port一致
 
# 公网通过ssh访问内部服务器
[ssh]
type = tcp              #连接协议
local_ip = 192.168.3.48 #内网服务器ip
local_port = 22         #ssh默认端口号
remote_port = 6000      #自定义的访问内部ssh端口号
 
# 公网访问内部web服务器以http方式
[web]
type = http         #访问协议
local_port = 8081   #内网web服务的端口号
custom_domains = repo.iwi.com   #所绑定的公网服务器域名，一级、二级域名都可以


# 启动
./frps -c ./frps.ini
./frpc -c ./frpc.ini
```

##### xshell文件上传到centos

```
yum install  lrzsz
#上传命令
rz    
# 覆盖上传
rz -y  
# 下载
sz {文件名} 
```

##### Chrome退出前提示

```
chrome -> 退出前提示
```



```
Command+Shift+G
```

##### curl: (7) Failed to connect to raw.githubusercontent.com port 443: Connectio问题

```
网站 https://www.ipaddress.com/ 的查看域名的ip raw.githubusercontent.com
添加进hosts
```






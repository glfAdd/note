##### mac 目录结构

```
* /bin 传统unix命令的存放目录，如ls，rm，mv等。
* /sbin 传统unix管理类命令存放目录，如fdisk，ifconfig等等。
* /usr 第三方程序安装目录。
* /usr/bin, /usr/sbin, /usr/lib，其中/usr/lib目录中存放了共享库（动态链接库）。
* /etc. 标准unix系统配置文件存放目录，如用户密码文件/etc/passwd。此目录实际为指向/private/etc的链接。
* /dev 设备文件存放目录，如何代表硬盘的/dev/disk0。
* /tmp 临时文件存放目录，其权限为所有人任意读写。此目录实际为指向/private/tmp的链接。
* /var 存放经常变化的文件，如日志文件。此目录实际为指向/private/var的链接。
* /Applications 应用程序目录，默认所有的GUI应用程序都安装在这里；
* /Library 系统的数据文件、帮助文件、文档等等；
* /Network 网络节点存放目录；
* /System 他只包含一个名为Library的目录，这个子目录中存放了系统的绝大部分组件，如各种framework，以及内核模块，字体文件等等。
* /Users 存放用户的个人资料和配置。每个用户有自己的单独目录。
* /Volumes 文件系统挂载点存放目录。
* /cores 内核转储文件存放目录。当一个进程崩溃时，如果系统允许则会产生转储文件。
* /private 里面的子目录存放了/tmp, /var, /etc等链接目录的目标目录。
* /installer.failurerequests 可能是用来记录发生crash时的日志


源代码手动安装的问题件在此目录下: /usr/local/software/
```

# etc

##### 修改 hostname

```
sudo scutil --set HostName XXX
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

##### mac 发热

```
禁用spotlight服务
sudo mdutil -a -i off 

启动spotlight服务
sudo mdutil -a -i on
```

##### 自己写的模块导入时红色波浪线

```
file->settings->project->project structure->点击项目路径->点击Excluded
```

##### 前后台

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

##### docker

```
brew cask install docker
```

##### xshell文件上传到centos

```
yum install lrzsz
#上传命令
rz    
# 覆盖上传
rz -y  
# 下载
sz {文件名} 
```

##### Chrome退出前提示

```
chrome -> 在使用 ⌘Q 退出前，先显示警告
```



```
Command+Shift+G
```

##### mac 制作 linux 驱动优盘

```
1. 格式化 U盘
选在 GUID分区

2. 取消 U盘挂载
方式(1): 
点卸载按钮

方式(2):
# 列出磁盘，找到你usb硬盘的盘符
diskutil list
# 取消usb硬盘的挂载
diskutil unmountDisk /dev/disk5

3. 写入磁盘
sudo dd if=/Users/glfadd/Downloads/ubuntu-20.04.2.0-desktop-amd64.iso of=/dev/disk5 bs=2m

4. 等待一段时间, 有格式化提示表示完成
```

##### Google Authenticator 二次验证登录

```bash
# 下载 sshpass.rb 文件
$ wget https://raw.githubusercontent.com/kadwanev/bigboybrew/master/Library/Formula/sshpass.rb
# 用 sshpass.rb 文件安装 sshpass
$ brew install sshpass.rb



```



# development

##### 安装 xcode 工具

```bash
$ xcode-select --install
```



# mac 2023.05.11

##### brew

```bash
# github 下载速速慢, 使用加速源安装
# 选择第 3 个，速度快
/bin/zsh -c "$(curl -fsSL https://gitee.com/cunkai/HomebrewCN/raw/master/Homebrew.sh)"
```

##### 国内源

```bash

# 查看 brew.git 当前源
$ cd "$(brew --repo)" && git remote -v
origin    https://github.com/Homebrew/brew.git (fetch)
origin    https://github.com/Homebrew/brew.git (push)
 
# 查看 homebrew-core.git 当前源
$ cd "$(brew --repo homebrew/core)" && git remote -v
origin    https://github.com/Homebrew/homebrew-core.git (fetch)
origin    https://github.com/Homebrew/homebrew-core.git (push)
 
# 修改 brew.git 为阿里源
$ git -C "$(brew --repo)" remote set-url origin https://mirrors.aliyun.com/homebrew/brew.git
 
# 修改 homebrew-core.git 为阿里源
$ git -C "$(brew --repo homebrew/core)" remote set-url origin https://mirrors.aliyun.com/homebrew/homebrew-core.git
 
# zsh 替换 brew bintray 镜像
$ echo 'export HOMEBREW_BOTTLE_DOMAIN=https://mirrors.aliyun.com/homebrew/homebrew-bottles' >> ~/.zshrc
$ source ~/.zshrc
 
# bash 替换 brew bintray 镜像
$ echo 'export HOMEBREW_BOTTLE_DOMAIN=https://mirrors.aliyun.com/homebrew/homebrew-bottles' >> ~/.bash_profile
$ source ~/.bash_profile
 
# 刷新源
$ brew update

```



##### 升级系统 python

```bash
$ brew reinstall python


brew install cmake ; brew install libevent ; brew install mandoc ; brew install libcbor ; brew install libfido2 ; brew install zlib ; brew install lz4 ; brew install zstd
```

##### 常用软件

```bash
brew install wget
```

##### xxx.app 文件损坏,打不开.你应该将它移到废纸篓

```bash
sudo xattr -r -d com.apple.quarantine /Applications/gridsutra.app
```

##### oh my zsh

```bash
# 使用加速源
sh -c "$(curl -fsSL https://gitee.com/mirrors/oh-my-zsh/raw/master/tools/install.sh)"
```

#####

```
添加 -> 选择 "remote" -> github 地址 https://raw.hellogithub.com/hosts
```




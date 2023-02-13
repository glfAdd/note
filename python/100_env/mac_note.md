# etc

##### 修改 hostname

```
sudo scutil --set HostName XXX
```

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

# development

##### 安装 xcode 工具

```bash
$ xcode-select --install
```

##### 升级系统python

```bash
$ brew reinstall python
```






[TOC]

##### 常用命令

```
apt-get install ./teamviewer_amd64.deb
查找软件包
apt-cache search 软件包名
显示软件包的详细信息
apt-cache show 软件包名

aptitude update		更新可用的包列表	
aptitude safe-upgrade		执行一次安全的升级	
aptitude full-upgrade		将系统升级到新的发行版	
aptitude install pkgname	安装包	
aptitude remove pkgname	删除包	
aptitude purge pkgname		删除包及其配置文件	
aptitude search string		搜索包	
aptitude show pkgname		显示包的详细信息	
aptitude clean			删除下载的包文件	
aptitude autoclean		仅删除过期的包文件

修复安装损坏的包
sudo apt update --fix-missing
sudo apt-get -f install 

强制 apt 查找并更正缺少的依赖项或损坏的包
sudo apt install -f

sudo apt clean
sudo apt update

卸载软件
1. 查看安装的软件
dpkg -l |grep virtualbox
aptitude remove --purge-unused youdao-dict

2. 卸载
apt remove --purge virtualbox
sudo dpkg -i sogoupinyin_版本号_amd64.deb

```

##### U盘安装过程中卡死

```
(ubuntu 20.04.2 LTS 已经修复了这个问题)
1. install ubuntu的页面按“e”， 
2. 将quiet splash 改为, quiet spl
3. F10 保存
4. 再进行安装
```

##### 在安装完ubuntu双系统后，第一次启动ubuntu系统时，卡死在启动界面（或者黑屏）

```
(ubuntu 20.04.2 LTS 已经修复了这个问题)
1.（如果已经卡死了，则强制关机）开机；
2.（在选择系统的界面）选择ubuntu高级选项，回车；
3.（在出现的两个模式中）选择恢复（recovery）模式，回车；
4.（在出现的众多选项中）选择grub，回车（你能看到貌似很牛逼的一行行代码跑过）；
5.（上面的代码跑完之后应该能重新回到众多选项的界面）选择resume，回车进入系统。

永久修改
1.修改/etc/default/grub文件
在打开的文件中，将其中的quiet splash修改为quiet splash nomodeset并保存;
2.更新修改完的grub：
sudo update-grub

```

##### ssh

```
如果无法登录需要重现安装
apt-get reinstall ssh
service sshd status

0. 生成ssh key
ssh-keygen -t rsa -C xxxxxx@qq.com


1. ssh不输入密码
在目标机器的 〜/.ssh/authorized_keys 中添加自己的ssh公钥
如果仍然无法登录需要修改该文件权限
chmod 644 ~/.ssh/authorized_keys
chmod 700 ~/.ssh


2. 编辑 ~/.ssh/config 文件
Host elk
    HostName xxxxxxxx
    User xxxxxx
    Port xxxxxxxx
    IdentitiesOnly yes
    IdentityFile ~/.ssh/id_rsa_test	
   
问题: Bad owner or permissions on /home/xxx/.ssh/config
解决办法: chmod 600 ~/.ssh/config
```

##### 20.04换阿里源

```
cp -ra /etc/apt/sources.list /etc/apt/sources.list.bak
vim /etc/apt/sources.list

deb http://mirrors.aliyun.com/ubuntu/ focal main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ focal-security main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal-security main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ focal-updates main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal-updates main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ focal-proposed main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal-proposed main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ focal-backports main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal-backports main restricted universe multiverse
```

##### 脚本升级最新内核

```
查看已经安装的内核
dpkg --get-selections | grep linux

1. wget https://raw.githubusercontent.com/pimlie/ubuntu-mainline-kernel.sh/master/ubuntu-mainline-kernel.sh

2. 添加执行权限

3. 查看最新的内核
./ubuntu-mainline-kernel.sh -c

4. 安装最新版本(太新不用)
./ubuntu-mainline-kernel.sh -i
安装指定版本
./ubuntu-mainline-kernel.sh  -i v5.11.17

5. 重启

6. 卸载最新内核
ubuntu-mainline-kernel.sh -u

以下是升级日志
root@lg:/home/glfadd/Downloads# ./ubuntu-mainline-kernel.sh -i
Finding latest version available on kernel.ubuntu.com
Latest version is: v5.11.15, continue? (y/N)
Will download 6 files from kernel.ubuntu.com:
Downloading amd64/linux-headers-5.11.15-051115-generic_5.11.15-051115.202104161034_amd64.deb: 100%
Downloading amd64/linux-headers-5.11.15-051115_5.11.15-051115.202104161034_all.deb: 100%
Downloading amd64/linux-image-unsigned-5.11.15-051115-generic_5.11.15-051115.202104161034_amd64.deb: 100%
Downloading amd64/linux-modules-5.11.15-051115-generic_5.11.15-051115.202104161034_amd64.deb: 100%
Downloading amd64/CHECKSUMS: 100%
Downloading amd64/CHECKSUMS.gpg: 100%
Importing kernel-ppa gpg key ok
Signature of checksum file has been successfully verified
Checksums of deb files have been successfully verified with sha256sum
Installing 4 packages
Cleaning up work folder

7. 设置默认的内核
  选择"Advanced options for Ubuntu" 的 第三个内核
GRUB_DEFAULT="1>6" 

8. 手动卸载其他内核
apt-get remove linux-image-5.8.0-43-generic (这种方式无法卸载干净)
dpkg -P linux-image-5.8.0-43-generic (卸载干净)
```

#####  nvidia(升级内核后这种方式安装失败)

```
1. 查看显卡型号
ubuntu-drivers devices

2. 禁用 nouveau
/etc/modprobe.d/blacklist.conf 末尾添加 blacklist nouveau

3. 更新重启
update-initramfs -u
reboot

4. 查看驱动是否禁用
lsmod | grep nouvea

5. 使用系统的  Additional Driver 安装驱动, 选择 tested 的这个

6. 删除 /etc/X11/xorg.conf 文件

7. 重启

8. 查看显卡状态
nvidia-smi
```

##### nvidia(安装后无法使用)

```
添加源
$ add-apt-repository ppa:graphics-drivers/ppa

查询当前适用版本
$ ubuntu-drivers devices

安装
$ ubuntu-drivers autoinstall

nvidia-smi 
nvidia-xconfig
nvidia-settings
nvidia-xconfig -a --cool-bits=31 --allow-empty-initial-configuration
```

##### 安装字体

```
gnome 中输入"input" -> 选择 "Language Support" -> 安装字体
```

#####  windows字体添加到ubuntu系统中

```
***** 可以解决 wine 安装应用以后输入框和其他一些地方显示是方块的问题

0. 安装需要的命令
aptitude install ttf-mscorefonts-installer
aptitude install fontconfig

1. 在 /usr/share/fonts 下创建 cp_windows_fonts 文件夹

2. 将 windows 的字体文件拷贝到这个目录下 (windows 字体文件在 windows/founts)

3. 修改该 cp_windows_fonts 权限
chmod -R cp_windows_fonts 755

4. 生成核心字体信息
mkfontscale  
mkfontdir

5. 刷新系统字体缓存
fc-cache -fv
```

##### 系统优化

```
1. 减少 swap 使用(效果不好, 直接关闭)
# 查看系统默认比例
cat /proc/sys/vm/swappiness 

# 系统默认是60，我们改成10
sudo vim /etc/sysctl.conf 
修改 vm.swappiness=10 ,如果没有就添加

1. 永久关闭 swap
内存不够是会缓存到 swap 中, 高负载时会降低系统性能
    (1) 查看内存情况
    free -h

    (2) 修改 /etc/fstab 文件, 注释掉最后一行的swap

    (3) 查看是否启动了 swap, 如果没有输出则没有开启
    swapon --show
    NAME           TYPE      SIZE USED PRIO
    /dev/nvme0n1p2 partition 954M   0B   -2

    (4) 关闭 swap
    swapoff -v /dev/nvme0n1p2

    (5) 删除 swap 文件：
    sudo rm /dev/nvme0n1p2

    (6)查看, total 为 0 表示已经关闭

2. 减少Grub时间
# 修改 /etc/default/grub 的两个选项, 如果没有则添加 
GRUB_TIMEOUT=10 (关机等待的时间)
GRUB_RECORDFAIL_TIMEOUT=2 (开机选择的时间)
GRUB_TIMEOUT_STYLE=hidden (隐藏grub)

# 更新
sudo update-grub2
sudo update-grub


3. 查看启动占用时间
systemd-analyze blame
  
4. 关闭没用的服务
# 
sudo systemctl disable apt-daily-upgrade.service
sudo systemctl disable apt-daily.service

# 
sudo systemctl disable NetworkManager-wait-online.service 
```

##### 安装字体

```
1. github 下载工具
https://github.com/cstrap/monaco-font

2. 根须系统选择对应的脚本, 通过url制定字体的文件
./install-font-ubuntu.sh 
sudo ./install-font-ubuntu.sh https://github.com/todylu/monaco.ttf/blob/master/monaco.ttf?raw=true

3. 打开tweak工具，在font栏进行调整

apt-get install aptitude
```

##### 常用软件

```
aptitude install terminator htop vim zsh git smplayer tree curl screenfetch net-tools

百度网盘, 网易音乐
```

##### firefox 开机会自动启动

```
1. 清空 ~/.cache/sessions 文件夹
2. 将 ~/.cache/sessions 权限设为 000
```

##### git客户端

```
aptitude install git-cola
```

##### google chrome

```
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
```

##### sublime text

```
# Install the GPG key:
wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -

# Ensure apt is set up to work with https sources:
sudo apt-get install apt-transport-https

# 安装稳定版本 source
echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list

# 安装
sudo apt-get update
sudo apt-get install sublime-text
```

##### docker ce

```
aptitude install apt-transport-https ca-certificates curl gnupg-agent software-properties-common
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
apt-get update
aptitude install docker-ce docker-ce-cli containerd.io


国内源
# vim /etc/docker/daemon.json
{
  "registry-mirrors": ["https://docker.mirrors.ustc.edu.cn/"]
}


systemctl status docker
service docker start
service docker restart
```


##### redis-desktop-manager

```
网址: https://snapcraft.io/redis-desktop-manager
sudo snap install redis-desktop-manager
```

##### linux ssh 客户端

```
wget www.hostbuf.com/downloads/finalshell_install_linux.sh
chmod +x finalshell_install_linux.sh
./finalshell_install_linux.sh
```

##### gnome 桌面创建快捷方式

```
在 /usr/share/applications目录下创建 aaa.desktop 文件

[Desktop Entry]
Name=pycharm
Exec=/home/glfadd/application/pycharm/bin/pycharm.sh
Type=Application
Icon=/home/glfadd/application/pycharm/bin/pycharm.png
Categories=Utility;TextEditor;
StartupNotify=false
Terminal=false
```

##### gnome Ubuntu系统配置Unity桌面工具(美化效果用)

```
 (刚装的试试效果)
aptitude install unity-tweak-tool
aptitude install unity-lens-applications 
aptitude install unity-lens-files

启动命令
unity-tweak-tool
```

##### gnome 桌面美化工具

```
apt-get install gnome-tweak-tool 
apt-get install chrome-gnome-shell

浏览安装插件
  # 把主题放置在user/share/themes
  User Themes
  # 应用窗口的菜单项放置在了桌面顶部栏中
  Gnome Global Application Menu
  # 任务栏
  dash-to-panel
  # 屏幕截图工具
  Screenshot Tool 
  # 在顶栏显示应用图标
  TopIcons Plus
  # 在顶栏显示移动盘图标
  Removable Drive Menu
  # 最近查看过的文件
  Recent Items
  # 顶栏显示应用图标，输入法切换的时候特别有用
  TopIcons Plus 
  # 顶栏显示网速
  Netspeed
  # 在顶栏显示当前工作区号
  WorkSpace indicator
  # 剪切版
  Clipboard Indicator
```

##### gcc安装

```
1. 安装多个gcc
sudo apt install gcc-8 g++-8 gcc-9 g++-9 gcc-10 g++-10

2. 为每个版本配置替代版本，并将优先级与之关联，默认版本是优先级最高的版本，在本例中为gcc-10
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-10 100 --slave /usr/bin/g++ g++ /usr/bin/g++-10 --slave /usr/bin/gcov gcov /usr/bin/gcov-10
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-9 90 --slave /usr/bin/g++ g++ /usr/bin/g++-9 --slave /usr/bin/gcov gcov /usr/bin/gcov-9
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-8 80 --slave /usr/bin/g++ g++ /usr/bin/g++-8 --slave /usr/bin/gcov gcov /usr/bin/gcov-8

3. 通过命令切换
sudo update-alternatives --config gcc
```

##### VMware Workstation Pro 16

```
VMware Workstation Pro v16
wget https://download3.vmware.com/software/wkst/file/VMware-Workstation-Full-16.1.1-17801498.x86_64.bundle

ZF3R0-FHED2-M80TY-8QYGC-NPKYF (可用)
YF390-0HF8P-M81RQ-2DXQE-M2UT6
ZF71R-DMX85-08DQY-8YMNC-PPHV8 
```

##### wine

```
教程
https://zhuanlan.zhihu.com/p/76331687


0. 安装需要的依赖
sudo apt-get install cabextract p7zip-full
 

1. 如果是 64 位系统，开启 32 bit 架构支持（如果您之前没有开启的话）：
sudo dpkg --add-architecture i386 


2. 下载添加仓库密钥
wget -nc https://dl.winehq.org/wine-builds/winehq.key
sudo apt-key add winehq.key


3. 添加源
sudo add-apt-repository 'deb https://dl.winehq.org/wine-builds/ubuntu/ focal main'
sudo apt-get update


4. 安装稳定版本
sudo aptitude install winehq-stable


5. 安装最新版的winetricks
sudo apt-get remove winetricks
wget  https://raw.githubusercontent.com/Winetricks/winetricks/master/src/winetricks
chmod +x winetricks
sudo mv -v winetricks /usr/local/bin


6. 安装微信.
(1)初始化wine bottle config 
  # WINARCH=win32是将架构配置为32位以便提供更好的兼容性
  # WINEPREFIX设置了相应bottle所在的目录, 给每个程序创建独立的运行环境, 类似anaconda. 
WINARCH=win32 WINEPREFIX=/home/glfadd/application/wine/wechat winecfg

(2)通过winetricks添加依赖项目
WINARCH=win32 WINEPREFIX=/home/glfadd/application/wine/wechat winetricks
选择默认的Wine容器 -> OK -> 安装Windows DLL组件 -> OK -> 勾选riched20.dll 和 riched32.dll -> OK -> 等待安装即可。


(3)安装微信
WINARCH=win32 WINEPREFIX=/home/glfadd/application/wine/wechat wine WeChatSetup.exe


(4)设置桌面快捷方式
将 Exec改为下面这样, 否则报错
Exec=env WINEPREFIX="/home/glfadd/application/wine/wechat" /usr/bin/wine explorer /desktop=wechat, 1920x1080 "/home/glfadd/application/wine/wechat/drive_c/Program Files (x86)/Tencent/WeChat/WeChat.exe"
  说明
  /usr/bin/wine: wine执行程序所在目录
  explorer: 启动窗口
  /desktop=wechat: 窗口名称
  , 1920x1080: 窗口分辨率
  "/home/frank/Wine/WeChat/drive_c/Program Files/Tencent/WeChat/WeChat.exe": 微信执行程序所在的绝对路径

(5)运行
./WeChat.desktop

(6)将启动快捷方式复制到 /usr/share/applications 文件夹内


7. 安装问题解决办法

(1)页面中文是方块, 无法正正常显示
  # 查看系统有没有 zh_CN.utf-8
  locale -a

  # 修改该WeChat.desktop, 第二行中wine前面加入LC_ALL=zh_CN.utf8
  Exec=env WINEPREFIX="/home/glfadd/application/wine/wechat" LC_ALL=zh_CN.utf8 /usr/bin/wine explorer /desktop=wechat, 1920x1080 "/home/glfadd/application/wine/wechat/drive_c/Program Files (x86)/Tencent/WeChat/WeChat.exe"

(2)ibus不能输入中文
https://forum.ubuntu.org.cn/viewtopic.php?t=488436

(3)ibus输入中文是方块, 有些地方显示方块
将windows系统中的字体都拷贝到ubuntu中

(4)窗口阴影(解决中)
商店安装 CompizConfig 插件 



(5)每次启动微信，会发现左上角有一个小窗口。如果把这个小窗口关闭了，就会导致直接关闭微信
这个小窗口实际上是任务栏图标，可以通过以下操作把这个图标显示在ubuntu的顶部状态栏内
商店安装 Topicons Plus 插件

(6)有个别软件打开时会提示缺少Adobe Flash Player插件 (没验证)
安装 msi 格式的 Adobe Flash Player
wine start ~/下载/xxx.msi 





8. 最终的文件是这样的
[Desktop Entry]
Name=WeChat
Exec=env LC_ALL=zh_CN.utf8 GTK_IM_MODILE=ibus QT_IM_MODULE=ibus XMODIFIERS="@im=ibus" WINEPREFIX="/home/glfadd/application/wine/wechat"  /usr/bin/wine  "/home/glfadd/application/wine/wechat/drive_c/Program Files (x86)/Tencent/WeChat/WeChat.exe"
Type=Application
StartupNotify=true
Path=/home/glfadd/application/wine/wechat/dosdevices/c:/Program Files (x86)/Tencent/WeChat
Icon=06F2_WeChat.0
StartupWMClass=wechat.exe
```

##### 安装字体

```
(这个用来这是系统的字体样式)

查看中文字体
fc-list :lang=zh-cn

安装中文字体
sudo apt-get install -y --force-yes --no-install-recommends fonts-wqy-microhei
sudo apt-get install -y --force-yes --no-install-recommends ttf-wqy-zenhei

#生成核心字体信息
mkfontscale  

mkfontdir

刷新系统字体缓存
fc-cache -fv
```

##### 搜狗输入法

```
1. 官网下载 deb

2.
aptitude install fcitx

3. 安装搜狗输入法
sudo dpkg -i sogoupinyin_版本号_amd64.deb

4. 修复安装的依赖
apt -f install
```

##### typora

```
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys BA300B7755AFCFAE
add-apt-repository 'deb https://typora.io/linux ./'
apt-get update
apt-get install typora

aptitude install purge
```

##### xfce 快捷方式

```
文件后缀名 .desktop
保存在目录下 /home/glfadd/.local/share/applications/
使用 settings manager -> menu editor -> 管理
使用 New Launcher 添加
```

##### 将系统设为中文

```
1. 创建或编辑 ~/.xprofile 文件， 并添加
export LC_ALL=zh_CN.UTF-8
 
2. 注销并重新登录
```

##### 词典 Golden Dict

```
aptitude install goldendict

1. 添加在线词典:
海词 http://dict.cn/%GDWORD%
汉典 http://www.zdic.net/sousuo/?q=%GDWORD%
bing http://cn.bing.com/dict/search?q=%GDWORD%
有道词典 http://dict.youdao.com/search?q=%GDWORD%&ue=utf8


2. 添加维基百科
中文百科 https://zh.wikipedia.org/w (失败)
中文词典 https://zh.wiktionary.org/w
English Wikipedia https://en.wikipedia.org/w (失败)
English Wiktionary https://en.wiktionary.org/w


2. 语言设为中文(失败)
Edit -> Preferences -> Interface Language 
重启电脑生效


3. 搜索后没有出结果
将维基百科关闭
将 "Link" 勾选去掉

4. 词典阅读发声(失败)
aptitude install mplayer
设为 mplayer


5. 添加离线词典
```

##### 开机弹匡错误

```
编辑  /etc/default/apport 
我们把enabled=1改为enabled=0
```

##### xfce4 窗口快捷键

```
windows manager 中设置快捷键

/usr/bin/xfce4-popup-whiskermenu 的快捷键不能设置为 super, 否则会和系统的快捷键冲突
```

##### filemanager 快捷键

```
c + M 显示/隐藏菜单栏
c + E 显示/隐藏左边栏(边栏树状)
c + B 显示/隐藏左边栏(边栏非树状)
c + H 显示/隐藏隐藏文件夹
c + L 地址栏输入路径
```

##### 系统死机, 按什么都没反映

```
伸出你的左手，同时按住<Ctrl>+<Alt>键，别松开
右手先按一下<SysRq> 和截屏在一个一个按键上，左手别松开，等1秒
右手按一下 R，左手别松开，等1秒
右手按一下 E，左手别松开。这时包括桌面在内，所有程序都会终止，你会看到一个黑乎乎的屏幕，稍微等一段时间
右手依次按下 I，S，U，B，左手别松开。每按一次都等那么几秒种，你会发现每按一次，屏幕上信息都会有所变化。
最后按下B时，屏幕显示reset，这时你的左手可以松开了，等几秒钟，计算机就会安全重启。

  r : unRaw 将键盘控制从 X Server 那里抢回来
  e : tErminate 给所有进程发送 SIGTERM 信号，让它们自己解决善后
  i : kIll 给所有进程发送 SIGKILL 信号，强制他们马上关闭
  s : Sync 将所有数据同步至磁盘
  u : Unmount 将所有分区挂载为只读模式
  b : reBoot 重启
```






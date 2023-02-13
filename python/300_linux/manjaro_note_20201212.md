##### 安装时驱动选择 “notfree”

##### 源

```
1. sudo vi /etc/pacman.conf
在文件最后添加如下内容：
[archlinuxcn]
SigLevel = Never
Server = http://mirrors.163.com/archlinux-cn/$arch

2. 生成可用中国镜像站列表：
sudo pacman-mirrors -i -c China -m rank
勾选 http://mirrors.aliyun.com/manjaro/，然后按OK键两次。
最后刷新缓存：

sudo pacman -S archlinux-keyring
sudo pacman -Syy
sudo pacman -Syu
```

##### yay

```
安装yay
sudo pacman -S yay


使用选项-S使用yay从AUR安装软件包：
$ yay -S package

要删除包，请使用-Rns选项：
$ yay -Rns package
```

##### system

```
yay -S core/binutils  
# 打包基本工具
yay -S base-devel

yay -S cmake
```

##### nvidia

```
0. 查看电脑硬件信息
inxi -Fx

0. 查看显示器分辨率信息
xrandr

0. 卸载bumblebee

1. 查看nouveau是否启动运, 没有返回代表没有运行。
lsmod | grep nouveau

2. 查看集成显卡
lspci | grep VGA

3. 查看NVIDIA显卡
lspci | grep NVIDIA

4. 查看自己的显卡驱动信息
inxi -G

5. 查找深度提供的包    
yay -Ss nvidia-prime
此命令的输出如下
aur/deepin-nvidia-prime-git 0.0.0.r1.0e1e70e-1 (+0 0.00) (Installed)
    nvidia prime for deepin
aur/arch-prime-git 0.9.4.r2.ge754390-1 (+2 0.00) (Orphaned) (Out-of-date: 2020-09-25) 
    Provide nvidia-prime like package for Archlinux
community/nemo-run-with-nvidia-prime-run 0.1.0-1 (5.7 KiB 618.0 B) 
    Nemo action to run a program with prime-run
extra/nvidia-prime 1.0-4 (2.8 KiB 112.0 B) (Installed)
    NVIDIA Prime Render Offload configuration and utilities

6. 在输出结果里面选择然后安装
yay -S deepin-nvidia-prime-git

7. 再次运行 yay -Ss nvidia-prime， 如果显示 Installed 表示安装成功

8. 查看GPU当前的状态
nvidia-smi

9. #### 安装完成之后在系统的显示设置里面把外接显示器设置为“已启用”

10. 重启
11. 执行 nvidia-xconfig
12. 重启
13. 删除 /etc/X11/xorg.conf
14. 重启
```

##### 输入法

```
yay -S fcitx
yay -S fcitx-im fcitx-configtool
yay -S fcitx-sogoupinyin
yay -S fcitx-googlepinyin

# 这个配置会讲系统语言设为中文
新建并配置~/.xprofile
export LC_ALL=zh_CN.UTF-8
export GTK_IM_MODULE=fcitx
export QT_IM_MODULE=fcitx
export XMODIFIERS="@im=fcitx"
```

##### 开关机速度

```
1. 关机
减少默认停止超时, 编辑 /etc/systemd/system.conf
DefaultTimeoutStopSec=5s


2. 开机
编辑 /etc/default/grub
    将 GRUB_TIMEOUT=10 改为 GRUB_TIMEOUT=1

3.更新修改完的grub
sudo update-grub



[FAILED] Failed to start Load/Save mess of backlight:acpi_video0. 
[FAILED] Failed to start Load/Save Screen Backlight Brightness of backlight:amdgpu_bl0.

```

##### 触控板

```
yay -S kcm-pointing-devices-git

```

##### 常用软件

```
yay -S netease-cloud-music google-chrome okular typora htop screenfetch smplayer vim docker postman

```

##### 安装中的问题错误解决办法

```
[gladd@G ~]$ sudo pacman -S fcitx-sogoupinyin
resolving dependencies...
looking for conflicting packages...

Packages (4) lsb-release-1.4-14  opencc-1.0.5-1  qtwebkit-2.3.4-6
             fcitx-sogoupinyin-2.2.0.0102-1

Total Download Size:   30.32 MiB
Total Installed Size:  96.26 MiB

:: Proceed with installation? [Y/n] y
:: Retrieving packages...
 qtwebkit-2.3.4-6-x86_64    8.5 MiB  9.53M/s 00:01 [######################] 100%
 fcitx-sogoupinyin-2...    21.8 MiB  11.1M/s 00:02 [######################] 100%
(4/4) checking keys in keyring                     [######################] 100%
(4/4) checking package integrity                   [######################] 100%
error: qtwebkit: signature from "lilac (build machine) <lilac@build.archlinuxcn.org>" is unknown trust
:: File /var/cache/pacman/pkg/qtwebkit-2.3.4-6-x86_64.pkg.tar.xz is corrupted (invalid or corrupted package (PGP signature)).
Do you want to delete it? [Y/n] y
error: fcitx-sogoupinyin: signature from "lilac (build machine) <lilac@build.archlinuxcn.org>" is unknown trust
:: File /var/cache/pacman/pkg/fcitx-sogoupinyin-2.2.0.0102-1-x86_64.pkg.tar.xz is corrupted (invalid or corrupted package (PGP signature)).
Do you want to delete it? [Y/n] y
error: failed to commit transaction (invalid or corrupted package (PGP signature))
Errors occurred, no packages were upgraded.

×××××××××解决办法×××××××××
修改/etc/pacman.conf，将原有的SigLevel=××××××注释掉，添加SigLevel = Never即可。
所有的SigLevel都要修改

```

##### VirtualBox

```
# 1. 查看当前系统的内核版本
uname -r 

# 2. 选择与当前内核相同的安装包
sudo pacman -S virtualbox

# 3. 安装VirtualBox扩展包
sudo pacman -Ss virtualbox-ext-oracle 

# 4. 重新启动系统或执行以下命令自动载入vboxdrv模块，不然打开虚拟机可能会提示'modprobe vboxdrv'错误。
sudo modprobe vboxdrv

```

##### sublime-text

```
curl -O https://download.sublimetext.com/sublimehq-pub.gpg && sudo pacman-key --add sublimehq-pub.gpg && sudo pacman-key --lsign-key 8A8F901A && rm sublimehq-pub.gpg
 
echo -e "\n[sublime-text]\nServer = https://download.sublimetext.com/arch/stable/x86_64" | sudo tee -a /etc/pacman.conf
 
sudo pacman -Syu sublime-text

```

##### 美化

```
https://www.cnblogs.com/zryabc/p/11408297.html

系统设置->图标->获取新的图标->搜索Mojave CT Icon安装
     

右键底栏->面板的选项，改变高度和把它放在屏幕上方->添加部件全局顶栏
安装dock栏 sudo yay -S latte-dock


窗口图标 MacBreeze Shadowless
```




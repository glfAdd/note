[TOC]

# system

##### 联想笔记本 bois 升级

```
官网下载地址
https://newsupport.lenovo.com.cn/driveList.html?fromsource=driveList&selname=%E6%8B%AF%E6%95%91%E8%80%85R7000%202020
```

##### 字体

> [字体下载地址]([Nerd Fonts - Iconic font aggregator, glyphs/icons collection, & fonts patcher](https://www.nerdfonts.com/))

```
DejaVuSansMono Nerd Font
Cousine Nerd Font
```

##### 包管理工具(弃用)

> 命令安装在: C:\Users\lg\scoop\apps

```bash
0. 管理员方式启动 powershell

1. 在 PowerShell 中输入下面内容，保证允许本地脚本的执行, 选择"全部"
set-executionpolicy remotesigned -scope currentuser

3
iwr https://chocolatey.org/install.ps1 -UseBasicParsing | iex

2. 执行下面的命令安装 Scoop：
iwr -useb get.scoop.sh | iex

3. 命令
scoop search firefox
    search 	搜索软件名
    update 	更新软件
    status 	查看软件状态
    uninstall 	卸载软件
    info 	查看软件详情
    home 	打开软件主页

scoop list                  显示已安装软件
scoop status                显示可更新的软件
scoop search <app>          查找软件
scoop info <app>            显示软件信息（含必要配置说明）
scoop cleanup *             清理所有旧版软件
scoop cleanup <app>         清理指定软件
scoop cleanup -k *  # 或 scoop cleanup --cache *     清理过期的安装包

# 更新scoop, 更新指定软件
scoop update
scoop update <app>
scoop update vscode-insiders -kf    # 更新 nightly 版本

4. scoop使用aria2进行多线程下载以加速下载：
scoop install aria2
aria2 配置文件路径: c：/user/xxx/.config/scoop/config.json
{
    "lastupdate":  "2020-06-16T23:58:19.3002510+08:00",
    "SCOOP_REPO":  "https://github.com/lukesampson/scoop",
    "SCOOP_BRANCH":  "master",
    "aria2-max-connection-per-server":  16,
    "aria2-split":  16,
    "aria2-min-split-size":  "2M"
}
配置命令
scoop config aria2-max-connection-per-server 16
scoop config aria2-split 16
scoop config aria2-min-split-size 1M

5. 添加仓库
scoop bucket add extras
# 第三方软件源bucket
scoop bucket add scoopbucket https://github.com/yuanying1199/scoopbucket
scoop bucket add versions

6. 常用软件
scoop install sudo
scoop install git 7zip openssh
scoop install aria2
scoop install ffmpeg
scoop install nodejs
scoop install python



***问题***
使用“1”个参数调用“DownloadString”时发生异常:“未能解析此远程名称: 'raw.githubusercontent.com'”
所在位置 行:1 字符: 1
+ iex (new-object net.webclient).downloadstring('https://get.scoop.sh')
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (:) [], MethodInvocationException
    + FullyQualifiedErrorId : WebException

***办法***
windows hosts 文件路径
    C:\Windows\System32\drivers\etc

在 hosts 文件里面添加
    151.101.76.133 raw.githubusercontent.com
```

##### 颜色管理工具

```
# 安装微软官方颜色工具
scoop install colortool

# 查看已安装主题
colortool -s

# 设置主题
colortool OneHalfDark
```

##### 安装字体

```
解决powershell乱码
https://github.com/powerline/fonts

进入目录以后执行
    .\install.ps1


符号字体官网
https://www.nerdfonts.com/

# 添加 nerd fonts 源
scoop bucket add 'nerd-fonts'
# 安装 nerd fonts
scoop install FantasqueSansMono-NF
sudo scoop install FantasqueSansMono-NF
```

#####  git 中文显示乱码

```
系统环境变量直接增加
LESSCHARSET=utf-8
```



##### mac type

```
字体美化
```

##### Windows Terminal

> C:\Users\xxx\AppData\Local\Packages\Microsoft.WindowsTerminalPreview_8wekyb3d8bbwe\LocalState\setting.json

- 下载 [MesloLGM NF字体]([跳转中... (zhihu.com)](https://link.zhihu.com/?target=https%3A//github.com/ryanoasis/nerd-fonts/releases/download/v2.1.0/Meslo.zip)). CTRL+A全选，右键点击安装

- 修改 setting.json 文件

  ```json
  {
      "profiles": {
          "defaults": {
              "font": {
                  "face": "MesloLGM NF"
              }
          }
      }
  }
  ```

- 快捷键

  ```
  SHIFT + ALT + ‘-’		水平分割
  SHIFT + ALT + ‘+’		垂直分割
  CTRL + SHIFT + ‘W’		关闭此时所处的窗口
  ```

##### oh my posh(弃用)

> [github](https://github.com/JanDeDobbeleer/oh-my-posh)
>
> [home page](https://ohmyposh.dev/)

- 管理启动 Powershell

- 安装 posh-git, oh-my-posh, PSReadLine

  > -Scope CurrentUser 限制仅当前用户可用

  ```bash
  > Install-Module posh-git -Scope CurrentUser
  > Install-Module oh-my-posh -Scope CurrentUser
  # PSReadLine 命令行增强补全工具
  > Install-Module PSReadLine -Scope CurrentUser
  
  # 查看主题的路径 (没有手动创建)
  > $env:POSH_THEMES_PATH
  # 查看主题
  > Get-PoshThemes
  # 下载主题 https://github.com/JanDeDobbeleer/oh-my-posh/tree/main/themes 复制到主题目录下
  
  
  winget install JanDeDobbeleer.OhMyPosh -s winget
  
  
  ```

- Windows Terminal 输入命令

  > $PROFILE 显示 WindowsPowerShell 配置文件路径

  ```bash
  # 1. 启动编辑power shell配置文件的引擎
  > if (!(Test-Path -Path $PROFILE )) { New-Item -Type File -Path $PROFILE -Force }
  
  # 2. 记事本打开配置文件
  > notepad $PROFILE
  ```

- 配置文件

  ```
  # 引入 posh-git
  Import-Module posh-git
  # 引入 oh-my-posh
  Import-Module oh-my-posh
  # 设置主题
  Set-PoshPrompt -Theme honukai
  
  # 引入 PSReadLine
  Import-Module PSReadLine
  Set-PSReadLineKeyHandler -Key UpArrow -Function HistorySearchBackward
  Set-PSReadLineKeyHandler -Key DownArrow -Function HistorySearchForward
  Set-PSReadLineKeyHandler -Key Tab -Function Complete
  ```

- 卸载

  ```bash
  # 移除缓存文件
  > Remove-Item $env:POSH_PATH -Force -Recurse
  # 卸载oh-my-posh
  > Uninstall-Module oh-my-posh -AllVersions
  ```


```
# 如果后面日期乱码, 使用命令
Set-Culture en-US

查看按键
> Get-PSReadLineKeyHandler
```

#####  删除win10预览版水印

```
Universal Watermark Disabler
```

##### Microsoft Stroe

```
quickLook              	空格浏览文件
EarTrumpet	系统和应用声音单独控制
Snipaste		截屏工具
TranslucentTB 汉化版 使任务栏透明
Fluent Terminal 终端
```

##### xshell 配色

.xcs 文件



# docker

> [docker hub](https://hub.docker.com/)

##### 国内源

```
docker desktop -> docker engine -> 添加

"registry-mirrors": ["https://docker.mirrors.ustc.edu.cn/"]
```

##### 下载地址

```
C:\Users\xxx\AppData\Local\Docker\wsl\data
```

# wsl

##### LxRunOffline

> [github](https://github.com/DDoSolitary/LxRunOffline)

```
下载
wget https://github.com/DDoSolitary/LxRunOffline/releases/download/v3.5.0/LxRunOffline-v3.5.0-msvc.zip

解压

环境变量 -> 系统变量 -> Path -> 添加"文件的目录"
```

##### 安装

- 管理员运行powershell

  ```bash
  # 启用虚拟机平台
  > Enable-WindowsOptionalFeature -Online -FeatureName VirtualMachinePlatform
  
  # 启用Linux子系统功能
  > Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
  ```
  
  cmd 管理员运行
  
  ```bash
  > dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
  ```
  
- 从 [官网](https://learn.microsoft.com/zh-cn/windows/wsl/install-manual#step-4---download-the-linux-kernel-update-package) 下载 [WSL2 Linux 内核更新包](https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi)

##### 命令

```bash
wsl --set-default-version 2			设置默认版本2
wsl -l -v							查看列表
wsl --set-version centos001 2		切换版本
wsl --terminate centos001			卸载子系统
wsl --unregister centos001			注销子系统
wsl --export centos001 D:\rootfs.tar导出系统镜像
wsl --shutdown          			关闭
wsl --list --running
wsl -u g							指定启动的用户

wslconfig /setdefault centos001		设置当前子系统为默认子系统
wslconfig /l

net stop LxssManager				关闭子系统

wslconfig
    /l, /list [/all] 列出已注册的发行版
    /s, /setdefault <DistroName> 将该发行版设为默认
    /t, /terminate <DistroName> 终止该发行版
    /u, /unregister <DistroName> 取消注册该发行版
```

##### 导入导出

```
wsl --export Ubuntu D:\Ubuntu.tar
wsl --unregister Ubuntu
wsl --import Ubuntu D:\Ubuntu D:\Ubuntu.tar --version 2
```

##### 安装 - centos

> [github](https://github.com/CentOS/sig-cloud-instance-images/)

```bash
# 1. 在分支中找对应的版本
> wget https://raw.githubusercontent.com/CentOS/sig-cloud-instance-images/CentOS-7.8.2003-x86_64/docker/centos-7.8.2003-x86_64-docker.tar.xz


# 2. 创建子系统, 名为 centos7-02, 安装在 D:\linux\centos7-02, 使用镜像 centos-7.8.2003-x86_64-docker.tar.xz
> LxRunOffline.exe install -n centos7-02 -d D:\linux\centos7-02 -f D:\software-wsl2\centos-7.8.2003-x86_64-docker.tar.xz


# 3. 启动
> LxRunOffline run -n centos001
或
> wsl -d centos001
```

##### 安装 - fedora

[github](https://github.com/fedora-cloud/docker-brew-fedora)

```bash
# 1. fedora 37 下载地址
https://raw.githubusercontent.com/fedora-cloud/docker-brew-fedora/37/x86_64/fedora-37-x86_64.tar.xz


# 2. 创建子系统, 名为 fedora37-02, 安装在 D:\linux\fedora37-02, 使用镜像 fedora-37-x86_64.tar.xz
> LxRunOffline.exe install -n fedora37-02 -d D:\linux\fedora37-02 -f D:\software-wsl2\fedora-37-x86_64.tar.xz
```

```bash
dnf install sudo git vim neovim tree wget htop zsh passwd util-linux-user python2 python python3-pip 
```

##### 安装 - ubuntu



##### 关闭 swap

```
新建 C:\Users\xxx\.wslconfig 增加

[wsl2]
swap=0
```

##### wsl.conf

```
1. 进入 wsl
2. 创建编辑 /etc/wsl.conf


[network]					# hostname
hostname = centos001
[user]						# 启动 wsl 默认用户
default = g
```

# env

##### pyenv

[github](https://github.com/pyenv-win/pyenv-win#get-pyenv-win)

```
choco install pyenv-win
```

##### windows python 环境管理

```shell
$ pip install virtualenvwrapper-win
$ mkvirtualenv --python=python3.9.13 p3913_learn

# 虚拟环境列表
$ workon
$ workon p3913_learn
# 退出环境
$ deactivate
# 删除环境
$ rmvirtualenv venv


虚拟环境安装在用户 Envs 路径下
```

# 效率软件

##### wox

```
快速启动

github: https://github.com/Wox-launcher/Wox/releases

使用: https://zhuanlan.zhihu.com/p/68383315/
```

```
教程 https://sspai.com/post/33460

1. 直接输入数字当做计算器使用
2. 安装插件
3. 剪切板历史插件
    安装 wpm install Clipboard History
    触发命令 cb
4. 弹出 USB 设备
    安装 wpm install Remove USB
    触发命令 reu
```



##### LoveString

```
字符编码转换，在Text段输入文字，各种编码就都能看到了。各个编码框也可以输入，用来调试乱码问题很方便。比如你看到一段乱码 浣犲ソ锛屼笘鐣? ，把它拷到Text输入框，你发现Ansi段的编码不像GBK，倒像是utf-8，然后把Ansi里的内容拷出来粘到utf-8，马上就能发现这段乱码的错误原因。要是用python查这个乱码，还要写好几行呢，用LoveString，拷一拷，粘一粘，搞定   
```

##### rapidee

```
环境变量管理工具

官网: https://www.rapidee.com/en/about

RapidEEx64.zip
```

##### Procmon

```
监视Windows系统里程序的运行情况

官网: https://docs.microsoft.com/en-us/sysinternals/downloads/procmon

ProcessMonitor.zip
```

##### OpenedFilesView

```
列出所有被操作系统或是应用程序打开的文件

下载地址: 
https://www.nirsoft.net/
https://www.nirsoft.net/utils/opened_files_view.html

ofview-x64.zip
```

##### FastStoneImageViewer

```
图片查看工具

下载地址: https://faststone-image-viewer.en.softonic.com/
```

##### 浏览器插件

```
Website IP 
查看访问网页的ip
```

# 应用

##### 删除VS2017右键菜单 在Visual Studio中打开

```
新建记事本 xxx.reg

Windows Registry Editor Version 5.00
[-HKEY_CLASSES_ROOT\Directory\Background\shell\AnyCode]
[-HKEY_CLASSES_ROOT\Directory\shell\AnyCode]
```

##### pycharm 设置 terminal

```
tool -> shell path -> powershell.exe
```

#####  visio 2019 激活方法

```
1.电脑新建一个记事本文件.txt（任何地方都可以）
2.复制下面代码到新建记事本文件.txt中，并保存
3.上述记事本文件.txt后缀成.bat 的Windows可执行脚本文件
4.直接右键使用【管理员权限身份】打开修改后的.bat文件
5.耐心等待一会，不要以为没有执行，等一会会有打印记录，激活成功。


@echo off
title Activate Microsoft Visio 2019&cls&echo ============================================================================&echo #Visio: Activating Microsoft software products for FREE without software&echo ============================================================================&echo.&echo #Supported products:&echo - Microsoft Visio Standard 2019&echo - Microsoft Visio Professional Plus 2019&echo.&echo.&(if exist "%ProgramFiles%\Microsoft Office\Office16\ospp.vbs" cd /d "%ProgramFiles%\Microsoft Office\Office16")&(if exist "%ProgramFiles(x86)%\Microsoft Office\Office16\ospp.vbs" cd /d "%ProgramFiles(x86)%\Microsoft Office\Office16")&cscript //nologo ospp.vbs /inslic:"..\root\Licenses16\pkeyconfig-office.xrm-ms" >nul&(for /f %%x in ('dir /b ..\root\Licenses16\client-issuance*.xrm-ms') do cscript ospp.vbs /inslic:"..\root\Licenses16\%%x" >nul)&(for /f %%x in ('dir /b ..\root\Licenses16\visioprovl_kms*.xrm-ms') do cscript ospp.vbs /inslic:"..\root\Licenses16\%%x" >nul)&(for /f %%x in ('dir /b ..\root\Licenses16\visiopro2019vl_kms*.xrm-ms') do cscript ospp.vbs /inslic:"..\root\Licenses16\%%x" >nul)&echo.&echo ============================================================================&echo 正在尝试激活...&cscript //nologo ospp.vbs /unpkey:7VCBB >nul&cscript //nologo ospp.vbs /inpkey:9BGNQ-K37YR-RQHF2-38RQ3-7VCBB >nul&set i=1
:server
if %i%==1 set KMS_Sev=kms8.MSGuides.com
if %i%==2 set KMS_Sev=kms9.MSGuides.com
if %i%==3 set KMS_Sev=kms7.MSGuides.com
if %i%==4 goto notsupported
cscript //nologo ospp.vbs /sethst:%KMS_Sev% >nul&echo ============================================================================&echo.&echo.
cscript //nologo ospp.vbs /act | find /i "successful" && (echo 已完成，按任意键退出) || (echo 连接KMS服务器失败! 试图连接到另一个… & echo 请等待... & echo. & echo. & set /a i+=1 & goto server)
pause >nul
exit
```


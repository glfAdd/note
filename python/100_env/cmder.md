##### 安装

```
scoop install cmder
```

##### 配置

```
设置任意地方鼠标右键启动Cmder
    1. 右键管理员身份运行cmder.exe执行
    2. Cmder.exe /REGISTER ALL

字体:
    修改成简体中文
大小&位置:
    显示&储存当前窗口的大小和位置
    退出时自动保存窗口大小和位置


使用powershell
启动 -> 指定命名任务 -> {PowerShell::PowerShell}


使用wsl
启动 -> 指定命名任务 -> {WSL::bash}


设置打开时显示的目录
Startup - > Task，修改{cmd::Cmder}项，把:
*cmd /k "%ConEmuDir%\..\init.bat" -new_console:d:%USERPROFILE%
修改成 :cmd /k "%ConEmuDir%\..\init.bat" -new_console:d:C:\


启动的时候直接启动zsh
vim ~/.bashrc
if test -t 1; then
    exec zsh
fi


启动wsl时设置打开的目录
if [ `pwd` = "/mnt/c/Users/lg/scoop/apps/cmder/1.3.14" ]; then
    cd /mnt/c/Users/lg
fi
```

##### 快捷键

```
2. 在视窗内搜索画面上出现过的关键字
4. 切换tab页按钮
5. 锁定窗口，无法输入新内容
6. 切换视窗是否提供卷轴功能，启动时可查询之前显示过的内容。
7. 左击可开启系统菜单，右击可直接开启设置 （ Win+Alt+P：开启设置）

新建tab 	Ctrl + t
关闭tab 	Ctrl + w
切换Tab 	Ctrl+Tab或Ctrl+1,2...
新建CMD 	Shift + Alt + 1
新建 PowerShell 	Shift + Alt + 2
全屏操作 	Alt + Enter
```


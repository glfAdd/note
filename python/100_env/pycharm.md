##### 函数注释

```
pycharm 设置注释
File -> Settings -> Tools -> Python Integrated Tools -> Docstrings -> Docstring format -> 选择 google


注释添加类型
File -> Settings -> Editor -> General -> Smart Keys -> python -> Insert type placeholders in the documentation comment stub
```

##### 重置试用

```
源
https://plugins.zhile.io

插件
IDE Eval Reset
```

##### 插件

```
IdeaVim
```

##### 无法输入中文

```
export LC_ALL=zh_CN.UTF-8
export GTK_IM_MODULE=fcitx
export QT_IM_MODULE=fcitx
export XMODIFIERS=@im=fcitx
```

##### pycharm 用 sudo 权限启动 python

- 创建脚本一定以 python 开头, 不然后面 Pycharm 无法识别 python_sudo.sh

  ```shell
  #!/bin/bash
  sudo /home/glfadd/.pyenv/versions/p3710-dev/bin/python "$@"
  ```

- 可执行权限

- pycharm 选择这个脚本


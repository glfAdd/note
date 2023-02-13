##### Package Control

```python
# 1.官网
https://packagecontrol.io/installation
# 2.ctrl+`
# 3.复制下面的代码
import urllib.request,os,hashlib; h = '6f4c264a24d933ce70df5dedcf1dcaee' + 'ebe013ee18cced0ef93d5f746d80ef60'; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) ); by = urllib.request.urlopen( 'http://packagecontrol.io/' + pf.replace(' ', '%20')).read(); dh = hashlib.sha256(by).hexdigest(); print('Error validating download (got %s instead of %s), please try manual install' % (dh, h)) if dh != h else open(os.path.join( ipp, pf), 'wb' ).write(by)
# 4.在preferences菜单下新增package control选项，安装成功
# 5.失败后手动下载安装
https://packagecontrol.io/Package%20Control.sublime-package
下载好以后，打开sublime text3，选择菜单Preferences->Browse Packages... 打开安装目录，
此时会进入到一个叫做Packages的目录下，点击进入上一层目录Sublime Text3，在此目录下有一个文件夹叫做Installed Packages，把刚才下载的文件放到这里就可以了。然后重启sublime text3，观察Preferences菜单最下边是否有Package Settings 和Package Control两个选项，如果有，则代表安装成功了。此时使用快捷键
# 6. Ctrl+Shift+P，输入install，选择install package，想安装什么插件，在里面搜索名字就可以了        
```

#####  删除插件

```
输入 remove package
```

##### git

```python

```

##### Ctags

```python
函数跳转，我的电脑上是Alt+点击 函数名称，会跳转到相应的函数
DocBlockr
```

##### DocBlockr

```python
注释插件，生成幽美的注释。标准的注释，包括函数名、参数、返回值等，并以多行显示，省去手动编写

```

##### 自动补全插件

```python
SublimeCodeIntel
```

##### 直接运行当前文件

```python
SublimeREPL
打开Preferences->Key Bindings，添加快捷键
[
    {
        "keys": ["f5"],
        "caption": "SublimeREPL: Python - RUN current file",
        "command": "run_existing_window_command",
        "args": {
            "id": "repl_python_run",
            "file": "config/Python/Main.sublime-menu"
        }
    }
]
```

##### 环境配置

```python
# 设置Sublime Text的语法为python
View -> syntax ->python
# 设置编译环境(默认python版本2.7)
Tools -> Build System -> Python
# 自定义环境
Tools -> Build System -> New Build System
{
	"cmd": ["C:/Users/wanliang/AppData/Local/conda/conda/envs/p27/python.exe", "-u", "$file"],
    "file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
    "selector": "source.python"
}
```

##### 快捷键

```python
Ctrl + B			运行
```

##### json格式化

```
pretty json

github地址: https://github.com/dzhibas/SublimePrettyJson

格式化快捷键: 
ctrl+alt+j 格式化json字符串
ctrl+alt+m 压缩json字符串

教程
http://www.mamicode.com/info-detail-245317.html

配置文件:
默认的配置文件不能修改, 可以修改用户的配置文件
```


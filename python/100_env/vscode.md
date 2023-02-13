```
字符串拼接
f'{name} {age}'

预定义代码片段

pytest 模块(在python扩展里设置)

kite		文档插件 依赖 CoPilot
Wolf		代码预览
AutoDocstring	注释
python docstring 注释
python type hint 请求参数类型补全
python test explorer for   测试插件
终端输出彩色日志

Bookmarks 跳转书签
Sourcegraph 在线开源代码搜索
GistPad 这是什么
Visual Studio IntelliCode 自动补全

sort lines 文本排序
code runner 代码运行 (cmd + R 直接运行 )
comment Anchors 

paste image 图片粘贴,(编辑 markdown 时, 直接粘贴图片, 图片可以直接粘贴进来, 不用选择或者拖动)
```

# 设置

### 系统设置

##### 终端

```

```

##### python 默认解释器

在 .vscode 下创建 setting.json 文件

```json
{
    "python.formatting.provider": "black",
    "python.defaultInterpreterPath":"C:\\Users\\xxxxxx\\Envs\\p378-dev\\Scripts\\python.exe"
}
```

### 快捷键

|                  |                |          |
| ---------------- | -------------- | -------- |
| Ctrl + Shift + P | 打开对话框     |          |
| Ctrl + Shift + N | 打开新窗口     |          |
| Ctrl + Shift + B | 打开/关闭边栏  | Ctrl + B |
| Alt + Shift + F  | 格式化 (black) |          |
|                  |                |          |
| F2               | 重命名变量     |          |
|                  |                |          |
| Ctrl+ `          | 打开终端       |          |
|                  |                |          |
|                  |                |          |
|                  | 搜索           |          |



```
Sort JSON objects
Cmd+Shift+P => Sort JSON

Sort lines
```

##### 修改快捷键

```

```



# 插件

##### Chinese (Simplified) (简体中文) Language Pack for Visual Studio Code

`v1.73.11020948`



##### Markdown Preview Enhanced

`v0.6.5` markdown

##### json (json 目录树)

`v2.0.2 ` 

##### Sort JSON objects (json 排序)

`v1.20.0` 

##### Sort lines (json 排序)

`v1.9.1` 

##### Import Cost (导入包大小)

`v3.3.0` 

##### Vim

`v1.24.3` vim

##### Todo Tree

`v0.0.220`

##### filesize (文件大小)

`v3.1.0` 

##### Docs View (文档窗口)

`v0.0.11` 

##### docstring (注释)

`v0.6.1` 

##### C/C++ (c 扩展)

`v1.12.4` 

##### Remote - SSH (远程调试)

`v0.92.0` 

使用命令 `Ctrl + Shift + P` 打开对话框, 输入 `remote-ssh:open` , 编辑 `C:\Users\glfadd\.ssh\config`

```
Host dev
    HostName 172.24.145.35
    User glfadd
    IdentityFile "私钥, 用括号括起来"
```

##### Remote Development

> `v0.23.0`

```

```

##### Code Spell Checker (拼写检测)

`v2.11.1` 

##### Parameter Hints

`v0.2.7`  参数类型提示

##### Git Graph

`v1.30.0` git 图像显示

##### Docs View (卸载)

`v0.0.11` 窗口文档

##### Tabnine AI Autocomplete

`3.6.25` ai 代码补全

##### Krinql(要登录, 卸载)

`v0.1.1` 自定写函数调用注释

##### wakatime

##### CodeSnap

`v1.3.4` 代码截图照片

##### Sourcegraph 

`v2.2.14` 开源库代码搜索

##### Draw.io Integration

`v1.6.6` 原型图工具

### UI

##### GitHub Theme

```
主题
v6.3.3
```





##### vscode-icons (图标)

`v12.0.1` 

### python

##### Python

`v2022.18.2`

代码分析, 高亮, 规范化

##### LiveCode for python

`v1.3.10` python代码实时展示

##### Python Preview (停止维护)

`v0.0.4` python代码实时展示

##### AREPL for python

`v2.0.4` 代码预览

##### Python Indent

`v1.18.0` 缩进修正

##### Python Snippets (卸载)

`v1.0.2` 预定义代码片段

##### Better Comments

`v3.0.2` 相同名字高亮

##### Thunder Client

`v2.0.2` api 工具, 代替 postman

##### autoDocstring - Python Docstring Generator

```
v0.6.1
注释

支持:
	google
    sphinx
    numpy
    docBlockr
    one-line-sphinx
    pep257

设置风格
"autoDocstring.docstringFormat": "numpy"


epytext
```



### 弃用

##### wakatime

```
需要连接外部 api
```

##### Material Theme

```
主题
v33.6.0
不好看
```



# 问题

##### 问题: 打开项目

- 描述

  ```
  无法在这个大型工作区文件夹中监视文件更改。请按照说明链接来解决此问题
  ```

- 原因

  ```
  工作区很大并且文件很多，导致VS Code文件观察程序的句柄达到上限
  ```

- 解决办法

  ```bash
  1. 查看系统最大句柄数
  $ cat /proc/sys/fs/inotify/max_user_watches
  
  2. 编辑 /etc/sysctl.conf, 添加
  fs.inotify.max_user_watches=524288
  
  3. 使配置生效
  $ sysctl -p
  ```

##### 问题: debug

```
debug 时报错:
No module named xxx
```

##### 问题 debug

```
https://blog.csdn.net/weixin_43343144/article/details/86601505
```

```
{
    // 使用 IntelliSense 了解相关属性。 
    // 悬停以查看现有属性的描述。
    // 欲了解更多信息，请访问: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Flask",
            "type": "python",
            "request": "launch",
            "module": "flask",
            "env": {
                "FLASK_APP": "${workspaceFolder}/mgt_portal/site_run.py",
                "FLASK_DEBUG": "0"
            },
            "args": [
                "run",
                "--no-debugger",
                "--no-reload",
                "--port", "1601",
                "--host", "0.0.0.0"
            ],
            "jinja": true,
            "justMyCode": true
        }
    ]
}
```

##### 问题3

```
Error in the AREPL extension!
err code: 9009

Are you sure you have installed python 3 and it is in your PATH?
            You can download python here: https://www.python.org/downloads/

Print Output:
Variables:
```







```
----------------------------- 插件
括号匹配: Bracket Pair Colorizer
todo和FIXME高亮: TODO Highlight
x 单词拼写错误检查: Code Spell Checker
运行选中代码段: Code Runner
成本提示(提示 import 命令导入包的大小): Improt Cost
x git 插件: GitLens — Git supercharged
x docker扩展插件: Docker
x markdown: markdownlint
主题: Material Theme

远程 ssh 编辑代码: Remote - SSH
----------------------------- 快捷键






代码格式化工具对比: autopep8 < yapf < black
安装方式: pip install black 

```

##### 设置 java 版本

```
1. c + s + P 输入 Configure Java Runtime 查看安装的 jdk 版本
2. 设置 Code Runner 的 java 版本

"java.configuration.runtimes": [
	{
	"name": "JavaSE-1.8",
	"path": "/path/to/jdk-8",
	},
	{
	"name": "JavaSE-11",
	"path": "/path/to/jdk-11",
	},
	{
      "name": "JavaSE-1.8",
      "path": "/Users/glfadd/.sdkman/candidates/java/current",
      "default": true
    },
]
```

##### 终端

打开终端提示如下信息, 禁止运行脚本, 导致虚拟环境无法启动

```
PS D:\code\pynote> & c:/Users/gonglongfei/Envs/p3710-dev/Scripts/Activate.ps1
& : 无法加载文件 C:\Users\gonglongfei\Envs\p3710-dev\Scripts\Activate.ps1，因为在此系统上禁止运行脚本。有关详细信息，请参阅 https:/go.microsoft.com/fwl
ink/?LinkID=135170 中的 about_Execution_Policies。
所在位置 行:1 字符: 3
+ & c:/Users/gonglongfei/Envs/p3710-dev/Scripts/Activate.ps1
+   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : SecurityError: (:) []，PSSecurityException
    + FullyQualifiedErrorId : UnauthorizedAccess
```

决绝办法

```bash
# 1. 管理源运行 powershell
# 2. 执行 get-ExecutionPolicy 显示状态, Restricted 表示禁止
# 3. 执行 set-ExecutionPolicy RemoteSigned
# 4. 输入 y
# 5. 再次查看状态, RemoteSigned 表示允许
```

# 设置

launch.json

```json
{
    // 使用 IntelliSense 了解相关属性。 
    // 悬停以查看现有属性的描述。
    // 欲了解更多信息，请访问: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [

        {
            "name": "site_run",
            "type": "python",
            "request": "launch",
            "module": "flask",
            // 默认解释器
            "python": "${command:python.interpreterPath}",
            "cwd": "${workspaceFolder}/py-service/mgt_portal",
            "env": {
                "FLASK_APP": "${workspaceFolder}/mgt_portal/site_run.py:app",
                "FLASK_ENV": "development",
                "FLASK_DEBUG": "1"
            },
            "args": [
                "run",
                "--no-debugger",
                "--no-reload",
                "--port", "1601",
                "--host", "0.0.0.0"
            ],
            "jinja": true,
            "justMyCode": true
        }
    ]
}
```


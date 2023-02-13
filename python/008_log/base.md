##### 参数

```
%(name)s            Logger的名字
%(levelno)s	        数字形式的日志级别
%(levelname)s	    文本形式的日志级别
%(pathname)s	    调用日志输出函数的模块的完整路径名，可能没有
%(filename)s	    调用日志输出函数的模块的文件名
%(module)s	        调用日志输出函数的模块名
%(funcName)s	    调用日志输出函数的函数名
%(lineno)d	        调用日志输出函数的语句所在的代码行
%(created)f	        当前时间，用UNIX标准的表示时间的浮 点数表示
%(relativeCreated)d	输出日志信息时的，自Logger创建以 来的毫秒数
%(asctime)s	        字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
%(thread)d	        线程ID。可能没有
%(threadName)s	    线程名。可能没有
%(process)d	        进程ID。可能没有
%(message)s	        用户输出的消息
```

##### 级别

```
DEBUG < INFO < WARNING < ERROR < CRITICAL

DEBUG       最详细
ERROR       出现严重问题, 导致某些功能不能正常运行记录信息
CRITICAL    系统即将崩溃或者已经崩溃
NOTSET      没有设置
```

#####

abc.conf

```ini
# -------------------- 设置 logger --------------------
[loggers]
# 定义 loggers 名, root 是父类, 必需存在
keys=root,error,info

# 定义每个 app 规则, 命名规范 logger_名字
[logger_root]
level=DEBUG
# root 的 app 可以填这个选项, 其他 app 必填, 用于定义打印输出时候的 app 名
qualname=root
# 指定过滤器, 多个以逗号分隔
handlers=debugs

[logger_error]
level=ERROR
qualname=error
handlers=errors

[logger_info]
level=INFO
qualname=INFO
handlers=infos

# -------------------- 设置 handler 过滤器 --------------------
[handlers]
# 定义过 handler 名称
keys=infos,errors,debugs  

[handler_infos]
#指定过滤器组件,详情请看官网，这个是以文件方式创建
class=FileHandler
level=INFO
#定义日志打印格式,下面会创建formatters，格式也是严格要求formatter_keysname 创建
formatter=form01   
#创建文件名字,以什么方式打开
args=('info.log','a')    

[handler_errors] 
class=FileHandler
level=DEBUG
formatter=form02
args=('info1.log','a')

[handler_debugs] 
class=FileHandler
level=DEBUG
formatter=form02
args=('info1.log','a')

# -------------------- 设置 formatter 格式 --------------------
[formatters]
# 定义名称
keys=form01,form02

[formatter_form01]
format=%(asctime)s %(filename)s %(levelname)s %(message)s #年-月-日 时-分-秒,毫秒，文件名,级别名，消息信息
# 日期输出格式
datefmt=%Y-%m-%d %H:%M:%S  

[formatter_form02]
format=%(asctime)s %(filename)s %(levelname)s %(message)s
datefmt=%Y-%m-%d %H:%M:%S
```



> https://www.jb51.net/article/190556.htm
>
> https://blog.csdn.net/qq_39564555/article/details/102514816?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task
>
> 
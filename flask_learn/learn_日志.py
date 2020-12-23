from flask import Flask
import logging
from logging.handlers import RotatingFileHandler

""" ============================
https://blog.csdn.net/qq_39564555/article/details/102514816?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task


flask的日志记录需要用到python标准库logging的支持

当想要为项目配置日志时，应当在程序启动时尽早进行配置

"""

""" ============================ 123 
参数:
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



DEBUG < INFO < WARNING < ERROR < CRITICAL
    DEBUG       最详细的日志信息
    INFO        一般的使用场景是重要的业务处理已经结束
    WARNING     当某些不被期望的事情发生的时候，需要记录的信息，比如磁盘即将存满，注意当前的程序一依旧可以正常运行，不报错
    ERROR       出现严重问题, 导致某些功能不能正常运行记录信息
    CRITICAL    系统即将崩溃或者已经崩溃
    NOTSET      没有设置

"""

# 等级
logging.basicConfig(level=logging.DEBUG)
# 创建日志记录器，指明日志保存路径,每个日志的大小，保存日志的上限
file_log_handler = RotatingFileHandler('logs/logs', maxBytes=1024 * 1024, backupCount=10)
# 格式
formatter = logging.Formatter('%(levelname)s %(filename)s %(lineno)d %(message)s')
# 将日志记录器指定日志的格式
file_log_handler.setFormatter(formatter)
# 为全局的日志工具对象添加日志记录器
logging.getLogger().addHandler(file_log_handler)

""" ============================ 123 """

""" ============================ 123 """

""" ============================ 123 """

""" ============================ 123 """

""" ============================ 123 """

""" ============================ 123 """

""" ============================ 123 """

""" ============================ 123 """

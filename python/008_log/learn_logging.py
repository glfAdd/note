import logging
from logging.handlers import RotatingFileHandler

""" ============================
https://blog.csdn.net/qq_39564555/article/details/102514816?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task
flask的日志记录需要用到python标准库logging的支持
当想要为项目配置日志时，应当在程序启动时尽早进行配置
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

""" ============================ 安装
pip install scrapydweb


参考
https://zhuanlan.zhihu.com/p/99449687
"""

""" ============================ 命令
运行命令scrapydweb，首次启动会在当前目录下生成配置文件 scrapydweb_settings_v8.py

启动
scrapydweb

web 页面
http://localhost:5000/
"""

""" ============================ scrapydweb_settings_v8.py 
1. web 登录验证
关闭
ENABLE_AUTH = False

启用
ENABLE_AUTH = True
USERNAME = 'username'
PASSWORD = 'password'


2. 端口
SCRAPYDWEB_PORT = 5000


3. 指定 Scrapy 项目开发目录
ScrapydWeb 将自动列出该路径下的所有项目，默认选定最新编辑的项目，选择项目后即可自动打包和部署指定项目.
ScrapydWeb 在本地的时候可以设置. 
如果 ScrapydWeb 运行在远程服务器上，除了通过当前开发主机上传常规的 egg 文件，也可以将整个项目文件夹添加到 zip/tar/tar.gz 压缩文件后直接上传即可，无需手动打包为 egg 文件
SCRAPY_PROJECTS_DIR = '/home/xieyabin/myprojects/'


4. 日志
# 日志文件保存的地址，用于日志分析
LOCAL_SCRAPYD_LOGS_DIR = '/Users/glfadd/Desktop'
# 开启日志
ENABLE_LOGPARSER = True


ENABLE_MONITOR = True





6.邮件设置：通过轮询子进程在后台定时模拟访问 Stats 页面，ScrapydWeb 将在满足特定触发器时根据设定自动停止爬虫任务并发送通知邮件，邮件正文包含当前爬虫任务的统计信息。
1.添加邮箱帐号：
    SMTP_SERVER = 'smtp.qq.com'
    SMTP_PORT = 465
    SMTP_OVER_SSL = True
    SMTP_CONNECTION_TIMEOUT = 10

    EMAIL_USERNAME = ''  # defaults to FROM_ADDR
    EMAIL_PASSWORD = 'password'
    FROM_ADDR = 'username@qq.com'
    TO_ADDRS = [FROM_ADDR]
2.设置邮件工作时间和基本触发器，以下示例代表：每隔1小时或当某一任务完成时，并且当前时间是工作日的9点，12点和17点，ScrapydWeb 将会发送通知邮件。
    EMAIL_WORKING_DAYS = [1, 2, 3, 4, 5]
    EMAIL_WORKING_HOURS = [9, 12, 17]
    ON_JOB_RUNNING_INTERVAL = 3600
    ON_JOB_FINISHED = True
3.除了基本触发器，ScrapydWeb 还提供了多种触发器用于处理不同类型的 log，包括 'CRITICAL', 'ERROR', 'WARNING', 'REDIRECT', 'RETRY' 和 'IGNORE'等。
    LOG_CRITICAL_THRESHOLD = 3
    LOG_CRITICAL_TRIGGER_STOP = True
    LOG_CRITICAL_TRIGGER_FORCESTOP = False
    # ...
    LOG_IGNORE_TRIGGER_FORCESTOP = False
以上示例代表：当日志中出现3条或以上的 critical 级别的 log 时，ScrapydWeb 将自动停止当前任务，如果当前时间在邮件工作时间内，则同时发送通知邮件。
"""

""" ============================ logparser 
日志
提示错误:
'pip install logparser' on host '127.0.0.1:6800' and run command 'logparser' to show crawled_pages and scraped_items.

安装
pip install logparser

配置
vim /Users/glfadd/.pyenv/versions/3.6.6/envs/p366/lib/python3.6/site-packages/logparser/settings.py
修改
SCRAPYD_LOGS_DIR = '/Users/glfadd/Desktop'
SCRAPYD_SERVER = '127.0.0.1:6800'


web页面
http://127.0.0.1:6800/logs/stats.json



"""

""" ============================ qwewqe """

""" ============================ qwewqe """

""" ============================ qwewqe """

""" ============================ qwewqe """

""" ============================ qwewqe """

""" ============================ qwewqe """

""" ============================ qwewqe """

""" ============================ qwewqe """

""" ============================ qwewqe """

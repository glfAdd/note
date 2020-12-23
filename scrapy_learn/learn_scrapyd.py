"""
配套组件:
    scrapy: 一个爬虫框架，你可以创建一个scrapy项目
    scrapyd: 相当于一个组件，能够将scrapy项目进行远程部署，调度使用等. 看作一个cs（client-server）程序
    scrapydwe: scrapyd的可视界面


scrapyd 启动时读取 scrapy.cfg 文件的配置
scrapydweb 管理多个 scrapyd
"""

""" ============================  安装 
pip install scrapyd
"""

""" ============================ 命令 
scrapyd
service scrapyd {start|stop|status}
"""

""" ============================ 配置 
会读取scrapy 项目 scrapy.cfg 文件的配置
[deploy]                            # target 名字
url = http://localhost:6800/        # scraypd 服务器地址
project = mySpider                  # 工程名


允许远程服务器访问
vim /usr/local/python3/lib/python3.6/site-packages/scrapyd/default_scrapyd.conf
将
bind_address = 127.0.0.1
改为
bind_address = 0.0.0.0
"""

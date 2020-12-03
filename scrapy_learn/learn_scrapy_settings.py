""" ============================ 参考
https://www.cnblogs.com/canhun/p/11124247.html
"""

""" ============================ setting
scrapy的参数共分为5个级别:
    1. scrapy默认参数
    2. 每个命令的默认参数
    3. 项目settings模块
    4. 单独爬虫参数设置
    5. 命令行选项


CONCURRENT_REQUESTS = 16                 # 全局最大并发数
CONCURRENT_REQUESTS_PER_DOMAIN = 8       # 单个域名最大并发数，如果下一个参数设置非0，此参数无效
CONCURRENT_REQUESTS_PER_IP = 0           # 单个ip最大并发数
COOKIES_ENABLED = True                   # 默认启用cookie，无需登录时一般将其关闭
DEFAULT_REQUEST_HEADERS = {              # 设置默认请求头
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
}
DOWNLOAD_DELAY = 0                       # 下载延时，高并发采集时设为0
DOWNLOAD_TIMEOUT = 180                   # 超时时间设置，一般设置在10-30之间
LOG_ENABLED = True                       # 启用日志
LOG_STDOUT = False                       # 将进程所有的标准输出(及错误)重定向到log中，默认False。如果开启，在项目中的print方法也会以log的形式输出
LOG_LEVEL = 'DEBUG'                      # 日志输出级别，上线后至少使用info级别
LOG_FILE = None                          # 将日志输出到文件中
LOGSTATS_INTERVAL = 60.0                 # 吞吐量输出间隔，就是输出每分钟下载多少个页面、捕获多少个item的那个，默认每分钟输出一次，自主配置
REDIRECT_ENABLED = True                  # 默认开启页面跳转，一般选择关闭
RETRY_ENABLED = True                     # 默认开启失败重试，一般关闭
RETRY_TIMES = 2                          # 失败后重试次数，默认两次
RETRY_HTTP_CODES = [500, 502, 503, 504, 522, 524, 408]    # 碰到这些验证码，才开启重试
ROBOTSTXT_OBEY = False                   # 遵守网站robot协议，一般是不遵守的···········
DOWNLOADER_MIDDLEWARES = {               # 下载中间件
   'myproject.middlewares.MyDownloaderMiddleware': 543,
}
ITEM_PIPELINES = {                       # 数据处理、存储pipeline
   'myproject.pipelines.MyPipeline': 300,
}





BOT_NAME = 'xigua'    # Scrapy项目的名字,这将用来构造默认 User-Agent,同时也用来log,当您使用 startproject 命令创建项目时其也被自动赋值。

SPIDER_MODULES = ['xigua.spiders']　　#Scrapy搜索spider的模块列表 默认: [xxx.spiders]
NEWSPIDER_MODULE = 'xigua.spiders'　　#使用 genspider 命令创建新spider的模块。默认: 'xxx.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#爬取的默认User-Agent，除非被覆盖
#USER_AGENT = 'xigua (+http://www.yourdomain.com)'

# Obey robots.txt rules
#如果启用,Scrapy将会采用 robots.txt策略，常使用不遵循Flase
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#Scrapy downloader 并发请求(concurrent requests)的最大值,默认: 16
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
#未同意网站的请求配置延迟（默认为0）
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3　　# 下载器延迟时间，下载器在同一网站面前需要等待的时间，该选项可以用来限制爬取速度,减轻服务器压力。同时也支持小数:0.25 以秒为单# The download delay setting will honor only one of:
# 下载延迟设置，只能有一个生效
#CONCURRENT_REQUESTS_PER_DOMAIN = 16　　# 对单个网站进行并发请求的最大值
#CONCURRENT_REQUESTS_PER_IP = 16　　
#对单个ip进行并发请求的最大值，如果非0，则忽略，CONCURRENT_REQUESTS_PER_DOMAIN 设定,使用该设定。 
#也就是说,并发限制将针对IP,而不是网站。该设定也影响 DOWNLOAD_DELAY: 如果 CONCURRENT_REQUESTS_PER_IP 非0,下载延迟应用在IP而不是网站上。


# Disable cookies (enabled by default)
# 禁用cookie（默认情况下启用）
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# 禁用Telent控制台（默认启用）
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# 覆盖默认请求标头，也可以加入请求头，获取同样来自开发着工具，
# 很多网站都会检查客户端的headers，比如豆瓣就是每一个请求都检查headers的user_agent，否则只会返回403，可以开启 USER_AGENT 请求头
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# 启用或禁用蜘蛛中间件
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'xigua.middlewares.XiguaSpiderMiddleware': 543,
#}


# Enable or disable downloader middlewares
# 启用或禁用下载器中间件
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'xigua.middlewares.XiguaDownloaderMiddleware': 543,
#}

# Enable or disable extensions
#启用或禁用扩展程序
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# 配置项目管道，如下载图片的图片管道，分布式爬虫多爬虫的pipeline，结尾int值是优先级，可以理解为权重，以逗号间隔，是个集合
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'xigua.pipelines.XiguaPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# 启用或配置AutoThrottle扩展（默认情况下禁用）
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True

# The initial download delay
# 初始下载延迟
#AUTOTHROTTLE_START_DELAY = 5

# The maximum download delay to be set in case of high latencies
# 在高延迟的情况下设置最大下载延迟
#AUTOTHROTTLE_MAX_DELAY = 60

# The average number of requests Scrapy should be sending in parallel to each remote server
# Scrapy请求的平均数量应该并行发送每个远程服务器
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# 启用显示所收到的每个响应的调节统计信息
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# 启用或配置 Http 缓存（默认情况下禁用）
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


这就是一个完整的setting.py的接本情况：
接下来再来详细看看，并且还有哪些可以配置的呢？
-----》

#-----------------------日志文件配置-----------------------------------
# 默认: True,是否启用logging。
# LOG_ENABLED=True
# 默认: 'utf-8',logging使用的编码。
# LOG_ENCODING='utf-8'
# 它是利用它的日志信息可以被格式化的字符串。默认值：'%(asctime)s [%(name)s] %(levelname)s: %(message)s'
# LOG_FORMAT='%(asctime)s [%(name)s] %(levelname)s: %(message)s'
# 它是利用它的日期/时间可以格式化字符串。默认值： '%Y-%m-%d %H:%M:%S'
# LOG_DATEFORMAT='%Y-%m-%d %H:%M:%S'
#日志文件名
#LOG_FILE = "dg.log"
#日志文件级别,默认值：“DEBUG”,log的最低级别。可选的级别有: CRITICAL、 ERROR、WARNING、INFO、DEBUG 。
LOG_LEVEL = 'WARNING'


# -----------------------------robots协议---------------------------------------------
# Obey robots.txt rules
# robots.txt 是遵循 Robot协议 的一个文件，它保存在网站的服务器中，它的作用是，告诉搜索引擎爬虫，
# 本网站哪些目录下的网页 不希望 你进行爬取收录。在Scrapy启动后，会在第一时间访问网站的 robots.txt 文件，
# 然后决定该网站的爬取范围。
# ROBOTSTXT_OBEY = True

# 对于失败的HTTP请求(如超时)进行重试会降低爬取效率，当爬取目标基数很大时，舍弃部分数据不影响大局，提高效率
RETRY_ENABLED = False
#请求下载超时时间，默认180秒
DOWNLOAD_TIMEOUT=20
# 这是响应的下载器下载的最大尺寸，默认值：1073741824 (1024MB)
# DOWNLOAD_MAXSIZE=1073741824
# 它定义为响应下载警告的大小，默认值：33554432 (32MB)
# DOWNLOAD_WARNSIZE=33554432


# ------------------------全局并发数的一些配置:-------------------------------
# Configure maximum concurrent requests performed by Scrapy (default: 16)
# 默认 Request 并发数：16
# CONCURRENT_REQUESTS = 32
# 默认 Item 并发数：100
# CONCURRENT_ITEMS = 100
# The download delay setting will honor only one of:
# 默认每个域名的并发数：8
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
# 每个IP的最大并发数：0表示忽略
# CONCURRENT_REQUESTS_PER_IP = 0

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY 会影响 CONCURRENT_REQUESTS，不能使并发显现出来,设置下载延迟
#DOWNLOAD_DELAY = 3

# Disable cookies (enabled by default)
#禁用cookies,有些站点会从cookies中判断是否为爬虫
# COOKIES_ENABLED = True
# COOKIES_DEBUG = True

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# 它定义了在抓取网站所使用的用户代理，默认值：“Scrapy / VERSION“
#USER_AGENT = ' (+http://www.yourdomain.com)'

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
}
# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
    'companyNews.middlewares.UserAgentmiddleware': 401,
    'companyNews.middlewares.ProxyMiddleware':426,
}
# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'companyNews.middlewares.UserAgentmiddleware': 400,
    'companyNews.middlewares.ProxyMiddleware':425,
    # 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware':423,
     # 'companyNews.middlewares.CookieMiddleware': 700,
}
MYEXT_ENABLED=True      # 开启扩展
IDLE_NUMBER=12           # 配置空闲持续时间单位为 360个 ，一个时间单位为5s
# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
# 在 EXTENSIONS 配置，激活扩展
EXTENSIONS = {
    # 'scrapy.extensions.telnet.TelnetConsole': None,
    'companyNews.extensions.RedisSpiderSmartIdleClosedExensions': 500,
}
# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
# 注意:自定义pipeline的优先级需高于Redispipeline,因为RedisPipeline不会返回item,
# 所以如果RedisPipeline优先级高于自定义pipeline,那么自定义pipeline无法获取到item
ITEM_PIPELINES = {
     #将清除的项目在redis进行处理，# 将RedisPipeline注册到pipeline组件中(这样才能将数据存入Redis)
    # 'scrapy_redis.pipelines.RedisPipeline': 400,
    'companyNews.pipelines.companyNewsPipeline': 300,# 自定义pipeline视情况选择性注册(可选)
}
# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings


# ----------------scrapy默认已经自带了缓存，配置如下-----------------
# 打开缓存
#HTTPCACHE_ENABLED = True
# 设置缓存过期时间（单位：秒）
#HTTPCACHE_EXPIRATION_SECS = 0
# 缓存路径(默认为：.scrapy/httpcache)
#HTTPCACHE_DIR = 'httpcache'
# 忽略的状态码
#HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPERROR_ALLOWED_CODES = [302, 301]
# 缓存模式(文件缓存)
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'



#-----------------Scrapy-Redis分布式爬虫相关设置如下--------------------------
# Enables scheduling storing requests queue in redis.
#启用Redis调度存储请求队列，使用Scrapy-Redis的调度器,不再使用scrapy的调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

# Ensure all spiders share same duplicates filter through redis.
#确保所有的爬虫通过Redis去重，使用Scrapy-Redis的去重组件,不再使用scrapy的去重组件
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# 默认请求序列化使用的是pickle 但是我们可以更改为其他类似的。PS：这玩意儿2.X的可以用。3.X的不能用
# SCHEDULER_SERIALIZER = "scrapy_redis.picklecompat"

# 使用优先级调度请求队列 （默认使用），
# 使用Scrapy-Redis的从请求集合中取出请求的方式,三种方式择其一即可:
# 分别按(1)请求的优先级/(2)队列FIFO/(先进先出)(3)栈FILO 取出请求（先进后出）
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.PriorityQueue'
# 可选用的其它队列
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.FifoQueue'
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.LifoQueue'

# Don't cleanup redis queues, allows to pause/resume crawls.
#不清除Redis队列、这样可以暂停/恢复 爬取，
# 允许暂停,redis请求记录不会丢失(重启爬虫不会重头爬取已爬过的页面)
#SCHEDULER_PERSIST = True



#----------------------redis的地址配置-------------------------------------
# Specify the full Redis URL for connecting (optional).
# If set, this takes precedence over the REDIS_HOST and REDIS_PORT settings.
# 指定用于连接redis的URL（可选）
# 如果设置此项，则此项优先级高于设置的REDIS_HOST 和 REDIS_PORT
# REDIS_URL = 'redis://root:密码@主机ＩＰ:端口'
# REDIS_URL = 'redis://root:123456@192.168.8.30:6379'
REDIS_URL = 'redis://root:%s@%s:%s'%(password_redis,host_redis,port_redis)
# 自定义的redis参数（连接超时之类的）
REDIS_PARAMS={'db': db_redis}
# Specify the host and port to use when connecting to Redis (optional).
# 指定连接到redis时使用的端口和地址（可选）
#REDIS_HOST = '127.0.0.1'
#REDIS_PORT = 6379
#REDIS_PASS = '19940225'


#-----------------------------------------暂时用不到-------------------------------------------------------
# 它定义了将被允许抓取的网址的长度为URL的最大极限，默认值：2083
# URLLENGTH_LIMIT=2083
# 爬取网站最大允许的深度(depth)值,默认值0。如果为0，则没有限制
# DEPTH_LIMIT = 3
# 整数值。用于根据深度调整request优先级。如果为0，则不根据深度进行优先级调整。
# DEPTH_PRIORITY=3

# 最大空闲时间防止分布式爬虫因为等待而关闭
# 这只有当上面设置的队列类是SpiderQueue或SpiderStack时才有效
# 并且当您的蜘蛛首次启动时，也可能会阻止同一时间启动（由于队列为空）
# SCHEDULER_IDLE_BEFORE_CLOSE = 10

# 序列化项目管道作为redis Key存储
# REDIS_ITEMS_KEY = '%(spider)s:items'

# 默认使用ScrapyJSONEncoder进行项目序列化
# You can use any importable path to a callable object.
# REDIS_ITEMS_SERIALIZER = 'json.dumps'

# 自定义redis客户端类
# REDIS_PARAMS['redis_cls'] = 'myproject.RedisClient'

# 如果为True，则使用redis的'spop'进行操作。
# 如果需要避免起始网址列表出现重复，这个选项非常有用。开启此选项urls必须通过sadd添加，否则会出现类型错误。
# REDIS_START_URLS_AS_SET = False

# RedisSpider和RedisCrawlSpider默认 start_usls 键
# REDIS_START_URLS_KEY = '%(name)s:start_urls'

# 设置redis使用utf-8之外的编码
# REDIS_ENCODING = 'latin1'

# Disable Telnet Console (enabled by default)
# 它定义是否启用telnetconsole,默认值：True
#TELNETCONSOLE_ENABLED = False

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
# 开始下载时限速并延迟时间
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#高并发请求时最大延迟时间
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

"""
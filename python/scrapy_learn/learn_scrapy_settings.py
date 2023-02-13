""" ============================ �ο�
https://www.cnblogs.com/canhun/p/11124247.html
"""

""" ============================ setting
scrapy�Ĳ�������Ϊ5������:
    1. scrapyĬ�ϲ���
    2. ÿ�������Ĭ�ϲ���
    3. ��Ŀsettingsģ��
    4. ���������������
    5. ������ѡ��


CONCURRENT_REQUESTS = 16                 # ȫ����󲢷���
CONCURRENT_REQUESTS_PER_DOMAIN = 8       # ����������󲢷����������һ���������÷�0���˲�����Ч
CONCURRENT_REQUESTS_PER_IP = 0           # ����ip��󲢷���
COOKIES_ENABLED = True                   # Ĭ������cookie�������¼ʱһ�㽫��ر�
DEFAULT_REQUEST_HEADERS = {              # ����Ĭ������ͷ
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
}
DOWNLOAD_DELAY = 0                       # ������ʱ���߲����ɼ�ʱ��Ϊ0
DOWNLOAD_TIMEOUT = 180                   # ��ʱʱ�����ã�һ��������10-30֮��
LOG_ENABLED = True                       # ������־
LOG_STDOUT = False                       # ���������еı�׼���(������)�ض���log�У�Ĭ��False���������������Ŀ�е�print����Ҳ����log����ʽ���
LOG_LEVEL = 'DEBUG'                      # ��־����������ߺ�����ʹ��info����
LOG_FILE = None                          # ����־������ļ���
LOGSTATS_INTERVAL = 60.0                 # ���������������������ÿ�������ض��ٸ�ҳ�桢������ٸ�item���Ǹ���Ĭ��ÿ�������һ�Σ���������
REDIRECT_ENABLED = True                  # Ĭ�Ͽ���ҳ����ת��һ��ѡ��ر�
RETRY_ENABLED = True                     # Ĭ�Ͽ���ʧ�����ԣ�һ��ر�
RETRY_TIMES = 2                          # ʧ�ܺ����Դ�����Ĭ������
RETRY_HTTP_CODES = [500, 502, 503, 504, 522, 524, 408]    # ������Щ��֤�룬�ſ�������
ROBOTSTXT_OBEY = False                   # ������վrobotЭ�飬һ���ǲ����صġ���������������������
DOWNLOADER_MIDDLEWARES = {               # �����м��
   'myproject.middlewares.MyDownloaderMiddleware': 543,
}
ITEM_PIPELINES = {                       # ���ݴ����洢pipeline
   'myproject.pipelines.MyPipeline': 300,
}





BOT_NAME = 'xigua'    # Scrapy��Ŀ������,�⽫��������Ĭ�� User-Agent,ͬʱҲ����log,����ʹ�� startproject �������Ŀʱ��Ҳ���Զ���ֵ��

SPIDER_MODULES = ['xigua.spiders']����#Scrapy����spider��ģ���б� Ĭ��: [xxx.spiders]
NEWSPIDER_MODULE = 'xigua.spiders'����#ʹ�� genspider �������spider��ģ�顣Ĭ��: 'xxx.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#��ȡ��Ĭ��User-Agent�����Ǳ�����
#USER_AGENT = 'xigua (+http://www.yourdomain.com)'

# Obey robots.txt rules
#�������,Scrapy������� robots.txt���ԣ���ʹ�ò���ѭFlase
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#Scrapy downloader ��������(concurrent requests)�����ֵ,Ĭ��: 16
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
#δͬ����վ�����������ӳ٣�Ĭ��Ϊ0��
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3����# �������ӳ�ʱ�䣬��������ͬһ��վ��ǰ��Ҫ�ȴ���ʱ�䣬��ѡ���������������ȡ�ٶ�,���������ѹ����ͬʱҲ֧��С��:0.25 ����Ϊ��# The download delay setting will honor only one of:
# �����ӳ����ã�ֻ����һ����Ч
#CONCURRENT_REQUESTS_PER_DOMAIN = 16����# �Ե�����վ���в�����������ֵ
#CONCURRENT_REQUESTS_PER_IP = 16����
#�Ե���ip���в�����������ֵ�������0������ԣ�CONCURRENT_REQUESTS_PER_DOMAIN �趨,ʹ�ø��趨�� 
#Ҳ����˵,�������ƽ����IP,��������վ�����趨ҲӰ�� DOWNLOAD_DELAY: ��� CONCURRENT_REQUESTS_PER_IP ��0,�����ӳ�Ӧ����IP��������վ�ϡ�


# Disable cookies (enabled by default)
# ����cookie��Ĭ����������ã�
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# ����Telent����̨��Ĭ�����ã�
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# ����Ĭ�������ͷ��Ҳ���Լ�������ͷ����ȡͬ�����Կ����Ź��ߣ�
# �ܶ���վ������ͻ��˵�headers�����綹�����ÿһ�����󶼼��headers��user_agent������ֻ�᷵��403�����Կ��� USER_AGENT ����ͷ
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# ���û����֩���м��
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'xigua.middlewares.XiguaSpiderMiddleware': 543,
#}


# Enable or disable downloader middlewares
# ���û�����������м��
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'xigua.middlewares.XiguaDownloaderMiddleware': 543,
#}

# Enable or disable extensions
#���û������չ����
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# ������Ŀ�ܵ���������ͼƬ��ͼƬ�ܵ����ֲ�ʽ����������pipeline����βintֵ�����ȼ����������ΪȨ�أ��Զ��ż�����Ǹ�����
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'xigua.pipelines.XiguaPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# ���û�����AutoThrottle��չ��Ĭ������½��ã�
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True

# The initial download delay
# ��ʼ�����ӳ�
#AUTOTHROTTLE_START_DELAY = 5

# The maximum download delay to be set in case of high latencies
# �ڸ��ӳٵ������������������ӳ�
#AUTOTHROTTLE_MAX_DELAY = 60

# The average number of requests Scrapy should be sending in parallel to each remote server
# Scrapy�����ƽ������Ӧ�ò��з���ÿ��Զ�̷�����
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# ������ʾ���յ���ÿ����Ӧ�ĵ���ͳ����Ϣ
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# ���û����� Http ���棨Ĭ������½��ã�
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


�����һ��������setting.py�Ľӱ������
������������ϸ���������һ�����Щ�������õ��أ�
-----��

#-----------------------��־�ļ�����-----------------------------------
# Ĭ��: True,�Ƿ�����logging��
# LOG_ENABLED=True
# Ĭ��: 'utf-8',loggingʹ�õı��롣
# LOG_ENCODING='utf-8'
# ��������������־��Ϣ���Ա���ʽ�����ַ�����Ĭ��ֵ��'%(asctime)s [%(name)s] %(levelname)s: %(message)s'
# LOG_FORMAT='%(asctime)s [%(name)s] %(levelname)s: %(message)s'
# ����������������/ʱ����Ը�ʽ���ַ�����Ĭ��ֵ�� '%Y-%m-%d %H:%M:%S'
# LOG_DATEFORMAT='%Y-%m-%d %H:%M:%S'
#��־�ļ���
#LOG_FILE = "dg.log"
#��־�ļ�����,Ĭ��ֵ����DEBUG��,log����ͼ��𡣿�ѡ�ļ�����: CRITICAL�� ERROR��WARNING��INFO��DEBUG ��
LOG_LEVEL = 'WARNING'


# -----------------------------robotsЭ��---------------------------------------------
# Obey robots.txt rules
# robots.txt ����ѭ RobotЭ�� ��һ���ļ�������������վ�ķ������У����������ǣ����������������棬
# ����վ��ЩĿ¼�µ���ҳ ��ϣ�� �������ȡ��¼����Scrapy�����󣬻��ڵ�һʱ�������վ�� robots.txt �ļ���
# Ȼ���������վ����ȡ��Χ��
# ROBOTSTXT_OBEY = True

# ����ʧ�ܵ�HTTP����(�糬ʱ)�������Իή����ȡЧ�ʣ�����ȡĿ������ܴ�ʱ�������������ݲ�Ӱ���֣����Ч��
RETRY_ENABLED = False
#�������س�ʱʱ�䣬Ĭ��180��
DOWNLOAD_TIMEOUT=20
# ������Ӧ�����������ص����ߴ磬Ĭ��ֵ��1073741824 (1024MB)
# DOWNLOAD_MAXSIZE=1073741824
# ������Ϊ��Ӧ���ؾ���Ĵ�С��Ĭ��ֵ��33554432 (32MB)
# DOWNLOAD_WARNSIZE=33554432


# ------------------------ȫ�ֲ�������һЩ����:-------------------------------
# Configure maximum concurrent requests performed by Scrapy (default: 16)
# Ĭ�� Request ��������16
# CONCURRENT_REQUESTS = 32
# Ĭ�� Item ��������100
# CONCURRENT_ITEMS = 100
# The download delay setting will honor only one of:
# Ĭ��ÿ�������Ĳ�������8
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
# ÿ��IP����󲢷�����0��ʾ����
# CONCURRENT_REQUESTS_PER_IP = 0

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY ��Ӱ�� CONCURRENT_REQUESTS������ʹ�������ֳ���,���������ӳ�
#DOWNLOAD_DELAY = 3

# Disable cookies (enabled by default)
#����cookies,��Щվ����cookies���ж��Ƿ�Ϊ����
# COOKIES_ENABLED = True
# COOKIES_DEBUG = True

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# ����������ץȡ��վ��ʹ�õ��û�����Ĭ��ֵ����Scrapy / VERSION��
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
MYEXT_ENABLED=True      # ������չ
IDLE_NUMBER=12           # ���ÿ��г���ʱ�䵥λΪ 360�� ��һ��ʱ�䵥λΪ5s
# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
# �� EXTENSIONS ���ã�������չ
EXTENSIONS = {
    # 'scrapy.extensions.telnet.TelnetConsole': None,
    'companyNews.extensions.RedisSpiderSmartIdleClosedExensions': 500,
}
# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
# ע��:�Զ���pipeline�����ȼ������Redispipeline,��ΪRedisPipeline���᷵��item,
# �������RedisPipeline���ȼ������Զ���pipeline,��ô�Զ���pipeline�޷���ȡ��item
ITEM_PIPELINES = {
     #���������Ŀ��redis���д���# ��RedisPipelineע�ᵽpipeline�����(�������ܽ����ݴ���Redis)
    # 'scrapy_redis.pipelines.RedisPipeline': 400,
    'companyNews.pipelines.companyNewsPipeline': 300,# �Զ���pipeline�����ѡ����ע��(��ѡ)
}
# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings


# ----------------scrapyĬ���Ѿ��Դ��˻��棬��������-----------------
# �򿪻���
#HTTPCACHE_ENABLED = True
# ���û������ʱ�䣨��λ���룩
#HTTPCACHE_EXPIRATION_SECS = 0
# ����·��(Ĭ��Ϊ��.scrapy/httpcache)
#HTTPCACHE_DIR = 'httpcache'
# ���Ե�״̬��
#HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPERROR_ALLOWED_CODES = [302, 301]
# ����ģʽ(�ļ�����)
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'



#-----------------Scrapy-Redis�ֲ�ʽ���������������--------------------------
# Enables scheduling storing requests queue in redis.
#����Redis���ȴ洢������У�ʹ��Scrapy-Redis�ĵ�����,����ʹ��scrapy�ĵ�����
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

# Ensure all spiders share same duplicates filter through redis.
#ȷ�����е�����ͨ��Redisȥ�أ�ʹ��Scrapy-Redis��ȥ�����,����ʹ��scrapy��ȥ�����
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# Ĭ���������л�ʹ�õ���pickle �������ǿ��Ը���Ϊ�������Ƶġ�PS���������2.X�Ŀ����á�3.X�Ĳ�����
# SCHEDULER_SERIALIZER = "scrapy_redis.picklecompat"

# ʹ�����ȼ������������ ��Ĭ��ʹ�ã���
# ʹ��Scrapy-Redis�Ĵ����󼯺���ȡ������ķ�ʽ,���ַ�ʽ����һ����:
# �ֱ�(1)��������ȼ�/(2)����FIFO/(�Ƚ��ȳ�)(3)ջFILO ȡ�������Ƚ������
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.PriorityQueue'
# ��ѡ�õ���������
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.FifoQueue'
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.LifoQueue'

# Don't cleanup redis queues, allows to pause/resume crawls.
#�����Redis���С�����������ͣ/�ָ� ��ȡ��
# ������ͣ,redis�����¼���ᶪʧ(�������治����ͷ��ȡ��������ҳ��)
#SCHEDULER_PERSIST = True



#----------------------redis�ĵ�ַ����-------------------------------------
# Specify the full Redis URL for connecting (optional).
# If set, this takes precedence over the REDIS_HOST and REDIS_PORT settings.
# ָ����������redis��URL����ѡ��
# ������ô����������ȼ��������õ�REDIS_HOST �� REDIS_PORT
# REDIS_URL = 'redis://root:����@�����ɣ�:�˿�'
# REDIS_URL = 'redis://root:123456@192.168.8.30:6379'
REDIS_URL = 'redis://root:%s@%s:%s'%(password_redis,host_redis,port_redis)
# �Զ����redis���������ӳ�ʱ֮��ģ�
REDIS_PARAMS={'db': db_redis}
# Specify the host and port to use when connecting to Redis (optional).
# ָ�����ӵ�redisʱʹ�õĶ˿ں͵�ַ����ѡ��
#REDIS_HOST = '127.0.0.1'
#REDIS_PORT = 6379
#REDIS_PASS = '19940225'


#-----------------------------------------��ʱ�ò���-------------------------------------------------------
# �������˽�������ץȡ����ַ�ĳ���ΪURL������ޣ�Ĭ��ֵ��2083
# URLLENGTH_LIMIT=2083
# ��ȡ��վ�����������(depth)ֵ,Ĭ��ֵ0�����Ϊ0����û������
# DEPTH_LIMIT = 3
# ����ֵ�����ڸ�����ȵ���request���ȼ������Ϊ0���򲻸�����Ƚ������ȼ�������
# DEPTH_PRIORITY=3

# ������ʱ���ֹ�ֲ�ʽ������Ϊ�ȴ����ر�
# ��ֻ�е��������õĶ�������SpiderQueue��SpiderStackʱ����Ч
# ���ҵ�����֩���״�����ʱ��Ҳ���ܻ���ֹͬһʱ�����������ڶ���Ϊ�գ�
# SCHEDULER_IDLE_BEFORE_CLOSE = 10

# ���л���Ŀ�ܵ���Ϊredis Key�洢
# REDIS_ITEMS_KEY = '%(spider)s:items'

# Ĭ��ʹ��ScrapyJSONEncoder������Ŀ���л�
# You can use any importable path to a callable object.
# REDIS_ITEMS_SERIALIZER = 'json.dumps'

# �Զ���redis�ͻ�����
# REDIS_PARAMS['redis_cls'] = 'myproject.RedisClient'

# ���ΪTrue����ʹ��redis��'spop'���в�����
# �����Ҫ������ʼ��ַ�б�����ظ������ѡ��ǳ����á�������ѡ��urls����ͨ��sadd��ӣ������������ʹ���
# REDIS_START_URLS_AS_SET = False

# RedisSpider��RedisCrawlSpiderĬ�� start_usls ��
# REDIS_START_URLS_KEY = '%(name)s:start_urls'

# ����redisʹ��utf-8֮��ı���
# REDIS_ENCODING = 'latin1'

# Disable Telnet Console (enabled by default)
# �������Ƿ�����telnetconsole,Ĭ��ֵ��True
#TELNETCONSOLE_ENABLED = False

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
# ��ʼ����ʱ���ٲ��ӳ�ʱ��
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#�߲�������ʱ����ӳ�ʱ��
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

"""
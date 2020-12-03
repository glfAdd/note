""" ============================ 参考
https://www.cnblogs.com/xiugeng/p/10090033.html
https://blog.csdn.net/lm_is_dc/article/details/81057811

Scrapy 是一个通用的爬虫框架，但是不支持分布式，Scrapy-redis是为了更方便地实现Scrapy分布式爬取，而提供了一些以redis为基础的组件
"""

""" ============================ dsfafd 
1. 继承 RedisSpider
from scrapy_redis.spiders import RedisSpider 
class WangyiSpider(RedisSpider):
    pass
    
2. redis_key代替start_urls, 表示调度器队列的名称
redis_key = 'wangyi'


3. redis数据库配置文件redis.conf配置
# 不注释时，只允许本机的客户端连接
# bind 127.0.0.1
# yes改为no，关闭redis的保护模式，客户端可以对服务器进行读写操作
protected-mode  no


4. 设置settings.py
REDIS_HOST = '192.168.31.31'
REDIS_PORT = 6379
REDIS_ENCODING = 'utf-8'
REDIS_PARAMS = {'password':'123456'} 


5. 使用scrapy-redis组件中封装好的管道
使用scrapy-redis组件中封装好的可以被共享的管道。
可以将每台机器爬取到的数据存储通过该管道存储到redis数据库中，从而实现了多台机器的管道共享。
# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    # 'wangyiPro.pipelines.WangyiproPipeline': 300,
    'scrapy_redis.pipelines.RedisPipeline': 400,
}



6. 使用scrapy-redis组件中封装好的调度器
# 使用scrapy-redis组件的去重队列
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# 使用scrapy-redis组件自己的调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"   # 核心配置
# 是否允许暂停
SCHEDULER_PERSIST = True   # 值为True表示：宕机恢复服务时，从宕机的那个地方开始爬取，不用从头开始


7. 启动项目
启动 redis
启动爬虫
将起始url扔到调度器队列( 写入 redis)

"""

""" ============================ dsfafd """

""" ============================ dsfafd """

""" ============================ dsfafd """

""" ============================ dsfafd """

""" ============================ dsfafd """

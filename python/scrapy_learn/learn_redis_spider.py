""" ============================ �ο�
https://www.cnblogs.com/xiugeng/p/10090033.html
https://blog.csdn.net/lm_is_dc/article/details/81057811

Scrapy ��һ��ͨ�õ������ܣ����ǲ�֧�ֲַ�ʽ��Scrapy-redis��Ϊ�˸������ʵ��Scrapy�ֲ�ʽ��ȡ�����ṩ��һЩ��redisΪ���������
"""

""" ============================ dsfafd 
1. �̳� RedisSpider
from scrapy_redis.spiders import RedisSpider 
class WangyiSpider(RedisSpider):
    pass
    
2. redis_key����start_urls, ��ʾ���������е�����
redis_key = 'wangyi'


3. redis���ݿ������ļ�redis.conf����
# ��ע��ʱ��ֻ�������Ŀͻ�������
# bind 127.0.0.1
# yes��Ϊno���ر�redis�ı���ģʽ���ͻ��˿��ԶԷ��������ж�д����
protected-mode  no


4. ����settings.py
REDIS_HOST = '192.168.31.31'
REDIS_PORT = 6379
REDIS_ENCODING = 'utf-8'
REDIS_PARAMS = {'password':'123456'} 


5. ʹ��scrapy-redis����з�װ�õĹܵ�
ʹ��scrapy-redis����з�װ�õĿ��Ա�����Ĺܵ���
���Խ�ÿ̨������ȡ�������ݴ洢ͨ���ùܵ��洢��redis���ݿ��У��Ӷ�ʵ���˶�̨�����Ĺܵ�����
# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    # 'wangyiPro.pipelines.WangyiproPipeline': 300,
    'scrapy_redis.pipelines.RedisPipeline': 400,
}



6. ʹ��scrapy-redis����з�װ�õĵ�����
# ʹ��scrapy-redis�����ȥ�ض���
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# ʹ��scrapy-redis����Լ��ĵ�����
SCHEDULER = "scrapy_redis.scheduler.Scheduler"   # ��������
# �Ƿ�������ͣ
SCHEDULER_PERSIST = True   # ֵΪTrue��ʾ��崻��ָ�����ʱ����崻����Ǹ��ط���ʼ��ȡ�����ô�ͷ��ʼ


7. ������Ŀ
���� redis
��������
����ʼurl�ӵ�����������( д�� redis)

"""

""" ============================ dsfafd """

""" ============================ dsfafd """

""" ============================ dsfafd """

""" ============================ dsfafd """

""" ============================ dsfafd """

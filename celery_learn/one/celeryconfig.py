# BROKER_URL = 'amqp://guest:guest@localhost:5672/web_develop' # 使用RabbitMQ作为消息代理

BROKER_URL = 'redis://localhost:6379/1'  # 把任务结果存在了Redis
CELERY_RESULT_BACKEND = 'redis://localhost:6379/2'  # 把任务结果存在了Redis
CELERY_TASK_SERIALIZER = 'msgpack'  # 任务序列化和反序列化使用msgpack方案
CELERY_RESULT_SERIALIZER = 'json'  # 读取任务结果一般性能要求不高，所以使用了可读性更好的JSON
CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24  # 任务过期时间，不建议直接写86400，应该让这样的magic数字表述更明显
CELERY_ACCEPT_CONTENT = ['json', 'msgpack']  # 指定接受的内容类型

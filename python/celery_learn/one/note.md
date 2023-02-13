https://www.cnblogs.com/cwp-bg/p/8759638.html


为什么使用

##### 是什么

Python 语言实现的分布式队列服务，除了支持即时任务，还支持定时任务

##### 网址

https://zhuanlan.zhihu.com/p/22304455

##### 场景

- Web应用。当用户触发的一个操作需要较长时间才能执行完成时，可以把它作为任务交给Celery去异步执行，执行完再返回给用户。这段时间用户不需要等待，提高了网站的整体吞吐量和响应时间。
- 定时任务。生产环境经常会跑一些定时任务。假如你有上千台的服务器、上千种任务，定时任务的管理很困难，Celery可以帮助我们快速在不同的机器设定不同种任务。
- 同步完成的附加工作都可以异步完成。比如发送短信/邮件、推送消息、清理/设置缓存等。

# 架构

##### 组件

- Producer：调用了Celery提供的API、函数或者装饰器而产生任务并交给任务队列处理的都是任务生产者。
- Beat：一个定时任务调度器，它会根据配置定时将任务发送给 Broker，等待 Worker 来消费。
- Worker：任务的消费者，它会实时地监控队列中有没有任务，如果有就立即取出来执行
- Broker：消息代理，或者叫作消息中间件，接受任务生产者发送过来的任务消息，存进队列再按序分发给任务消费方（通常是消息队列或者数据库）。
- Backend：用于保存任务的执行结果。Celery默认已支持Redis、RabbitMQ、MongoDB、Django ORM、SQLAlchemy等方式。

##### 消息代理

Celery目前支持RabbitMQ、Redis、MongoDB、Beanstalk、SQLAlchemy、Zookeeper等作为消息代理，但适用于生产环境的只有RabbitMQ和Redis，其他的方式，一是支持有限，二是可能得不到更好的技术支持。

Celery官方推荐的是RabbitMQ，Celery的作者Ask  Solem  Hoel最初在VMware就是为RabbitMQ工作的，Celery最初的设计就是基于RabbitMQ，所以使用RabbitMQ会非常稳定，如果使用Redis，则需要能接受发生突然断电之类的问题造成Redis突然终止后的数据丢失等后果。

##### 序列化

在客户端和消费者之间传输数据需要序列化和反序列化

- pickle: pickle是Python标准库中的一个模块，支持Python内置的数据结构，但是它是 Python的专有协议。从Celery3.2开始，由于安全性等原因Celery将拒绝pickle这个方案
- json: 支持多种语言，可用于跨语言方案
- yaml: yaml的表达能力更强，支持的数据类型比json多，但是Python客户端的性能不如JSON
- msgpack: msgpack是一个二进制的类json的序列化方案，但是比json的数据结构更小、更快

##### 方案

- 选择RabbitMQ作为消息代理
- RabbitMQ的Python客户端选择librabbitmq这个C库
- 选择Msgpack做序列化
- 选择Redis做结果存储

##### 配置文件

```python
# 注意，celery4版本后，CELERY_BROKER_URL改为BROKER_URL
# BROKER_URL = 'amqp://username:password@localhost:5672/yourvhost'
BROKER_URL = 'amqp://dongwm:123456@localhost:5672/web_develop'
# 把任务结果存在了Redis
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
# 任务序列化和反序列化使用msgpack方案
CELERY_TASK_SERIALIZER = 'msgpack'
# 读取任务结果一般性能要求不高，所以使用了可读性更好的JSON
CELERY_RESULT_SERIALIZER = 'json'
# 任务过期时间，不建议直接写86400，应该让这样的magic数字表述更明显
CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24
# 指定接受的内容类型
CELERY_ACCEPT_CONTENT = ['json', 'msgpack']
# 任务发送完成是否需要确认，这一项对性能有一点影响
CELERY_ACKS_LATE = True
# 压缩方案选择，可以是zlib, bzip2，默认是发送没有压缩的数据
CELERY_MESSAGE_COMPRESSION = 'zlib'
# 规定完成任务的时间
CELERYD_TASK_TIME_LIMIT = 5  # 在5s内完成任务，否则执行该任务的worker将被杀死，任务移交给父进程
# celery worker的并发数，默认是服务器的内核数目,也是命令行-c参数指定的数目
CELERYD_CONCURRENCY = 4
# celery worker 每次去rabbitmq预取任务的数量
CELERYD_PREFETCH_MULTIPLIER = 4
# 每个worker执行了多少任务就会死掉，默认是无限的
CELERYD_MAX_TASKS_PER_CHILD = 40
# 设置默认的队列名称，如果一个消息不符合其他的队列就会放在默认队列里面，如果什么都不设置的话，数据都会发送到默认的队列中
CELERY_DEFAULT_QUEUE = "default"

# 定义任务队列. 通常它会使用默认的名为celery的队列（可以通过CELERY_DEFAULT_QUEUE修改）用来存放任务。我们可以使用优先级不同的队列来确保高优先级的任务不需要等待就得到响应。
CELERY_QUEUES = (
    # 路由键以“task.”开头的消息都进default队列
    Queue('default', routing_key='task.#'),
    # 路由键以“web.”开头的消息都进web_tasks队列
    Queue('web_tasks', routing_key='web.#'),
)
# 默认的交换机名字为tasks
CELERY_DEFAULT_EXCHANGE = 'tasks'
# 默认的交换类型是topic
CELERY_DEFAULT_EXCHANGE_TYPE = 'topic'
# 默认的路由键是task.default，这个路由键符合上面的default队列
CELERY_DEFAULT_ROUTING_KEY = 'task.default'
CELERY_ROUTES = {
    # tasks.add的消息会进入web_tasks队列
    'projq.tasks.add': {
        'queue': 'web_tasks',
        'routing_key': 'web.add',
    }
}

# CELERYBEAT_SCHEDULE中指定了tasks.add这个任务每10秒跑一次，执行的时候的参数是16和16
CELERYBEAT_SCHEDULE = {
    'add': {
        'task': 'projb.tasks.add',
        'schedule': timedelta(seconds=10),
        'args': (16, 16)
    }
}

```

##### 指定队列



```python

```

##### 安装

```
pip install "celery[librabbitmq,redis,msgpack]"
```
















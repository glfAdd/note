"""
1. app.task装饰add函数成一个Task实例，add.delay函数将task实例序列化后，通过librabbitmq库的方法将任务发送到rabbitmq
2. 该过程创建一个名字为celery的exchange交换机，类型为direct（直连交换机）;创建一个名为celery的queue，队列和交换机使用路由键celery绑定
3. 打开rabbitmq管理后台，可以看到有一条消息已经在celery队列中
4. 任务执行完毕后结果存储在redis中，查看redis中的数据，发现存在一个string类型的键值对

当有多个装饰器的时候，app.task一定要在最外层
如果使用redis作为任务队列中间人，在redis中存在两个键 celery和_kombu.binding.celery
    _kombu.binding.celery表示有一名为 celery 的任务队列（Celery 默认）
    celery为默认队列中的任务列表，使用list类型，可以看看添加进去的任务数据。



启动程序
celery -A app.celery_tasks.celery worker -Q queue --loglevel=info
-A 创建的celery对象的位置，该app.celery_tasks.celery指的是app包下面的celery_tasks.py模块的celery实例，注意一定是初始化后的实例，后面加worker表示该实例就是任务执行者；
-Q worker接收指定的队列的任务，这是为了当多个队列有不同的任务时可以独立；如果不设会接收所有的队列的任务；
-l worker输出的日志级别



 -------------- celery@bogon v4.3.0 (rhubarb)
---- **** -----
--- * ***  * -- Darwin-18.6.0-x86_64-i386-64bit 2019-07-11 17:30:36
-- * - **** ---
- ** ---------- [config]
- ** ---------- .> app:         tasks:0x10f9ca438                                           celery实例
- ** ---------- .> transport:   redis://localhost:6379/0                                    broker
- ** ---------- .> results:     disabled://                                                 backend没开启
- *** --- * --- .> concurrency: 4 (prefork)
-- ******* ---- .> task events: OFF (enable -E to monitor tasks in this worker)
--- ***** -----
 -------------- [queues]
                .> celery           exchange=celery(direct) key=celery


[tasks]
  . task.send_mail                                                                          任务列表

"""
from main import app


@app.task
def add(x, y):
    return x + y

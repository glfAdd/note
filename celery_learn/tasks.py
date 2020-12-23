"""
启动Worker来监听Broker中是否有任务
    celery -A tasks worker --loglevel=info
    -A 指定 celery 实例在哪个模块中，例子中，celery实例在tasks.py文件中



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
from celery import Celery

# 创建Celery实例
app = Celery('tasks', broker='redis://localhost:6379/1')


# 创建任务. 函数用app.task 装饰器修饰之后，就会成为Celery中的一个Task
@app.task
def send_mail(email):
    print("send mail to ", email)
    import time
    time.sleep(5)
    return "success"

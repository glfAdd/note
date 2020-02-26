"""
将任务发送给 Broker， 而不是真正执行该任务


"""
from celery_learn.tasks import send_mail
import time
import json


def register():
    start = time.time()
    print("1. 插入记录到数据库")
    print("2. celery 帮我发邮件")
    send_mail.delay("xx@gmail.com")
    # send_mail("xx@gmail.com")
    print("3. 告诉用户注册成功")
    print("耗时：%s 秒 " % (time.time() - start))


if __name__ == '__main__':
    register()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pika
import time

credentials = pika.PlainCredentials('admin', '123456')
connection = pika.BlockingConnection(pika.ConnectionParameters('132.232.134.232', 5672, '/', credentials))


def product():
    # 用户密码
    # 在连接上创建一个频道
    channel = connection.channel()
    # 声明一个队列，生产者和消费者都要声明一个相同的队列，用来防止万一某一方挂了，另一方能正常运行
    channel.queue_declare(queue='balance')
    # exchange:     交换机
    # routing_key:  将消息发往哪个队列
    # body:         消息内容
    while True:
        channel.basic_publish(exchange='', routing_key='balance', body='Hello World!')
        print(" [x] Sent 'Hello World!'")
        time.sleep(3)
    # 当生产者发送完消息后，可选择关闭连接
    connection.close()


product()

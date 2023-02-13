#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pika

credentials = pika.PlainCredentials('admin', '123456')
connection = pika.BlockingConnection(pika.ConnectionParameters('132.232.134.232', 5672, '/', credentials))


def cumtomer():
    channel = connection.channel()
    channel.queue_declare(queue='balance')
    channel.basic_consume(callback, queue='balance', no_ack=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


def callback(ch, method, properties, body):
    print 'ch=======%s' % ch
    print 'method=======%s' % method
    print 'properties======%s' % properties
    print(" [x] Received %r" % body)


cumtomer()

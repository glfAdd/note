### RabbitMQ

- python队列内置有两种
- 

线程queue同一个进程下的线程间



```python
python队列内置有两种，线程queue同一个进程下的线程间，进程Queue同一个进程下的线程间或者父进程与子进程之间进行队列通讯,并不能进行程序与程序之间的信息交换，这时候我们就需要一个中间件，来实现程序之间的通讯.用于在分布式系统中存储转发消息，在易用性、扩展性、高可用性等方面表现不俗。

息中间件最主要的作用是解耦，中间件最标准的用法是生产者生产消息传送到队列，消费者从队列中拿取消息并处理，生产者不用关心是谁来消费，消费者不用关心谁在生产消息，从而达到解耦的目的。在分布式的系统中，消息队列也会被用在很多其它的方面，比如：分布式事务的支持，RPC的调用等等

RabbitMQ主要是为了实现系统之间的双向解耦而实现的。当生产者大量产生数据时，消费者无法快速消费，那么需要一个中间层。保存这个数据

AMQP，即Advanced Message Queuing Protocol，高级消息队列协议，是应用层协议的一个开放标准，为面向消息的中间件设计。消息中间件主要用于组件之间的解耦，消息的发送者无需知道消息使用者的存在，反之亦然。AMQP的主要特征是面向消息、队列、路由（包括点对点和发布/订阅）、可靠性、安全。

通常我们谈到队列服务, 会有三个概念： 发消息者、队列、收消息者，RabbitMQ 在这个基本概念之上, 多做了一层抽象, 在发消息者和 队列之间, 加入了交换器 (Exchange). 这样发消息者和队列就没有直接联系, 转而变成发消息者把消息给交换器, 交换器根据调度策略再把消息再给队列。


```

- 虚拟主机：一个虚拟主机持有一组交换机、队列和绑定。用户只能在虚拟主机控制，如果需要禁止A组访问B组的交换机/队列/绑定，必须为A和B分别创建一个虚拟主机。每一个RabbitMQ服务器都有一个默认的虚拟主机“/”。
- 交换机：Exchange 用于转发消息，但是它不会做存储 ，如果没有 Queue bind 到 Exchange 的话，它会直接丢弃掉 Producer 发送过来的消息。
- 路由键 : 消息到交换机的时候，交换机根据该路由键转发到对应的队列中
- 绑定：也就是交换机需要和队列相绑定, 可以是多对多的关系。

##### 交换机(Exchange)

交换机的功能主要是接收消息并且转发到绑定的队列，交换机不存储消息，在启用ack模式后，交换机找不到队列会返回错误。交换机有四种类型:Direct, Topic, Headers, Fanout

- Headers：设置header attribute参数类型的交换机
- Fanout：转发消息到所有绑定队列

##### Direct Exchange

默认的交换机模式, 根据key全文匹配去寻找队列, 在绑定时设定一个routing_key, 消息的routing_key 匹配时, 才会被交换器投送到绑定的队列中去

##### Topic Exchange

转发消息主要是根据通配符。 队列和交换机的绑定会定义一种路由模式，通配符就要在这种路由模式和路由键之间匹配后交换机才能转发消息

- 路由键必须是一串字符，用句号（.） 隔开，比如说 agreements.us，或者 agreements.eu.stockholm 
- 路由模式必须包含一个 星号（\*），主要用于匹配路由键指定位置的一个单词，比如说，一个路由模式是这样子：agreements..b.*，那么就只能匹配路由键是这样子的：第一个单词是 agreements，第四个单词是 b。 
- 井号（#）就表示相当于一个或者多个单词，例如一个匹配模式是agreements.eu.berlin.#，那么，以agreements.eu.berlin开头的路由键都是可以的。

```python
rabbitTemplate.convertAndSend("testTopicExchange","key1.a.c.key2", " this is  RabbitMQ!");
```

##### Headers Exchange

headers 也是根据规则匹配, 相较于 direct 和 topic 固定地使用 routing_key , headers 则是一个自定义匹配规则的类型.
在队列与交换器绑定时, 会设定一组键值对规则, 消息中也包括一组键值对( headers 属性), 当这些键值对有一对, 或全部匹配时, 消息被投送到对应队列.

##### Fanout Exchange

消息广播的模式，不管路由键或者是路由模式，会把消息发给绑定给它的全部队列，如果配置了routing_key会被忽略。

##### 安装

```python
# 下载RabbitMQ的rpm
wget http://www.rabbitmq.com/releases/rabbitmq-server/v3.6.6/rabbitmq-server-3.6.6-1.el6.noarch.rpm
# 安装rabbitmq
yum -y install rabbitmq-server-3.6.6-1.el6.noarch.rpm
# 前台运行
rabbitmq-server start 
# 后台运行
rabbitmq-server -detached
# 启动web管理界面
rabbitmq-plugins enable rabbitmq-management
# 增加访问用户
rabbitmqctl add_user admin 123456
# 设置角色
rabbitmqctl set_user_tags admin administrator
# 设置默认vhost（”/”）访问权限
rabbitmqctl set_permissions -p "/" admin "." "." ".*"
# 浏览器访问
http://132.232.134.232:15672
# MQ服务器中查看队列状态
rabbitmqctl list_queues
# 重启
sudo service rabbitmq-server restart
```

##### pika

```python
# 安装
sudo pip install pika
# https://www.cnblogs.com/kerwinC/p/5967584.html




```

##### 轮询消费模式

此模式下，发送队列的一方把消息存入mq的指定队列后，若有消费者端联入相应队列，即会获取到消息，并且队列中的消息会被消费掉。若有多个消费端同时连接着队列，则会已轮询的方式将队列中的消息消费掉

```python
# ------------------------生产者------------------------
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
    # routing_key:  路由键, 将消息发往哪个队列
    # body:         消息内容
    while True:
        channel.basic_publish(exchange='', routing_key='balance', body='Hello World!')
        print(" [x] Sent 'Hello World!'")
        time.sleep(3)
    # 当生产者发送完消息后，可选择关闭连接
    connection.close()


product()
# ------------------------消费者------------------------
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
```

##### 队列持久化

当rabbitMQ意外宕机时，可能会有持久化保存队列的需求（队列中的消息不消失）。

```python
channel.basic_publish(exchange='', routing_key='durable', body='Hello cheng!', properties=pika.BasicProperties(delivery_mode=2, ))




```



##### 广播模式

当producer发送消息到队列后，所有的consumer都会收到消息，需要注意的是，此模式下producer与concerned之间的关系类似与广播电台与收音机，如果广播后收音机没有接受到，那么消息就会丢失。

```python



```



https://www.cnblogs.com/ityouknow/p/6120544.html
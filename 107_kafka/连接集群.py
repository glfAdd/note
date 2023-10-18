# -* coding:utf8 *-

from kafka import KafkaConsumer

consumer = KafkaConsumer("123", bootstrap_servers=["10.135.2.39:9092", "10.135.2.39:9093", "10.135.2.49:9092", "10.135.2.49:9093", "10.135.2.22:9092",
                                                   "10.135.2.22:9093"])
for message in consumer:
    a = message.topic
    print(11111111111111)
    # print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,message.offset, message.key,

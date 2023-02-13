from kafka import KafkaConsumer
import json


def commit_callback(*args, **kwargs):
    print('back')
    print(args)
    print(kwargs)


consumer = KafkaConsumer(
    'my_favorite_topic2',
    bootstrap_servers=['172.18.0.12:9092'],
    enable_auto_commit=False,
    auto_offset_reset='earliest',
    group_id='test1'
)
# print(consumer.beginning_offsets)
print(consumer.assignment())
for msg in consumer:
    # print(msg.value.decode('utf-8'))
    print(json.loads(msg.value.decode('utf-8')))
    consumer.commit_async(callback=commit_callback)

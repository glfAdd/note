"""
pip install kafka-python

"""

from kafka import KafkaProducer
import json

# 简单生产者
producer = KafkaProducer(bootstrap_servers=['172.18.0.12:9092'])
a = {'name': '小明', 'age': 10}
future = producer.send('my_favorite_topic2', key=b'my_key', value=json.dumps(a).encode('utf-8'), partition=0)
result = future.get(timeout=10)
print(result)

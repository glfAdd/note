# -*- coding: utf-8 -*-
from pymongo import MongoClient

client = MongoClient(host='127.0.0.1', port=27017)
client.school.teacher.insert_one({'name': '张三'})
client.school.teacher.insert_many([
    {'name': '赵四'},
    {'name': '刘能'}
])

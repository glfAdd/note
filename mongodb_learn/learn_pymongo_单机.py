# -*- coding: utf-8 -*-

""" ============================ 参考
https://www.cnblogs.com/melonjiang/p/6536876.html
"""

from pymongo import MongoClient

client = MongoClient(host='10.211.55.11', port=27017)  # 建立客户端对象
# 如果设置了用户名和密码
# client.admin.authenticate('admin', '123456789')

# 连接mydb数据库，没有则自动创建
db = client.mydb

# 使用test_set集合，没有则自动创建
my_set = db.testset

""" ============================ insert_one / insert_many """
my_set.insert_one({"name": "zhangsan", "age": 8})
my_set.insert_many([
    {"name": "zhangsan", "age": 30},
    {'name': '刘能'}
])
my_set.insert_one({"name": "zhangsan", "age": 1, 'sex': '1'})

""" ============================ find_one / find 
find({}, {})
    第一个{}: 查询所有
    第二个{}: 条件
    find({},{'_id':0,'name':1,'flag':1})
没有返回None, 有返回迭代器
"""
for i in my_set.find():
    print(i)

for i in my_set.find({'name': '123', 'age': 4}):
    print(i)

""" ============================ update_one / update_many """
# 把name为zhangsan的age更新为200
my_set.update_one({"name": "zhangsan"}, {'$set': {"age": 200}})
my_set.update_many({"name": "zhangsan"}, {'$set': {"age": 200}})

""" ============================ delete_one / delete_many """
my_set.delete_one({'name': '赵四'})
my_set.delete_many({'name': '赵四'})

""" ============================ 比较运算符 
$gt     大于
$lt     小于
$gte    大于等于
$lte    小于等于
"""
for i in my_set.find({"age": {"$gt": 20}}):
    print(i)

""" ============================ 排序 
1 为升序，-1为降序
"""
for i in my_set.find().sort([("age", 1)]):
    print(i)

""" ============================ limit / skip 
limit() 方法用来读取指定数量的数据
skip()  方法用来跳过指定数量的数据
"""
# 下面表示跳过2条数据后读取6条
for i in my_set.find().skip(2).limit(6):
    print(i)

""" ============================ IN / OR /  all 

"""
for i in my_set.find({"age": {"$in": (20, 30, 35)}}):
    print(i)

for i in my_set.find({"$or": [{"age": 20}, {"age": 35}]}):
    print(i)

dic = {"name": "lisi", "age": 18, "li": [1, 2, 3]}
dic2 = {"name": "zhangsan", "age": 18, "li": [1, 2, 3, 4, 5, 6]}
my_set.insert(dic)
my_set.insert(dic2)
for i in my_set.find({'li': {'$all': [1, 2, 3, 4]}}):
    print(i)

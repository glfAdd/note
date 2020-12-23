# -*- coding: utf-8 -*-
import pymongo

""" ============================

isinstance

shard_key

https://blog.csdn.net/xiaominggunchuqu/article/details/79916504

分片集群
https://blog.csdn.net/sinat_40438972/article/details/80104797?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task

mongodb://[username:password@]host1[:port1][,host2[:port2],…[,hostN[:portN]]][/[database][?options]]

"""

""" ============================ 123123 """

""" ============================ 123123 """

""" ============================ 123123 """

""" ============================ 123123 """

""" ============================ 123123 """

""" ============================ 123123 """

""" ============================ 123123 """

from pymongo import MongoClient

client = MongoClient('mongodb://hezhiguo:naxions2019.com@39.105.116.74,39.105.121.133,39.105.122.238/admin?readPreference=secondaryPreferred')
print(client.list_database_names())
db = client.work_weixin_msg
print(client.list_database_names())




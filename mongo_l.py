# -*-coding:utf-8 -*-
import pandas as pd
from pymongo import MongoClient


def shard_handler(shard_key, indx='hashed', unique=False, background=True):
    """
    indx : text, hashed, 1
    处理一切与分片相关的操作
    """
    mongo_db_name = "haodf_com"
    mongo_col_name = "haodf_doctor_info"
    mongo_uri = "mongodb://hezhiguo:naxions2019.com@39.105.122.238,39.105.116.74,39.105.121.133/admin?readPreference=secondaryPreferred&w=majority&connectTimeoutMS=3000&socketTimeoutMS=60000"
    m = MongoClient(mongo_uri)
    shard_type = indx
    if isinstance(shard_key, str):
        shard_key = shard_key
        key = {shard_key: shard_type}
        if shard_key != "_id":
            m[mongo_db_name][mongo_col_name].create_index([(shard_key, shard_type)], unique=unique,
                                                          background=background)
    elif isinstance(shard_key, list) or isinstance(shard_key, tuple):
        li = []
        key = {}
        for i in shard_key:
            key.update({i: shard_type})
            li.append((i, shard_type))
        m[mongo_db_name][mongo_col_name].create_index(li, unique=unique, background=background)
    else:
        assert "shard_key must be str、list or tuple"
        return

    db_col_path = "{}.{}".format(mongo_db_name, mongo_col_name)
    __adminDb = m['admin']
    __adminDb.command("enablesharding", mongo_db_name)
    __adminDb.command("shardcollection", db_col_path, key=key)


def run():
    mongo_db_name = "gaode_com"
    mongo_col_name = "gaode_hospital"
    mongo_uri = "mongodb://hezhiguo:naxions2019.com@39.105.122.238,39.105.116.74,39.105.121.133/admin?readPreference=secondaryPreferred&w=majority&connectTimeoutMS=3000&socketTimeoutMS=60000"
    m = MongoClient(mongo_uri)
    res = m[mongo_db_name][mongo_col_name].find({'hospital_province': '山东省'})
    li = []
    l, t = 0, 0
    for i in res:
        if '天和堂' in i['hospital_name']:
            del i['_id']
            li.append(i)
            t += 1
        if '立健' in i['hospital_name']:
            del i['_id']
            li.append(i)
            l += 1
    if li:
        pf = pd.DataFrame(li)
        pf.to_excel("lvgu_hospital.xlsx")
        print(l)
        print(t)


if __name__ == '__main__':
    run()

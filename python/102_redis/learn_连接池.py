import redis

"""
通过预先创建多个连接, 当进行redis操作时, 直接获取已经创建的连接进行操作, 而且操作完成后, 不会释放, 用于后续的其他redis操作，这样就达到了避免频繁的redis连接创建和释放的目的, 从而提高性能。
redis模块采用ConnectionPool来管理对redis server的所有连接



"""

# 创建连接池
pool = redis.ConnectionPool(host='127.0.0.1', port=6379, max_connections=10)
# 从池子中拿一个链接
conn = redis.Redis(connection_pool=pool, decode_responses=True)
print(conn.get('name').decode('utf-8'))

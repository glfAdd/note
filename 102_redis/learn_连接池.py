import redis

# 创建连接池
pool = redis.ConnectionPool(host='127.0.0.1', port=6379, max_connections=10)
# 从池子中拿一个链接
conn = redis.Redis(connection_pool=pool, decode_responses=True)
print(conn.get('name').decode('utf-8'))

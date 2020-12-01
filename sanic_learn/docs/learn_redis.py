"""

https://aredis.readthedocs.io/en/latest/
https://pypi.org/project/aredis/1.0.3/



https://littlerpl.me/2019/10/29/StrictRedis/




aredis: 支持集群, 速度比 asyncio_redis 快

StrictRedis 和 StrictRedisCluster 内部支持连接池


decode_responses=True，写入的键值对中的value为str类型，不加这个参数写入的则为字节类型



"""

"""
单点
"""
import asyncio
import aredis
from aredis import StrictRedis, StrictRedisCluster


async def single():
    client = StrictRedis(host='172.17.0.2', port=6379, db=0)
    await client.flushdb()
    await client.set('foo', 1)
    assert await client.exists('foo') is True
    await client.incr('foo', 100)

    assert int(await client.get('foo')) == 101
    await client.expire('foo', 1)
    await asyncio.sleep(0.1)
    await client.ttl('foo')
    await asyncio.sleep(1)
    assert not await client.exists('foo')


"""
集群
"""


async def cluster():
    client = StrictRedisCluster(host='172.17.0.2', port=6379)
    await client.flushdb()
    await client.set('foo', 1)
    await client.lpush('a', 1)
    print(await client.cluster_slots())

    await client.rpoplpush('a', 'b')
    assert await client.rpop('b') == b'1'


"""
连接池
"""


async def pool():
    rdb_pool = aredis.ConnectionPool(host='172.17.0.2', port=6379, max_connections=20, db=0)
    r_db = StrictRedis(connection_pool=rdb_pool)
    await r_db.set('foo1', 1)


loop = asyncio.get_event_loop()
loop.run_until_complete(single())
# loop.run_until_complete(cluster())
loop.run_until_complete(pool())

"""

@asyncio.coroutine


"""

import asyncio

import aiomysql


async def test_example(loop):
    pool = await aiomysql.create_pool(
        host='172.17.0.1',
        port=3306,
        user='root',
        password='123456',
        db='learn',
        loop=loop,
        autocommit=False
    )
    async with pool.acquire() as conn:  # 从空闲池获取连接的协程。根据需要创建新连接，并且池的大小小于maxsize。
        async with conn.cursor() as cur:
            await cur.execute("SELECT * from person")
            print(cur.description)
            r = await cur.fetchall()
            print(r)
    pool.close()
    # 等待释放和关闭所有已获取连接的协同程序。应该在close（）之后调用，以等待实际的池关闭。
    await pool.wait_closed()


loop = asyncio.get_event_loop()
loop.run_until_complete(test_example(loop))

"""
数据库连接

文档
https://aiomysql.readthedocs.io/en/latest/




"""

import asyncio

import aiomysql

loop = asyncio.get_event_loop()


async def test_example():
    conn = await aiomysql.connect(host='172.17.0.1', port=3306, user='root', password='123456', db='learn', loop=loop)
    cur = await conn.cursor()
    await cur.execute(""" SELECT * FROM person """)
    print(cur.description)
    r = await cur.fetchall()
    print(r)
    await cur.close()
    conn.close()


loop.run_until_complete(test_example())

"""
异步数据库连接

文档
https://aiomysql.readthedocs.io/en/latest/
"""

import asyncio

import aiomysql

loop = asyncio.get_event_loop()


async def test_select():
    """
    需要执行 fetchall fetchmany fetchone
    耗时的io操作可以使用await来修饰
    """
    # 创建连接
    conn = await aiomysql.connect(host='172.17.0.1', port=3306, user='root', password='123456', db='learn', loop=loop)
    # 获取游标执行sql语句
    cur = await conn.cursor()
    await cur.execute(""" SELECT * FROM person """)
    print(cur.description)
    r = await cur.fetchall()
    print(r)
    await cur.close()
    conn.close()


async def test_insert():
    """
    需要commit rollback
    耗时的io操作可以使用await来修饰
    """
    conn = await aiomysql.connect(host='172.17.0.1', port=3306, user='root', password='123456', db='learn', loop=loop)
    cur = await conn.cursor()
    await cur.execute(""" UPDATE person SET age = 20 WHERE user_name = 'Tom' """)
    cur.commit()
    await cur.close()
    conn.close()


# loop.run_until_complete(test_select())
loop.run_until_complete(test_insert())

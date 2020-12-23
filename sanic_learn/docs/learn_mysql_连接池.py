"""

@asyncio.coroutine


"""

import asyncio

import aiomysql


async def mysql_db_pool():
    """
    创建连接池
    """
    try:
        pool = await aiomysql.create_pool(
            host='172.17.0.1',
            port=3306,
            user='root',
            password='asdf123456',
            db='learn',
            loop=loop,
            autocommit=False,
            minsize=20,
            maxsize=30,
            cursorclass=aiomysql.DictCursor
        )
        return pool
    except Exception as e:
        print(str(e))


async def get_cursor():
    '''
    获取db连接和cursor对象，用于db的读写操作
    '''
    pool = await mysql_db_pool()
    # 连接 commit 和 rollback
    conn = await pool.acquire()
    # 游标执行 sql 语句
    cur = await conn.cursor()
    return conn, cur


async def test_select():
    conn, cur = await get_cursor()
    sql = """ SELECT * FROM person WHERE user_name = %s """
    number = await cur.execute(sql, ('Tom',))
    print(number)
    res = await cur.fetchall()
    print(cur.rowcount)
    print(res)
    conn.close()


async def test_insert():
    conn, cur = await get_cursor()
    data = (
        (11, 'Jack'),
        (45, '小明')
    )
    sql = """ INSERT INTO person ( age, user_name ) VALUES ( %s, %s) """
    await cur.executemany(sql, data)
    print(cur.rowcount)
    await conn.commit()
    conn.close()


loop = asyncio.get_event_loop()
loop.run_until_complete(test_select())
loop.run_until_complete(test_insert())
loop.close()

"""
异步上下文管理器


"""

import asyncio
from contextlib import contextmanager
from datetime import datetime


async def a():
    await asyncio.sleep(3)
    return 'A'


async def b():
    await asyncio.sleep(1)
    return 'B'


async def s1():
    return await asyncio.gather(a(), b())


@contextmanager
def timed(func):
    start = datetime.now()
    yield asyncio.run(func())
    end = datetime.now()
    print(end - start)


if __name__ == '__main__':
    with timed(s1) as aa:
        print(aa)
        print('end')

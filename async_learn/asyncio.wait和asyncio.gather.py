"""
https://www.jianshu.com/p/6872bf356af7?utm_campaign=hugo&utm_medium=reader_share&utm_content=note&utm_source=weixin-friends


1. asyncio.wait 和 asyncio.gather 实现的效果是相同的，都是把所有 Task 任务结果收集起来
2. asyncio.wait 会返回两个值：done 和 pending，done 为已完成的协程 Task，pending 为超时未完成的协程 Task，需通过 future.result 调用 Task 的 result
3. asyncio.gather 返回的是所有已完成 Task 的 result，不需要再进行调用或其他操作，就可以得到全部结果


"""

import asyncio
from datetime import datetime


def current_time():
    cur_time = datetime.now()
    return cur_time


async def do_something(number):
    print('do_something')
    await asyncio.sleep(number)
    return number


""" ============================ wait
async def wait(fs, *, loop=None, timeout=None, return_when=ALL_COMPLETED):
return_when 包含 FIRST_COMPLETED, FIRST_EXCEPTION, ALL_COMPLETED
"""


async def run_wait():
    task_list = []
    for i in range(5):
        task = asyncio.create_task(do_something(i))
        task_list.append(task)

    print('创建task完成')
    done, pending = await asyncio.wait(task_list, timeout=2)
    print('全部task执行完成')
    for i in done:
        print(i.result())
    for i in pending:
        print(i)


def main_wait():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run_wait())


""" ============================ gather 
def gather(*coros_or_futures, loop=None, return_exceptions=False):
    return_exceptions: 返回异常, False抛出异常, True继续执行将异常当作结果返回
"""


async def run_gather():
    task_list = []
    for i in range(5):
        task = asyncio.create_task(do_something(i))
        task_list.append(task)
    print('创建task完成')
    results = await asyncio.gather(*task_list)
    print('全部task执行完成')
    for i in results:
        print(i)


def main_gather():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run_gather())


if __name__ == '__main__':
    main_wait()
    # main_gather()

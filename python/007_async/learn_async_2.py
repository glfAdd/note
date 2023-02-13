"""
多线程(多进程)推荐使用 cocurrent.futures.ThreadPoolExecutor 和 cocurrent.futures.ProcessPoolExecutor 两个池.

一个异步的函数, 有个更标准的称呼, 我们叫它 "协程" (coroutine).

"""

"""


await 后面必须跟一个 awaitable 类型或者具有 __await__ 属性的对象
执行异步函数, 不能用这样的调用方法, 用 asyncio 库中的事件循环机制来启动


"""

import time
import asyncio


def test():
    async def run_1():
        await asyncio.sleep(2)
        print('run_1')

    async def run_2():
        await asyncio.sleep(2)
        print('run_2')

    async def run_3():
        await asyncio.sleep(2)
        print('run_3')

    # 1. 创建一个事件循环
    loop = asyncio.get_event_loop()

    # 2. 将异步函数加入事件队列
    tasks = [
        run_1(),
        run_2(),
        run_3(),
    ]

    # 3. 执行事件队列, 直到最晚的一个事件被处理完毕后结束
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()


test()

"""
官网文档
https://docs.python.org/zh-cn/3/library/asyncio-dev.html#running-blocking-code


1. 异步函数就是携程coroutine
2. 函数前面加上 async 就是异步函数, 函数里面可以使用 await
3. await 后面必须跟一个 awaitable 类型或者具有 __await__ 属性的 对象.
4. sleep() 不是 awaitable, 会导致线程阻塞的 "真性睡眠"
5. 使用asyncio 库的 sleep()
    await asyncio.sleep(3)
6. 异步函数不能直接执行, 需要使用事件循环
    创建一个事件循环
    将异步函数加入事件队列
    执行事件队列, 直到最晚的一个事件被处理完毕后结束
    最后建议用 close() 方法关闭事件循环, 以彻底清理 loop 对象防止误用
"""

import asyncio


def test():
    async def run_1():
        await asyncio.sleep(5)
        print('run 1 over')
        return 'run 1'

    async def run_2():
        await asyncio.sleep(1)
        print('run 2 over')
        return 'run 2'

    async def run_3():
        await asyncio.sleep(1)
        print('run 3 over')
        return 'run 3'

    loop = asyncio.get_event_loop()
    # 第一种
    # task = [
    #     run_1(),
    #     run_2(),
    #     run_3()
    # ]
    # # 等待最晚的一个结束才继续执行
    # loop.run_until_complete(asyncio.wait(task))
    # print('all over 1')

    # 第二种. 遍历task_2获取返回值
    task_2 = [
        loop.create_task(run_1()),
        loop.create_task(run_2()),
        loop.create_task(run_3()),
    ]
    loop.run_until_complete(asyncio.wait(task_2))
    for i in task_2:
                print(i.result())
    print('all over 2')

    loop.close()



def hello():
    pass

test()

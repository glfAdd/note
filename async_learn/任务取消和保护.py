"""
1. 取消任务, 当在事件循环启动前取消一下 task 时， await task 会抛出 CancelledError 异常:
cancel()

2. 保护任务不被取消
shield

3. 使用
    先创建task
    取消任务
    gather/wait
"""

import asyncio


async def a():
    print('begin a')
    await asyncio.sleep(1)
    return 'end a'


async def b():
    print('begin b')
    await asyncio.sleep(2)
    return 'end b'


async def test():
    task_1 = asyncio.shield(a())
    # task_1 = asyncio.create_task(a())
    task_2 = asyncio.create_task(b())
    task_1.cancel()
    res = await asyncio.gather(task_1, task_2, return_exceptions=True)
    print(res)


""" ============================  
返回的记过虽然是 [CancelledError(), 'end b'], 但从打印的结果看task还是执行完毕的

# create_task 执行结果
begin b
[CancelledError(), 'end b']


# shield 执行结果
begin a
begin b
[CancelledError(), 'end b']
"""

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test())

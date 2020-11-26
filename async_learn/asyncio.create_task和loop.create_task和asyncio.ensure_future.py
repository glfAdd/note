"""
https://zhuanlan.zhihu.com/p/73568282

从Python 3.7开始可以统一的使用更高阶的asyncio.create_task。其实asyncio.create_task就是用的loop.create_task
def create_task(coro):
    loop = events.get_running_loop()
    return loop.create_task(coro)


"""



"""
https://zhuanlan.zhihu.com/p/73568282

1. asyncio.create_task 就是用的 loop.create_task
def create_task(coro):
    loop = events.get_running_loop()
    return loop.create_task(coro)

2. loop.create_task接受的参数需要是一个协程，但是asyncio.ensure_future除了接受协程，还可以是Future对象或者awaitable对象:
    如果参数是协程，其实底层还是用的loop.create_task，返回Task对象
    如果是Future对象会直接返回
    如果是一个awaitable对象会await这个对象的__await__方法，再执行一次ensure_future，最后返回Task或者Future
    Task是Future 子类

3. 一般情况下开发者不需要自己创建Future, 对于绝大多数场景要并发执行的是协程，所以直接用asyncio.create_task就足够了


"""

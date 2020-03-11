""" ============================ 参考
https://www.zhihu.com/question/63477745
"""

import asyncio

""" ============================ Coroutine 
协程对象

class Coroutine(Awaitable):
    pass
"""

""" ============================ Awaitable
1. 只要一个类实现了__await__方法，那么通过它构造出来的实例就是一个Awaitable
2. 用async修饰的函数，它返回的是一个Coroutine对象, Coroutine继承于Awaitable


class Awaitable(metaclass=ABCMeta):
    __slots__ = ()

    @abstractmethod
    def __await__(self):
        yield

    @classmethod
    def __subclasshook__(cls, C):
        if cls is Awaitable:
            return _check_methods(C, "__await__")
        return NotImplemented
"""

""" ============================ 自定义awaitable """


class B:
    def __iter__(self):
        return self

    def __next__(self):
        raise StopIteration('end')


class A:
    def __await__(self):
        return B()


async def a():
    s = await A()
    print(s)


loop = asyncio.get_event_loop()
loop.run_until_complete(a())
loop.close()

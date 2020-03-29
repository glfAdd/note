""" ============================ 参考
https://www.zhihu.com/question/63477745
https://zhuanlan.zhihu.com/p/27258289
"""

import asyncio

""" ============================ Coroutine 对象
协程对象
Coroutine类也继承了Awaitable，而且实现了send，throw和close方法

class Coroutine(Awaitable):
    __slots__ = ()

    @abstractmethod
    def send(self, value):
        ...

    @abstractmethod
    def throw(self, typ, val=None, tb=None):
        ...

    def close(self):
        ...
        
    @classmethod
    def __subclasshook__(cls, C):
        if cls is Coroutine:
            return _check_methods(C, '__await__', 'send', 'throw', 'close')
        return NotImplemented
"""

""" ============================ Awaitable 对象
1. 只要一个类实现了__await__方法，那么通过它构造出来的实例就是一个Awaitable
2. 用async修饰的函数，它返回的是一个Coroutine对象


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

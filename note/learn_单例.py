"""
装饰器单例

https://blog.csdn.net/youzi_yun/article/details/77509838


"""

from functools import wraps


def single(cls):
    __instance = dict()

    @wraps(cls)
    def tmp(*args, **kwargs):
        if cls in __instance:
            return __instance[cls]
        else:
            a = cls(*args, **kwargs)
            __instance[cls] = a
            return a

    return tmp


@single
class Test():
    def __init__(self, age):
        self.age = age


a = Test(10)
b = Test(33)
print(a.age)
print(b.age)

"""
__new__ 单例
"""


class Test2():
    __instance = None
    __is_first = True

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, name):
        if self.__is_first:
            self.name = name
            self.__is_first = False


c = Test2('Tome')
d = Test2('Jack')
print(c.name)
print(d.name)

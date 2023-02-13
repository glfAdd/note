"""
装饰器单例
https://blog.csdn.net/youzi_yun/article/details/77509838
"""
import threading


def single(cls):
    __instance = {}

    def func(*args, **kwargs):
        with threading.Lock():
            if cls in __instance:
                return __instance[cls]
            else:
                temp = cls(*args, **kwargs)
                __instance[cls] = temp
                return temp

    return func


@single
class Test(object):
    def __init__(self, age):
        self.age = age


a = Test(10)
print(a.age)
b = Test(20)
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

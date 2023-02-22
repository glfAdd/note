import time
from functools import wraps

"""
本质上是一个嵌套函数, 它接受被装饰的函数作为参数, 并返回一个包装过的函数
不改变被装饰函数的代码的情况下给被装饰函数或程序添加新的功能

使用场景 ?
  - 缓存
  - 权限校验
  - 性能测试
  - 插入日志
"""

print(""" ============================ 不使用装饰器 """)


def test_1():
    print('run test_1')


def test_2(func):
    print('run test_2 ')

    def test_3():
        print('run test_3')
        func()

    return test_3


a = test_2(test_1)
a()

print(""" ============================ 代码执行时间装饰器 """)
"""
functools.wraps
作用: 不改变使用装饰器原有函数的结构(如__name__, __doc__,__module__)
"""


def timeit(func):
    # 由此函数使用装饰器时, 函数__name__被装饰器改变
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print('used:', end - start)

    return wrapper


# 只要解释器执行到这里就会自动进行装饰, 不是等到调用函数时才装饰
@timeit
def f(number):
    print(number)
    time.sleep(1)


f(100.21)

print(""" ============================ 多个装饰器 """)


def out_2(fn):
    print('out_2 begin')

    def in_2():
        print("in_2 run ...")
        return "<b>" + fn() + "<b>"

    return in_2


def out_3(fn):
    print('out_3 begin')

    def in_3():
        print("in_3 run ...")
        return "<i>" + fn() + "<i>"

    return in_3


@out_2
@out_3
def func_1():
    print("func_1 run ...")
    return "hello"


print(func_1())

print(""" ============================ 带有参数的装饰器 """)


def out_5(arg):
    print(arg)

    def in_5(fn):
        def aaa(*args, **kwargs):
            a = fn(*args, **kwargs)
            return a

        return aaa

    return in_5


# 1.先执行out_5("装饰器参数")这个函数返回in_5引用
# 2.再使用@out_5对函数int_5进行装饰
@out_5("装饰器参数")
def func_3():
    pass


func_3()

print(""" ============================ 类做装饰器 """)
"""
1. Class1 做装饰器先创建 Class1 的实例对象, 并把函数引用func_4当做参数传递__init__中, __func指向这个函数
2. func_4指向了Class1的实例对象
3. func_4()相当于让实例对象执行(), 会调用__call__方法
4. self.__func()调用了最开始的func_4函数
"""


class Class1(object):
    def __init__(self, func):
        print("Class1 正在初始化")
        self.__func = func

    def __call__(self):
        print("Class1 装饰器功能")
        self.__func()


# func_4 = Class1(func_4)
@Class1
def func_4():
    pass


func_4()

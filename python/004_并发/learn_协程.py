import inspect
from functools import wraps

"""
获取携程的状态
inspect.getgeneratorstate()

协程的4个状态:
  - GEN_CREATED     等待开始执行
  - GEN_RUNNING     解释器正在执行（只有在多线程应用中才能看到这个状态）
  - GEN_SUSPENDED   在yield表达式处暂停
  - GEN_CLOSED      执行结束


next
send    参数成为暂停的yield表达式的值, 所以当处于暂停状态时才能发送值
throw   抛出异常. 使生成器暂停的yield处抛出指定异常,
close   终止生成器


1. 一直运行到下一个yield或者终止
2. 预激协程: 先执行next或send使其停在yield处
3. 生成器没有启动, 没有在yield处停止, 所以开始无法发送数据
"""


def simple():
    x = yield


a = simple()
print(inspect.getgeneratorstate(a))
a.__next__()
print(inspect.getgeneratorstate(a))

""" ============================ 预激协程装饰器 """


def coroutine(func):
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen

    return primer()


""" ============================ 协程异常处理 
1. 协程内部没有处理异常携程会终止, 当重新激活时会抛出异常StopIteration
2. 如果传入协程的异常没有处理协程会停止
"""


def throw_test():
    print('ready')
    while True:
        try:
            x = yield
        except IndentationError as e:
            print('IndentationError')
        except EOFError:
            print('EOFError')
        else:
            print('success --', x)
        finally:
            print('over')


th = throw_test()
next(th)
th.send(123)
th.throw(EOFError)
th.send(123)

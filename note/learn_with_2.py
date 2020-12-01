"""
参考
https://developer.ibm.com/zh/languages/python/articles/os-cn-pythonwith/
https://www.python.org/dev/peps/pep-0343/
"""

""" ============================ 作用
自动关闭文件、线程锁的自动获取和释放等
"""

""" ============================ 格式
with context_expression [as target(s)]:
        with-body


contextexpression 要返回一个上下文管理器对象，该对象并不赋值给 as 子句中的 target(s)
如果指定了 as 子句的话，会将上下文管理器的 _enter() 方法的返回值赋值给 target(s)
target(s) 可以是单个变量，或者由”()”括起来的元组（不能是仅仅由”,”分隔的变量列表，必须加”()”）
"""

""" ============================ 操作文件
不管在处理文件过程中是否发生异常，都能保证 with 语句执行完毕后已经关闭了打开的文件句柄

with open(r'somefileName') as somefile:
        for line in somefile:
            print line
            # ...more code
"""

""" ============================ with 语句执行过程
"""

""" ============================ 自定义上下文管理器
要实现上下文管理协议所需要的 enter() 和 exit() 两个方法


contextmanager._enter()
    进入上下文管理器的运行时上下文，在语句体执行前调用
    如果指定了 as 子句, with 语句将该方法的返回值赋值给 as 子句中的 target

contextmanager._exit(exc_type, exc_value, exc_traceback)
    退出与上下文管理器相关的运行时上下文
    exc_traceback: 是否处理异常. 如果自定义的with里面发生了异常, 则会代替 with-body 中的异常


"""


class DummyResource:
    def __init__(self, tag):
        self.tag = tag
        print('tag: {}'.format(tag))

    def __enter__(self):
        # enter() 返回的是自身的引用，这个引用可以赋值给 as 子句中的 target 变量；返回值的类型可以根据实际需要设置为不同的类型，不必是上下文管理器对象本身
        print('run enter')
        # 可以返回不同的对象
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        # exit() 方法中对变量 exctb 进行检测，如果不为 None，表示发生了异常，返回 False 表示需要由外部代码逻辑对异常进行处理
        # 如果没有发生异常，缺省的返回值为 None，在布尔环境中也是被看做 False，但是由于没有异常发生，_exit() 的三个参数都为 None，上下文管理代码可以检测这种情况，做正常处理
        print('run exit')
        if exc_tb is None:
            print('没有发生异常')
        else:
            print('发生异常')
            # False / None: 将异常抛出由外部处理
            # True: 不抛出异常
            return True


with DummyResource('Normal'):
    print('test 1')
    print('[with-body] Run without exceptions.')

print('-----------------')

with DummyResource('With-Exception'):
    print('test 2 start')
    raise Exception
    print('test 2 end ')

""" ============================ contextlib
对已有的生成器函数或者对象进行包装，加入对上下文管理协议的支持，避免了专门编写上下文管理器来支持 with 语句。
contextlib 模块提供了3个对象：
    装饰器 contextmanager
    函数 nested 
    上下文管理器 closing



nested






"""

from contextlib import contextmanager

"""
contextmanager
1. 用于装饰生成器函数, 返回上下文管理器, 其 enter() 和 exit() 方法由 contextmanager 实现
2. 被装饰的生成器函数只能产生一个值，否则会导致异常 RuntimeError；产生的值会赋值给 as 子句中的 target，如果使用了 as 子句的话
3. 成器函数中 yield 之前的语句在 enter() 方法中执行，yield 之后的语句在 exit() 中执行，yield 产生的值赋给了 as 子句中的 value 变量。
4. contextmanager 只是省略了 enter() / exit() 的编写，但并不负责实现资源的”获取”和”清理”工作；”获取”操作需要定义在 yield 语句之前，”清理”操作需要定义 yield 语句之后，
    这样 with 语句在执行 enter() / exit() 方法时会执行这些语句以获取/释放资源，即生成器函数中需要实现必要的逻辑控制，包括资源访问出现错误时抛出适当的异常。
"""


@contextmanager
def demo():
    print(1)
    yield 2
    print(3)


with demo() as value:
    print(value)
    print(value)

"""
nested

可以将多个上下文管理器组织在一起，避免使用嵌套 with 语句

with nested(A(), B(), C()) as (X, Y, Z):
    pass
    
         
with A() as X:
        with B() as Y:
            with C() as Z:
                 pass



"""

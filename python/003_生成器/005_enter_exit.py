import threading
from contextlib import contextmanager

"""
作用: 自动关闭文件、线程锁的自动获取和释放等
适用于: 对资源进行访问的场合，确保不管使用过程中是否发生异常都会执行必要的“清理”操作, 释放资源, 比如文件使用后自动关闭、线程中锁的自动获取和释放等.


上下文管理协议 (Context Management Protocol), 支持该协议的对象要实现这两个方法
    __enter__()
        - 在代码块开始前调用, 返回值赋值给as后的参数
    __exit__()
        - 方法负责执行“清理”工作，如释放资源等
        - 如果执行过程没有异常, 或者语句体中执行了语句 break/continue/return, 则以 None 作为参数调用 __exit__(None, None, None)
        - 如果执行过程出现异常, 则使用 sys.exc_info 得到的异常信息为参数调用 __exit__(exc_type, exc_value, exc_traceback)
        - 出现异常时，如果返回 False 则会重新抛出异常, 让with之外的语句逻辑来处理异常; 如果返回 True, 则忽略异常不再对异常进行处理。


上下文管理器 (Context Manager):
支持上下文管理协议的对象, 这种对象实现了 __enter__() 和 __exit__()


with context_expression [as target(s)]:
    with-body
    
1. context_expression 要返回一个上下文管理器对象, 该对象并不赋值给 as 子句中的 target(s)
2. 如果指定了 as 子句, 会将 __enter__() 的返回值赋值给 target(s)
3. 执行 BLOCK 中的表达式
4. 不管是否执行过程中是否发生了异常，执行上下文管理器的 __exit__() 方法
"""

""" ============================ 自定义上下文管理器 """


class DummyResource:
    def __init__(self, tag):
        self.tag = tag
        print('tag: {}'.format(tag))

    def __enter__(self):
        # enter() 返回的是自身的引用，这个引用可以赋值给 as 子句中的 target 变量
        # 返回值的类型可以根据实际需要设置为不同的类型，不必是上下文管理器对象本身
        print('run enter')
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        # exc_type 错误的类型
        # exc_val 错误类型对应的值
        # exc_tb 代码中错误发生的位置
        # __exit__() 方法中对变量 exctb 进行检测，如果不为 None，表示发生了异常，返回 False 表示需要由外部代码逻辑对异常进行处理
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

with DummyResource('With-Exception'):
    print('test 2 start')
    raise Exception
    print('test 2 end ')

""" ============================ 线程锁 """
lock = threading.RLock()
number = 0
with lock:
    print(1)

""" ============================ 操作文件
不管在处理文件过程中是否发生异常, 都能保证 with 语句执行完毕后已经关闭了打开的文件句柄
"""
with open(r'fileName') as f:
    for line in f:
        print(line)

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

""" ============================ contextlib
对已有的生成器函数或者对象进行包装，加入对上下文管理协议的支持，避免了专门编写上下文管理器来支持 with 语句。
contextlib 模块提供了3个对象：
    装饰器 contextmanager
    函数 nested 
    上下文管理器 closing



nested
"""

"""
适用于
对资源进行访问的场合，确保不管使用过程中是否发生异常都会执行必要的“清理”操作, 释放资源, 比如文件使用后自动关闭、线程中锁的自动获取和释放等.


上下文管理协议 (Context Management Protocol):
支持该协议的对象要实现这两个方法
__enter__()
  - 在代码块开始前调用, 返回值赋值给as后的参数
__exit__()
  - 方法负责执行“清理”工作，如释放资源等。
  - 如果执行过程中没有出现异常，或者语句体中执行了语句break/continue/return，则以None作为参数调用__exit__(None, None, None)
  - 如果执行过程中出现异常，则使用sys.exc_info得到的异常信息为参数调用__exit__(exc_type, exc_value, exc_traceback)
  - 出现异常时，如果返回False，则会重新抛出异常，让with之外的语句逻辑来处理异常
  - 如果返回True，则忽略异常，不再对异常进行处理。


上下文管理器 (Context Manager):
支持上下文管理协议的对象, 这种对象实现了__enter__() 和 __exit__()
定义执行with语句时要建立的运行时上下文, 负责执行with语句块上下文中的进入与退出操作


with EXPR as VAR:
    BLOCK
1. 执行表达式, 生成上下文管理器context_manager
2. 获取上下文管理器的__exit()__方法，并保存起来用于之后的调用；
3. 调用上下文管理器的__enter__()方法, 如果使用了as子句，则将__enter__()方法的返回值赋值给as子句中的变量
4. 执行BLOCK中的表达式
5. 不管是否执行过程中是否发生了异常，执行上下文管理器的__exit__()方法，
"""

""" ============================ 自定义上下文管理器 """


class DBManager(object):
    def __init__(self):
        print('__init__')

    def __enter__(self):
        print('__enter__')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # exc_type 错误的类型
        # exc_val 错误类型对应的值
        # exc_tb 代码中错误发生的位置
        print('__exit__')
        return True


def getInstance():
    return DBManager()


with getInstance() as dbManagerIns:
    print('with demo')

""" ============================ 线程锁 """

import threading

lock = threading.RLock()
number = 0
with lock:
    print(1)

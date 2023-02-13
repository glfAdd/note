"""
参考:
https://blog.csdn.net/freeking101/article/details/109615618




使用装饰器 contextmanager 就不用自己去写 __enter__ 和 __exit__,
装饰的对象必须是生成器函数, 这个值将赋值给 as 后的变量
yield 前的代码相当于 __enter__
yield 后的代码相当于 __exit__


"""
from contextlib import contextmanager


@contextmanager
def demo():
    print('------------ 1')
    yield '------------ 0'
    print('------------ 2')


with demo() as value:
    print(value)
    print(f'Assigned Value: {value}')

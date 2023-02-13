"""
装饰器在实现的时候，被装饰后的函数其实已经是另外一个函数了（函数名等函数属性会发生改变），为了不影响，
Python的functools包中提供了一个叫wraps的decorator来消除这样的副作用。写一个decorator的时候，最好在实现之前加上functools的wrap，它能保留原有函数的名称和docstring。
"""

from functools import wraps


def my_decorator(func):
    def wrapper(*args, **kwargs):
        """decorator"""
        print('Calling decorated function...')
        return func(*args, **kwargs)

    return wrapper


@my_decorator
def example():
    """Docstring"""
    print('Called example function')


print(example.__name__, example.__doc__)

('wrapper', 'decorator')


# -------------------------------------------------------


def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """decorator"""
        print('Calling decorated function...')
        return func(*args, **kwargs)

    return wrapper


@my_decorator
def example():
    """Docstring"""
    print('Called example function')


print(example.__name__, example.__doc__)

('example', 'Docstring')

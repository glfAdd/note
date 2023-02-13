"""
如果__new__() 创建的是当前类的实例，会自动调用__init__()函数，通过return调用的__new__()的参数cls来保证是当前类实例，如果是其他类的类名，那么创建返回的是其他类实例，就不会调用当前类的__init__()函数。

执行过程:
1. Tom('Tom', 12) 执行类 Tom 的 __new__ 方法, 并调 super(Tom, cls).__new__(cls), 返回一个实例
2. 用实例调用 __init__ 初始化
"""


class Person:
    def __new__(cls, *args, **kwargs):
        print('run person __new__')
        return super(Person, cls).__new__(cls)

    def __init__(self):
        print('run person __init__')


class Tom(Person):
    # 1. 用于创建实例, 在实例创建之前被调用
    # 2. 必须有返回值, 返回实例对象. 如果不 return 就不会调用 __init__ 方法
    # 3. 可以 return 父类或 __new__ 一个实例
    # 4. 子类没有定义 __new __ 时, 会自动调用父类的 __new__, 直到 object 的 __new__
    # cls 是类
    def __new__(cls, name, age):
        print('run Tom __new__')
        return super(Tom, cls).__new__(cls)

    # 1. 用于初始化实例, 在实例创建之后调用
    # 2. 可以没有返回值
    # self 就是这个 __new__ 返回的实例
    def __init__(self, name, age):
        super(Tom, self).__init__()
        print('run Tom __init__')


if __name__ == '__main__':
    t = Tom('Tom', 12)

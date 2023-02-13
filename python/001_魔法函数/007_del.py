"""
__del__()
对象手动或自动销毁时都调用



"""


class Test:
    def __del__(self):
        print('Test run __del__')


a = Test()
b = a
# del 只会使 Test() 的引用计数 -1, 此时引用计数并不是 0, 所以对象不会销毁, 不会执行 __del__
del a
# del 使 Test() 的引用计数变为 0, 对象销毁, 执行 __del__
del b
print('------------------')

"""
父类非 object 时, 如果重写子类的 __del__() 方法, 必须显式调用父类的 __del__() 方法, 
这样才能保证在回收子类对象时, 其占用的资源 (可能包含继承自父类的部分资源) 能被彻底释放
"""


class Person:
    def __init__(self):
        print('Person run __init__')

    def __del__(self):
        print('Person run __del__')


class Cat(Person):
    def __init__(self):
        super(Cat, self).__init__()
        print('Cat run __init__')

    def __del__(self):
        # 如果不调用父类的 __del__, 父类的资源不会释放
        super(Cat, self).__del__()
        print('Cat run __del__')


c = Cat()
del c

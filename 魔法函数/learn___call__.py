"""
callable: 可调用对象, 但凡是可以把一对括号()应用到某个对象身上都可称之为可调用对象. 允许一个类的实例像函数一样被调用.

在Python中的可调用对象:
1.可以是函数
2.可以是一个实例，它的类实现了__call__方法
3.可以是一个类，这时候，用这个类生成实例的过程就相当于调用这个类

如果在类中实现了 __call__ 方法，那么实例对象也将成为一个可调用对象. 这意味着 x() 与 x.__call__() 是相同的.
"""


class Test1(object):
    def __init__(self, name, age, num):
        self.name = name
        self.age = age
        self.num = num

    def __call__(self, age, num):
        self.age = num
        self.num = age

    def __str__(self):
        return '{} {} {}'.format(self.name, self.age, self.num)


t1 = Test1('xiaoming', 10, 300)
print(t1)
t1(22, 40)
print(t1)

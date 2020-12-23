# -*- coding: utf-8 -*-

"""
__dict__
类: 静态函数、类函数、普通函数、全局变量以及一些内置的属性
对象: 存储了一些self.xxx
基本数据类型: 没有__dict__属性 'abc'.__dict__

继承:
实例属性会在子对象的__dict__里面
方法和类属性不会在子类__dict__里面
"""


class A(object):
    a = 0
    b = 1

    def __init__(self):
        self.a = 2
        self.b = 3

    def test(self):
        print('a normal func.')

    @staticmethod
    def static_test(self):
        print('a static func.')

    @classmethod
    def class_test(self):
        print('a calss func.')


obj = A()
print(A.__dict__)
print(obj.__dict__)

"""================发生继承时候的__dict__属性"""


class Parent(object):
    a = 0

    def __init__(self):
        self.a = 2

    def p_test(self):
        pass


class Child(Parent):
    b = 5


p = Parent()
c = Child()
print(Parent.__dict__)
print(Child.__dict__)  # {'__module__': '__main__', 'b': 5, '__doc__': None}
print(p.__dict__)  # {'a': 2, 'b': 3}
print(c.__dict__)  # {'a': 2, 'b': 3}

"""================使用__dict__给对象添加属性"""


class AddTest(object):
    i = 10

    def __init__(self):
        self.j = 20

    def add_object(self):
        self.__dict__.setdefault('home', 'Chian')


a = AddTest()
a.add_object()
print(a.__dict__, a.home)  # {'j': 20, 'home': 'Chian'} Chian

"""================判断类和对象是否包含属性"""


# in 和 __contains__

class Test4(object):
    age = 20

    def __init__(self):
        self.name = 'Xiaoming'


t4 = Test4()
print(t4.__dict__.__contains__('name'))  # True
print(Test4.__dict__.__contains__('age'))  # True
print('name' in t4.__dict__)  # True
print('age' in Test4.__dict__)  # True

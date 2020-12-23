"""
x       : 共有变量
_x		: 私有化属性或方法. 类对象和子类可以访问, 只有本模块能用, 别的模块不能用. from ... import禁止导入, 只影响from...import不影响import直接导入这种方式
__x		: 别的模块不能用, 名字重整所以不能访问
__x__	: 魔法对象或属性, 系统给的, 不要这么命名
x_		: 用于避免与python关键字的冲突, 不要这么用

名字重整: 根据_Class__object规则改名字, 所以不能直接操作, 可以操作新的名字 a._Test1__number
"""

""" ============================ 私有属性添加getter和setter方法 """


class Test1(object):
    def __init__(self):
        self.__number = 100

    def setNumber(self, number):
        self.__number = number

    def getNumber(self):
        return self.__number


a = Test1()
b = a.getNumber()
print(b)

""" ============================ 使用property. 取值和赋值时自动调用对应的方法,位置不能调换 """


class Test2(object):
    def __init__(self):
        self.__number = 100

    def setNumber(self, number):
        self.__number = number

    def getNumber(self):
        return self.__number

    # property是对方法进行了封装, 使用更方便
    number = property(getNumber, setNumber)


a = Test2()
# a.number会调用getNumber和setNumber
a.number = 200
print(a.number)

""" ============================ 使用装饰器 """


class Test3(object):
    def __init__(self):
        self.__number = 100

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        self.__number = number


a = Test3()
a.number = 200
print(a.number)

""" ============================ property 
def __init__(self, fget=None, fset=None, fdel=None, docs=None):
fget 只读
fset 读写
"""


class Test4(object):
    def __init__(self):
        self.age = 0

    def setAge(self, a):
        self.age = a

    def getAge(self):
        return self.age

    new_age = property(getAge, setAge)


a = Test4()
a.new_age = 3
print(a.new_age)

""" ============================ learn_private_test """

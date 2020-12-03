# coding=utf-8
"""
Python2.x默认都是经典类，只有显式继承了object才是新式类
class Person(object):pass
class Person():pass
class Person:pass

Python3.x取消了经典类，默认都是新式类，并且不必显式的继承object, (三种写法并无区别, 推荐第一种)
class Person(object):pass
class Person():pass
class Person:pass
"""

""" ============================ 继承搜索的顺序发生了改变 
经典类: 深度优先
新式类: 广度优先
"""


class A(object):
    def test(self):
        print('is A')


class B(A):
    pass


class C(A):
    def test(self):
        print('is C')


class D(B, C):
    pass


d = D()
# 经典类   is A
# 新式类   is C
d.test()

""" ============================ 继承搜索的顺序发生了改变 
经典类
  所有的类都是classobj类型
  类的实例都是instance类型
  无法通过type比较类型, 只能通过__class__比较
  
新式类
  类的类型和实例的类型相同
"""
a = A()
b = B()
print(type(a))  # <type 'instance'>
print(type(b))  # <type 'instance'>
print(a.__class__)  # __main__.A
print(b.__class__)  # __main__.B

print(type(a))  # __main__.A
print(type(b))  # __main__.B
print(a.__class__)  # __main__.A
print(b.__class__)  # __main__.B

""" ============================ 构造方法 
def __init__(self):
def __init__(self, age=3):

super(class_name,self).__init__(*args)
super(class_name,self).__init__(age)

super:即使已经继承了多个超类, 使用一次super就可以了, 但要确保超类也使用super
"""

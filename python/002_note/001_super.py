"""
参考:
https://blog.csdn.net/wo198711203217/article/details/84097274


MRO:
1. Method Resolution Order 方法解析顺序, 简称 MRO 列表, 它代表了类继承的顺序, 处理二义性问题
2. 每一个类都有


python 支持多继承，
二义性问题:
    1. 有两个基类 A 和 B, 且都定义了方法 f()，C 继承 A 和 B, 调用 C 的 f() 不确定执行 A 还是 B 的.
    2. 有一个基类 A 定义了方法 f(), B 和 C 继承了 A 类的 f() 方法, D 继承了 B 和 C , 调用 D 的 f() 不知道应该执行 B 还是 C 的
参考: https://blog.csdn.net/qwertyupoiuytr/article/details/56439134


super
super也是一个类，不是一个方法，必须用到新式类上
5. super并不是一个函数，是一个类名，形如super(B, self)事实上调用了super类的初始化函数，产生了一个super对象
6. super类的初始化函数并没有做什么特殊的操作，只是简单记录了类类型和具体实例；
7. super(B, self).func的调用并不是用于调用当前类的父类的func函数；使用C3算法，先搜索到func函数才是，父类的func函数不见得就一定先搜索到；
super(self,A).func() 调用的并不是其父类 A 的 func,而是 A 在MRO中的下一个类的 func
8. Python的多继承类是通过mro的方式来保证各个父类的函数被逐一调用，而且保证每个父类函数只调用一次（如果每个类都使用super）；


super 原理
# cls 代表类，inst 代表实例
def super(cls, inst):
    # 获取 inst 的 MRO 列表
    mro = inst.__class__.mro()
    # 查找 cls 在当前 MRO 列表中的 index, 并返回它的下一个类，即 mro[index + 1]
    return mro[mro.index(cls) + 1]
"""


class Base:
    def eat(self):
        print('init base')


class A(Base):
    def eat(self):
        super(A, self).eat()
        print('init A')


class B(Base):
    def eat(self):
        super(B, self).eat()
        print('init B')


class C(A, B):
    def eat(self):
        super(C, self).eat()
        print('init C')


if __name__ == '__main__':
    # 查看类 MRO
    print(C.mro())
    C().eat()

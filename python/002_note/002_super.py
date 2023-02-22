"""
参考:
https://blog.csdn.net/qwertyupoiuytr/article/details/56439134


MRO:
1. Method Resolution Order 方法解析顺序, 简称 MRO 列表, 它代表了类继承的顺序, 处理二义性问题
2. 每一个类都有
3. Python 的多继承类是通过 mro 的方式来保证各个父类的函数被逐一调用



python 支持多继承, 会存在二义性问题, 使用 C3 算法:
    1. 有两个基类 A 和 B, 且都定义了方法 f(), C 继承 A 和 B, 调用 C 的 f() 不确定执行 A 还是 B 的.
    2. 有一个基类 A 定义了方法 f(), B 和 C 继承了 A 类的 f() 方法, D 继承了 B 和 C , 调用 D 的 f() 不知道应该执行 B 还是 C 的



C3 算法
将继承关系拓扑排序后, 按照得到的拓扑序列遍历即可满足单调性, 原因是由根到叶即是子类到基类的方向, 当基类的入度为0是, 它就是子类的唯一基类, 此时会优先遍历此基类, 符合单调性
因为当多个子类继承自同一个基类时, 该基类的入度不会先于子类减为0, 所以可以保证优先遍历入度减为0的子类

C3 算法执行步骤 (003_MRO.png 箭头指向父类)
    1. 首先找入度为0的点, 只有A, 把A取出, 把A相关的边去掉
    2. 再找下一个入度为0的点, B和C满足条件, 从左侧开始取, 取出B, 这时顺序是AB, 然后去掉B相关的边
    3. 这时候入度为0的点有E和C, 依然取左边的E, 这时候顺序为ABE, 接着去掉E相关的边
    4. 这时只有一个点入度为0, 那就是C, 取C, 顺序为ABEC
    5. 去掉 C 的边得到两个入度为0的点D和F, 取出D, 顺序为ABECD, 然后去掉D相关的边, 那么下一个入度为0的就是F, 然后是object
    6. 所以最后的排序就为ABECDFobject



Python 2
    super(Class, self).xxx
    super(A, self).__init__(a, b)
Python 3
    super().xxx 
    super().__init__(a, b)



super
1. super 不是函数, 是一个类, 如 super(B, self) 产生了一个super对象
2. super(self,A).func() 调用的并不是其父类 A 的 func,而是 A 在MRO中的下一个类的 func



super 原理
def super(cls, inst):
    # cls 代表类
    # inst 代表实例
    # 获取 inst 的 MRO 列表
    mro = inst.__class__.mro()
    # 查找 cls 在当前 MRO 列表中的 index, 并返回它的下一个类, 即 mro[index + 1]
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

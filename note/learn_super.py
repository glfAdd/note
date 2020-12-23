"""

https://blog.csdn.net/wo198711203217/article/details/84097274


MRO:
每一个类，Python 会计算出一个方法解析顺序（Method Resolution Order, MRO）列表, 它代表了类继承的顺序

"""

class Test():
    pass

print(Test.mro())
print(Test.__class__)

"""
super 原理


def super(cls, inst):
    mro = inst.__class__.mro()
    return mro[mro.index(cls) + 1]
    
    
解释: 
cls 代表类，inst 代表实例，上面的代码做了两件事：
    获取 inst 的 MRO 列表
    查找 cls 在当前 MRO 列表中的 index, 并返回它的下一个类，即 mro[index + 1] 
"""
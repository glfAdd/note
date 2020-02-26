import gc
import weakref

""" ============================ weakref 弱引用
1. 如果对象有一个常规的引用, 它是不会被垃圾收集器销毁的, 如果对象只剩下一个弱引用, 那么它可能被垃圾收集器收回
2. 来实现缓存或者大对象的映射。就是当其他地方没有对这些大文件的引用的时候, 这个对象会被销毁。
3. 并不是所有的对象都可以进行弱引用。许多内置的类型, 例如列表和字典不能够直接支持弱引用, 但是可以通过子类支持。其他的内置类型诸如元组和long, 即使通过子类的方式也不能够进行弱引用。


使用场景 ? 
  有很多比较大的图像, 你希望每个都有一个名字相关联。
  如果用dict类型的对象来完成名字到图像对象的映射, 这些对象会一直存在着, 因为其存在于字典中
  weakref中的WeakKeyDictionary和WeakValueDictionary可以用来解决这个问题(也就是说这些大对象可以作为键或者值)
  当仅有弱引用指向这些对象的时候, 这些对象会被销毁, 并且WeakKeyDictionary和WeakValueDictionary中对应的映射也会被删除


模块方法
weakref.ref(object[, callback]):        创建一个弱引用对象, 引用计数并没有改变, callback是回调函数（当被引用对象被删除时的, 会调用改函数）
weakref.proxy(object[, callback]):      创建一个用弱引用实现的代理对象, 参数同上。
weakref.getweakrefcount(object):        获取对象object关联的弱引用对象数
weakref.getweakrefs(object):            获取object关联的弱引用对象列表
weakref.WeakKeyDictionary([dict]):      创建key为弱引用对象的字典
weakref.WeakValueDictionary([dict]):    创建value为弱引用对象的字典
weakref.WeakSet([elements]):            创建成员为弱引用对象的集合对象


模块属性
  - weakref.ReferenceType               被引用对象的类型
  - weakref.ProxyType                   被代理对象（不能被调用）的类型
  - weakref.CallableProxyType           被代理对象（能被调用）的类型
  - weakref.ProxyTypes                  所有被代理对象的类型序列
  - exception weakref.ReferenceError 
"""

""" ============================ del __del__
del 不删除对象，而是删除对象的引用
__del__ 特殊方法，但是它不会销毁实例，不应该在代码中调用。即将销毁实例时， Python 解释器会调用 __del__ 方法，给实例最后的机会，释放外部资源。
在 CPython 中，垃圾回收使用的主要算法是引用计数。每个对象都会统计有多少引用指向自己。当引用计数归零时，对象立即就被销毁；CPython 会在对象上调用__del__ 方法（如果定义了），然后释放分配给对象的内存。
"""

""" ============================ ref / proxy 
ref:           返回对象弱引用, 要获取原对象可以调用引用对象
proxy:         返回原对象弱引用的一个代理对象, 和使用原对象一样
回调函数:       在建立弱引用的时候指定一个回调函数, 引用的对象被销毁时调用

代理和弱引用的区别就是不需要 ()
"""


def delete_obj(arg):
    print('回收对象回调')


class ExpensiveObject(object):
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print('(Deleting %s)' % self)


obj = ExpensiveObject('小明')
r = weakref.ref(obj, delete_obj)
p = weakref.proxy(obj, delete_obj)
print(obj.name, r().name, p.name)
del obj
gc.collect()

""" ============================ 弱引用的局限 
不是每个对象都可以作为弱引用的目标
  - 基本的list和dict实例不能作为所指对象, 但是它们的子类可以
  - set 实例可以作为所指对象。用户定义的类型也没问题。
  - int 和 tuple 实例不能作为弱引用的目标, 子类也不行。
"""


class MyList(list):
    def __init__(self, number):
        self.number = number


a_list = MyList(350)
wref_to_a_list = weakref.ref(a_list)

""" ============================ WeakValueDictionary 
返回一个value中使用弱引用保存对象的字典

1. ref 和 proxy弱引用单个对象
2. WeakKeyDictionary 和 WeakValueDictionary 弱引用多个对象
3. 本质是字典类型, 值是弱引用, 当这些值引用的对象不再被其他非弱引用对象引用时, 这些引用的对象就可以回收

为长时间运行的函数实现缓存机制. 缓存中的值从未停留在那里,直到实际再次使用它们,但几乎每次都需要重新计算.
由于访问存储在WeakValueDictionary中的值之间没有强引用,因此GC消除了它们
"""


class Class2(object):
    def __init__(self, number):
        self.number = number

    def __repr__(self):
        return self.number

    def __del__(self):
        print('销毁对象', self.number)


one = weakref.WeakValueDictionary()
two = {}

for a in [100, 300, 20]:
    obj = Class2(a)
    two[a] = obj
    one[a] = obj

del two
gc.collect()
print(len(one))

import gc
import weakref
import sys

"""
python采用"引用计数"和"垃圾回收"两种机制来管理内存

容器对象: 列表、字典、类、元组
不可达对象: 垃圾对象
del         只使变量所代表的对象的引用计数减1，并在对应空间中删除该变量名
"""

""" ============================ 引用计数 
引用计数通过记录对象被引用的次数来管理对象. 对对象的引用都会使得引用计数加1, 移除对对象的引用计数则会减1, 当引用计数减为0时, 对象所占的内存就会被释放掉
引用计数可以高效的管理对象的分配和释放, 但是有一个缺点, 就是无法释放引用循环的对象

查看对象引用计数. 创建了一个临时的引用因此结果，会比期望的+1
sys.getrefcount(对象)
"""


class NumberOne(object):
    pass


number_one = NumberOne()
print(sys.getrefcount(number_one))

""" ============================ 垃圾回收 gc (garbage collection)
什么时候调用 ?
根据内存的分配和释放情况的而被调用
当内存溢出时, 不会自动调用gc, 因为gc更看重的是垃圾对象的个数, 而不是大小. 对于长时间运行的程序, 尤其是一些服务器应用, 人为主动的调用gc是非常有必要的

三种触发垃圾回收的情况
调用gc.collect()，需要先导入gc模块
当gc模块的计数器达到阈值的时候
程序退出时

调用gc的策略
  - 1. 固定时间间隔进行调用
  - 2. 基于事件的调用
         用户终止了对应用的访问
         明显监测到应用进入到闲置的状态
         运行高性能服务前后
         周期性、或阶段性工作的前后

gc垃圾回收方法(寻找引用循环对象)
只有容器对象才会出现引用循环. 为了追踪容器对象, 需要每个容器对象维护两个额外的指针, 用来将容器对象组成一个链表, 指针分别指向前后两个容器对象, 方便插入和删除操作. 其次, 每个容器对象还得添加gc_refs字段. 
一次gc垃圾回收步骤:
  - 1. 使得gc_refs等于容器对象的引用计数
  - 2. 遍历每个容器对象(a), 找到它(a)所引用的其它容器对象(b), 将那个容器对象(b)的gc_refs减去1. 
  - 3. 将所有gc_refs大于0的容器对象(a)取出来, 组成新的队列, 因为这些容器对象被容器对象队列的外部所引用. 
  - 4. 任何被新队列里面的容器对象, 所引用的容器对象(旧队列中)也要加入到新队列里面. 
  - 5. 释放旧队列里面的剩下的容器对象. (释放容器对象时, 它所引用的对象的引用计数也要减1)
  
gc分代机制
  - 第0代: 放新产生的对象
  - 第1代: 第0代的一次gc垃圾回收中活了下来
  - 第2代: 第1代的一次gc垃圾回收中活了下来

设置gc每一代垃圾回收所触发的阈值
  - 1. 从上一次第0代gc后，如果创建对象的个数减去释放对象的个数大于threshold0, 那么就会对第0代中的对象进行gc垃圾回收检查
  - 2. 从上一次第1代gc后，如过第0代被gc垃圾回收的次数大于threshold1，那么就会对第1代中的对象进行gc垃圾回收检查
  - 3. 从上一次第2代gc后，如过第1代被gc垃圾回收的次数大于threshold2，那么就会对第2代中的对象进行gc垃圾回收检查

__del__
我们知道当引用计数变为0的时候，会先调用对象的__del__方法，然后再释放对象。
但是当一个引用循环中对象有__del__方法时，gc就不知道该以什么样的顺序来释放环中对象。因为环中的a对象的__del__方法可能调用b对象，而b对象的__del__方法也有可能调用a对象。所以需要人为显式的破环。


设置gc每一代垃圾回收所触发的阈值. 如果threshold0设置为0，表示关闭分代机制
def set_threshold(threshold0, threshold1=None, threshold2=None): 
"""

""" ============================ gc 
暂停自动垃圾回收
gc.disable()

执行一次完整的垃圾回收, 返回垃圾回收所找到无法到达的对象的数量
gc.collect()

设置Python垃圾回收的阈值
gc.set_threshold(700, 10, 5)

获取垃圾回收的阈值
gc.get_threshold()

设置垃圾回收调试信息会
gc.set_debug(gc.DBEUG_LEAK)

获取垃圾列表, 列表项是垃圾收集器发现的垃圾对象, 但又不能释放, 通常gc.garbage中的对象是引用对象还中的对象。'
因Python不知用什么顺序来调用对象的__del__函数，导致对象始终存活在gc.garbage中，造成内存泄露
gc.garbage
"""


# 调用一次gc.collect()，首先检查因为引用循环而不可达对象，如果一个引用循环中所有对象都不包含__del__方法，那么这个引用循环中的对象都将直接被释放掉。
# 否则，将引用循环中包含__del__方法的对象加入到gc.garbage列表中。（这时它们的引用计数也会加1，因此gc.collect()不会再对这个环进行处理）
# 用户通过gc.garbage来获取这些对象，手动消除引用，进行破环。
# 最后消除gc.garbage对这些对象的引用，这时这些对象的引用计数减1等于0，就自动被回收了。否则由于gc.garbage对这些对象存在引用，这些对象将永远不会被回收。


class A(object):
    def __del__(self):
        print('__del__ in A')


class B(object):
    def __del__(self):
        print('__del__ in B')


class C(object):
    pass


print('collect: ', gc.collect())
print('garbage: ', gc.garbage)
a = A()
b = B()
c = C()
a.cc = c
c.bb = b
b.aa = a
del a, b, c
print('collect: ', gc.collect())
print('garbage: ', gc.garbage)


# del gc.garbage[0].cc  # 当然，这是在我们知道第一个对象是 a的情况下，手动破除引用循环中的环
# del gc.garbage[:]  # 消除garbage对a和b对象的引用，这样引用计数减1等于0，就能回收a、b、c三个对象了
# print('garbage: ', gc.garbage)
# print('----------------------------')
# print('collect: ', gc.collect())
# print('garbage: ', gc.garbage)


class Foo(object):
    pass


a = Foo()
a.bar = 123
a.bar2 = 123

# del a.bar2
# del a

b = weakref.ref(a)
print(b().bar)
print(a == b())

c = weakref.proxy(a)
print(c.bar)
print(c == a)

""" ============================ 闭包空间的变量和自由变量的释放 """


class A(object):
    def __init__(self, name):
        self._name = name

    def __del__(self):
        print('__del__ in ', self._name)


def f1():
    a = A('a')
    b = A('b')

    def f2():
        c = A('c')
        print(a)

    return f2


f2 = f1()
print(f2.__closure__)  # 查看f2的闭包里面引用了a对象
f2()
del f2  # 此时已经没有任何变量可以引用到返回的f2对象了

""" ============================ 标记清除 
标记清除是一种基于追踪回收的算法，分两个阶段（下图4和5是两个非活动对象）
第一阶段，从跟对象出发，沿着有向边遍历对象，可达的对象标记为“活动对象”，不可达的对象就是要被清除的”非活动对象“
第二阶段，把那些“非活动对象”进行回收
标记清除主要处理一些容器对象，比如list、dict、tuple、instance等
算法缺陷：操作时必须顺序扫描整个堆内存
"""

""" ============================ 循环有引用
https://www.cnblogs.com/Leon-The-Professional/p/10137405.html

"""

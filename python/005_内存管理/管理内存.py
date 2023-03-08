import gc
import weakref
import sys


class NumberOne(object):
    pass


number_one = NumberOne()
print(sys.getrefcount(number_one))

""" ============================ 垃圾回收 gc (garbage collection)
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
  


"""

""" ============================ gc """
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


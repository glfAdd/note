import multiprocessing
from ctypes import *
from threading import Thread

"""

############################ 是否有问题 #########################
多核多线程和单核多线程
多核多线程比单核多线程更差, 
原因是单核下多线程, 每次释放GIL, 唤醒的那个线程都能获取到GIL锁, 所以能够无缝执行, 
但多核下, CPU0释放GIL后, 其他CPU上的线程都会进行竞争, 但GIL可能会马上又被CPU0拿到, 导致其他几个CPU上被唤醒后的线程会醒着等待到切换时间后又进入待调度状态, 这样会造成线程颠簸(thrashing), 导致效率更低
"""

""" ============================ 规避方法: 1
如果完全使用python可以使用multiprocessing模块创建进程池.
每当有线程执行CUP密集型任务时, 它就把任务提交到进程池中, 然后进程池将任务交给另一个进程的解释器, 当线程等待结果的时候释放GIL, 由于是在另一个独立解释器进行, 就不受GIL限制了.
在创建任何线程之前将进程池作为单例在程序启动时创建, 这样就可以使用相同的进程池来处理计算密集型任务, 

涉及到和另一个解释器之间数据序列化和通讯, 完成的工作规模必须足够大这样就可以弥补额外产生的通讯开销
"""

pool = None


def some_word():
    pass


def some_thread():
    while True:
        pool.apply(some_word)


if __name__ == '__man__':
    pool = multiprocessing.pool()

""" ============================ 规避方法: 2
将计算密集型的任务转移到C语言中, 使其独立于Python, 在C代码中释放GIL, 通过C代码插入特殊的宏实现的

如果C语言扩展阻塞了C函数或执行时间很长的操作, 那么必须等到C函数返回才会释放GIL, 这时其他线程就将死了.
保持一解释器的隔离, 不使用python的数据结构和python的API


把c文件编译成动态库文件
gcc cdemo.c -shared -o libcdemo.so
"""

# 加载动态库
lib = cdll.LoadLibrary("./libcdemo.so")
# 创建子线程
t = Thread(target=lib.DeadLoop)
t.start()
# 主线程死循环
while True:
    pass

""" ============================ 规避方法: 3
更换cpython为jpython, java实现的python解释器, 不建议
"""

import multiprocessing
from ctypes import *
from threading import Thread

"""
并发：交替处理多个任务的能力 
并行：同时处理多个任务的能力

解释器
  - CPython
  - PyPy
  - Psyco
  - CPython
  - JPython
GIL是解释器的特性, GIL只有CPython有, JPython就没有GIL

Python程序执行过程
  - 1. 获取GIL
  - 2. 切换进一个线程中去运行
  - 3. 指定数量的字节码指令, 线程主动让出控制权, 可以调用time.sleep(0)来完成
  - 4. 把线程设置会睡眠状态（切换出线程）
  - 5. 释放GIL
  - 6. 重复上述步骤 

GIL是什么 ?
  - 1. 全局解释器锁 global interpreter lock
  - 2. 每个进程有各自独立的GIL互不干扰
  - 3. 解释器的C语言实现中, 有一部分并不是线程安全的, 因此不能完全支持并发执行, 任意时刻只允许在解释器运行一个线程
  - 4. 对于I/O密集型的线程, 每当阻塞I/O操作是解释器会释放GIL
  - 5. 对于CPU密集型线程, 解释器会执行一定数量的字节码之后释放GIL, 其他线程获取执行的机会
  - 6. C语言扩展模块不同, 调用C函数时GIL会被锁定, 直到他返回为止, 由于C代码的执行不受解释器控制, 这期间解释器不会执行任何Python字节码, 因此解释器无法释放GIL
  - 7. 保证同一时刻多线程中只有一个被调用, 无论几个cpu核心
  - 8. 每个线程在执行的过程都需要先获取GIL, 保证同一时刻只有一个线程可以执行代码, 无论有多少个线程, 多线程并不是真正的并发。
  - 9. 每次释放GIL锁, 线程进行锁竞争、切换线程, 会消耗资源
  - 10. 如果Thread1是因为I/O阻塞 让出的Gil Thread2必定拿到Gil,如果 Thread1是因为ticks计数满100让出Gil 这个时候 Thread1 和 Thread2 公平竞争
  
什么时候会释放GIL锁 ?
  - 一个线程执行一段时间之后就要释放GIL让其他线程有执行的机会,而且从获取与释放GIL的实现来看,只有持有GIL的线程主动释放GIL,其他线程才有机会获取GIL执行自己的任务
  - 每次释放GIL锁, 线程进行锁竞争、切换线程, 会消耗资源。并且由于GIL锁存在, python里一个进程永远只能同时执行一个线程(拿到GIL的线程才能执行)
  - python2.x
    1.GIL的释放逻辑是当前线程遇见IO操作
    2.ticks计数达到100（ticks可以看作是python自身的一个计数器, 专门做用于GIL, 每次释放后归零, 这个计数可以通过 sys.setcheckinterval 来调整）, 进行释放。
  - python3.x
    使用计时器（执行时间达到阈值后, 当前线程释放GIL）
  
互斥锁和Gil锁的关系 ?
  - GIL锁: 保证同一时刻只有一个线程能使用到cpu
  - 互斥锁: 多线程时, 保证在同一时间数据只被一个线程所持有, 保证线程的数据安全
假设1个进程有2个线程 Thread1,Thread2, 要修改共享的数据data, 并且有互斥锁
  - 1. 假设Thread1获得GIL可以使用cpu, 这时Thread1获得互斥锁LOCK, Thread1可以改data数据(但并没有开始修改数据)
  - 2. Thread1修改data数据前发生了I/O操作或者ticks计数满100, 这个时候 Thread1 让出了GIL
  - 3. Thread1 和 Thread2 开始竞争 GIL
  - 4. 设Thread2正好获得了GIL, 运行代码去修改共享数据date,由于Thread1有互斥锁lock, 所以Thread2无法更改共享数据date,这时Thread2让出Gil锁 , GIL锁再次发生竞争 
  - 5. 假设Thread1又抢到GIL, 由于其有互斥锁Lock所以其可以继续修改共享数据data,当Thread1修改完数据释放互斥锁lock,Thread2在获得GIL与lock后才可对data进行修改

GIL对多线程的影响 ?
  - 1. CPU密集型: ticks计数很快就会达到阈值, 然后触发GIL的释放与再竞争（多个线程来回切换当然是需要消耗资源的）, 单线程会比多线程快
  - 2. IO密集型: 多线程能够有效提升效率(单线程下有IO操作会进行IO等待, 造成不必要的时间浪费, 而开启多线程能在线程A等待时, 自动切换到线程B, 可以不浪费CPU的资源, 从而能提升程序执行效率)。多线程会比单线程快

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

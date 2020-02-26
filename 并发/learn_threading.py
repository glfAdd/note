import threading
import time

"""
python当前版本的多线程库没有实现优先级、线程组，线程也不能被停止、暂停、恢复、中断

threading 模块提供的常用方法：
  threading.current_thread()    返回当前的线程变量
  threading.enumerate()         返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。
  threading.activeCount()       返回正在运行的线程数量，与len(threading.enumerate())有相同的结果。

threading 模块提供的常量：
  threading.TIMEOUT_MAX         设置threading全局超时时间。
"""

""" ============================ Thread 
Thread(group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None)
group       线程组
target      要执行的方法
name        线程名
args
kwargs
daemon


start()         启动线程
isAlive()       是否在运行
is_alive()
join()          将会使主调线程堵塞，直到被调用线程运行结束或超时, 在start会后调用
setName()     
getName()
setDaemon()     是否后台线程, 默认False
  如果是后台线程，主线程执行过程中，后台线程也在进行，主线程执行完毕后，后台线程不论成功与否，主线程和后台线程均停止
  如果是前台线程，主线程执行过程中，前台线程也在进行，主线程执行完毕后，等待前台线程也执行完成后，程序停止
  

t.name = "My-Thread"
t.daemon = False  
t.ident         获取线程的标识符。线程标识符是一个非零整数，只有在调用了start()方法之后该属性才有效，否则它只返回None
"""


# 直接调用
def test1(*args, **kwargs):
    time.sleep(2)
    print('test1 - ', args, kwargs)


t3 = threading.Thread(target=test1, name='001', args=(5, 6), kwargs={'a': 1, 'b': 3}, daemon=False)
t3.start()


# 继承Thread, 重写run
class MyThread(threading.Thread):
    def __init__(self, arg):
        super(MyThread, self).__init__()
        self.arg = arg

    def run(self):
        time.sleep(0.5)
        print('MyThread run - %s \n' % self.arg)


for i in range(3):
    t = MyThread(i)
    t.start()
for i in range(10, 14):
    t = MyThread(i)
    t.start()
    t.join()

""" ============================ Lock / RLock
RLock
  允许在同一线程中被多次acquire
  acquire和release必须成对出现，即调用了n次acquire，必须调用n次的release才能真正释放所占用的琐

acquire([timeout])      调用时线程一直阻塞, 直到获得锁或timeout, 返回是否获得锁
release()               释放锁。使用前线程必须已获得锁定，否则将抛出异常。

死锁: 如果两个线程分别占有一部分资源并且同时等待对方的资源，就会造成死锁
"""
# 创建锁
# True堵塞(默认), 如果这个锁在上锁之前已经被上锁了，那么这个线程会在这里一直等待到解锁为止
# False非堵塞, 不管本次调用是否成功上锁，都不会卡在这而是继续执行下面的代码
lock = threading.Lock()
number_lock = 0


def lock_one():
    lock.acquire(2)
    global number_lock
    time.sleep(0.5)
    number_lock += 1
    print('lock number %s' % number_lock)
    lock.release()


for i in range(4):
    lock_one()

# lock.acquire()
# lock.acquire()  # 死锁
# lock.release()
# lock.release()

rlock = threading.RLock()
rlock.acquire()
rlock.acquire()  # 同一个线程内程序不会阻塞
rlock.release()
rlock.release()

""" ============================ Condition 
高级的琐, 能够实现在某个事件触发后才处理数据, 能够控制复杂的线程同步问题
创建Condigtion对象的时候把琐对象作为参数传入, 默认Rlock

acquire([timeout])  返回bool
release()

在占用琐(acquire)之后才能调用，否则将会报RuntimeError异常
wait([timeout])     释放内部所占用的琐，同时线程被挂起，直至接收到通知被唤醒或超时（如果提供了timeout参数的话）。当线程被唤醒并重新占有琐的时候，程序才会继续执行下去
notify()            唤醒一个挂起的线程(如果存在挂起的线程). 不会释放所占用的琐
notifyAll()         唤醒所有挂起的线程(如果存在挂起的线程). 不会释放所占用的琐
__enter__
__exit__
"""
condition = threading.Condition()
products = 0


class Producer(threading.Thread):
    def run(self):
        global products
        while True:
            if condition.acquire():
                if products < 10:
                    products += 1
                    print("Producer(%s):deliver one, now products:%s" % (self.name, products))
                    condition.notify()  # 不释放锁定，因此需要下面一句
                    condition.release()
                else:
                    print("Producer(%s):already 10, stop deliver, now products:%s" % (self.name, products))
                    condition.wait();  # 自动释放锁定
                time.sleep(2)


class Consumer(threading.Thread):
    def run(self):
        global products
        while True:
            if condition.acquire():
                if products > 1:
                    products -= 1
                    print("Consumer(%s):consume one, now products:%s" % (self.name, products))
                    condition.notify()
                    condition.release()
                else:
                    print("Consumer(%s):only 1, stop consume, products:%s" % (self.name, products))
                    condition.wait()
                time.sleep(2)


for p in range(0, 2):
    p = Producer()
    p.start()

for c in range(0, 3):
    c = Consumer()
    c.start()

""" ============================ Event 
threading.Event()可以创建一个事件管理标志，该标志（event）默认为False

wait(timeout)       调用该方法的线程会被阻塞，如果设置了timeout参数，超时后，线程会停止阻塞继续执行
set()               将event的标志设置为True，调用wait方法的所有线程将被唤醒
clear()             将event的标志设置为False，调用wait方法的所有线程将被阻塞
isSet()             判断event的标志是否为True
"""


def test(n, event):
    while not event.isSet():
        print('Thread %s is ready' % n)
        time.sleep(1)
    event.wait()
    while event.isSet():
        print('Thread %s is running' % n)
        time.sleep(1)


def main():
    event = threading.Event()
    for i in range(0, 2):
        th = threading.Thread(target=test, args=(i, event))
        th.start()
    time.sleep(3)
    print('----- event is set -----')
    event.set()
    time.sleep(3)
    print('----- event is clear -----')
    event.clear()


main()
""" ============================ timer 
定时器, 在指定时间后调用一个方法

Timer(interval, function, args=[], kwargs={})
interval            指定的时间 
function            要执行的方法 
args
kwargs 
"""


def timer_fun(*args):
    print('timer function', args)


timer = threading.Timer(interval=5, function=timer_fun, args=(1, 2))
timer.start()

""" ============================ local 
用来保存一个全局变量，但是只能在当前线程才能访问, 互不干扰
"""

# 创建全局ThreadLocal对象:
local_school = threading.local()


def process_student():
    # 获取当前线程关联的student:
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))


def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()


t1 = threading.Thread(target=process_thread, args=('dongGe',), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('老王',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()

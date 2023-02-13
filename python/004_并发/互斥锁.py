from threading import Thread, Lock

"""
同步：按预定的先后次序进行运行
异步：顺序不确定
轮询：不停判断是否符合条件

互斥锁
  - 某个线程要更改共享数据时, 先将其锁定, 此时资源的状态为“锁定”, 其他线程不能更改
  - 直到该线程释放资源，将资源的状态变成“非锁定”，其他的线程才能再次锁定该资源。
  - 互斥锁保证了每次只有一个线程进行写入操作，从而保证了多线程情况下数据的正确性。
给最少的代码上锁
全局变量是多个线程都共享的数据，而局部变量等是各自线程的，是非共享的不用加锁
"""

g_num = 0


def test1():
    global g_num
    for i in range(1000000):
        # True表示堵塞
        if mutex.acquire(True):
            g_num += 1
            mutex.release()
    print("---test1---g_num=%d" % g_num)


def test2():
    global g_num
    for i in range(1000000):
        if mutex.acquire(True):
            g_num += 1
            mutex.release()
    print("---test2---g_num=%d" % g_num)


mutex = Lock()
p1 = Thread(target=test1)
p1.start()
p2 = Thread(target=test2)
p2.start()
print("---g_num=%d---" % g_num)

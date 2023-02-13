from queue import Queue
from threading import Thread
import time

"""
Queue拥有所有需要的锁, 可以安全在任意多个线程间共享, 被所有线程共享
"""


def t_put(q):
    while 1:
        q.put('1')
        print('put')
        time.sleep(2)


def t_get(q):
    while 1:
        print(q.get())
        time.sleep(1)


q = Queue()
t_1 = Thread(target=t_put, args=(q,))
t_2 = Thread(target=t_get, args=(q,))
t_1.start()
t_2.start()

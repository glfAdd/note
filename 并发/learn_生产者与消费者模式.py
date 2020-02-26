import threading
import time
from queue import Queue

"""
通过容器解决生产者和消费者耦合问题
生产者和消费者彼此之间不直接通讯, 而通过阻塞队列来进行通讯, 所以生产者生产完数据之后不用等待消费者处理, 直接扔给阻塞队列, 消费者不找生产者要数据, 而是直接从阻塞队列里取
阻塞队列就相当于一个缓冲区, 平衡了生产者和消费者的处理能力

为什么要使用生产者和消费者模式
生产者就是生产数据的线程，消费者就是消费数据的线程。在多线程开发当中，如果生产者处理速度很快，而消费者处理速度很慢，那么生产者就必须等待消费者处理完，才能继续生产数据。同样的道理，如果消费者的处理能力大于生产者，那么消费者就必须等待生产者。为了解决这个问题于是引入了生产者和消费者模式。

put()       添加数据到队列
get()       从队列中取数据
qsize()     数据个数
"""

queue = Queue()


class Producer(threading.Thread):
    def run(self):
        global queue
        count = 0
        while True:
            if queue.qsize() < 1000:
                for i in range(100):
                    count = count + 1
                    msg = '生成产品' + str(count)
                    queue.put(msg)
                    print(msg)
            time.sleep(0.5)


class Consumer(threading.Thread):
    def run(self):
        global queue
        while True:
            if queue.qsize() > 100:
                for i in range(3):
                    msg = self.name + '消费了 ' + queue.get()
                    print(msg)
            time.sleep(1)


if __name__ == '__main__':
    for i in range(500):
        queue.put('初始产品' + str(i))
    for i in range(2):
        p = Producer()
        p.start()
    for i in range(5):
        c = Consumer()
        c.start()

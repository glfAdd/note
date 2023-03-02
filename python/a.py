from multiprocessing import Process, Queue
import os, time, random


def write(q):
    for value in ["A", "B", "C"]:
        print("write ---- %s" % value)
        q.put(value)
        time.sleep(2)


def read(q):
    while True:
        if not q.empty():
            value = q.get(True)
            print("write ---- %s" % value)
            time.sleep(4)
        else:
            break


if __name__ == "__main__":
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    w = Process(target=write, args=(q,))
    r = Process(target=read, args=(q,))
    # 启动子进程w，写入:
    w.start()
    # 等待w结束:
    w.join()
    # 启动子进程r，读取:
    r.start()
    r.join()

import multiprocessing
import os
import time
import logging

""" ============================ multiprocessing
当前进程
multiprocessing.current_process()


设置调试的日志
默认情况下，日志记录级别设置为NOTSET不生成任何消息
multiprocessing.log_to_stderr(logging.DEBUG)  设置调试的日志
"""

""" ============================ Process
用来创建子进程
def __init__(self, group, target, name, args, kwargs, *, daemon):
  - target
  - args
  - kwargs
  - name        进程实例的别名, Process-1
  - group


is_alive()
start()
run()           去调用target指定的函数，自定义类的类中一定要实现该方法
terminate()     强制终止进程，不会进行任何清理操作。如果该进程终止前，创建了子进程，那么该子进程在其强制结束后变为僵尸进程；如果该进程还保存了一个锁那么也将不会被释放，进而导致死锁。使用时，要注意
join([timeout]) 主线程等待子线程终止。timeout为可选择超时时间；需要强调的是，p.join只能join住start开启的进程，而不能join住run开启的进程 。


name        str     别名
daemon      bool
pid         int     当前进程实例的PID值
exitcode    int     子进程的退出代码. None如果流程尚未终止, 负值-N表示孩子被信号N终止
authkey     bytes
sentinel    int
daemon      bool    守护进程




默认情况: 在所有子进程退出之前，主程序不会退出
守护进程:
  - 主进程代码执行结束后就终止.
  - 内无法再开启子进程,否则抛出异常：AssertionError: daemonic processes are not allowed to havechildren

"""


class MyProcess(multiprocessing.Process):
    def __init__(self):
        super(self, MyProcess).__init__()

    def run(self):
        print('My Process')


def test(*args):
    time.sleep(2)
    print(multiprocessing.current_process().name)
    print(multiprocessing.current_process().name)
    print(*args, os.getpid())


if __name__ == '__main__':
    multiprocessing.log_to_stderr(logging.DEBUG)
    p = multiprocessing.Process(target=test, args=('a', 'b', 'c'))
    print(multiprocessing.current_process().name)
    print('父进程 %d' % os.getpid())
    p.start()
    print(p.exitcode)
    p.join()
    print(p.exitcode)

""" ============================ Queue 
进程之间通信, 使用Queue来传递消息


"""

""" ============================ Pool 


"""

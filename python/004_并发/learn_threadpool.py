import threadpool
import time

"""
ThreadPool
def __init__(self, num_workers, q_size=0, resq_size=0, poll_timeout=5):
    self._requests_queue = Queue.Queue(q_size)
    self._results_queue = Queue.Queue(resq_size)
    self.workers = []
    self.dismissedWorkers = []
    self.workRequests = {}
    self.createWorkers(num_workers, poll_timeout)

  - num_works               线程池中线程个数
  - q_size                  任务队列的长度限制，如果限制了队列的长度，那么当调用putRequest()添加任务时，到达限制长度后，那么putRequest将会不断尝试添加任务，除非在putRequest()设置了超时或者阻塞
  - resq_size               任务结果队列的长度
  - pool_timeout            工作线程如果从request队列中，读取不到request,则会阻塞pool_timeout,如果仍没request则直接返回

  - self._requests_queue    任务队列，通过threadpool.makeReuests(args)创建的任务都会放到此队列中
  - self._results_queue     字典，任务对应的任务执行
  - self.workers            工作线程list，通过self.createWorkers()函数内创建的工作线程会放到此工作线程list中
  - self.dismisssedWorkers  被设置线程事件，并且没有被join的工作线程
  - self.workRequests       字典，记录推送到线程池的任务，结构为requestID:request。其中requestID是任务的唯一标识，会在后面作介绍


创建任务放入到任务队列
def makeRequests(callable_, args_list, callback=None, exc_callback=_handle_thread_exception):
  - callable_       调用的函数名
  - args_list       list, 列表元素类型为元组，元组中有两个元素item[0]，item[1]，
                      item[0]为位置参数
                      item[1]为字典类型关键字参数
                      列表中元组的个数，代表启动的任务个数
  - callback        从任务结果队列中get结果，对result进行进一步处理
  - exc_callback    从任务结果队列中get结果，如果设置了异常，则需要调用异常回调处理异常


任务放入到队列中, 并执行
def putRequest(self, request, block=True, timeout=None):


阻塞，直到线程池中所有的线程都结束
def wait(self):


工作线程的启动
def createWorkers(self, num_workers, poll_timeout=5):


工作线程的退出
def dismissWorkers(self, num_workers, do_join=False):
def joinAllDismissedWorkers(self):
"""


# def add(a, b):
#     print '{0}+{1}={2}'.format(a, b, (a + b))
#     time.sleep(2)
#
#
# if __name__ == '__main__':
#     pool = threadpool.ThreadPool(2)
#     while 1:
#         data = [(None, {'b': 3, 'a': 2})]
#         reqs = threadpool.makeRequests(add, data)
#         [pool.putRequest(req) for req in reqs]
#     pool.wait()


def func(name):
    print('hi {}\n'.format(name))


if __name__ == '__main__':
    data = ['xijun.gong', 'xijun', 'gxjun']
    pool = threadpool.ThreadPool(5)
    pool.createWorkers()
    reqs = threadpool.makeRequests(func, data)
    [pool.putRequest(req) for req in reqs]
    pool.wait()

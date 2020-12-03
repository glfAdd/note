import queue

""" ============================ 拷贝原来的列表 """
# 先入先出 maxsize 设置队列最大长度
q = queue.Queue(maxsize=3)

q.put(1, block=False)  # 存入数据
q.put(2)
print(q.get())  # 获取数据
print(q.get(timeout=1))
print(q.qsize())
print(q.full())
print(q.get_nowait())  # 获取数据 当没有数据时直接抛出异常
print(q.get_nowait())

# lIFO队列----------------------------------
q = queue.LifoQueue()  # 后进先出
q.put(1)
q.put(2)
q.put(3)
print(q.get())
print(q.get())
print(q.get())

# 优先级队列----------------------------------
q = queue.PriorityQueue()  # 存储时设置优先级
q.put((2, 'asq2'))
q.put((1, 'asw1'))
q.put((1, 'asw5'))
q.put((4, 'ase3'))
q.put((10, 'asr4'))

print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(q.get())

# 双向队列----------------------------------
q = queue.deque()
q.append(123)
q.append(456)
q.appendleft(780)
print(q.pop())
print(q.popleft())

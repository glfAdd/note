from random import randint


""" ============================ iter
第一个参数: 必须是可调用对象
第二个参数: 哨值, 当迭代器返回这个值时抛出StopIteration异常, 停止迭代
"""


def callable_test1():
    return randint(1, 6)


a = iter(callable_test1, 3)
print(a)
for i in a:
    print(i)

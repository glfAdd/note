"""
Timer()
stmt: string 要计时的语句或者函数
setup: string 为stmt参数语句构建环境的导入语句


timeit()
执行一次
number: int 重复测试次数, 默认1000000


repeat()
执行n次
repeat: int 重复测试次数, 默认5
number: int 每个测试中调用被计时语句的次数, 默认1000000
"""

from timeit import Timer


def test1():
    n = 0
    for i in range(101):
        n += i
    return n


def test2():
    return sum(range(101))


def test3():
    return sum(x for x in range(101))


if __name__ == '__main__':
    t1 = Timer("test1()", "from __main__ import test1")
    t2 = Timer("test2()", "from __main__ import test2")
    t3 = Timer("test3()", "from __main__ import test3")
    print(t1.timeit(10000))
    print(t2.timeit(10000))
    print(t3.timeit(10000))
    print(t1.repeat(3, 10000))
    print(t2.repeat(3, 10000))
    print(t3.repeat(3, 10000))

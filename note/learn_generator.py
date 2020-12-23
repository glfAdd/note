"""
1. 包含yield的函数, 返回迭代器对象, 遇到 yield 函数会暂停并保存当前所有的运行信息, 返回 yield 的值, 并在下一次执行 next() 方法时从当前位置继续运行
2. 生成器的本质就是迭代器
3. 生成器包括两种: 生成器函数和生成器表达式


1. 生成器函数执行之后返回返回生成器, 并不会执行函数体
2. 执行了__next__()方法之后才会执行函数体, 并且获得返回值
3. next()内置方法, 内部调用生成器函数的__next__()方法
4. yield和return可以返回值, 但yield 不会结束函数

__next__ 相当于 next()
超出范围报错 StopIteration
"""


def generator():
    for i in range(1, 5):
        a = yield i
        print(a)


ret = generator()
print(next(ret))
ret.__next__()
ret.send('A')
for i in ret:
    print(i)

""" ============================  yield from
替代内层for循环
"""


# 嵌套
def g_test_1(*args):
    for i in args:
        for j in i:
            print(j)


a = [1, 2, 3]
b = ['A', 'B', 'C']
g_test_1(a, b)


# yield from
def g_test_2(*args):
    for i in args:
        # 调用iter(j)获取迭代器, x必须可迭代
        yield from i


for i in g_test_2(a, b, ):
    print(i)

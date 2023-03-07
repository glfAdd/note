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

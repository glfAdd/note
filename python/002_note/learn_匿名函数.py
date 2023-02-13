"""

https://zhuanlan.zhihu.com/p/78698111




"""


def test_1(a, b):
    return a + b


a_1 = test_1(1, 5)
print(a_1)

a_2 = lambda a, b: a + b
print(a_2(11, 22))

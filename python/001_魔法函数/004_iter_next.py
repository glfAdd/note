"""
container: 容器, 用来储存元素的一种数据结构, 如 list，set，dict，str 等
可迭代对象: 实现了 __iter__ 方法的对象, 这个方法返回可迭代对象
迭代器: 实现了 __next__ 方法的对象, 返回下一个元素
生成器: 包含 yield 的函数, 返回迭代器对象


for 循环原理:
1. for 调用 __iter__() 方法, 返回迭代器
2. for 调用 next() 方法, next 调用迭代器的 __next__(), 每次返回迭代器的下一个值,
3. 迭代器没有值抛出 StopIteration, for 循环退出
"""


class Test1:
    def __init__(self, num):
        self.num = num

    def __iter__(self):
        return self

    def __next__(self):
        if self.num > 10:
            raise StopIteration
        else:
            self.num += 1
            return self.num


class Test2:
    def __init__(self, num):
        self.num = num

    # def __iter__(self):
    #     return self

    def __next__(self):
        if self.num > 10:
            raise StopIteration
        else:
            self.num += 1
            return self.num


if __name__ == '__main__':
    t = Test1(7)
    for i in Test1(1):
        print(i)
    for i in Test2(1):
        print(i)
    # for i in range(7):
    #     print(t.__next__())

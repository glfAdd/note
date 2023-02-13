from random import randint

"""
python从可迭代的对象获取迭代器

__iter__
  - 返回当前对象的迭代器实例
  - 直观理解就是能用for循环进行迭代的对象就是可迭代对象. 比如：字符串, 列表, 元祖, 字典, 集合

__next__
  - 就是从上一个终止点开始，到下一个yield结束，返回值就是yield表达式的值
  - 返回容器中的下一个值, 直到抛出StopIteration异常

sent()
  - 可以传递参数给yield表达式
  - 生成器第一次使用必须是 None

next()
  - 内置函数 next() 通过迭代器调用 __next__ 方法返回下一项
  - 返回容器中的下一个值, 直到抛出StopIteration异常

iter()
  - 内置函数. 如果对象实现了__iter__方法可获取迭代器对象

yield
  - 类似 return
  - 迭代一次遇到yield时就返回yield后面的值
  - 下一次迭代时，从上一次迭代遇到的yield后面的代码开始执行


迭代: 扫描内存放不下数据时, 惰性获取数据方式, 一次获取一个数据

for ... in
  - 1. 调用可迭代对象的__inter__方法返回一个迭代器对象（iterator）
  - 2. 不断调用迭代器的__next__方法返回元素
  - 3. 迭代完成后, 处理StopIteration异常
"""

""" ============================ 可迭代对象 (iterable)
序列都可以迭代
实现__iter__或__getitem__方法的对象
"""

""" ============================ 迭代器 (iterator)
实现__iter__和next方法 
访问集合元素的一种方式, 从第一个元素开始访问, 直到所有的元素被访问完结束，不能后退. 可以记住遍历的位置
"""


class Test(object):
    def __init__(self, data=1):
        self.data = data

    def __iter__(self):
        return self

    def __next__(self):
        if self.data > 5:
            raise StopIteration
        else:
            self.data += 1
            return self.data


a = Test(3)
print(iter(a))
print(next(a))
for item in Test(3):
    print(item)


class FruitShop(object):
    def __getitem__(self, i):
        return self.fruits[i]


shop = FruitShop()
print(shop)
shop.fruits = ["apple", "banana"]
print(shop[1])
for item in shop:
    print(item)

""" ============================ 生成器 (generator)
包含关键字 yield 的函数, 不会执行任何函数代码, 直到对调用next()
函数的返回值是一个生成器对象
第一次调用时必须先next()或send(None)，否则会报错
"""


def foo():
    print('第一次进入')
    while True:
        one = yield
        print(one)
        two = yield
        print(two)


# 返回一个生成器, 函数不会执行
f = foo()
# 进入函数执行代码, 遇到yield函数返回
f.send(None)
# 再次进入函数体，接着冻结的代码继续执行，把111传给变量one, 遇到yield函数返回
f.send(222)


def fun():
    for i in range(20):
        x = yield i
        print('good', x)


a = fun()
print(a.__next__())
print(a.send(5))

""" ============================ 生成器表达式
是列表推倒式的生成器版本, 返回一个生成器对象而不是列表对象
"""
a_list = (x for x in range(10))

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

# 逐行读取文件, 直到遇到空行或文件结尾为止
with open('learn_yield.py') as f:
    for i in iter(f.readline, '\n'):
        print(i)

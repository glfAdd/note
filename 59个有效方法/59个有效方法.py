# -*-coding=utf-8-*-

"""

切割字符串
实现了__getitem__和__setitem__方法
"""

""" ============================ 生成器表达式 """
# 推导式: 当输入的数据非常大时消耗很多内存
# 生成器表达式: 调动next返回下一个值, 不会内存激增
# value = (x for x in open('59.md'))
# print(value)

# enumerate: 把迭代器包装成生成器
""" ============================ zip """
# 其中一个遍历完就停止了
# python3: 把2个或以上的迭代器, 包装为生成器
# python2: 把2个或以上的迭代器, 直接返回list, 大文件内存激增.
""" ============================ 修改闭包外面的值
表达式引用变量时,解释器按照顺序遍历
1. 当前函数作用域
2. 任何外围作用域(如包含当前函数的作用域)
3. 包含当前代码的模块, 叫全局作用域
4. 内置作用域
如果都没有抛出NameError异常

给变量赋值时
1. 如果当前作用域有了, 则赋新值
2. 如果当前作用域没有, 则定义新变量

python3: nonlocal
在上层作用域寻找变量, 但不能延伸到模块级别
如果再闭包中使用, 使用的是外层函数的变量

python2: 可变类型变量, list set dict都可以
"""


def test1(one, two):
    tag = 2

    def test2(x):
        nonlocal tag
        tag = one + two + x
        return tag

    return test2


fun_1 = test1(1, 5)
print(fun_1(9))


def test3(one, two):
    tag = [0]

    def test4(y):
        tag[0] = one + two + y
        return tag[0]

    return test4


fun_2 = test3(2, 4)
print(fun_2(5))

""" ============================ 直接返回列表的函数使用生成器 """


# 迭代器只能迭代一次
# 迭代器可以使用 * 解包


def test5(word):
    l = []
    if not word:
        l.append(0)
    for index, item in enumerate(word):
        if item == ' ':
            l.append(index)
    return l


fun_3 = test5('hello word China Ha Ha')
for i in fun_3:
    print(i)


def test6(word):
    if not word:
        yield 0
    for index, item in enumerate(word):
        if item == ' ':
            yield index


fun_4 = test6('hello word China Ha Ha')
print(*fun_4)

""" ============================ 必要的时候函数抛出异常, 返回错误的详细信息, 不return None """


def test7(a, b):
    try:
        return a / b
    except Exception as e:
        return None


def test8(a, b):
    # 当b为0时有异常
    try:
        return a / b
    except Exception as e:
        raise ValueError('number error') from e

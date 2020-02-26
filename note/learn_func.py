import datetime

""" ============================ 位置可变参数 """
# 变长参数传递参数时, 会先转成元组.
# 如果使用带有*的生成器做参数, 必须先把生成器迭代一轮, 并把生成器的每一个值放入元组. 可能消耗大量内存导致程序崩溃.
# 当确定接收的参数较少时才这样使用


""" ============================ 动态默认参数 
1. 默认参数会在每个模块加载时算出, 很多模块在程序启动时加载
2. 动态默认参数通常设为None, 并在函数内部给默认参数赋值. 
3. 如果默认参数的实际类型是可变类型, 一定要使用None做为默认参数.
"""


def test10(name, time=datetime.datetime.now()):
    # 两次的结果是相同的
    print('{}---{}'.format(name, time))


test10('xiao')  # xiao---2019-06-24 23:07:17.032463
test10('xiao')  # xiao---2019-06-24 23:07:17.032463


def test11(name, time=None):
    time = datetime.datetime.now() if time is None else time
    print('{}---{}'.format(name, time))


test11('ming')  # ming---2019-06-24 23:09:44.330391
test11('ming')  # ming---2019-06-24 23:09:44.330397

""" ============================ 强制使用关键字参数 """


# python3: * 之后的必须使用关键字参数, 否则报错
def test12(x, y, *, name='xiao', age=12):
    print('{} {} {} {}'.format(x, y, name, age))


test12(34, 44, name='xiao')


# python2:
# 1. 先使函数接收**kwargs参数
# 2. 用pop方法将期望的参数取走, 如果没有回使用默认值
# 3. 如果没有传或者传错了手动抛出异常
def test13(name, age, **kwargs):
    address = kwargs.pop('address', 'China')
    if kwargs:
        # 这里可以抛出异常
        print('传递的参数错误')
    print('{} {} {}'.format(name, age, address))


test13('xiao', 44, address='ShangHai')

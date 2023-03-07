"""
1. yield from 完全代替了内层的 for 循环。
2. yield from x 表达式对 x 对象所做的第一件事是，调用 iter(x)，从中获取迭代器。因此，x 可以是任何可迭代的对象。
3. yield from 会自动处理异常
4. 生成器退出时抛出 StopIteration(expr)异常


    调用方：调用委派生成器的客户端（调用方）代码
    委托生成器：包含yield from表达式的生成器函数
    子生成器：yield from后面加的生成器函数


教程
https://juejin.im/post/6844903632534503437




"""

print(""" ============================ 简单使用 """)


def test_1():
    a = ['aa', 'bb', 'cc']
    for i in a:
        for j in i:
            yield j


for i in test_1():
    print(i)


def test_2():
    a = ['aa', 'bb', 'cc']
    for i in a:
        yield from i


print('--------')
for i in test_2():
    print(i)

print(""" ============================ 子生成器 """)


# 子生成器
def average_gen():
    total = 0
    count = 0
    average = 0
    while True:
        new_num = yield average
        if new_num is None:
            break
        count += 1
        total += new_num
        average = total / count

    # 每一次return，都意味着当前协程结束。
    return total, count, average


# 委托生成器
def proxy_gen():
    while True:
        # 只有子生成器要结束（return）了，yield from左边的变量才会被赋值，后面的代码才会执行。
        # 委托生成器没有办法对子生成器的值进行拦截
        total, count, average = yield from average_gen()
        print("计算完毕！！\n总共传入 {} 个数值， 总和：{}，平均数：{}".format(count, total, average))


# 调用方
def main():
    calc_average = proxy_gen()
    next(calc_average)  # 预激协程
    print(calc_average.send(10))  # 打印：10.0
    print(calc_average.send(20))  # 打印：15.0
    print(calc_average.send(30))  # 打印：20.0
    calc_average.send(None)  # 结束协程

    # 此处再调用 send ，由于上一协程已经结束，将重开一协程
    print(calc_average.send(10))  # 打印：10.0
    calc_average.send(None)  # 结束协程


main()

print(""" ============================ 双向通道 """)
# 双向通道: 调用方可以通过send()直接发送消息给子生成器，而子生成器yield的值，也是直接返回给调用方


print(""" ============================ 自动捕获异常 """)


# 如果不用 yield from 需要手动捕获异常


def average_gen_2():
    total = 0
    count = 0
    average = 0
    while True:
        new_num = yield average
        if new_num is None:
            break
        count += 1
        total += new_num
        average = total / count
    return total, count, average


def main_2():
    calc_average = average_gen_2()
    next(calc_average)  # 预激协程
    print(calc_average.send(10))  # 打印：10.0
    print(calc_average.send(20))  # 打印：15.0
    print(calc_average.send(30))  # 打印：20.0

    try:
        calc_average.send(None)
    except StopIteration as e:
        print('error')
        total, count, average = e.value
        print("计算完毕！！\n总共传入 {} 个数值， 总和：{}，平均数：{}".format(count, total, average))


main_2()

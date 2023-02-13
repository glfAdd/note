def customer():
    print('run -- customer')
    tag = True
    while True:
        n = yield tag
        print("我拿到了{}!".format(n))
        if n == 3:
            tag = False


def producer(customer):
    print('run -- production')
    n = 5
    while n > 0:
        # yield给主程序返回消费者的状态
        yield customer.send(n)
        n -= 1


# 不执行任何代码, 返回生成器对象
c = customer()
c.send(None)
p = producer(c)
for tag in p:
    if not tag:
        print("我只要3,4,5就行啦")
        break
print("程序结束")

# 子生成器
def test_1():
    a = 0
    while True:
        tmp = yield a
        if a == 0:
            break
        print("%s -----" % tmp)
        a += 1


# 委托生成器
def test_2():
    while True:
        for i in test_1():
            print(i)
        # yield from test_1()

# def test_3():
#     while True:


# 调用方
def main():
    t = test_2()
    next(t)
    print(t.send(10))
    print(t.send(20))


if __name__ == "__main__":
    main()

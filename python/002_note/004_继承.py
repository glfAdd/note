class A:
    def test(self):
        print("a")

    # 私有的方法和属性不会被继承
    def __learn(self):
        print("learn")


class B:
    def test(self):
        print("b")


class C(A, B):
    def run(self):
        print("run")


if __name__ == '__main__':
    aa = C()
    aa.test()
    # __mro__ 或 mro() 查看调用方法的时候搜索的顺序，找到就停止搜索
    print(C.__mro__)
    print(C.mro())

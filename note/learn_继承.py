"""





"""


# 多继承时如果方法有重名的，执行先继承的。避免出现方法重名的情况
# __mro__ 查看调用方法的时候搜索的顺序，找到就停止搜索
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


aa = C()
aa.test()
print(C.__mro__)

"""
类调用类方法
类调用静态方法
实例对象调用类方法
实例对象调用静态方法
"""


class Person(object):
    number = 2017
    __password = "hello"

    # 只创建对象。重写是必须调用父类的方法。有返回值
    # cls指向类对象，至少有一个参数cls，调用是传参数
    def __new__(cls):
        print("只用来创建对象")
        return object.__new__(cls)

    # 初始化对象。
    def __init__(self, new_name, new_height):
        self.name = new_name
        # 属性前面加上 __ 表示隐藏属性，外界不能直接访问
        self.__height = new_height

    # 获取对象的信息是调用。比如print这个对象
    def __str__(self):
        b = ("我的名字是。。。%s" % (self.name))
        return b

    # 对象被释放前调用。当引用计数为0时调用。程序结束时调用
    def __del__(self):
        print("对象讲被释放")

    @classmethod
    def add_person(cls):
        print("添加人")

    @staticmethod
    def print_person():
        print("")

    def eat(self):
        print("他的年龄是" % (self.age))

    def __run(self):
        print("正在跑")

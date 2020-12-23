class Person(object):
    __instance = None
    __init_flag = False

    # 两个参数
    def __new__(cls, name):
        print(222, name)
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            return cls.__instance

    # 两个参数
    def __init__(self, name):
        print(1111, name)
        if Person.__init_flag == False:
            self.name = name
            Person.__init_flag = True


a = Person("黑")
b = Person("白")
print(a.name)
print(b.name)

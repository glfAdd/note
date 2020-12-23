"""

init 通常用于初始化一个新实例，控制这个初始化的过程，比如添加一些属性， 做一些额外的操作，发生在类实例被创建完以后。它是实例级别的方法。

new 通常用于控制生成一个新实例的过程。它是类级别的方法。



"""




class Test(object):
    __instance = None

    def __new__(cls, *args,**kwargs):

        if cls.__instance is None:
            cls.__instance = super().__new__(cls, *args,**kwargs)
            return cls.__instance
        else:
            return cls.__instance

    def __init__(self):
        print(1111)


if __name__=='__main__':
    a = Test()
    print(id(a))

    b = Test()
    print(id(b))















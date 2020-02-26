import time

""" ============================ 实例方法
1. 第一个参数必须是实例对象, 一般self, 通过它来传递实例的属性和方法

1. 只能由实例对象调用.
2. 实例方法权限最大
"""

""" ============================ 类方法
1. @classmethod
2. 第一个参数必须是当前类对象, 一般cls

1. 不能使用实例的属性和方法
2. 实例对象和类对象都可以调用.

场景:
1. 类方法是将类本身作为对象进行操作的方法.假设有个方法, 且这个方法在逻辑上采用类本身作为对象来调用更合理, 那么这个方法就可以定义为类方法.
2. 另外, 如果需要继承, 也可以定义为类方法.

例子:
假设我有一个学生类和一个班级类, 想要实现的功能为:
    1. 执行班级人数增加的操作、获得班级的总人数；
    2. 学生类继承自班级类, 每实例化一个学生, 班级人数都能增加；
    3. 最后, 我想定义一些学生, 获得班级中的总人数.
实例化的是学生, 但是如果我从学生这一个实例中获得班级总人数, 在逻辑上显然是不合理的.
同时, 如果想要获得班级总人数, 如果生成一个班级的实例也是没有必要的.
"""

""" ============================ 静态方法
1. @staticmethod 
2. 参数随意, 没有“self”和“cls”参数, 但是方法体中不能使用类或实例的任何属性和方法

调用:
1. 不能使用实例的属性和方法
2. 实例对象和类对象都可以调用

场景:
用来存放逻辑性的代码, 逻辑上属于类, 但是和类本身没有关系, 也就是说在静态方法中, 不会涉及到类中的属性和方法的操作.
可以理解为, 静态方法是个独立的、单纯的函数, 它仅仅托管于某个类的名称空间中, 便于使用和维护.

例子:
我想定义一个关于时间操作的类, 其中有一个获取当前时间的函数.
若要获得当前时间的字符串时, 并不一定需要实例化对象, 此时对于静态方法而言, 所在类更像是一种名称空间.
其实, 我们也可以在类外面写一个同样的函数来做这些事, 但是这样做就打乱了逻辑关系, 也会导致以后代码维护困难.
"""


class ClassTest(object):
    __num = 0

    @classmethod
    def addNum(cls):
        cls.__num += 1

    @classmethod
    def getNum(cls):
        return cls.__num

    # 这里我用到魔术方法__new__, 主要是为了在创建实例的时候调用累加方法.
    def __new__(self):
        ClassTest.addNum()
        return super(ClassTest, self).__new__(self)


class Student(ClassTest):
    def __init__(self):
        self.name = ''


a = Student()
b = Student()
print(ClassTest.getNum())


class TimeTest(object):
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    @staticmethod
    def showTime():
        return time.strftime("%H:%M:%S", time.localtime())


print(TimeTest.showTime())
t = TimeTest(2, 10, 10)
nowTime = t.showTime()
print(nowTime)

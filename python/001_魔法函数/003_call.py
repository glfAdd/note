"""
1. 可调用对象: 可以把一对括号 () 应用到某个对象身上都可称之为可调用对象
2. __call__ 作用: 将类的实例对象变为可调用对象
3. x() 等同于 x.__call__() 的缩写
"""


class Test:
    def __init__(self, name):
        self.name = name

    def __call__(self, name):
        self.name = name

    def __str__(self):
        return 'name: %s' % self.name


if __name__ == '__main__':
    t = Test('Tom')
    print(t)
    t('Jack')
    print(t)
    t.__call__('Luck')
    print(t)

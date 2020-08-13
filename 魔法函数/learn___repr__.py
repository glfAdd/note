# -*-coding=utf-8-*-

"""
print时有哪个调用哪个
同时存在print时调用__str__
__repr__在交互模式下可以生效, __str__不能
"""


class Test(object):
    name = 'xiaoming'
    age = 12

    def __init__(self):
        self.num = 12

    def __str__(self):
        return '{}--str'.format(self.num)

    def __repr__(self):
        return '{}--repr'.format(self.num)

    def run(self, a):
        print(a)

    eat = run


t = Test()
print(t)
t.run('123')
t.eat('456')

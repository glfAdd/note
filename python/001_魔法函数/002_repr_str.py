# -*-coding=utf-8-*-
"""
__repr__在交互模式下可以生效, __str__不能
"""


class Test(object):
    name = 'Tom'
    age = 12

    def __init__(self):
        self.num = 12

    def __str__(self):
        return '{}--str'.format(self.num)

    def __repr__(self):
        return '{}--repr'.format(self.num)


t = Test()
print(t)

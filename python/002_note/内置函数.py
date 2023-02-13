""" ============================ __getattr__ """


# 内建函数，当调用的属性或者方法不存在时，该方法会被调用
# https://www.jianshu.com/p/61c10a59fdab

class Student(object):
    def __getattr__(self, attr):
        if attr in ('name', 'age', 'score'):
            print(attr)
        else:
            raise AttributeError('Unkonw attribute : %s' % attr)


s = Student()
s.name
s.age


class Student(object):
    def __getattr__(self, attr):
        def _func(*arg, **kwargs):
            print(arg, '======', kwargs)

        if not attr.startswith('_'):
            _func.func_name = attr
            return _func
        raise AttributeError('Unkonw attribute : %s' % attr)


a = Student()
a.test(12)
a.name('a', 'b', c=1, d=2)
a.name('a', 'b', c=1, d=2)
# a._age('a', 'b', c=1, d=2)

""" ============================ 如果没有目录就创建 """
""" ============================ 如果没有目录就创建 """
""" ============================ 如果没有目录就创建 """
""" ============================ 如果没有目录就创建 """
""" ============================ 如果没有目录就创建 """
""" ============================ 如果没有目录就创建 """
""" ============================ 如果没有目录就创建 """
""" ============================ 如果没有目录就创建 """
""" ============================ 如果没有目录就创建 """
""" ============================ 如果没有目录就创建 """
""" ============================ 如果没有目录就创建 """
""" ============================ 如果没有目录就创建 """
""" ============================ 如果没有目录就创建 """
""" ============================ 如果没有目录就创建 """
""" ============================ 如果没有目录就创建 """
""" ============================ 如果没有目录就创建 """
""" ============================ 如果没有目录就创建 """
""" ============================ 如果没有目录就创建 """
""" ============================ 如果没有目录就创建 """
""" ============================ 如果没有目录就创建 """
""" ============================ 如果没有目录就创建 """
""" ============================ 如果没有目录就创建 """
""" ============================ 如果没有目录就创建 """
""" ============================ 如果没有目录就创建 """
""" ============================ 如果没有目录就创建 """
""" ============================ 如果没有目录就创建 """

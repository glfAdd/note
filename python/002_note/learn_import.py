# -*- coding: utf-8 -*-

"""
__import__ 使用

__import__() 函数用于动态加载类和函数
evel参数，指定是使用绝对导入还是相对导入。 0(默认值)表示只执行绝对导入
"""
if __name__ == '__main__':
    # # 导入模块 相当于 import
    # a = __import__('a.b.c')
    # # 获取类
    # c = getattr(a.b.c, 'tests')
    # # 实例化对象
    # d = c()
    # # 调用方法
    # getattr(d, 'ccc')(1111)

    # 导入模块 相当于 from ... import ...
    a = __import__('a.b.c', fromlist=('tests',))
    print(dir(a))
    # 获取类
    c = getattr(a, 'tests')
    # 实例化对象
    d = c()
    # 调用方法
    getattr(d, 'ccc')(1111)

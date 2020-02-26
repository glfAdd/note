"""
dis库是python(默认的CPython)自带的一个库, 可以用来分析字节码

命令
python -m dis xxx.py


文档
https://docs.python.org/2/library/dis.html



Python代码是先被编译为字节码后，再由虚拟机来执行字节码, pyc文件主要就是用于存储字节码指令的


>>                  跳转到指定索引的命令
LOAD_VALUE          把数压到栈中
LOAD_GLOBAL         加载全局变量名称
LOAD_FAST           加载本地变量名称
LOAD_NAME
LOAD_CONST          加载常量
SETUP_LOOP          循环代码块入栈, (to 26)可理解为当前指令到26索引前的为循环块
BINARY_ADD
BINARY_MULTIPLY
RETURN_VALUE        返回值
POP_JUMP_IF_FALSE

代码行数  字节码索引  指令名称  指令的参数  计算后实际参数

 14           0 LOAD_GLOBAL              0 (print)
              2 LOAD_FAST                0 (a)
              2 LOAD_FAST                0 (a)
              4 CALL_FUNCTION            1
              6 POP_TOP




"""
import dis

"""
dis.dis()
"""

a3 = '全局变量'


def test1(a):
    print(a)
    print(a3)
    # a3='1'


test1('参数')

dis.dis(test1)

print(""" ============================ 变量作用域 """)
# dis.dis([bytesource])，
# 参数为一个代码块，可以得到这个代码块对应的字节码指令序列

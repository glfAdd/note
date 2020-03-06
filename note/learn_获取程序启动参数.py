import argparse

""" ============================ 参考
https://www.cnblogs.com/cuhm/p/10643765.html

自动生成帮助和使用手册，并在用户给程序传入无效参数时报出错误信息
"""

""" ============================ 添加参数
1. 位置参数-positional arguments
    参数名前缀不带 - 和 --, 按照顺序进行解析, 在命令中必须出现, 否则报错
    
    parser.add_argument("a")
    parser.add_argument("b")
    parser.add_argument("c")


2. 可选参数-optional arguments
    参数名前缀带 - 和 --
    前缀是-的为短参数, 前缀是--是长参数, 两者可以都有, 也可以只有一个,效果一样 -h --help
    可选参数在位置参数的后面, 不影响位置参数的解析顺序。

    action      'store_true' 使参数值只能为True或False, 触发是为True, 没触发为False
    type        指定参数类别, 默认str, 传入数字要定义(int float)
    help        提示信息
    default     默认值
    metavar     在 usage 说明中的参数名称, 对于必选参数默认就是参数名称, 对于可选参数默认是全大写的参数名称.
    choices     限定值的取值范围
    
    parser.add_argument('--batch-size', type=int, default=64, metavar='N', help='input batch size for training (default: 64)')
    parser.add_argument('--momentum', action='store_true', default=False, help='disables CUDA training')
"""

""" ============================ 解析参数

"""

# 创建解析器
#
parser = argparse.ArgumentParser(description='使用description可以设置一些简单的描述')

# 添加位置参数
parser.add_argument('a', help='位置参数')

# 添加可选参数, 如果有b, 则必须有值, 否则报错
# python learn_获取程序启动参数.py 1 -b 2
# python learn_获取程序启动参数.py 1 -b=2
parser.add_argument('-bb', type=int, help='input b int')

# action="store_true" 使c只能为True和False, 触发是为True, 没触发为False
# python learn_获取程序启动参数.py 1 -c
parser.add_argument('-c', '--count', action='store_true', help='input c int')

# 限定值的取值范围
# python learn_获取程序启动参数.py 1 -d d1
# python learn_获取程序启动参数.py 1 -d=d1
parser.add_argument('-d', choices=['d1', 'd2', 'd3'], help='input d str')

# 互斥组, 内只能出现一个, 否则报错
g = parser.add_mutually_exclusive_group()
g.add_argument('-e', help='互斥组, e')
g.add_argument('-f', help='互斥组, f')

args = parser.parse_args()
print('a', args.a)
print('b', args.b)
print('c', args.c)
print('d', args.d)
print('d', args.e)
print('d', args.f)

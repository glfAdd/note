"""
Environs是解析环境变量的Python库
启动程序的参数可以通过两种方式配置: 命令行参数或环境变量

安装:
pip install environs
"""

import os
from environs import Env
from marshmallow.validate import OneOf, Length, Email

""" ============================ os.environ
系统的 os.environ 保存了系统的环境变量, 这种方式缺点:
    1. 如果环境变量是临时的, 没测都需要设置
    2. 设置成永久的需要修改系统文件
    3. 不能设置类型, 都是字符串
"""
print(os.environ)
# print(os.environ['VAR1'])
print(os.environ.get('VAR1', '没有'))

""" ============================ 使用 environs 
读取环境变量, 支持不同数据类型
    env.str
    env.bool
    env.int
    env.float
    env.decimal
    env.list (accepts optional subcast keyword argument)
    env.dict (accepts optional subcast keyword argument)
    env.json
    env.datetime
    env.date
    env.timedelta (assumes value is an integer in seconds)
    env.url
    env.uuid
    env.log_level
    env.path (casts to a pathlib.Path)

首先设置环境变量, 这里 VAR3 是列表，我们可以直接用逗号分隔开来
export VAR1=300
export VAR2='1984-06-25'
export VAR3=1,222
export VAR4='{"name": "germey", "age": 25}'
"""
env = Env()
print(env.int('VAR1', 1))
print(env.date('VAR2', '2020-12-20'))
print(env.list('VAR3', [1, 1]))
print(env.json('VAR4', {}))

""" ============================ 变量名前缀比配
比如 MYSQL_HOST, REDIS_HOST 这种情况, 会根据前缀将名字区分开, 里面都可应用 HOST
"""
with env.prefixed('MYSQL_'):
    host = env('HOST', 'localhost')
with env.prefixed('REDIS_'):
    host = env('HOST', 'localhost')

""" ============================ 判断环境变量是否合法 """
env.int('VAR1', validate=OneOf([1, 2, 3]), error='VAR1 不在选择范围内')
env.json('VAR4', validate=Length(min=1), error='VAR4 长度错误')

""" ============================ 将环境变量写入文件 """
# 此方法默认会读取本地当前运行目录下的 .env 文件
env.read_env()
with env.prefixed('MYSQL_'):
    print(env.str('HOST'))
    print(env.str('PORT'))

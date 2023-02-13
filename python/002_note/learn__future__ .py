"""
Python的每个新版本都会增加一些新的功能，或者对原来的功能作一些改动。有些改动是不兼容旧版本的，
也就是在当前版本运行正常的代码，到下一个版本运行就可能不正常了

__future__目的是把下一个版本的特性导入到当前版本，这样我们就可以在当前版本中测试一些新版本的特性，从而使得python未来版本的迁移更加容易。
future语句是一种针对编辑器的指令，指明某个特定模块应当使用在某个python发行版中成为标准特性的语法或语义。

future语句必须在靠近模块开头的位置出现。只有以下内容可以放在future语句之前。
1、模块的文档字符串
2、注释
3、空行
4、其他future语句

__future__.py文件语法格式
FeatureName=_Feture(OptionalRelease,MandatoryRelease,CompilerFlag)
OptionalRelease记录了一个特性首次发布时的python版本。
MandatoryRelease表示该特性会变成语言的一部分的预测时间，其他情况MandatoryRelease用来记录这个特性是何时成为语言的一部分的，从该版本往后，使用该特性将不需要future语句，不过大多数人还是会加上对应的import。MandatoryRelease也可能是None，表示这个特性已经被撤销。
CompilerFlag是一个（位）标记，对于动态编译的代码，需要将这个标记作为第四个参数传入内建函数compile()中已开启对应的特性。
"""

# absolute_import
#
# 包结构:
# pkg/
# pkg/init.py
# pkg/main.py
# pkg/string.py
#
# 如果你在main.py中写import string
# Python 2.5或之前, Python会先查找当前目录下有没有string.py, 若找到了，则引入该模块，然后你在main.py中可以直接用string了。
# 如果忽略掉同目录的string.py而引入系统自带的标准string.py。需要from __future__ import absolute_import
# 这样，就可以用import string来引入系统的标准string.py, 用from pkg import string来引入当前目录下的string.py了


# unicode_literals
#
# 将模块中显式出现的所有字符串转为unicode类型
# 2.x里的字符串用'xxx'表示str，Unicode字符串用u'xxx'
# 3.x中，默认的编码采用了unicode, 并取消了前缀u 因此，写u'xxx'和'xxx'是完全一致的
#
# 2.x中
# 对于str类型的字符串，调用len()和遍历时，其实都是以字节为单位的，同一个字符使用不同的编码格式，长度往往是不同的。
# 对unicode类型的字符串调用len()和遍历才是以字符为单位
# len('哈哈')  长度是 6
# len(u'哈哈') 长度是2


# division
#
# 精确整除
# 2.x中 10/3 得到 3
# 3.x中 10/3 得到 3.3333333333333335

# generators
#
# 使用生成器.能够产生能保存当前状态的函数.


# with_statement
#
# with 语句适用于对资源进行访问的场合，确保不管使用过程中是否发生异常都会执行必要的“清理”操作，释放资源
# 使用with open("file name ") as xx
# 比如文件使用后自动关闭、线程中锁的自动获取和释放
# https://www.ibm.com/developerworks/cn/opensource/os-cn-pythonwith/


# nested_scopes
#
# 当需要修改第三方python包的某个类的某个方法时，这种修改方式非常有用。


from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import division
from __future__ import generators
from __future__ import generator_stop
from __future__ import print_function
from __future__ import nested_scopes
from __future__ import with_statement

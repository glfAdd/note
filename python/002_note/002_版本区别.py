""" ============================ 字符串
Python2
str         每个字节8个二进制序列, 转为unicode需要decode
unicode     unicode字符序列, 转为二进制需要encode

Python3
str         unicode字符序列
bytes       每个字节8个二进制序列
"""

""" ============================ ASCII
Python2
如果只包含7位的ASCII字符, unicode和str可以当成一种类型处理互相操作.

Python3
如果只包含7位的ASCII字符, unicode和str是不同类型, 即使空字符串也不行.
"""

""" ============================ open
open('xx', 'w') python2默认二进制. python3默认utf-8, 只接受unicode的字符, 不接受二进制
open('xx', 'wb') 可以同时兼容python2和python3
"""


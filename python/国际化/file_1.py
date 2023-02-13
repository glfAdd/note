# -*- coding: utf-8 -*-
from i18n.i18n import I18nBase

"""
cpython 源码 Tools/i18n 下载地址
https://github.com/python/cpython/tree/main/Tools/i18n




https://www.cnblogs.com/JentZhang/p/16775758.html
https://snapcraft.io/poedit
https://github.com/python/cpython/tree/main/Tools/i18n
https://blog.csdn.net/weixin_39517298/article/details/121593399




1. 生成 *.pot, pygettext.py 从 *.py 文件中提取所有被标记成需要本地化的字符串, 在 _() 里面的, 其他的字符串不被提取
$ python i18n/pygettext.py -o abc.pot file_1.py

2. 改名为 *.po 文件, 否则生成 *.mo 文件是报错时报错
	[Errno 2] No such file or directory: 'resource.pot.po'
	
3. 复制多个, 每个语言一个 *.po 文件, 并进行编辑

4. 将每种语言的 po 文件编译为 gettext 可读写的二进制 mo 文件
$ python i18n/msgfmt.py -o zh-CN/LC_MESSAGES/abc.mo zh-CN/LC_MESSAGES/abc.po
$ python i18n/msgfmt.py -o en-US/LC_MESSAGES/abc.mo en-US/LC_MESSAGES/abc.po
"""

_ = I18nBase.get_i18n(file_name='abc', languages=['zh-CN', 'en-US'])
# _ = I18nBase.get_i18n(file_name='abc', languages=['en-US', 'zh-CN'])
a = _("hello")
b = _("保存")
print(a)
print(b)

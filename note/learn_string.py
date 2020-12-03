"""
a = "aa"
b = "bb"
c = a + b (aabb)

# 索引
a[0]	a[-1]	a[len(a) - 1]
a[2:5]	a[2:-1]	a[2:]	a[:-3]
a[2:-1:2] (步长默认为1)
将字符串倒序3种方式a[-1:0:-1] a[-1::-1] a[::-1]
IndexError:string index out of range

a.find("aa")	查找,找到返回索引，没找到返回-1
a.rfind("aa")	从右边开始找
a.index("aa")	查找,找到返回索引，没找到报异常ValueError:substring not found
a.rindex("aa")	从右边开始找

a.count("aa")		aa出现次数
a.count("aa", start=1, end=-2)	指定范围

a.replace("aa", "bb")		bb替换aa，只替换一次
a.replace("aa", "bb", 4)	制定替换次数
a.replace("aa", "bb", a.count("aa")-2)

a.split()			切割掉素有的空格和\t，返回list
a.split("aa")		用aa切割字符串，返回list
a.split("aa", 3)	切3次
a.capitalize()		第一个字母大写
a.title()			每个单词第一个字母大写
a.startswith("aa")	true false
a.endwith("aa")		true false
a.lower()			所有字符小写
a.upper()			所有字符大写
a.ljust(20)			左对齐，长度20，不够空格补齐
a.rjust(20)			右
a.center(20)		中
a.lstrip()			删除左边空格和\t
a.rstrip()			删除右
a.strip()			删除两边
a.partition("aa")	用aa将字符串分为3部分
a.rpartition("aa")	右边开始
a.splitlines()		用\n分割，返回list
a.isalpha()			都是字母 true false
a.isdigit()			都是数字 true false
a.isalnum()			只有数字、字母 true false
a.isspace()			只有空格 true false
len(a)				长度

每个元素后面加上"-"组成新字符串
a = "-"
b = ["aa", "bb", "cc"]
a.join(b)
aa-bb-cc'
"""
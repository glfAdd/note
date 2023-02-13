import os

print(os.path)

print('-------------------------------------------- 判断')
'''
os.path.exists()
os.path.isfile()
os.path.isdir()
os.path.islink()
os.path.isabs()
os.path.ismount()
'''

print('-------------------------------------------- __file__')
# 文件路径的变量
print(__file__)

print('-------------------------------------------- split')
# 路径切割, 将最后一个 "/" 切割, 两边用元组返回
print(os.path.split('/home/Tom/a.py'))
print(os.path.split('/home/Tom/'))
print(os.path.split('/home/Tom'))

print('-------------------------------------------- dirname')
# 文件或文件夹 的最里层目录
print(os.path.dirname('/home/Tom/a.py'))
print(os.path.dirname('/home/Tom/'))
print(os.path.dirname('/home/Tom'))

print('-------------------------------------------- basename')
# 最后一个 "/" 后的文件或文件夹
print(os.path.basename('/home/Tom/a.py'))
print(os.path.basename('/home/Tom/'))
print(os.path.basename('/home/Tom'))

print('-------------------------------------------- join')
# 路径拼接
# 每两个参数中间加上路径符号
# 路径符号过多重复会导致路径错误
print(os.path.join('home/', 'Lucy', 'code', 'a.py'))
print(os.path.join('/home/', 'Lucy', 'code', 'a.py'))
# /Lucy/code/a.py
print(os.path.join('/home/', '/Lucy', 'code', 'a.py'))

print('-------------------------------------------- splitext')
# 扩展名分隔, 与 split 类似
print(os.path.splitext('/home/Tom/a.py'))
print(os.path.splitext('/home/Tom/'))
print(os.path.splitext('/home/Tom'))

print('-------------------------------------------- splitdrive')
# # windows 磁盘分隔符
# # 当第 2 个字符是 ":" 时切割, 否则返回值第一个元素为空
# print(os.path.splitdrive('/home/Tom/a.py'))
# print(os.path.splitdrive('x:\\test.py'))
# print(os.path.splitdrive(r'T:\home\Tom/a.py'))
# print(os.path.splitdrive(r'TT:\home\Tom\a.py'))

print('-------------------------------------------- abspath')
# 绝对路径
print(os.path.abspath('.'))
print(os.path.abspath('..'))
print(os.path.abspath('Tom'))
print(os.path.abspath('./Jack'))
print(os.path.abspath('../Luck'))
print(os.path.abspath('../../../Cat'))
print(os.path.abspath('/Xiao'))

print('-------------------------------------------- realpath')

print('-------------------------------------------- normpath')
# 路径替换为当前操作系统的格式
# 有盘符不起作用
print(os.path.normpath(r'D:\abc\123\LenovoDrivers'))
print(os.path.normpath(r'abc\123\LenovoDrivers'))
print(os.path.normpath(__file__))

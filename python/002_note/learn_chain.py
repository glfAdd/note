"""



"""
from itertools import chain

a = [1, 2]
b = {'name': '小明', 'age': 12}
for i in chain(a, b):
    print(i)
'''
1
2
name
age
'''

for i in chain(a, b.values()):
    print(i)
'''
1
2
小明
12
'''

# 利用*解包, 将迭代器转为 list
d = chain(a, b)
print(d)


e = list(chain(a))
print(e)

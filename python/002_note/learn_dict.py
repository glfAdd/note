"""
len(a)                      长度
del a["name"]               删除
a.pop("name)                删除, 并返回删除的值
a.setdefault('name', 123)   不存在就设置, 如果key已经有值了就不设置
a.__contains__('name')      是否包含key
a.has_key('name)            是否包含key (python 2)
a.__iter__()
a.items()                   list [(key, value),(key, value)]
a.iteritems()               返回迭代器
"""

# 字符串, 数字, 元组都可以做key
{"name": "xiao", 12: "AA", (1, 2, 3): (11, 22)}

# 字典, 列表不能做key
# 字典讲key进行哈希算法得到一个值，讲value放入这个值对相应的内存中。字典 列表可以改变，改变以后哈希值就变了，就找不到value了。
# 哈希算法：将任何内容转为长度相同但内容绝对不同的码。
# {{"age": 12}: "AA", [1, 2, 3]: (11, 22)}


print(""" ============================ 合并两个字典 """)
dic = {"A": 1, "B": 2}
dic2 = {"C": 3}
dic.update(dic2)
# {'A': 1, 'B': 2, 'C': 3}
print(dic)

a = {'a': 1, 'b': 2}
b = {'aa': 11, 'bb': 22}
c = {'a': 100, 'cc': 33}
print(dict(a, **b, **c))

print(""" ============================ 推导式 """)
g = {'name': 'xiao', 'age': 11, 'address': 'China'}
# {'xiao': 'name', 11: 'age', 'China': 'address'}
print({b: a for a, b in g.items()})
# {11, 'China', 'xiao'}
print({a for a in g.values()})

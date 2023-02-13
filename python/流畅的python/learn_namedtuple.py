"""
带字段名的元组.
具名元组的实例和普通元组消耗的内存一样多，因为字段名都被存在对应的类里面。
这个类跟普通的对象实例比起来也要小一些，因为Python 不会用__dict__来存放这些实例的属性。
"""
from collections import namedtuple

"""创建namedtuple类"""
# typename: 返回一个具名元组子类
# field_names: 类的各个字段的名字。可以是由数个字符串组成的可迭代对象，或者是由空格分隔开的字段名组成的字符串。
City = namedtuple('City', 'name country population coordinates')
# City = namedtuple('City', ['name', 'country', 'population', 'coordinates'])

"""创建对象"""
# 存放在对应字段里的数据要以一串参数的形式传入到构造函数中注意，元组的构造函数却只接受单一的可迭代对象）。
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))

"""获取所有字段名"""
print(tokyo.coordinates)

# _fields: 包含这个类所有字段名称的元组。
print(City._fields)
# _make(): 通过接受一个可迭代对象来生成这个类的一个实例，它的作用跟 City(*delhi_data) 是一样的
LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
delhi = City._make(delhi_data)
# _asdict: 把具名元组以 collections.OrderedDict 的形式返回
print(delhi._asdict())

"""修改属性. 返回一个新的对象"""
new_tokyo = tokyo._replace(country='China')
print(tokyo)
print(new_tokyo)

"""
__getitem__
用self[key]的方式操作对象时
如果属性是list, 整数和切片
如果属性是dict, 可以使用key获取值

__setitem__
self[key] 赋值是调用
每当属性被赋值的时候都会调用该方法，因此不能再该方法内赋值 self.name = value 会死循环
只有使用这种方式复制才会调用 self['age'] = 12 并且需要在方法里面手动添加 __dict__的属性

__delitem__
self[key] 删除属性时调用该方法

__len__
返回属性元素的数量
"""


class Person:
    def __init__(self, name_list):
        self.name = name_list
        self['age'] = 12

    def __getitem__(self, index):
        return self.name[index]

    def __setitem__(self, key, value):
        print('----------')
        self.__dict__[key] = value

    def __len__(self):
        return len(self.name)


"""__getitem__属性为list"""
p = Person(["dog", "cat", "fish"])
print(p[2])
print(len(p))
for i in p:
    print(i)

"""__getitem__属性为dict"""
b = Person({'aa': 'bb', 'cc': 'dd'})
print(len(b))

"""__setitem__"""
print(b['age'])

print(p.name)
print(p.ago)

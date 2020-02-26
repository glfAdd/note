"""
学习
https://www.jianshu.com/p/594865f0681b


序列化: 将数据转化为可存储或可传输的数据类型

marshmallow: 将orm对象与python原生数据类型之间相互转换的库
    object -> dict
    objects -> list
    string -> dict
    string -> list
"""

from marshmallow import Schema, fields, post_load
from marshmallow import pprint


class User(object):
    """类"""

    def __init__(self, name, email):
        self.name = name
        self.email = email


class UserSchema(Schema):
    """用于序列化和反序列化的类"""
    name = fields.Str()
    email = fields.Email()

    # @post_load
    # def format_data(self, data):
    #     return User(**data)


""" ============================ 序列化 
dump()      obj -> dict，
dumps()     obj -> string，
"""
user = User(name="Monty", email="monty@python.org")
schema1 = UserSchema()
result1 = schema1.dump(user)
pprint(result1)  # {'email': 'monty@python.org', 'name': 'Monty'}

""" ============================ 过滤输出 
only        指定要输出的字段
exclude     排除不想输出的字段
"""
schema2 = UserSchema(only=('name',))
result2 = schema2.dump(user)
pprint(result2)  # {'name': 'Monty'}

schema3 = UserSchema(exclude=('name',))
result3 = schema3.dump(user)
pprint(result3)  # {'email': 'monty@python.org'}

""" ============================ 反序列化 
load()      string -> object
@post_load  string -> object每次调用load()方法时, 会按照format_data的逻辑，返回一个User类对象
"""
data4 = {
    'email': 'ken@yahoo.com',
    'name': 'Ken'
}
schema4 = UserSchema()
result4 = schema4.load(data4)
pprint(result4)  # {'email': 'ken@yahoo.com', 'name': 'Ken'}

""" ============================ 多个对象 
many        默认处理一个对象, 当处理多个对象时设为 True
"""
user1 = User(name="Mick", email="mick@stones.com")
user2 = User(name="Keith", email="keith@stones.com")
users = [user1, user2]

# option 1:
schema = UserSchema(many=True)
result = schema.dump(users)
pprint(result)

# Option 2:
schema = UserSchema()
result = schema.dump(users, many=True)
pprint(result)

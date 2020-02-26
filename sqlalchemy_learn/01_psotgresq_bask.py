# coding=utf-8
"""
安装
pip  install sqlalchemy
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

# 创建对象的基类:
Base = declarative_base()


# 必须继承基类
class User(Base):
    # 表的名字:
    __tablename__ = 'user'
    id = Column(String(20), primary_key=True, autoincrement=True)
    name = Column(String(20))
    age = Column(Integer)


# 初始化数据库连接 数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名
engine = create_engine("postgresql://postgres:123456@localhost/psql_learn")
# 创建Session类型:
DBSession = sessionmaker(bind=engine)
# 创建session对象:
session = DBSession()
"""查询"""
# print session.query(User).filter(User.name == 'Tom')
# print session.query(User).filter(User.name == 'Tom').all()
# print session.query(User).filter(User.name == 'Tom').one()
res = session.query(User).filter(User.name == 'Tom').first()
print(res.id, res.name, res.age)
"""删"""
# session.delete(res)
# session.commit()
"""改"""
# res.name = 'ming'
# session.commit()
"""增"""
# new_user = User(id=10, name='Bob', age=11)
# session.add(new_user)
# session.commit()
"""关闭"""
session.close()

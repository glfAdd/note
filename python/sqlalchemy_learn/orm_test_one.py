# !/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String  # 区分大小写
from sqlalchemy import func
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey  # 区分大小写
from sqlalchemy.orm import sessionmaker, relationship

# 创建连接
engine = create_engine("mysql+pymysql://root:123456@localhost/learn", encoding='utf-8', echo=True)
# 生成orm基类
base = declarative_base()


class Student(base):
    """
    必须继承base
    """
    __tablename__ = 'student'  # 表名
    id = Column(Integer, primary_key=True)
    last_name = Column(String(30))
    first_name = Column(String(30))
    age = Column(String(30))

    def __repr__(self):
        """
        print 输出时会调用
        :return:
        """
        return 'id: %s, last_name: %s, first_name: %s, age: %s' % (self.id, self.last_name, self.first_name, self.age)


# class Score(base):
#     """
#     必须继承base
#     """
#     __tablename__ = 'score'  # 表名
#     id = Column(Integer, primary_key=True)
#     person_id = Column(Integer(11), ForeignKey(Student.id))
#     class_name = Column(String(30))
#     score = Column(Integer(4))


# 创建表结构
base.metadata.create_all(engine)
# 创建与数据库的会话
Session_class = sessionmaker(bind=engine)
Session = Session_class()

"""...........插入.........."""
# 把要创建的数据对象添加到这个session里
user_obj = Student(last_name="rr", first_name='123', age=45)
Session.add(user_obj)
# 提交
Session.commit()

"""...........查询.........."""
my_user = Session.query(Student).filter_by(last_name="xiao").first()
print(my_user.id, my_user.first_name, my_user.age, my_user)
print(Session.query(Student.last_name, Student.age).filter(Student.last_name.in_(['xiao', 'li'])).all())
print(Session.query(Student.last_name, Student.first_name).all())
# 相当于 AND
print(Session.query(Student.id).filter(Student.id < 30).filter(Student.id >= 1).all())

"""...........回滚.........."""
Session.add(Student(last_name="rr", first_name='123', age=45))
print(Session.query(Student.last_name, Student.first_name).all())
Session.rollback()
print(Session.query(Student.last_name, Student.first_name).all())

"""...........统计分组.........."""
# todo 一个字符和多个字符
# todo 正则
print(Session.query(Student.last_name, Student.first_name).filter(Student.last_name.like('x%')).count())
print(Session.query(func.count(Student.last_name)).group_by(Student.last_name).all())

"""...........链表.........."""

'''
在user表里通过backref字段反向查出所有它在addresses表里的关联项，在内存中创建。
在addresses表中可以使用user来查询users表中的数据，
在users表中可以使用backref后的addresses来查询assresses表中的数据。'''

"""...........查询.........."""
"""...........查询.........."""

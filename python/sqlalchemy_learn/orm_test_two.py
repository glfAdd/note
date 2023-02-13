# conding:utf-8
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String  # 区分大小写
from sqlalchemy.orm import sessionmaker

# 创建连接
engine = create_engine("mysql+pymysql://root:123456@localhost/ceshi", encoding='utf-8', echo=True)
# 生成orm基类
base = declarative_base()


class user(base):
    __tablename__ = 'users'  # 表名
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(64))


base.metadata.create_all(engine)  # 创建表结构
Session_class = sessionmaker(bind=engine)  ##创建与数据库的会话，class,不是实例
Session = Session_class()  # 生成session实例
user_obj = user(name="rr", password="123456")  # 插入你要创建的数据对象，每执行一次都会新增一次数据。
print(user_obj.name, user_obj.id)  # 此时还没创建对象呢，不信你打印一下id发现还是None
Session.add(user_obj)  # 把要创建的数据对象添加到这个session里
print(user_obj.name, user_obj.id)  # 此时也依然还没创建
Session.commit()  # 提交，使前面修改的数据生效。

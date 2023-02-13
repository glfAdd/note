# coding=utf-8

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Column, Integer

# 创建数据库链接
engine = create_engine("mysql+mysqldb://root:123456@localhost:3306/learn")
Session = sessionmaker(bind=engine)
Base = declarative_base()


# 必须继承declaraive_base得到的那个基类
class Person(Base):
    """
    创建表
    """
    # 必须要有__tablename__来指出这个类对应什么表，这个表可以暂时在库中不存在，SQLAlchemy会帮我们创建这个表
    __tablename__ = "person"

    # Column类创建一个字段
    id = Column(Integer, primary_key=True)
    # nullable就是决定是否not null，unique就是决定是否unique。。这里假定没人重名，设置index可以让系统自动根据这个字段为基础建立索引
    name = Column(String(20), nullable=False, unique=True, index=True)
    sex = Column(String(2), nullable=False)
    age = Column(Integer, nullable=False)

    def __repr__(self):
        # __repr__方法不是必须的，但是可以写在这里来使得调试时更加容易分辨清楚谁是谁
        return "<Student>{}:{}".format(self.Sname, self.Sno)


# 这就是为什么表类一定要继承Base，因为Base会通过一些方法来通过引擎初始化数据库结构。不继承Base自然就没有办法和数据库发生联系了。
Base.metadata.create_all(engine)

# --------------------------------------------------------
# 实例化了一个会话（或叫事务），之后的所有操作都是基于这个对象的 commit rollback close
session = Session()
# 数据对象得到创建，此时为Transient状态
frank = Person(name='Frank')
# 数据对象被关联到session上，此时为Pending状态
session.add(frank)
# 数据对象被推到数据库中，此时为Persistent状态
session.commit()
print(frank.name)  # 此时会报错DetachedInstanceError，因为此时是Detached状态。
# 关闭session对象
session.close()

new_session = Session()
print(new_session.query(Person).get(1).name)  # 可以查询到数据
new_session.close()

"""
python database.py db init          # 初始化
python database.py db upgrade
python database.py db migrate
python database.py db downgrade
python database.py db downgrade 版本号

# echo=True 打印sql语句信息
engine=create_engine('mysql+pymysql://username:password@hostname:port/dbname', echo=True)


# 插入一条数据
db.session.add(us1)
# 插入多条数据
db.session.add_all([us1,us2,us3,us4])
# 精确查询
User.query.filter_by(name='wang').all()
# 模糊查询
User.query.filter(User.name.endswith('g')).all()
# 参数为主键，如果主键不存在没有返回内容
User.query.get(123)
# and or not
User.query.filter(and_(User.name!='wang',User.email.endswith('163.com'))).all()
User.query.filter(or_(User.name!='wang',User.email.endswith('163.com'))).all()
User.query.filter(not_(User.name=='chen')).all()
# update
User.query.filter_by(name='zhang').update({'name':'li'})
# delete
user = User.query.first()
db.session.delete(user)
db.session.commit()
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Shell, Manager
from sqlalchemy import and_, not_, or_

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@127.0.0.1:5432/tests'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

manager = Manager(app)
db = SQLAlchemy(app)
# 第一个参数是Flask的实例，第二个参数是Sqlalchemy数据库实例
migrate = Migrate(app, db)
# manager是Flask-Script的实例，这条语句在flask-Script中添加一个db命令
manager.add_command('db', MigrateCommand)


# 定义模型Role
class Role(db.Model):
    # 定义表名
    __tablename__ = 'roles'
    # 定义列对象
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return 'Role:'.format(self.name)


# 定义用户
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)

    def __repr__(self):
        return 'User:'.format(self.username)


if __name__ == '__main__':
    manager.run()

"""







"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@127.0.0.1:3306/test1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@127.0.0.1/tests'
# 设置每次请求结束后会自动提交数据库中的改动
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# 设置成 True，SQLAlchemy 将会追踪对象的修改并且发送信号。这需要额外的内存， 如果不必要的可以禁用它。
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# 实例化SQLAlchemy对象
db = SQLAlchemy(app)


class Author(db.Model):
    __tablename__ = 'author'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    email = db.Column(db.String(64))
    au_book = db.relationship('Book', backref='author')

    def __repr__(self):
        return 'Author:%s' % self.name


class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    info = db.Column(db.String(32), unique=True)
    leader = db.Column(db.String(32))
    au_book = db.Column(db.Integer, db.ForeignKey('author.id'))

    def __repr__(self):
        return 'Book:%s,%s' % (self.info, self.lead)

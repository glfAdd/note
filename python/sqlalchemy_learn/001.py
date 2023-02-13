"""
db.Model    # 创建模型
db.Column   # 创建模型属性
"""

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

base_dir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:123456@127.0.0.1:tests'
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
db = SQLAlchemy(app)

""" 一对多 ------------------------------------------"""


class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    # relationship: Role类实例的users属性将返回User组成的列表
    #   第一个参数表示这个关系的另一端是哪个模型
    #   backref: 向User模型添加了一个role数据属性, 从而定义反向关系. 这一属性可替代role_id访问Role模型, 此时获取的是模型对象, 而不是外键的值.
    users = db.relationship('User', backref='role')
    def __repr__(self):
        """非必须, 用于在调试或测试时, 返回一个具有可读性的字符串表示模型."""
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    # db.ForeignKey 外键关系
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<Role %r>' % self.username


""" 一对多 ------------------------------------------"""
# 最复杂的关系类型, 需要用到关联表, 这样多对多关系可以分解成原表和关联表之间的两个一对多关系


registrations = db.Table(
    "registrations",
    db.Column("student_id", db.Integer, db.ForeignKey("students.id")),
    db.Column("class_id", db.Integer, db.ForeignKey("classes.id"))
)


class Student(db.Model):
    __tablename__ = "students"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    classes = db.relationship("Class",
                              secondary=registrations,
                              backref=db.backref("students", lazy="dynamic"),
                              lazy="dynamic")


class Class(db.Model):
    __tablename__ = "classes"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

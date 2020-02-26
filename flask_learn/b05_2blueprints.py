# coding=utf-8
from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

# 蓝图名字
# 蓝图所在模块
# static_folder: 静态文件路径
# template_folder: 模板路径
one = Blueprint('page1', __name__)
two = Blueprint('page2', __name__, url_prefix='/new')


# two = Blueprint('simple_page', __name__, template_folder='templates', static_folder='static')


@one.route('/home1')
def show():
    return 'home1'


@two.route('/home2')
def search():
    return 'home2'

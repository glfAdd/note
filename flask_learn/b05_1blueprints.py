# coding=utf-8
"""
1.创建蓝图
2.注册蓝图路由
3.在程序实例中注册蓝图

可以在app注册的时候设置, 也可以在注册路由时设置
导入包的时候回执行__init__文件
"""
from flask import Flask
from b05_2blueprints import one, two

app = Flask(__name__)
app.register_blueprint(one)
app.register_blueprint(one, url_prefix='/tests')
app.register_blueprint(two)
if __name__ == '__main__':
    app.run(debug=True)

# -*-coding=utf-8-*-
"""
app启动参数
配置文件加载和读取

request
current_app 获取当先的app
g: 空字典容器, 可以在一次请求的多个函数之间传递参数

命令行启动flask
python a.py runserver --help
python a.py reunsever -p 6000

类似ipython的交互模式
python a.py shell

flask调试模式修改环境变量
export FLASK_ENV=development 
或
export FLASK_DEBUG=1
flask run
"""

from flask import Flask, current_app

"""创建flask对象"""
# import_name:当前文件所在的目录为项目的根目录
# static_url_path:访问金泰资源URL前缀,用来区分访问视图还是静态资源,默认status.如果发现url是用python开头的就回去找静态文件
#   http://127.0.0.1:5000/python/home/index.html
# static_folder: 静态文件目录,默认status
# template_folder: 模板目录,默认templates
app = Flask(__name__, static_url_path='/python', static_folder='static_files', template_folder='template')

"""加在配置文件"""
# 1.使用配置文件
app.config.from_pyfile('config.cfg')


# 2.使用对象配置参数
class Config(object):
    DEBUT = True
    MY_NAME = 'Gong'


app.config.from_object(Config)
# 3.直接操作config字典
app.config['DEBUG'] = True


@app.route('/')
def hello_world():
    """读取配置文件"""
    # 1.能获取到app对象时直接获取
    print(app.config.get('MY_NAME'))
    # 2.无法获取app对象时使用功能current_app, 和操作app对象一样
    print(current_app.config.get('MY_NAME'))
    return 'hello'


if __name__ == '__main__':
    # 查看这个flask路由映射
    print(app.url_map)

    """启动文件配置"""
    # host:能访问的ip. 如果都能访问设置为 0.0.0.0 默认只能自己访问
    # port:端口
    # debug:
    app.run(host='0.0.0.0', port=5000, debug=True)

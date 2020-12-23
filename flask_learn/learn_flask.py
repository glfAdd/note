""" ============================ 扩展包
Flask-SQLalchemy        操作数据库
Flask-migrate           管理迁移数据库
Flask-Mail              邮件
Flask-WTF               表单
Flask-script            插入脚本
Flask-Login             认证用户状态
Flask-RESTful           开发REST API的工具
Flask-Bootstrap         集成前端Twitter Bootstrap框架
Flask-Moment            本地化日期和时间
"""

from flask import Flask, current_app, url_for, redirect, session, make_response, request
from werkzeug.routing import BaseConverter

""" ============================ 线程局部变量 


"""

""" ============================ 上下文
请求上下文(request context)
  - 保存了客户端和服务器交互的数据
  - request: 封装了HTTP请求的内容
  - session: 用来记录请求会话中的信息，针对的是用户信息。举例：session['name'] = user.id，可以记录用户信息。还可以通过session.get('name')获取用户信息。

应用上下文(application context)
  - 在flask程序运行过程中，保存的一些配置信息，比如程序文件名、数据库的连接、用户信息等
  - current_app: 当前运行程序文件的程序实例. current_app.name当前应用程序实例的名字
  - g:处理请求时，用于临时存储的对象，每次请求都会重设这个变量。比如：我们可以获取一些临时请求的用户信息
    - 当调用app = Flask(_name_)的时候，创建了程序应用对象app；
    - request 在每次http请求发生时，WSGI server调用Flask.call()；然后在Flask内部创建的request对象
    - app的生命周期大于request和g，一个app存活期间，可能发生多次http请求，所以就会有多个request和g
    - 最终传入视图函数，通过return、redirect或render_template生成response对象，返回给客户端


"""

""" ============================ 请求钩子
在客户端和服务器交互的过程中，有些准备工作或扫尾工作需要处理，比如：在请求开始时，建立数据库连接；在请求结束时，指定数据的交互格式。
为了让每个视图函数避免编写重复功能的代码，Flask提供了通用设施的功能，即请求钩子。请求钩子是通过装饰器的形式实现，Flask支持如下四种请求钩子

before_first_request    在处理第一个请求前运行
before_request          在每次请求前运行
after_request           如果没有未处理的异常抛出，在每次请求后运行
teardown_request        在每次请求后运行，即使有未处理的异常抛出
"""

""" ============================ Werkzeug
是一个遵循WSGI协议的python函数库。其内部实现了很多Web框架底层的东西
  - request和response对象
  - 与WSGI规范的兼容
  - 支持Unicode
  - 支持基本的会话管理和签名Cookie
  - 集成URL请求路由
  
Werkzeug库的routing模块负责实现URL解析。不同的URL对应不同的视图函数
"""

""" ============================ 路由配置
装饰器
  - 将路由映射到视图函数
  - 视图函数可以有多个路由
  - methord:允许的请求方式, 默认GET
@app.route('/home/', methods=["POST", "GET"])
@app.route('/send/<number>')
@app.route('/send/<int:number>')
@app.route("/send/<regex(r'1[35678]\d{9}'):number>")
@app.errorhandler(404)

url_for             通过视图函数获取url
redirect            重定向
current_app
url_map
abort               如果在视图函数执行过程中，出现了异常错误，我们可以使用abort函数立即终止视图函数的执行, 向前端返回一个http标准中存在的错误状态码，表示出现的错误信息
jsonify
make_response
Response
"""

""" ============================ request 
request.form.get('age', 0, int)
request.from.getlist('base_image2')
request.args.get('point')
request.args.getlist('base_image2')
request.values.getlist('base_image2')
request.headers.get('Connection')

request.url
request.data
request.cookies
request.method
"""

""" ============================ session 
session['name'] = 'xiaoming'
session['age'] = 23
"""

""" ============================ session 
默认是临时cookie, 关闭浏览器以后失效, max_age 设置cookie有效时间(秒). 只针对某个值有效
设置的cookie在response headier里面有set-cookie可以区分出来
"""

app = Flask(__name__)


@app.route('/home/', methods=["POST", "GET"])
@app.route('/king/', methods=["POST"])
def index():
    return 'hello'


def login():
    url = url_for(index)
    return redirect(url)


@app.route('/score/<int:number>')
def num(number):
    return '%s' % number


"""设置cookie"""


@app.route('/set')
def set_cookie():
    res = make_response('success')
    res.set_cookie('name', 'Tom')
    res.set_cookie('age', '12', max_age=3000)
    return res


@app.route('/get')
def get_cookie():
    name = request.cookies.get('name')
    return name


@app.route('/delete')
def delete_cookie():
    # 并不是真的删除了, 而是修改cookie的过去时间
    res = make_response('delete cookie')
    res.delete('name')
    return res


"""自定义类型转换器"""


class RegeConverter(BaseConverter):
    # regex: 用于匹配的正则表达式
    def __init__(self, url_map, regex):
        super(RegeConverter, self).__init__(url_map)
        # 将正则表达式的参数保存到自定义转换器的属性中, flask会使用这个属性进行路由的正则匹配
        self.regex = regex

    def to_python(self, value):
        """
        处理转换器获取的参数
        :param value: 正则表达式匹配到的值
        :return: 转换器最终获取的值
        """
        print('to_python = ' + value)
        return value

    def to_url(self, value):
        """
        调用url_for方法时调用, 处理传进来的参数
        :param value: 传进来的参数
        :return: 最终的值
        """
        print('to_url : ' + value)
        return value


# 2.将自定义的转化器添加到flask转化器中
app.url_map.converters['regex'] = RegeConverter


@app.route("/send/<regex(r'1[35678]\d{9}'):number>")
def get_phont(number):
    return str(number)


@app.route("/tests/")
def test():
    url = url_for('get_phont', number='13444444444')
    return redirect(url)


if __name__ == '__main__':
    print(app.url_map)
    app.run(host='0.0.0.0', port=5000, debug=True)

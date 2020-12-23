##### 依赖

> ```
> WSGI：Web服务器和Web应用程序之间通用接口的规范。
> jinja2：是Python的一个流行的模板引擎
> ```

##### 事例

```python
from flask import Flask, url_for, request, make_response, redirect, abort, render_template, session

# 第一个参数是应用模块或者包的名称
app = Flask(__name__)
# 如果不设置秘钥设置session时会报错
app.config['SECRET_KEY'] = '123456'


# 路由装饰器告诉 Flask 什么样的URL 能触发函数
@app.route('/')
@app.route('/root/<user_name>')
def hello_world(user_name=None):
    # 日志
    app.logger.debug('log debug')
    app.logger.warning('log warning')
    app.logger.error('log error')
    if 'passwd' in session:
        print('have session')
    return 'Hello World! -- %s' % user_name


# 访问的url没有斜线会重定向到有斜线的URL上
@app.route('/tests/')
# 访问的url有些线会404
# @app.route('/tests')
def test():
    return 'text'

# 接收URL参数 限制类型
@app.route('/home/<user_name>')
def home(user_name):
    return 'home page %s' % user_name


# 指定接收参数的类型，不一样则Not Found
# int float
@app.route('/score/<int:number>')
def num(number):
    return '%s' % number


# methods:默认是GET请求
@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # url_for 拼接URL, filename 静态文件名字，路径 文件名
        print(url_for('static', filename='abc.text'))
        # 获取form属性 可能会KeyError
        user_name = request.form['user_name']
        # 获取cookie
        cookie = request.cookies.get('name')
        print('%s---%s' % (user_name, cookie))
        # 保存cookie
        res = make_response()
        res.set_cookie('username', 'xiaoming')
        return res
    else:
        # 获取URL中的属性
        passwd = request.args.get('id', '')
        print('**%s' % passwd)
        # 设置session。session对cookie进行秘钥签名
        session['passwd'] = passwd
        # 重定向到其他方法 hello_world()方法
        return redirect(url_for('hello_world'))


@app.route('/error/')
def error_page():
    # 返回错误码，使用系统默认的样式。这句后面的代码就不执行了，相当于return
    abort(404)


# todo 这里有问题
# # 自定义错误页面
# @app.errorhandler(404)
# def error_page2():
#     return render_template('test_error.html'), 404


if __name__ == '__main__':
    # run:运行脚本。只能从自己的计算机访问
    # host:服务器公开可用。如果不加只能从自己的计算机访问
    # debug:服务器会在代码修改后自动重新载入
    app.run(host='0.0.0.0', debug=True)
```




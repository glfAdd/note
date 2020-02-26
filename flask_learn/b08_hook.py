from flask import Flask, request

app = Flask(__name__)


@app.route('/home/')
def home():
    return 'home'


@app.route('/index/')
def index():
    return 'index'


@app.before_first_request
def one():
    """第一次请求执行之前调用"""
    print('before fitst request')


@app.before_request
def two():
    """每次请求之前执行"""
    # 可以根据路径区分是哪个请求
    if request.path == '/home/':
        print('before request: home')
    if request.path == '/index/':
        print('before request: index')


@app.after_request
def three(response):
    """制图函数没有异常, 每次请求时候执行"""
    print('after request')
    return response


@app.teardown_request
def four(reponse):
    """无论视图函数是否有异常, 每次请求之后都执行, 并且debug=False"""
    print('teardown request')
    return reponse


app.run(debug=True)

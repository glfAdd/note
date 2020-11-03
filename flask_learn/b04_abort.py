from flask import Flask, abort, Response, make_response, jsonify

app = Flask(__name__)

"""返回状态码/response"""


@app.route('/')
def home():
    # 1.返回状态码, 必须是标准的http状态码
    # abort(502)
    # 2.返回相应体
    res = Response('response !!')
    abort(res)


"""自定义错误处理"""


# 当出现404时调用
@app.errorhandler(404)
def handle_404_error(error):
    return u'出现错误信息 %s' % error


"""自定义相应"""


@app.route('/page')
def index():
    # 1.使用元祖 (相应内容, 状态码, header)
    # return 'my responst', 400, [('name', 'xiao'), ('age', '20')]
    # 可以使用任意的状态码
    # return 'my responst', 666, {'name': 'xiao', 'age': '20'}
    # 个人任意的状态码添加藐视, 否则chrome控制机台看状态码是unknown
    # return 'my responst', '666 hello', {'name': 'xiao', 'age': '20'}
    # 可以省略header
    # return 'my responst', '666 hello'

    # 2.使用make_response构造相应体
    res = make_response('content text')
    res.status = '333 tests'
    res.headers['name'] = 'xiao'
    return res


"""返回json"""


@app.route('/json')
def format():
    data = {'name': 'xiaoming', 'age': 12}
    # 这种方式返回header Content-Type: text/html; charset=utf-8
    # return json.dumps(data)

    # 这样返回的header显示才正确 Content-type: application/json
    # return json.dumps(data), 200, {'Content-type': 'application/json'}

    # 使用封装好的, 转为json并设置header
    # return jsonify(data)
    #
    return jsonify(name='xiao', age=1)


if __name__ == '__main__':
    app.run(debug=True)

# -*-coding=utf-8-*-
"""
1.创建status目录
2.拷贝js文件夹
3.是否能跨域名
4.return的json必须dumps
5.ajax返回的数据直接用 . 获取
"""

"""
1.基础模板中, block的位置会被子模块代替
{% block 模块名字 %}{% endblock %}

2.子模板
{% extends 模板名字%}
{{ super() }} 来渲染父模块的内容。这将返回父模块的结果

过滤器
safe：禁用转义；
capitalize：把变量值的首字母转成大写，其余字母转小写；
lower：把值转成小写；
upper：把值转成大写；
title：把值中的每个单词的首字母都转成大写；
trim：把值的首尾空格去掉；
reverse:字符串反转；
format:格式化输出；
striptags：渲染之前把值中所有的HTML标签都删掉；

<p>{{ '<em>hello</em>' | safe | upper }}</p>
"""
from flask import Flask, render_template, request
import json

app = Flask(__name__)


@app.route('/')
def hello_itcast():
    data = {
        'home': 'China',
        'number': [1, 2, 3, 4, 5, 6],
        'info': {'a': 1, 'b': 2, 'c': 3},
        'score': 2,
        'zero': 0,
        'one': 1
    }
    return render_template('index.html', name='xiaoming', age=20, **data)
    # return render_template('child_01.html')


@app.route('/tests/')
def test_tm():
    return '12312'


"""自定义过滤器"""


# 1.使用装饰器添加过滤器
@app.template_filter('name1')
def format(list):
    return u'这是过滤器: %s' % list


# 2.使用函数添加
# 函数, 使用时过滤器的名字
app.add_template_filter(format, 'name2')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

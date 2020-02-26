"""
安装
pip install flask-restful

官网文档
http://www.pythondoc.com/Flask-RESTful/quickstart.html
https://www.jianshu.com/p/81cd461c7e8f

"""
from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

todos = {}


class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        # 获取表单参数
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}


# resource:视图函数名
# urls:路由的具体地址, 以及参数
api.add_resource(TodoSimple, '/<string:todo_id>')

if __name__ == '__main__':
    app.run(debug=True)

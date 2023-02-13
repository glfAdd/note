"""
蓝图: 存储操作路由映射方法的容器, 主要用来实现客户端请求和URL相互关联的功能
注册路由: 调用route装饰器注册路由时, 将修改对象的url_map路由映射列表


蓝图对象上调用route装饰器注册路由时, 它只是在内部的一个延迟操作记录列表defered_functions中添加了一个项。
当执行应用对象的 register_blueprint() 方法时，应用对象从蓝图对象的 defered_functions 列表中取出每一项，即调用应用对象的 add_url_rule() 方法，这将会修改程序实例的路由映射列表。


<Rule '/admin/tests/' (HEAD, OPTIONS, GET) -> admin.admin_index>
蓝图名称 . 视图函数名称
"""

from flask import Flask, Blueprint

# 创建蓝图对象
admin = Blueprint('admin', __name__)


# 注册蓝图路由
@admin.route('/tests/')
def admin_index():
    return 'admin_index'


app = Flask(__name__)
# 注册蓝图
# blueprint: 蓝图对象
# url_prefix: 蓝图注册路由url添加前缀, 默认值是根路由
app.register_blueprint(admin, url_prefix='/admin')

if __name__ == '__main__':
    print(app.url_map)
    app.run()

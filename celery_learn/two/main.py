from celery import absolute_import
from celery import Celery

# app是Celery类的实例，创建的时候添加了proj.tasks这个模块，也就是包含了proj/tasks.py这个文件
app = Celery('two', include=['two.tasks'])
# 把Celery配置存放进proj/celeryconfig.py文件，使用app.config_from_object加载配置
app.config_from_object('two.celeryconfig')

if __name__ == '__main__':
    app.start()

"""
启动
celery -A two worker -l info
-A参数默认会寻找proj.celery这个模块

"""

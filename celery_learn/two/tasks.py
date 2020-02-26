"""
启动worker命令
celery -A tasks worker -Q queue --loglevel=info

"""
from main import app


@app.task
def add(x, y):
    return x + y

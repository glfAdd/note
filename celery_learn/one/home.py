from celery import Celery
import celeryconfig

app = Celery(__name__, include=["task"])
# 引入配置文件
app.config_from_object(celeryconfig)

if __name__ == '__main__':
    result = add.delay(30, 42)

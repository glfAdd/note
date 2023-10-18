import json
import uuid
from logging.config import dictConfig

from flask import Flask, request

dictConfig({
    "version": 1,
    "disable_existing_loggers": False,  # 不覆盖默认配置
    "formatters": {  # 日志输出样式
        "default": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",  # 控制台输出
            "level": "DEBUG",
            "formatter": "default",
        },
        "log_file": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "INFO",
            "formatter": "default",  # 日志输出样式对应formatters
            "filename": "flask.log",  # 指定log文件目录
            "maxBytes": 20 * 1024 * 1024,  # 文件最大20M
            "backupCount": 10,  # 最多10个文件
            "encoding": "utf8",  # 文件编码
        },

    },
    "root": {
        "level": "DEBUG",  # # handler中的level会覆盖掉这里的level
        "handlers": ["console", "log_file"],
    },
})

app = Flask(__name__)


@app.route('/')
def index():
    par = {k: request.args.get(k) for k in request.args}
    app.logger.info('request args: %s' % par)
    return json.dumps(par)


@app.route("/action", methods=["POST"])
def action():
    par = {k: request.args.get(k) for k in request.args}
    app.logger.info('versions v999889.0')
    app.logger.info('request args: %s' % par)
    app.logger.info('request json: %s' % request.json)
    return json.dumps({
        'par': par,
        'json': request.json
    })


@app.route("/create", methods=["POST"])
def create():

    app.logger.info('request json: %s' % request.json)
    return json.dumps(request.json)


@app.route("/update", methods=["POST"])
def update():
    app.logger.info('request json: %s' % request.json)
    return json.dumps(request.json)


if __name__ == '__main__':
    app.run(app.run(host='0.0.0.0'))

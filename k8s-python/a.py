import json
import logging
from logging.handlers import RotatingFileHandler

from flask import Flask, request

app = Flask(__name__)
# 设置是否传递异常 , 如果为True, 则flask运行中的错误会显示到网页中, 如果为False, 则会输出到文件中
app.config['PROPAGATE_EXCEPTIONS'] = False

command = ""

# 自定义格式化类
class RequestFormatter(logging.Formatter):
    def format(self, record):
        """每次生成日志时都会调用, 该方法主要用于设置自定义的日志信息

        :param record 日志信息
        """
        # 获取请求的url
        record.url = request.url
        # 获取客户端的ip
        record.remote_addr = request.remote_addr
        # 执行父类的默认操作
        return super().format(record)


def create_logger():
    """配置flask日志

    flask 中提供了两个日志  1> werkzeug 记录web应用运行中出现的错误  2> flask.app  给开发者预留的日志
    flask 中的运行错误也会记录到flask.app的日志中
    """
    # 创建flask.app日志器
    flask_logger = logging.getLogger('flask.app')
    # 设置全局级别
    flask_logger.setLevel('DEBUG')

    # 创建控制台处理器
    console_handler = logging.StreamHandler()

    # 给处理器设置输出格式
    console_formatter = logging.Formatter(fmt='%(name)s %(levelname)s %(pathname)s %(lineno)d %(message)s')
    console_handler.setFormatter(console_formatter)

    # 日志器添加处理器
    flask_logger.addHandler(console_handler)

    # 创建文件处理器
    # 转存文件处理器  当达到限定的文件大小时, 可以将日志转存到其他文件中
    file_handler = RotatingFileHandler(filename='flask.log', maxBytes=100 * 1024 * 1024, backupCount=10)

    # 给处理器设置输出格式
    file_formatter = RequestFormatter(
        fmt='[%(asctime)s] %(remote_addr)s requested %(url)s %(name)s %(levelname)s %(pathname)s %(lineno)d %(message)s'
    )
    file_handler.setFormatter(file_formatter)
    # 单独设置文件处理器的日志级别
    file_handler.setLevel('INFO')

    # 日志器添加处理器
    flask_logger.addHandler(file_handler)


@app.route('/')
def index():
    app.logger.error('this is a error')
    return "index"


@app.route("/action", methods=["POST"])
def action():
    app.logger.info(request.json)
    return json.dumps(request.json)


if __name__ == '__main__':
    create_logger()
    app.run(debug=True)

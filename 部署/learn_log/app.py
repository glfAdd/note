import logging
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def default_route():
    """Default route"""
    app.logger.debug('this is a DEBUG message')
    app.logger.info('this is an INFO message')
    app.logger.warning('this is a WARNING message')
    app.logger.error('this is an ERROR message')
    app.logger.critical('this is a CRITICAL message')
    return jsonify('hello world')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8088, debug=True)
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)

"""
启动命令
gunicorn --workers=4 --bind=0.0.0.0:8000 --log-level=warning app:app
"""

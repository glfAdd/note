""" ============================ flask_script
可以在Flask服务器启动的时候，通过命令行的方式传入参数, 而不仅仅通过app.run()方法中传参


启动命令
python learn_flask_script.py runserver --help
python learn_flask_script.py runserver -p 5001
"""

from flask import Flask
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)


@app.route('/')
def index():
    return 'success'


if __name__ == "__main__":
    manager.run()

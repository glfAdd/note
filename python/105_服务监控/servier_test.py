# -*-coding=utf-8-*-

from flask import Flask, request

app = Flask(__name__)


@app.route('/home2', methods=['GET', 'POST'])
def home():
    print("home")
    return "home"


@app.route('/alert/error/api/status', methods=['GET', 'POST'])
def error_api_status():
    print(request.url)
    print(request.get_json())
    print('error api status')
    return 'error api_status'


@app.route('/alert/normal/api/status', methods=['GET', 'POST'])
def normal_api_status():
    print(request.url)
    print(request.get_json())
    print('normal api status')
    return 'normal api_status'


@app.route('/alert/error/node/status', methods=['GET', 'POST'])
def error_node_status():
    print(request.url)
    print(request.get_json())
    print('error node_status')
    return 'error node_status'


@app.route('/alert/normal/node/status', methods=['GET', 'POST'])
def normal_node_status():
    print(request.url)
    print(request.get_json())
    print('normal node_status')
    return 'normal node_status'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10421, debug=True)

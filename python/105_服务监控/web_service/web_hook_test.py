import json
import logging

import requests
from flask import Flask, make_response, request

app = Flask(__name__)


@app.route('/test', methods=['POST'])
def test():
    prometheus_data = json.loads(request.data)
    a = prometheus_data.get('a')
    b = prometheus_data.get('b')
    print(a)
    print(b)
    print('test---------------')
    resp = make_response("test")
    resp.status = "200"
    resp.headers["city"] = "sz"
    return resp


@app.route('/home', methods=['GET', 'POST'])
def home():
    print('home---------------')
    resp = make_response("home")
    resp.status = "401"
    resp.headers["city"] = "sz"
    return resp


def send_alert(text: str):
    data = {
        "msgtype": "text",
        "text": {
            "content": text
        }
    }
    url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=3ae59ddf-ea27-4910-b952-606c26172167'
    headers = {
        'Content-Type': 'application/json'
    }
    res = requests.post(url=url, data=json.dumps(data), timeout=2)


@app.route('/alertmanager', methods=['GET', 'POST'])
def alertmanager():
    print('alertmanager++++++++')
    prometheus_data = json.loads(request.data)
    print(prometheus_data)
    for i in prometheus_data['alerts']:
        text = i['annotations']['summary']
        send_alert(text)

    return 'success alertmanager'


if __name__ == '__main__':
    app.debug = True
    handler = logging.FileHandler('/logs/flask.log', encoding='UTF-8')
    handler.setLevel(logging.DEBUG)
    logging_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(logging_format)
    app.logger.addHandler(handler)
    app.run(port=11469)

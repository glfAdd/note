import json

import requests
from flask import Flask, make_response

app = Flask(__name__)


@app.route('/tests')
def get_cookie():
    data = {"instances": [1.0, 2.0, 5.0]}
    res = requests.post('http://localhost:8501/v1/models/half_plus_two:predict', data=json.dumps(data))
    print(res.text)
    return make_response('success')


if __name__ == '__main__':
    print(app.url_map)
    app.run(host='0.0.0.0', port=5000, debug=True)

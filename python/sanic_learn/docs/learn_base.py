"""
@app.route('/number/<integer_arg:int>')
@app.route('/number/<number_arg:number>')
@app.route('/person/<name:[A-z]+>')
@app.route('/folder/<folder_id:[A-z0-9]{0,4}>')
"""

import aiohttp
from sanic import Sanic
from sanic.exceptions import NotFound
from sanic.response import json, redirect

app = Sanic(__name__)


async def request_baidu():
    url = 'https://www.baidu.com'
    async with aiohttp.ClientSession() as session:
        headers = {'content-type': 'application/json'}
        async with session.get(url=url, headers=headers) as res:
            # 断言
            assert res.status == 200
            # 跳转到源代码中, 如果方法前面由 async 则需要加 await
            url = res.url
            print(url)
            data = await res.text()
            print(data)
            return 'success'


# 定义错误状态
@app.exception(NotFound)
def not_found(request, exception):
    # 重定向
    return redirect('/search')


# http://127.0.0.1:8000/search?num=10
@app.route('/search', methods=['GET'])
async def search_with_num(request):
    num = request.args.get('num', 1)
    r = await request_baidu()
    data = {'name': '小明', 'num': num, 'status': r}
    return json(data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)

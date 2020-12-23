"""  ============================
文档
https://www.osgeo.cn/sanic/index.html
https://sanic.readthedocs.io/en/latest/

"""

from sanic import Sanic
from sanic.log import logger
from sanic.response import json
from sanic.response import text


""" ============================ 加载配置
配置文件是.py文件, 定义大写变量, 给变量赋值
DB_HOST = 'localhost'
DB_NAME = 'appdb'
DB_USER = 'appuser


方式1: 从环境变量
    - 定义的任何变量 SANIC_ 前缀将应用于sanic配置。例如，设置 SANIC_REQUEST_TIMEOUT 将由应用程序自动加载并馈送到 REQUEST_TIMEOUT 配置变量。
    - 可以向Sanic传递不同的前缀自定义, 如MYAPP_, 那么上面的变量是 MYAPP_REQUEST_TIMEOUT
        app = Sanic(load_env='MYAPP_')
    - 如果要禁用从环境变量加载，可以将其设置为 False
        app = Sanic(load_env=False)


方式2: 将配置写成模块
    - 使用import导入
        import myapp.default_settings
        app = Sanic('myapp')
        app.config.from_object(myapp.default_settings)

    - 使用路径导入
        app = Sanic('myapp')
        app.config.from_object('config.path.config.Class')
        

方式3: 将配置文件路径写入环境变量
    - MYAPP_SETTINGS 环境变量集
        #$ MYAPP_SETTINGS=/path/to/config_file python3 myapp.py
        #INFO: Goin' Fast @ http://0.0.0.0:8000

        app = Sanic('myapp')
        app.config.from_envvar('MYAPP_SETTINGS')
        

变量                         默认值
REQUEST_MAX_SIZE            100000000           请求的大小（字节）
REQUEST_BUFFER_QUEUE_SIZE   100                 请求流缓冲区队列大小
REQUEST_TIMEOUT             60                  请求到达需要多长时间（秒）
RESPONSE_TIMEOUT            60                  处理响应需要多长时间（秒）
KEEP_ALIVE                  True                禁用“假时保持活动”
KEEP_ALIVE_TIMEOUT          5                   保持TCP连接打开的时间（秒）
GRACEFUL_SHUTDOWN_TIMEOUT   15.0                强制关闭非空闲连接的等待时间（秒）
ACCESS_LOG                  True                禁用或启用访问日志
PROXIES_COUNT               -1                  应用程序前面的代理服务器数量（例如nginx；请参见下文）
FORWARDED_FOR_HEADER        “X-Forwarded-For”   包含客户端和代理ip的“X-Forwarded-For”HTTP头的名称
REAL_IP_HEADER              “X-Real-IP”         包含真实客户端IP的“X-Real-IP”HTTP头的名称

REQUEST_TIMEOUT
    新的打开的TCP连接传递到Sanic后端服务器与接收到整个HTTP请求之间的时间间隔. 超时被视为客户端错误返回408
RESPONSE_TIMEOUT
    从Sanic服务器将HTTP请求传递到Sanic应用程序，到将HTTP响应发送到客户端之间的持续时间. 超时被视为服务器错误返回503 
KEEP_ALIVE_TIMEOUT
    true: http服务器（Sanic）在发送响应后不关闭TCP连接。这允许客户端重用现有的TCP连接来发送后续的HTTP请求
    false: 立即关闭
"""

""" ============================ 日志
Sanic使用3种日志
    logger          sanic.root      用于记录内部消息
    error_logger    sanic.error     用于记录错误日志
    access_logger   sanic.access    用于记录访问日志


默认访问日志格式:
%(asctime)s - (%(name)s)[%(levelname)s][%(host)s]: %(request)s %(message)s %(status)d %(byte)d


参数:
host        request.ip                              STR
request     request.method + " " + request.url      STR
status      response.status                         int
byte        len(response.body)                      int
"""

""" ============================ 请求 
https://www.yuanrenxue.com/sanic/sanic-request_data.html

args            dict    ?key1=value1&key2=value2 
                        字典的value是list存储新式 {'name':['jim'], 'age': ['12']}
raw_args        dict    ?key1=value1&key2=value2
                        字典的value是string类型 {'key1':'value1','key2':'value2'}
query_string    str     变量保存未分析的字符串值
query_args      list    将请求参数用[('key,'value') ... ] 的形式保存
                        ?name=jim&age=12                [('name', 'jim'), ('age', '12')]
                        ?name=jim&age=12&name=tom       [('name', 'jim'), ('age', '12'), ('name', 'tom')]
json            json    post请求的json数据
body            str     request的原始数据。
headers         dict    包含请求头（headers）的不区分大小写的字典。
method          str     HTTP请求的方法，比如GET, POST等。
ip              str     客户端（浏览器）的IP地址。
port            str     客户端（浏览器）的端口地址。
socket          tuple   客户端（浏览器）的(IP, port)
app                     正在处理该request的Sanic应用对象的引用。当我们在blueprint文件里面或其它模块需要使用全局的app时可以通过request.app来访问它。
url             str     请求的完整URL。
scheme          str     请求的URL scheme：http或https。
host            str     请求的host：127.0.0.1:8888。
path            str     请求的路径path： 比如/files。
query_string    str     请求的查询字符串，name=jim&age=12或空字符串''。
uri_template    str     路由处理器匹配的模板：/posts/<id>/。
token           str     授权header的值，，比如Basic YWRtaW46YWRtaW4=。
file            dict    文件对象的字典
                        test_file = request.files.get('tests')
                        file_parameters = {
                            'body': test_file.body,     # 文件数据
                            'name': test_file.name,     # 文件名
                            'type': test_file.type,     # 文件类型
                        }
form            dict    以POST方式传递的form变量

{
    "parsed":true,
    "url":"http:\/\/0.0.0.0:8000\/test_request_args?key1=value1&key2=value2&key1=value3",
    "query_string":"key1=value1&key2=value2&key1=value3",
    "args":{"key1":["value1","value3"],"key2":["value2"]},
    "raw_args":{"key1":"value1","key2":"value2"},
    "query_args":[["key1","value1"],["key2","value2"],["key1","value3"]]
}
"""

""" ============================ get_args
keep_blank_values
    - url中的空值是否当做空字符串. bool, 默认False. 
        Flask: 如果key值为空, 则当没有传这个参数
        True: 如果key值为空, 则当做传了空字符串
        
    ?t1=1&t2=&t3=3
    aaa = request.get_args(keep_blank_values=True)
    
    
strict_parsing
    - 如何处理解析错误. bool, 默认False
        False: 自动忽略错误
        True: 错误会引发ValueError异常
        
        
encoding
    - str, 默认utf-8


errors
    - str, 默认replace
"""

""" ============================ get_query_args 
"""

""" ============================ 日志 """

""" ============================ 日志 """

""" ============================ 日志 """

""" ============================ 日志 """

# 加载自己的日志配置 app = Sanic('tests', log_config=LOGGING_CONFIG)
app = Sanic('tests')
app.config


@app.route("/")
async def test(request):
    logger.info('Here is your log')
    aaa = request.get_args(keep_blank_values=True)
    print(aaa)
    return json({
        "args": request.args,
        "raw_args": request.raw_args,
        "url": request.url,
        "form_data": request.form,
        "tests": request.form.get('tests'),
        "query_string": request.query_string,
        "message": request.json,
        'aaa': aaa
    })


@app.route('/tag/<tag>')
async def tag_handler(request, tag):
    return text('Tag - %s' % tag)


@app.route('/tag/<tag:int>')
async def tag_handler(request, tag):
    return text('Tag - %s' % tag)


if __name__ == "__main__":
    # 关闭日志 access_log=False
    app.run(host="0.0.0.0", port=8000, debug=True, access_log=True)

## WSGI

- Web Server Gateway Interface, 是为 Python 语言定义的 Web 服务器和 Web 应用程序或框架之间的一种简单而通用的接口
- WSGI 是服务器程序与应用程序的一个约定，它规定了双方各自需要实现什么接口，提供什么功能，以便二者能够配合使用。

- 实际生产中，python 程序是放在服务器的 http server（比如 apache， nginx 等）上的。

- WSGI用来传递服务器程序和python之间传递数据

##### 对应用程序的规定

1. 应用程序需要是一个可调用的对象
2. 可调用对象接收两个位置参数
3. 可调用对象要返回一个值，这个值是可迭代的。

```python
# 1. 可调用对象是一个函数
def application(environ, start_response):
    response_body = 'The request method was %s' % environ['REQUEST_METHOD']
    # HTTP response code and message
    status = '200 OK'
    # 应答的头部是一个列表，每对键值都必须是一个 tuple。
    response_headers = [('Content-Type', 'text/plain'), ('Content-Length', str(len(response_body)))]
    # 调用服务器程序提供的 start_response，填入两个参数
    start_response(status, response_headers)
    # 返回必须是 iterable
    return [response_body]


# 2. 可调用对象是一个类
class AppClass:
    """这里的可调用对象就是 AppClass 这个类，调用它就能生成可以迭代的结果。
        使用方法类似于： 
        for result in AppClass(env, start_response):
             do_somthing(result)
    """
    def __init__(self, environ, start_response):
        self.environ = environ
        self.start = start_response

    def __iter__(self):
        status = '200 OK'
        response_headers = [('Content-type', 'text/plain')]
        self.start(status, response_headers)
        yield "Hello world!\n"


# 3. 可调用对象是一个实例 
class AppClass:
    """这里的可调用对象就是 AppClass 的实例，使用方法类似于： 
        app = AppClass()
        for result in app(environ, start_response):
             do_somthing(result)
    """

    def __init__(self):
        pass

    def __call__(self, environ, start_response):
        status = '200 OK'
        response_headers = [('Content-type', 'text/plain')]
        self.start(status, response_headers)
        yield "Hello world!\n"
```

##### 对服务器端规定

1. 服务器程序需要调用应用程序
2. 把应用程序需要的两个参数设置好, environ 和 start_response
3. 调用应用程序
4. 迭代访问应用程序的返回结果，并将其传回客户端

```python
import os, sys

def run_with_cgi(application):  # application 是程序端的可调用对象
    # 准备 environ 参数，这是一个字典，里面的内容是一次 HTTP 请求的环境变量
    environ = dict(os.environ.items())
    environ['wsgi.input'] = sys.stdin
    environ['wsgi.errors'] = sys.stderr
    environ['wsgi.version'] = (1, 0)
    environ['wsgi.multithread'] = False
    environ['wsgi.multiprocess'] = True
    environ['wsgi.run_once'] = True
    environ['wsgi.url_scheme'] = 'http'

    headers_set = []
    headers_sent = []

    # 把应答的结果输出到终端
    def write(data):
        sys.stdout.write(data)
        sys.stdout.flush()

    # 实现 start_response 函数，根据程序端传过来的 status 和 response_headers 参数，
    # 设置状态和头部
    def start_response(status, response_headers, exc_info=None):
        headers_set[:] = [status, response_headers]
        return write

    # 调用客户端的可调用对象，把准备好的参数传递过去
    result = application(environ, start_response)

    # 处理得到的结果，这里简单地把结果输出到标准输出。
    try:
        for data in result:
            if data:  # don't send headers until body appears
                write(data)
    finally:
        if hasattr(result, 'close'):
            result.close()
```

##### middleware

- 有些程序可能处于服务器端和程序端两者之间：对于服务器程序，它就是应用程序；而对于应用程序，它就是服务器程序。这就是中间层 middleware。
- middleware 对服务器程序和应用是透明的，它像一个代理/管道一样，把接收到的请求进行一些处理，然后往后传递，一直传递到客户端程序，最后把程序的客户端处理的结果再返回。

```python
# Router middleware
class Router(object):
    def __init__(self):
        self.path_info = {}
    def route(self, environ, start_response):
        application = self.path_info[environ['PATH_INFO']]
        return application(environ, start_response)
    def __call__(self, path):
        def wrapper(application):
            self.path_info[path] = application
        return wrapper

router = Router()
```



```
https://blog.csdn.net/yangz_xx/article/details/37508909



```










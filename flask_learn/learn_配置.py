from flask import Flask
from . import config

""" ============================ 4种加载方式
config 本质是一个字段
"""
# 1. 字典形式配置
app = Flask(__name__)
app.config['TESTING'] = True

# 2. 通过对象配置
app.testing = True

# 3. 更新多个配置
app.config.update(
    TESTING=True,
    SECRET_KEY=b'_5#y2L"F4Q8z\n\xec]/'
)

# 4. 引入配置文件 .py
app.config_from_object(config)

""" ============================ FLASK_ENV 
production      (默认)
development     调试模式

$ export FLASK_ENV=development
$ flask run
"""

""" ============================ ENV """

""" ============================ DEBUG 
缺省值：当 ENV 是 'development' 时，为 True ；否则为 False 
"""

""" ============================ TESTING 
缺省值： False
"""

""" ============================ PROPAGATE_EXCEPTIONS 
缺省值： None
"""

""" ============================ PRESERVE_CONTEXT_ON_EXCEPTION 
缺省值： None
"""

""" ============================ TRAP_HTTP_EXCEPTIONS 
缺省值： False
"""

""" ============================ TRAP_BAD_REQUEST_ERRORS 
缺省值： None
"""

""" ============================ SECRET_KEY 
缺省值： None
密钥用于会话 cookie 的安全签名
"""

""" ============================ SESSION_COOKIE_NAME 
缺省值： 'session'
会话 cookie 的名称。假如已存在同名 cookie ，本变量可改变。
"""

""" ============================ SESSION_COOKIE_DOMAIN 
缺省值： None
认可会话 cookie 的域的匹配规则。如果本变量没有设置，那么 cookie 会被 SERVER_NAME 的所有子域认可。如果本变量设置为 False ，那么 cookie 域不会被设置。
"""

""" ============================ SESSION_COOKIE_PATH 
缺省值： None
认可会话 cookie 的路径。如果没有设置本变量，那么路径为 APPLICATION_ROOT ，如果 APPLICATION_ROOT 也没有设置，那么会是 / 。
"""

""" ============================ SESSION_COOKIE_HTTPONLY 
缺省值： True
为了安全，浏览器不会允许 JavaScript 操作标记为“ HTTP only ”的 cookie 。
"""

""" ============================ SESSION_COOKIE_SECURE 
缺省值： False
如果 cookie 标记为“ secure ”，那么浏览器只会使用基于 HTTPS 的请求发 送 cookie 。应用必须使用 HTTPS 服务来启用本变量。
"""

""" ============================ SESSION_COOKIE_SAMESITE 
缺省值： None
限制来自外部站点的请求如何发送 cookie 。可以被设置为 'Lax' （推荐） 或者 'Strict' 。参见 Set-Cookie 选项.
"""

""" ============================ PERMANENT_SESSION_LIFETIME 
缺省值： timedelta(days=31) （ 2678400 秒）
如果 session.permanent 为真， cookie 的有效期为本变量设置的数字， 单位为秒。本变量可能是一个 datetime.timedelta 或者一个 int 。

Flask 的缺省 cookie 机制会验证电子签章不老于这个变量的值。
"""

""" ============================ SESSION_REFRESH_EACH_REQUEST 
缺省值： True
当 session.permanent 为真时，控制是否每个响应都发送 cookie 。每次 都发送 cookie （缺省情况）可以有效地防止会话过期，但是会使用更多的带宽。 会持续会话不受影响。
"""

""" ============================ USE_X_SENDFILE 
缺省值： False
当使用 Flask 提供文件服务时，设置 X-Sendfile 头部。有些网络服务器， 如 Apache ，识别这种头部，以利于更有效地提供数据服务。本变量只有使用这 种服务器时才有效。
"""

""" ============================ SEND_FILE_MAX_AGE_DEFAULT 
缺省值： timedelta(hours=12) （ 43200 秒）
当提供文件服务时，设置缓存，控制最长存活期，以秒为单位。可以是一个 datetime.timedelta 或者一个 int 。在一个应用或者蓝图上使 用 get_send_file_max_age() 可以基于单个文件重载本变 量。
"""

""" ============================ SERVER_NAME 
缺省值： None

"""

""" ============================ APPLICATION_ROOT 
缺省值： '/'
通知应用应用的根路径是什么。这个变量用于生成请求环境之外的 URL （请求 内的会根据 SCRIPT_NAME 生成；参见 应用调度 ）。

如果 SESSION_COOKIE_PATH 没有配置，那么本变量会用于会话 cookie 路 径。
"""

""" ============================ PREFERRED_URL_SCHEME 
缺省值： 'http'
当不在请求情境内时使用些预案生成外部 URL 。
"""

""" ============================ MAX_CONTENT_LENGTH 
缺省值： None
在进来的请求数据中读取的最大字节数。如果本变量没有配置，并且请求没有指 定 CONTENT_LENGTH ，那么为了安全原因，不会读任何数据。
"""

""" ============================ JSON_AS_ASCII 
缺省值： True
把对象序列化为 ASCII-encoded JSON 。如果禁用，那么 JSON 会被返回为一个 Unicode 字符串或者被 jsonify 编码为 UTF-8 格式。本变量应当保持 启用，因为在模块内把 JSON 渲染到 JavaScript 时会安全一点。
"""

""" ============================ JSON_SORT_KEYS 
缺省值： True
按字母排序 JSON 对象的键。这对于缓存是有用的，因为不管 Python 的哈希种 子是什么都能够保证数据以相同的方式序列化。为了以缓存为代价的性能提高可 以禁用它，虽然不推荐这样做。
"""

""" ============================ JSONIFY_PRETTYPRINT_REGULAR 
缺省值： False
jsonify 响应会输出新行、空格和缩进以便于阅读。在调试模式下总是启用 的。
"""

""" ============================ JSONIFY_MIMETYPE 
缺省值： 'application/json'
jsonify 响应的媒体类型。
"""

""" ============================ TEMPLATES_AUTO_RELOAD 
缺省值： None
当模板改变时重载它们。如果没有配置，在调试模式下会启用。
"""

""" ============================ EXPLAIN_TEMPLATE_LOADING 
缺省值： False
记录模板文件如何载入的调试信息。使用本变量有助于查找为什么模板没有载入 或者载入了错误的模板的原因。
"""

""" ============================ MAX_COOKIE_SIZE 
当 cookie 头部大于本变量配置的字节数时发出警告。缺省值为 4093 。 更大的 cookie 会被浏览器悄悄地忽略。本变量设置为 0 时关闭警告。
"""

""" ============================ instance_relative_config """
""" ============================ 123 """
""" ============================ 123 """
""" ============================ 123 """
""" ============================ 123 """
""" ============================ 123 """
""" ============================ 123 """
""" ============================ 123 """
""" ============================ 123 """
""" ============================ 123 """

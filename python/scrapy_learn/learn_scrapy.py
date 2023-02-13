""" ============================ qwewqe
Scrapy Engine(引擎): 负责Spider、ItemPipeline、Downloader、Scheduler中间的通讯，信号、数据传递等。
Scheduler(调度器): 它负责接受引擎发送过来的Request请求，并按照一定的方式进行整理排列，入队，当引擎需要时，交还给引擎。
Item Pipeline(管道):它负责处理Spider中获取到的Item，并进行进行后期处理（详细分析、过滤、存储等）的地方.
Downloader（下载器）:负责下载Scrapy Engine(引擎)发送的所有Requests请求，并将其获取到的Responses交还给Scrapy Engine(引擎)，由引擎交给Spider来处理，
Downloader Middlewares（下载中间件）:你可以当作是一个可以自定义扩展下载功能的组件。
Spider（爬虫）:它负责处理所有Responses,从中分析提取数据，获取Item字段需要的数据，并将需要跟进的URL提交给引擎，再次进入Scheduler(调度器)
Spider Middlewares（Spider中间件）:你可以理解为是一个可以自定扩展和操作引擎和Spider中间通信的功能组件（比如进入Spider的Responses;和从Spider出去的Requests）

代码写好，程序开始运行...
引擎: Spider, 你要处理哪一个网站？
Spider:老大要我处理xxxx.com。
引擎:你把第一个需要处理的URL给我吧。
Spider:给你，第一个URL是xxxxxxx.com。
引擎: 调度器，我这有request请求你帮我排序入队一下。
调度器:好的，正在处理你等一下。
引擎: 调度器，把你处理好的request请求给我。
调度器:给你，这是我处理好的request
引擎: 下载器，你按照老大的下载中间件的设置帮我下载一下这个request请求
下载器:好的！给你，这是下载好的东西。（如果失败:sorry，这个request下载失败了。然后引擎告诉调度器，这个request下载失败了，你记录一下，我们待会儿再下载）
引擎: Spider，这是下载好的东西，并且已经按照老大的下载中间件处理过了，你自己处理一下（注意！这儿responses默认是交给def parse()这个函数处理的）
Spider:（处理完毕数据之后对于需要跟进的URL）， 引擎，我这里有两个结果，这个是我需要跟进的URL，还有这个是我获取到的Item数据。
引擎:Hi ！管道 我这儿有个item你帮我处理一下！调度器！这是需要跟进URL你帮我处理下。然后从第四步开始循环，直到获取完老大需要全部信息。
管道``调度器:好的，现在就做！




"""

""" ============================ scrapy.Request
调用scrapy.Request()方法发起get请求

1. 先爬取最外成的网址, 获取其中需要爬取的网址（url）
2. 对网址逐个遍历，生成Request对象，即爬取对象，逐个爬取。爬取成功后调用回调函数分析爬取的结果

url :Request要请求（爬取）的地址
callback :Request要请求成功后的回调函数，支持两种类型，一个是函数类型；一个是字符串，注意这里不能写成函数调用（曾习惯而为之）
meta :作为参数传递到response对象中，dict类型





"""

""" ============================ Middlewares 
下载中间键
process_request     拦截请求
process_response    拦截响应对象（下载器传递给Spider的响应对象）


from scrapy.http import HtmlResponse




"""

""" ============================ item 

"""

""" ============================ pipeline 

"""

""" ============================ downloader middlewares 
1. 引擎将请求传递给下载器前, 下载中间件可以对请求进行一系列处理, 比如设置请求的 User-Agent，设置代理等
2. 在下载器完成将Response传递给引擎前, 下载中间件可以对响应进行一系列处理。比如进行gzip解压等
3. 在引擎和下载器之间做处理

"""

""" ============================ User-Agent 
步骤:
    1.在下载中间件中拦截请求
    2.将拦截到的请求的请求头信息中的UA进行篡改伪装
    3.在配置文件中开启下载中间件


"""


""" ============================ Proxy 

"""


""" ============================ DOWNLOADER_MIDDLEWARES 
https://zhuanlan.zhihu.com/p/42498126


下载中间件


自定义Downloader Middleware


如果要关闭中间件复制为 None    
DOWNLOADER_MIDDLEWARES = {
    'myproject.middlewares.CustomDownloaderMiddleware': 543,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
}




"""


""" ============================ Proxy """
""" ============================ Proxy """
""" ============================ Proxy """
""" ============================ Proxy """
""" ============================ Proxy """
""" ============================ Proxy """
""" ============================ Proxy """
""" ============================ Proxy """

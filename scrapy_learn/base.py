""" ============================ 参考
https://www.jianshu.com/p/43029ea38251

选择器文档
https://scrapy.readthedocs.io/en/latest/topics/selectors.html
"""

""" ============================ 命令
创建项目
scrapy startproject mySpider

创建爬虫, 将在mySpider/spider目录下创建一个名为itcast的爬虫，并指定爬取域的范围
scrapy genspider itcast "itcast.cn"

运行爬虫
将结果输出到文件, 数据会追加不会删除

scrapy crawl itcast
scrapy crawl maoyan -o maoyan.csv
scrapy crawl maoyan -o maoyan.xml
scrapy crawl maoyan -o maoyan.json

关闭日志
scrapy crawl wangyi --nolog
"""

""" ============================ 目录
scrapy.cfg              部署配置文件
mySpider/               项目文件
mySpider/items.py       项目的目标文件
mySpider/pipelines.py   项目的管道文件
mySpider/settings.py    项目的设置文件
mySpider/spiders/       存储爬虫代码目录
"""

""" ============================ 配置
设置编码方式
settings.py文件中添加FEED_EXPORT_ENCODING='UTF8
scrapy crawl maoyan -o maoyan.json -s FEED_EXPORT_ENCODING=UTF8


"""

""" ============================ scrapy shell
# 启动
scrapy shell 'http://quotes.toscrape.com/page/1/'
[s] Available Scrapy objects:
[s]   scrapy     scrapy module (contains scrapy.Request, scrapy.Selector, etc)
[s]   crawler    <scrapy.crawler.Crawler object at 0x109fc3d00>
[s]   item       {}
[s]   request    <GET http://quotes.toscrape.com/page/1/>
[s]   response   <200 http://quotes.toscrape.com/page/1/>
[s]   settings   <scrapy.settings.Settings object at 0x109fc3a30>
[s]   spider     <DefaultSpider 'default' at 0x10a37c100>
[s] Useful shortcuts:
[s]   fetch(url[, redirect=True]) Fetch URL and update local objects (by default, redirects are followed)
[s]   fetch(req)                  Fetch a scrapy.Request and update local objects
[s]   shelp()           Shell help (print this help)
[s]   view(response)    View response in a browser


css选择器, 底层是XPath
# 标题Selector集合
# css 返回列表
>>> response.css('title')
[<Selector xpath='descendant-or-self::title' data='<title>Quotes to Scrape</title>'>]

# 完整标题元素
>>> response.css('title').extract()
['<title>Quotes to Scrape</title>']

# 标题文字
>>> response.css('title::text').extract()
['Quotes to Scrape']

# 只返回一个元素的文字
# 在没有获取到元素是[0]会IndexError, extract_first不会发生IndexError
>>> response.css('title::text').extract_first()
'Quotes to Scrape'
>>> response.css('title::text')[0].extract()
'Quotes to Scrape'

# 正则表达式
>>> response.css('title::text').re(r'Quotes.*')
['Quotes to Scrape']
>>> response.css('title::text').re(r'Q\w+')
['Quotes']
>>> response.css('title::text').re(r'(\w+) to (\w+)')
['Quotes', 'Scrape']


XPath选择器
>>> response.xpath('//title')
[<Selector xpath='//title' data='<title>Quotes to Scrape</title>'>]
>>> response.xpath('//title/text()').extract_first()
'Quotes to Scrape'
"""

""" ============================ 示例1
<div class="quote">
    <span class="text">“The world as we have created it is a process of our
    thinking. It cannot be changed without changing our thinking.”</span>
    <span>
        by <small class="author">Albert Einstein</small>
        <a href="/author/Albert-Einstein">(about)</a>
    </span>
    <div class="tags">
        Tags:
        <a class="tag" href="/tag/change/page/1/">change</a>
        <a class="tag" href="/tag/deep-thoughts/page/1/">deep-thoughts</a>
        <a class="tag" href="/tag/thinking/page/1/">thinking</a>
        <a class="tag" href="/tag/world/page/1/">world</a>
    </div>
</div>

quote = response.css("div.quote")[0]
title = quote.css("span.text::text").extract_first()
tags = quote.css("div.tags a.tag::text").extract()
"""

""" ============================ 示例2: 获取链接
<ul class="pager">
    <li class="next">
        <a href="/page/2/">Next <span aria-hidden="true">&rarr;</span></a>
    </li>
</ul>
>>> response.css('li.next a::attr(href)').extract_first()
'/page/2/'
"""

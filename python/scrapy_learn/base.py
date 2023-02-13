""" ============================ �ο�
https://www.jianshu.com/p/43029ea38251

ѡ�����ĵ�
https://scrapy.readthedocs.io/en/latest/topics/selectors.html
"""

""" ============================ ����
������Ŀ
scrapy startproject mySpider

��������, ����mySpider/spiderĿ¼�´���һ����Ϊitcast�����棬��ָ����ȡ��ķ�Χ
scrapy genspider itcast "itcast.cn"

��������
�����������ļ�, ���ݻ�׷�Ӳ���ɾ��

scrapy crawl itcast
scrapy crawl maoyan -o maoyan.csv
scrapy crawl maoyan -o maoyan.xml
scrapy crawl maoyan -o maoyan.json

�ر���־
scrapy crawl wangyi --nolog
"""

""" ============================ Ŀ¼
scrapy.cfg              ���������ļ�
mySpider/               ��Ŀ�ļ�
mySpider/items.py       ��Ŀ��Ŀ���ļ�
mySpider/pipelines.py   ��Ŀ�Ĺܵ��ļ�
mySpider/settings.py    ��Ŀ�������ļ�
mySpider/spiders/       �洢�������Ŀ¼
"""

""" ============================ ����
���ñ��뷽ʽ
settings.py�ļ������FEED_EXPORT_ENCODING='UTF8
scrapy crawl maoyan -o maoyan.json -s FEED_EXPORT_ENCODING=UTF8


"""

""" ============================ scrapy shell
# ����
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


cssѡ����, �ײ���XPath
# ����Selector����
# css �����б�
>>> response.css('title')
[<Selector xpath='descendant-or-self::title' data='<title>Quotes to Scrape</title>'>]

# ��������Ԫ��
>>> response.css('title').extract()
['<title>Quotes to Scrape</title>']

# ��������
>>> response.css('title::text').extract()
['Quotes to Scrape']

# ֻ����һ��Ԫ�ص�����
# ��û�л�ȡ��Ԫ����[0]��IndexError, extract_first���ᷢ��IndexError
>>> response.css('title::text').extract_first()
'Quotes to Scrape'
>>> response.css('title::text')[0].extract()
'Quotes to Scrape'

# ������ʽ
>>> response.css('title::text').re(r'Quotes.*')
['Quotes to Scrape']
>>> response.css('title::text').re(r'Q\w+')
['Quotes']
>>> response.css('title::text').re(r'(\w+) to (\w+)')
['Quotes', 'Scrape']


XPathѡ����
>>> response.xpath('//title')
[<Selector xpath='//title' data='<title>Quotes to Scrape</title>'>]
>>> response.xpath('//title/text()').extract_first()
'Quotes to Scrape'
"""

""" ============================ ʾ��1
<div class="quote">
    <span class="text">��The world as we have created it is a process of our
    thinking. It cannot be changed without changing our thinking.��</span>
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

""" ============================ ʾ��2: ��ȡ����
<ul class="pager">
    <li class="next">
        <a href="/page/2/">Next <span aria-hidden="true">&rarr;</span></a>
    </li>
</ul>
>>> response.css('li.next a::attr(href)').extract_first()
'/page/2/'
"""

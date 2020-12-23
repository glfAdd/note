import re

"""
是什么 ?
使用单个字符串来描述、匹配一系列匹配某个句法规则的字符串


# 表示字符
  . 	匹配任意1个字符（除了\n）
  [ ] 	匹配[ ]中列举的字符
  \d 	匹配数字，即0-9
  \D 	匹配非数字，即不是数字
  \s 	匹配空白，即 空格，tab键
  \S 	匹配非空白
  \w 	匹配单词字符，即a-z、A-Z、0-9、_
  \W 	匹配非单词字符

# 表示数量
  * 	匹配前一个字符可有可无
  + 	匹配前一个字符至少有1次
  ? 	匹配前一个字符要么有1次，要么没有
  {m} 	匹配前一个字符出现m次
  {m,} 	匹配前一个字符至少出现m次
  {m,n} 	匹配前一个字符出现从m到n次

# 表示边界
  ^ 	匹配整个字符串开头 # 表示字符串开头
  $ 	匹配整配字符串结尾 # 表示字符串结尾
  \b 	匹配一个单词的边界 # 1个单词开头和结尾（空白为边界）
  \B 	匹配非一个单词边界 

# 匹配分组
  | 	匹配左右任意一个表达式
  (ab) 	将括号中字符作为一个分组
  \num 	引用分组num匹配到的字符串
  (?P<name>) 	分组起别名
  (?P=name) 	引用别名为name分组匹配到的字符串




match方法返回匹配对象，否则返回None
re.match(正则表达式,要匹配的字符串)
匹配对象具有group方法，用来返回字符串的匹配部分






match	从最左边开始匹配，找到1个就结束了，返回字符串
search	从左向右搜索，找到1个就结束了，返回字符串
findall	从左向右搜索所有的，返回列表
sub		将匹配到的数据替换
split	根据匹配进行切割字符串，并返回一个列表



"""

# ['LF1A', 'LF1A', 'LF1A', 'LF1A']
print(re.split(r'[/|]', 'LF1A|LF1A/LF1A|LF1A'))

""" ============================ 贪婪和非贪婪 
贪婪：从左到右的顺序求值时，会尽量“抓取”满足匹配最长字符串，直到无法满足条件为止。
非贪婪：少

在 * ? + {} 表示数量的符号后面加上 ? 就变成非贪婪了

>>> s="This is a number 234-235-22-423"
>>> r=re.match(".+(\d+-\d+-\d+-\d+)",s)
>>> r.group(1)
'4-235-22-423'
>>> r=re.match(".+?(\d+-\d+-\d+-\d+)",s)
>>> r.group(1)
'234-235-22-423'
>>> re.match(r"aa(\d+)","aa2343ddd").group(1)
'2343'
>>> re.match(r"aa(\d+?)","aa2343ddd").group(1)
'2'
>>> re.match(r"aa(\d+)ddd","aa2343ddd").group(1) 
'2343'
>>> re.match(r"aa(\d+?)ddd","aa2343ddd").group(1)
'2343'
"""

""" ============================ 正则使用匿名函数 
http://www.interoem.com/messageinfo.asp?id=35
http://3995503.com/class/class09/news_show.asp?id=14
http://lib.wzmc.edu.cn/news/onews.asp?id=769
http://www.zy-ls.com/alfx.asp?newsid=377&id=6
http://www.fincm.com/newslist.asp?id=415
正则后
http://www.interoem.com/
http://3995503.com/
http://lib.wzmc.edu.cn/
http://www.zy-ls.com/
http://www.fincm.com/
"""

# 方式1
re.match(r"http://.+?/", "http://www.zy-ls.com/alfx.asp?newsid=377&id=6").group()
# 方式2
re.sub(r"(http://.+?/).*", lambda x: x.group(1), "http://3995503.com/class/class09/news_show.asp?id=14")

# 正确的地址
ret = re.match("[\w]{4,20}@163\.com", "xiaoWang@163.com")
# 不正确的地址
ret = re.match("[\w]{4,20}@163\.com", "xiaoWang@163.comheihei")
# 通过$来确定末尾
ret = re.match("[\w]{4,20}@163\.com$", "xiaoWang@163.comheihei")
# 单词边界
re.match(r".*\bver\b", "ho ver abc")
re.match(r".*\Bver\B", "hoverabc")
# | 两边都可以，多的时候写在括号里面
re.match("[1-9]?\d$|100", "78")
re.match("\w{4,20}@(163|126|qq)\.com", "tests@126.com")
# 使用第x个括号里面的内容
# \2使用第2个括号的内容
re.match(r"<(\w*)><(\w*)>.*</\2></\1>", "<html><h1>www.itcast.cn</h1></html>")
# 给或开里面的
# 给括号里面匹配的起个名字name1
# 获取name1匹配上的字符串
re.match(r"<(?P<name1>\w*)><(?P<name2>\w*)>.*</(?P=name2)></(?P=name1)>", "<html><h1>www.itcast.cn</h1></html>")

# # -*- coding:utf-8 -*-
#
# """
# 注册3天过期的邮箱
# """
#
# import requests
# import json
# import random
# from pyquery import PyQuery as pq
#
# USER_AGENT_LIST = [
#     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27 ",
#     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1 ",
#     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7 ",
#     "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 ",
#     "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 ",
#     "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2 ",
#     "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1 ",
#     "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre ",
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0",
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36",
#     "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36"
# ]
#
#
# class LogonEmailManager(object):
#
#     def __init__(self):
#         requests.packages.urllib3.disable_warnings()
#         self.timeout = 30
#
#     def begin(self):
#         # 获取注册邮箱
#         mail = self.get_email()
#         if not mail:
#             print "get mail error"
#         print mail
#         # getgo网站注册
#         # self.getgo_logon()
#
#     def get_email(self):
#         session = requests.session()
#         session.headers["User-Agent"] = random.choice(USER_AGENT_LIST)
#         session.headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
#         session.headers["Accept-Language"] = "en-US,en;q=0.9"
#         session.headers["Cache-Control"] = "no-cache"
#         session.headers["Connection"] = "keep-alive"
#         session.headers["Pragma"] = "no-cache"
#         session.headers["Upgrade-Insecure-Requests"] = "1"
#         url1 = 'http://www.yopmail.com/en/'
#         r1 = session.get(url=url1, timeout=self.timeout)
#         b1 = pq(r1.content)
#         if b1('title').text() != 'YOPmail - Disposable Email Address':
#             print 'request homepage error'
#             return None
#         print 'request homepage success'
#
#         yp = None
#         yj = None
#         login = "123ccckesk"
#         #  注册并获取yp
#         for one in b1('input').items():
#             if str(one('input').attr('id')) == 'yp':
#                 yp = one('input').attr('value')
#                 data = {"yp": yp, "login": login}
#                 session.post(url=url1, data=data, timeout=self.timeout)
#                 break
#
#         # 获取yj
#         url2 = "http://www.yopmail.com/style/2.8/webmail.js"
#         r2 = session.get(url=url2)
#         yj = r2.text.split("&v='+ver+")
#         yj = yj[0]
#         yj = yj[yj.rfind("=") + 1:]
#
#         # 判断是否注册成功
#         url3 = 'http://www.yopmail.com/en/inbox.php'
#         params = {
#             "login": login,
#             "p": "1",
#             "d": "",
#             "ctrl": "",
#             "scrl": "",
#             "spam": True,
#             "yf": "005",
#             "yp": yp,
#             "yj": yj,
#             "v": "2.8",
#             "r_c": "",
#             "id": "",
#         }
#
#         r3 = session.get(url=url3, timeout=self.timeout, params=params)
#         if "Inbox" in r3.text:
#             print "logon mail success"
#             return "%s@yopmail.com " % login
#         return None
#
#     def getgo_logon(self):
#         session = requests.session()
#         session.headers["User-Agent"] = random.choice(USER_AGENT_LIST)
#         session.headers[
#             "Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
#         session.headers["Accept-Language"] = "en-US,en;q=0.9"
#         session.headers["Cache-Control"] = "no-cache"
#         session.headers["Connection"] = "keep-alive"
#         session.headers["Pragma"] = "no-cache"
#         session.headers["Upgrade-Insecure-Requests"] = "1"
#         session.headers["Host"] = "www.getgo.com.ph"
#         session.get(url="https://beta.getgo.com.ph/", timeout=self.timeout, verify=False)
#
#         url1 = "https://www.getgo.com.ph/member/quick-enroll-login?tab=1"
#         session.get(url=url1, timeout=self.timeout, verify=False)
#
#
#
# if __name__ == "__main__":
#     a = LogonEmailManager()
#     a.begin()
#     print '------------------------'

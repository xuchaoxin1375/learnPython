# -*- coding: utf-8 -*-
# request_urlopen.py
import urllib.request as ur

url = r'http://www.lagou.com/zhaopin/Python/?labelWords=label'
headers = {  # 伪装成浏览器
    'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) \
                   AppleWebKit/537.36(KHTML, like Gecko) '
                  r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
    'Referer': r'http://www.lagou.com/zhaopin/Python/?labelWords=label',
    'Connection': 'keep-alive'}
# get the Request instance (initiate with the headers:
req = ur.Request(url, headers=headers)
print(req)
page = ur.urlopen(req).read()  # the result type is Any
page = page.decode('utf-8') # the result type is Any.
print(page)

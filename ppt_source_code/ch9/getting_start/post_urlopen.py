# -*- coding: utf-8 -*-
#post_urlopen.py
from urllib import request, parse
url = r'http://www.lagou.com/jobs/positionAjax.json?'
headers = {        #伪装成浏览器
    'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) \
                    AppleWebKit/537.36 (KHTML, like Gecko) '
                  r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
    'Referer': r'http://www.lagou.com/zhaopin/Python/?labelWords=label',
    'Connection': 'keep-alive' }

data = {
    'first': 'true',
    'pn': 1,
    'kd': 'Python' }
data = parse.urlencode(data).encode('utf-8')
req = request.Request(url, headers=headers, data=data)
page = request.urlopen(req).read()
page = page.decode('utf-8')

print(page)
# -*- coding: utf-8 -*-

#bs4_title_crawler.py
from urllib import request
from bs4 import BeautifulSoup

#获取简书首页的全部文章标题
url = r'http://www.jianshu.com'
# 模拟真实浏览器进行访问
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
page = request.Request(url, headers=headers)
page_data_bytes = request.urlopen(page).read()
page_data_str = page_data_bytes.decode('utf-8')
# 将获取到的内容转换成BeautifulSoup格式，并将html.parser作为解析器
soup_BS = BeautifulSoup(page_data_str, 'html.parser')
# 以格式化的形式打印html
# print(soup.prettify())
"""
Look in the children of this PageElement and find all PageElements that match the given criteria.
All find_* methods take a common set of arguments. See the online documentation for detailed explanations."""
titles_RS = soup_BS.find_all('a', 'title')  # 查找所有a标签中class='title'的语句
# 打印查找到的每一个a标签的string
#print(titles)
for title in titles_RS:
    print(title.string)

""":
BeautifulSoup 对象
find_all()方法
"""
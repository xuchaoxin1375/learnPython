# -*- coding: utf-8 -*-
"""
Created on Fri May 21 22:17:08 2021

@author: zero
"""

# bs4.pics.py
'''1. 获取主网页源代码'''
import requests
from bs4 import BeautifulSoup

# url="https://sc.chinaz.com/tupian/"
url = "http://www.jituwang.com/tuku/naturally/"
url = "http://www.jituwang.com/tuku/biology"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
}
response = requests.get(url=url, headers=headers)
response.encoding = "utf-8"
"""
Property text of requests.models.Response @property def text(self) -> str
Content of the response, in unicode.
If Response.encoding is None, encoding will be guessed using chardet.
The encoding of the response content is determined based solely on HTTP headers, 
following RFC 2616 to the letter. 
If you can take advantage of non-HTTP knowledge to make a better guess at the encoding, you should set r.encoding appropriately before accessing this property."""
resp_text = response.text

'''2.从网页源代码获取子标签里的链接'''
soup = BeautifulSoup(resp_text, 'html.parser')
# print(soup)
img_tags_RS = soup.find_all("img")
# print(img_tags_RS)

'''3.爬取链接下的图片，并写入文件'''
for img_tag in img_tags_RS:
    href = img_tag.get('src')
    # 超链接目标:href
    # 查看获取的src的属性值
    print(href)
    # 请断开代理(如果有的话,否则可能失败)
    # 从这里开始,就基本和requests操作一致:
    # get the Response instance
    # get the bytes from the Response instance
    # save the bytes as a file(with open() as...)
    img_response = requests.get(href)
    img_content_bytes = img_response.content
    img_name = href.split('/')[-1]
    with open("image2/" + img_name, mode='wb')as fos:
        fos.write(img_content_bytes)

response.close()

# -*- coding: utf-8 -*-

# tieba_crawler.py
import urllib.request  # 主要用于打开和阅读url
from os.path import join  # 用于串联完整路径

wp = r"c:/users/cxxu/desktop/test_crawl_pictures/"
print("模拟抓取百度贴吧python、java、C#页面,并写入指定路径文件")


def tieba_baidu_html_crawler(url, s):
    header = {'User-Agent': r'Mozilla/5.0 (Windows NT 6.3; WOW64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.235'}  # 伪装成浏览器
    for i in range(len(s)):
        # join the strings to a path of the file to save.
        file_name = join(wp, s[i] + ".html")
        print("正在下载" + s[i] + "页面，并保存为" + file_name)
        # get the Request instance constructed with the headers
        req = urllib.request.Request(url + s[i], headers=header)
        # pass the Request instance to the urlopen() to handle,and invoke the read method to get the information
        content = urllib.request.urlopen(req).read()
        # write the file to with the binary mode "
        with open(file_name, "wb") as file:
            file.write(content)


if __name__ == "__main__":
    url = "http://tieba.baidu.com/f?kw="
    s_tieba = ["python", "java", "c#","test"]
    tieba_baidu_html_crawler(url, s_tieba)

# -*- coding: utf-8 -*-


import os
import re
import urllib.error  # 用于错误处理
# picture_crawler.py
import urllib.request  # 主要用于打开和阅读url

print("爬取指定页面的jpg格式的图片")
prefix_path = "c:/users/cxxu/desktop/crawler_pictures/"


def baidu_tieba_picture_crawler(url, s):
    '''根据传入的地址和关键字列表进行图片抓取'''
    for i in range(len(s)):
        count = 1
        # file_name: str = os.path.join(dirpath,s[i]+".html")
        file_name = os.path.join(prefix_path, s[i] + ".html")
        print("正在下载" + s[i] + "页面，并保存为" + file_name)
        read_result = urllib.request.urlopen(url + s[i]).read()
        middle_dir = s[i]  # parent_dir(图片主题分类)
        to_save_path = os.path.join(prefix_path, middle_dir)
        if not os.path.isdir(to_save_path):
            os.makedirs(to_save_path)  # 创建目录保存每个网页上的图片
        page_data_str = read_result.decode()
        predict_char_num = 100  # page_data_str.index("\n")
        # print(page_data_str[:predict_char_num])
        # 匹配图片的pattern
        #这里括号中的分组用?:来放置findall只返回该括号中匹配到的部分(抗截取,具体查看官方文档(idea不提示用法的话):
        image_pattern = re.compile('<img .*src=\"(.+?)\"')
        image_tag_list=image_pattern.findall(page_data_str)
        for item in image_tag_list:
            print(item)
        # print(image_tag_list)
        for image in image_tag_list:  # 用正则表达式匹配所有的图片
            pattern = re.compile(r'http://.*.jpg$')  # 尝试匹配jpg格式的文件
            # 如果匹配，则获取图片信息，若不匹配，进行下一个页面的匹配
            if pattern.match(image):
                try:
                    # 读取打开图片链接并读取:
                    image_data = urllib.request.urlopen(image).read()  # 获取图片信息
                    count += 1#记录图片序号:
                    image_path = os.path.join(prefix_path, middle_dir, str(count) + ".jpg")  # 给图片命名
                    # 将图片写入文件(二进制形式)
                    with open(image_path, "wb") as image_file:
                        image_file.write(image_data)
                except urllib.error.URLError as e:
                    print("Download failed")
            # 将页面写入文件
            with open(file_name, "wb") as file:
                file.write(read_result)


if __name__ == "__main__":
    url = "http://tieba.baidu.com/f?kw="#kw:key word
    s_tieba = ["itachi"]#中文报错(编码):'ascii' codec can't encode character '\u9f2c' in position 32: ordinal not in range(128)
    baidu_tieba_picture_crawler(url, s_tieba)

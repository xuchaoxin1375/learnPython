# -*- coding: utf-8 -*-


import os
import re
import urllib.error  # 用于错误处理
# picture_crawler.py
import urllib.request  # 主要用于打开和阅读url

prefix_path = r"pics"


def picCraw(url, topic, img_pattern_str):
    count = 1
    file_name = os.path.join(prefix_path, topic + ".html")
    print("正在保存:" + file_name)
    read_result_bytes = urllib.request.urlopen(url).read()
    to_save_path = os.path.join(prefix_path, topic)
    if not os.path.isdir(to_save_path): os.makedirs(to_save_path)  # 创建目录保存图片

    page_data_str = read_result_bytes.decode()
    MatchedImage_link_list = re.findall(img_pattern_str, page_data_str)  # 找出所有匹配
    print("MatchedImages:", MatchedImage_link_list)
    for image in MatchedImage_link_list:  # 用正则表达式匹配所有的图片
        pattern = re.compile(r'//.*\.jpg$')  # 匹配jpg格式的文件
        if pattern.search(image):  # 如果匹配成功，则获取图片信息；若不成功继续下一个
            try:
                if "http" not in image: image = "http:" + image
                image_data_bytes = urllib.request.urlopen(image).read()  # 获取图片信息
                image_path = os.path.join(prefix_path, topic, str(count) + ".jpg")  # 给图片命名
                count += 1
                with open(image_path, "wb") as image_file:
                    image_file.write(image_data_bytes)  # 将图片写入jpg文件
            except urllib.error.URLError as e:
                print("Download failed")
        with open(file_name, "wb") as file:  # 将页面写入文件
            file.write(read_result_bytes)


if __name__ == "__main__":
    url = 'https://sc.chinaz.com/tupian/fengjingtupian.html'
    # 匹配图片的pattern,可通过查看网页源代码获悉
    #通过findall(),该会返回匹配该分组的匹配部分所构成的集合
    img_pattern_str = r'<img src2=\"(.+\.jpg)\"'
    picCraw(url, "scene", img_pattern_str)

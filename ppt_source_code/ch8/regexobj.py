# -*- coding: utf-8 -*-
#regexobj.py
import re
text="Joodie is a handsome boy. He is cool, clever.."
regex_pattern=re.compile('\w*oo\w*')#查找所有包含'oo'的单词
#1.正则表达式对象的方法findall
a=regex_pattern.findall(text)
print("正则表达式模式对象的方法:",a)
#2.模块re的函数findall
b=re.findall('\w*oo\w*',text)
print("模块re的函数:",b)

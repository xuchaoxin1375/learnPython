# -*- coding: utf-8 -*-
#re_group.py
import re
pattern=re.compile(r'www\.(.*)\.(.*)') #用()表示组1，组2,...
# 使用模式对象便于复用,减少模式串的输入
# 实现被匹配串的部分字符功能,当然,除了group函数,还依赖于模式串中的分组
m=pattern.match('www.dxy.com')
m0=m.group()       #默认为0，表示匹配整个字符串   
m1=m.group(1)      #返回给定组1匹配的子字符串
m2=m.group(2)      #返回给定组2匹配的子字符串
print(m0)
print(m1)
print(m2)

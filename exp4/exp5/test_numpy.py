'''
Description: 
Version: 2.0
Author: xuchaoxin
Date: 2021-04-14 23:04:21
LastEditors: xuchaoxin
LastEditTime: 2021-04-15 07:28:35
'''
import numpy as np
a=np.logspace(0,2,20)
b=np.logspace(0,4,5)
""" 定开始值，结束值 ，元素个数，不指定对数底数，默认为10 """
a=np.diag([1,2,3])
# print(a)
# print(b)

from numpy import random as nr
a=nr.randn()
""" randn(d0, d1, ..., dn)
Return a sample (or samples) from the "standard normal" distribution. """
print(a)
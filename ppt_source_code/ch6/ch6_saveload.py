# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 22:12:57 2021

@author: zero
"""

#ch6_saveload.py
import numpy as np
a=np.arange(30).reshape(2,3,5)
print('array a:\n',a)

np.save('a.npy',a)
b=np.load('a.npy')
print("array b:\n",b)

np.savez('c.npz',a) #存储压缩数据
c=np.load('c.npz')
print("c:\n",c)
print("array c:\n",c['arr_0'])

#压缩多个数组
u = np.array([[1,2,3],[4,5,6]])
v = np.arange(0, 1.0, 0.1)
w = np.sin(v)
np.savez("result.npz", u, v, sin_array = w)
r = np.load("result.npz")
print('array u:\n',r["arr_0"]) # 数组u
print('array v:\n',r["arr_1"]) # 数组v
print('array w:\n',r["sin_array"]) # 数组w

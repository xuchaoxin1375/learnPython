# -*- coding: utf-8 -*-
"""
Created on Wed Nov 02 16:50:41 2016

@author: gsdx
"""
# ch6_math_sin_numpy_sin_comparison_ufunc.py
import time,math
import numpy as np

x = [i * 0.001 for i in range(1000000)]
start = time.time()
for i, t in enumerate(x):
    x[i] = math.sin(t)
print("math.sin:", time.time() - start)

x = [i * 0.001 for i in range(1000000)]
x = np.array(x)
start = time.time()
np.sin(x,x) #ufunc运算
print("numpy.sin:", time.time() - start)

x = [i * 0.001 for i in range(1000000)]
start = time.time()
for i, t in enumerate(x):
    x[i] = np.sin(t) #迭代逐个计算
print("numpy.sin loop:", time.time() - start)



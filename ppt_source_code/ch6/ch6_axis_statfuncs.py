# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 11:22:22 2021

@author: zero
"""
#ch6_axis_statfuncs.py
import numpy as np
a=np.array([range(10*i,10*i+3) for i in range(2)])
print("array a:\n",a)
print(np.sum(a),np.max(a),np.min(a),np.mean(a),np.std(a))
print(a.sum(),a.max(),a.min(),a.mean(),a.std())

print("sum0:",np.sum(a,axis=0))
print("sum1:",np.sum(a,axis=1))
print("mean0:",a.mean(axis=0))
print("mean1:",a.mean(axis=1))


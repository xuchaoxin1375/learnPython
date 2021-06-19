# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 16:20:31 2021

@author: zero
"""
#ch6_linearSystemOfEquations.py
import numpy as np
from scipy import linalg
A = np.array([[1,3,5],[2,5,1],[2,3,8]])
print("array A:\n",A)
b = np.array([[10],[8],[3]])
print("b:\n",b)

x1=linalg.inv(A).dot(b)  # solution
print("solution x1:\n",x1)
print('check1:\n',A.dot(linalg.inv(A).dot(b))-b)

x2=np.linalg.solve(A, b)  # fast 
print("solution x2:\n",x2)
print("check2:",A.dot(np.linalg.solve(A, b))- b) 




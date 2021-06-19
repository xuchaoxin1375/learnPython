# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 21:34:53 2021

@author: zero
"""
#ch6_savetxt_loadtxt.py
import numpy as np
a=np.arange(50).reshape(5,10)
print("array a:\n",a)
np.savetxt('a.csv',a,fmt='%d',delimiter=',')

b=np.arange(30).reshape(3,10)
np.savetxt('b.csv',b,fmt='%.1f',delimiter=',')
c=np.loadtxt('b.csv',delimiter=',')
print("array c:\n",c)

d=np.arange(12).reshape(3,2,2)
print("array d:\n",d)
d.tofile('d.dat',sep=',',format='%d')
e=np.fromfile('d.dat',dtype=np.int,sep=',')
print("array e:\n",e)


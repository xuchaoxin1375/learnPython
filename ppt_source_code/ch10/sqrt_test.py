# -*- coding: utf-8 -*-
#sqrt_test.py
import time
N=10**7
import sqrt_py as sp
t1=time.time()
sp.fsq(N) #pure python
t2=time.time()
print("time for py:%.3fs"%(t2-t1))

import sqrt_cy1 as sc1
t1=time.time()
sc1.fsq(N) 
t2=time.time()
print("time for cy1:%.3fs"%(t2-t1))

import sqrt_cy2 as sc2
t1=time.time()
sc2.fsq(N)
t2=time.time()
print("time for cy2:%.3fs"%(t2-t1))

import sqrt_cy3 as sc3
t1=time.time()
sc3.fsq(N)
t2=time.time()
print("time for cy3:%.3fs"%(t2-t1))

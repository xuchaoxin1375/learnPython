# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 08:15:24 2021

@author: zero
"""
#ch4:pickle_dump_load.py
import pickle
tup0 = ('I love Python', {"HZ":5,"SX":4,"OT":3},[7,8],None)

pick1 = pickle.dumps(tup0) #将tup0转成二进制对象
mytup = pickle.loads(pick1)#将pick1转成Python对象
print(mytup)


#ch4:pickle_dump_load.py
import pickle

def fsq(x):
    return x**2+5
tup1 = ('Python', {"HZ":5,"SX":4,"OT":3},fsq, None)

with open ("a.txt", 'wb') as f: #打开文件
    pickle.dump(tup1, f) #用dump将Python对象转成二进制对象文件
with open ("a.txt", 'rb') as f: #打开文件
    tup2 = pickle.load(f) #将二进制文件对象转换成Python对象
print(tup2)
x=10
print("fsq(%d)="%x,tup2[2](x))


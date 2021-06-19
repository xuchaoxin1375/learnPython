# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 10:50:07 2021

@author: zero
"""
#ch6_numpy_random.py
#from numpy import random as nr
#rand_x=nr.rand(2,3)
#rand_x0=nr.rand()
#randn_x=nr.randn(2,3)
#randn_x0=nr.randn()
#
#randint_x1=nr.randint(5,10, size=(2,4))
#randint_x2=nr.randint(5, size=10)
#
#cho_x1=nr.choice(5,4)#等价于randint(0,5,3),且权值相同
#cho_x2=nr.choice(5,4,p=[0.1,0,0.3,0.6,0])#非均匀分布，服从分布p
#cho_x3=nr.choice(5,3,replace=False) #无放回抽样
#cho_x4=nr.choice(5,3,replace=False,p=[0.1,0,0.3,0.6,0])
#words = ['pooh', 'rabbit', 'piglet', 'Christopher']
#cho_x5=nr.choice(words,3, p=[0.5,0.1,0.1,0.3])
#
#print("rand_x:\n",rand_x)
#print("rand_x0:\n",rand_x0)
#print("randn_x:\n",randn_x)
#print("randn_x0:\n",randn_x0)
#print("randint_x1:\n",randint_x1)
#print("randint_x2:\n",randint_x2)
#print("cho_x1:\n",cho_x1)
#print("cho_x2:\n",cho_x2)
#print("cho_x3:\n",cho_x3)
#print("cho_x4:\n",cho_x4)
#print("cho_x5:\n",cho_x5)

#ch6_numpy_random.py
import numpy as np
mu, sigma = 0, 0.1#mean and standard deviation
s = np.random.normal(mu, sigma, 10000)
print("#samples:",len(s))
print(abs(mu-np.mean(s))<0.01)
print(abs(sigma-np.std(s,ddof=1))<0.01)
#ddof=1表示无偏估计，除式分母使用N-ddof

import matplotlib.pyplot as plt
count, bins, ignored = plt.hist(s, 20)
print(len(bins),bins)
print(len(count),count)




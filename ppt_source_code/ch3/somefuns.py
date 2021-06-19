# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 21:08:00 2018

@author: zero
"""
#somefuns.py
a=[5,7,9,1]
print(sum(a),len(a))
print()
for x in a:
    print(x)
print()
for i, x in enumerate(a):
    print(i,x)
print()
b=[11,22,33,44]
print(zip(a,b))
for x,y in zip(a,b):
    print(x,y)
print()
c=['Are','you','OK','?']
for x,y,z in zip(a,b,c):
    print(x,y,z)
    

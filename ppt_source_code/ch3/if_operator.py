# -*- coding: utf-8 -*-
#ch3: if_operator.py
def jia(x,y):
    print(x+y)   
def jian(x,y):  
    print(x-y) 
def cheng(x,y):  
    print(x*y)
def chu(x,y):  
    print(x/y) 
operator = {'+':jia,'-':jian,'*':cheng,'/':chu}  
def f(x,o,y):  
    operator.get(o)(x,y)  
f(3,'+',2)  



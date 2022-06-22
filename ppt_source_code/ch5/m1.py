# -*- coding: utf-8 -*-
#ch5: m1.py
PI=3.1415
year=2014

def fib(n): #print Fibonacci series up to n-1
    a,b=0,1
    while b<n:
        print(b,)
        a,b=b,a+b

def fib2(n): #return Fibonacci series up to n-1
    result=[]
    a,b=0,1
    while b<n:
        result.append(b)
        a,b=b,a+b
    return result

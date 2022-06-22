# -*- coding: utf-8 -*-
#ch6_frompyfunc.py
import numpy as np

def triangle_func(c,c0,hc):
    def trifunc(x):
        x=x-int(x)
        if x>=c: r=0.0
        elif x<c0: r=x/c0*hc
        else: r=(c-x)/(c-c0)*hc
        return r
    return np.frompyfunc(trifunc,1,1)

trifun=triangle_func(0.6,0.4,1.0)
a=np.linspace(1,10,5)
print(a)
print(trifun(a))


# -*- coding: utf-8 -*-
"""
Created on Wed Nov 02 19:50:51 2016
@author: zero
"""
#ch6_scipy_least_square
import numpy as np
from scipy.optimize import leastsq
import pylab as pl
def func(x, p):
    """数据拟合所用的函数: A*sin(2*pi*k*x + theta)"""
    A, k, theta = p
    return A*np.sin(2*np.pi*k*x+theta)   
def residuals(p, y, x): #定义计算误差的函数
    """实验数据x, y和拟合函数之间的差，p为拟合需要找到的系数"""
    return y - func(x, p)
x = np.linspace(0, -2*np.pi, 100)
A, k, theta = 10, 0.34, np.pi/6 # 真实数据的函数参数
y0 = func(x, [A, k, theta]) # 真实数据
y1 = y0 + 2 * np.random.randn(len(x))#加入噪声后的y值    
p0 = [7, 0.2, 0] # p0为拟合参数的初始值
# 调用leastsq进行数据拟合，args为需要拟合的实验数据
plsq = leastsq(residuals, p0, args=(y1, x))
print("真实参数:", [A, k, theta])
print("拟合参数:", plsq[0]) # 实验数据拟合后的参数
pl.plot(x, y0, label="real data")
pl.plot(x, y1, label="experimental data with noise")
pl.plot(x, func(x, plsq[0]), label="fitted data")
pl.ylim(-15,25)
pl.legend()
pl.show() 


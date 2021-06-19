# -*- coding: utf-8 -*-

#ch6_scipy_integrate_area.py
from scipy import integrate

#定义半圆曲线
def half_circle(x):
    return (1-x**2)**0.5
#利用quad函数进行数值积分
pi_half,err = integrate.quad(half_circle, -1, 1)
print("PI value:", pi_half*2)

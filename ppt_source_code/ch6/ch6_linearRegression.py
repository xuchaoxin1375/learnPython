# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 21:17:30 2021

@author: zero
"""
#ch6_linearRegression.py
import numpy as np
from sklearn.linear_model import LinearRegression
X = np.array([[3, 1.1], [1, 5.7], [2, 2], [2, 3]])
# y = 1 * x_0 + 2 * x_1 + 3
# y = np.dot(X, np.array([1, 2])) + 3 #真实的y值
y=[1,2,5,3]
print(y)
reg = LinearRegression()
reg.fit(X, y)
print("weights:",reg.coef_)
print("intercept:",reg.intercept_)
print("prediction:",reg.predict(np.array([[7, 5.9]])))


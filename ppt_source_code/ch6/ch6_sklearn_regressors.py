# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 21:59:16 2021

@author: zero
"""


### 决策树回归 ###
from sklearn import tree
model_DecisionTreeRegressor = tree.DecisionTreeRegressor()
 
### 线性回归 ###
from sklearn import linear_model
model_LinearRegression = linear_model.LinearRegression()
 
### SVM回归 ###
from sklearn import svm
model_SVR = svm.SVR()
 
### KNN回归 ###
from sklearn import neighbors
model_KNeighborsRegressor = neighbors.KNeighborsRegressor()
 
### 随机森林回归 ###
from sklearn import ensemble
model_RandomForestRegressor = ensemble.RandomForestRegressor(n_estimators=20)#用20个决策树
 
### Adaboost回归 ###
from sklearn import ensemble
model_AdaBoostRegressor = ensemble.AdaBoostRegressor(n_estimators=50)#用50个决策树
 
### GBRT回归 ###
from sklearn import ensemble
model_GradientBoostingRegressor = ensemble.GradientBoostingRegressor(n_estimators=100)#用100个决策树
 
### Bagging回归 ###
from sklearn.ensemble import BaggingRegressor
model_BaggingRegressor = BaggingRegressor()
 
### ExtraTree极端随机树回归 ###
from sklearn.tree import ExtraTreeRegressor
model_ExtraTreeRegressor = ExtraTreeRegressor()


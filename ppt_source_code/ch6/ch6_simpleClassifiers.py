# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 22:27:12 2021

@author: zero
"""

#ch6_SimpleClassifiers.py

#K-nearest neighbors
X = [[0.2,1.,1.5], [1.2,3.1,0.8], [2.,3.2,1.], [3.,2.,0.3]]
y = [0, 0, 1, 1]#二分类：训练集含4个样本,类标号为0或1
from sklearn.neighbors import KNeighborsClassifier
neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(X, y)
newx=[[1.1,-1.2,2.3]]
print("Pred_KNN:",neigh.predict(newx))
print("Prob_KNN:",neigh.predict_proba(newx))

#Gaussian naive bayes
import numpy as np
X = np.array([[-1,-1],[-2,-1],[-3,-2],[1,1],[2,1],[3,2]])
Y = np.array([1, 1, 1, 2, 2, 2])
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
clf.fit(X, Y)
newx=[[0.8, -1],[1,1.2]]
print("Pred_GNB:",clf.predict(newx))
print("Prob_GNB:",clf.predict_proba(newx))

#logistic regression
from sklearn.datasets import load_iris
X, y = load_iris(return_X_y=True)
print("X shape:",X.shape,type(X)) #150个样本，4个特征
print("label:",set(y)) #3分类问题
from sklearn.linear_model import LogisticRegression
clf = LogisticRegression().fit(X, y)
testX=X[:2, :]
print("Pred_logR:",clf.predict(testX))
print("Prob_logR:",clf.predict_proba(testX))



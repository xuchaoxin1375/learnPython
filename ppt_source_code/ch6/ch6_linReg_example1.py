# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 21:44:55 2021

@author: zero
"""

#ch6_linReg_example1.py
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
#Load the diabetes dataset
diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True)
#Split the features and targets into training/testing sets
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]
diabetes_y_train = diabetes_y[:-20]
diabetes_y_test = diabetes_y[-20:]

regr = linear_model.LinearRegression()#Linear regression object
regr.fit(diabetes_X_train, diabetes_y_train)#Train the model
diabetes_y_pred = regr.predict(diabetes_X_test)# Make predictions

print("训练集特征个数：",diabetes_X_train.shape[1])
print('Coefficients: \n', regr.coef_)#The coefficients
print("Intercept:\n",regr.intercept_)
print('Mean squared error: %.2f'
      % mean_squared_error(diabetes_y_test, diabetes_y_pred))
# The coefficient of determination: 1 is perfect prediction
print('Coefficient of determination: %.2f'
      % r2_score(diabetes_y_test, diabetes_y_pred))
print("Actual labels of the test set:\n",diabetes_y_test)


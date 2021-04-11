'''
Description:
Version: 2.0
Author: xuchaoxin
Date: 2021-01-31 10:02:26
LastEditors: xuchaoxin
LastEditTime: 2021-01-31 20:05:16
'''


def factorial(x):
    if x == 1:
        return 1
    # print(str(x)+" ")
    return factorial(x-1)*x

print(factorial(5))

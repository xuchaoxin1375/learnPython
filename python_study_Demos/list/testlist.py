'''
Description: 
Version: 2.0
Author: xuchaoxin
Date: 2021-04-08 22:55:30
LastEditors: xuchaoxin
LastEditTime: 2021-04-11 14:23:25
'''
""" if else list comprehesion """
a = [i for i in range(10) if i % 2 == 0]
print(a)
a = [i if i % 2 == 0 else "pass" for i in range(10)]
a = [i if i % 2 == 0 else 'qi' for i in range(10)]
print(a)
# test git
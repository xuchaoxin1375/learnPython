# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 20:52:27 2019
@author: zero
"""
#sort_lambda.py
nums = [1, 3, 2, 4]
# nums.sort()
print("Sorted numbers1:",nums) # [1, 2, 3, 4]
nums.sort(reverse=True)
print("Sorted numbers2:",nums) # [4, 3, 2, 1]


dat = [['Li',10],['Hu',30],['Yu',20],['Ji',40]]
dat.sort()
print("Sorted list1:")
print(dat)
dat.sort(key=lambda pair: pair[1])
print("Sorted list2:")
print(dat)
dat.sort(key=lambda pair: pair[1],reverse=True)
print("Sorted list3:")
print(dat)


# %%

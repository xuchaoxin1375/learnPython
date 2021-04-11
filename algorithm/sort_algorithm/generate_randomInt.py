'''
Description: 
Version: 2.0
Author: xuchaoxin
Date: 2021-03-07 11:00:11
LastEditors: xuchaoxin
LastEditTime: 2021-03-27 12:46:36
'''
import random 
from print_some import printSome

# n=input("Enter a integer that represents the number of elements for the sort problem you want to simulate:")
# n=int(n)
def generate(n=50):
    arr=[]
    for i in range(n):
        arr.append(random.randint(0,n*10))
    return arr
    
#   printSome(arr,str="原始序列")


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
import numpy as np

# n=input("Enter a integer that represents the number of elements for the sort problem you want to simulate:")
# n=int(n)
def generate(n=50):
    """ 产生指定数量的随机数,默认50个整形数 """
    arr=[]
    for i in range(n):
        arr.append(random.randint(0,n*10))
    return arr
def generate_by_shuffle(n=30):
    l=list(range(n))
    random.shuffle(l)
    return l
import numpy.random as npr
def generate_by_numpy(n):
    base_arr=npr.random(size=(n))
    ret=base_arr*3+4
    # base_arr
    return ret
    # print(ret)
#   printSome(arr,str="原始序列")
if __name__=="__main__":
    # print(generate(100))
    printSome(generate(20))
    printSome(generate_by_shuffle(20))
    print(generate_by_numpy(20))

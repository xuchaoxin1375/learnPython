'''
Description: 
Version: 2.0
Author: xuchaoxin
Date: 2021-03-06 11:18:54
LastEditors: xuchaoxin
LastEditTime: 2021-03-06 20:10:10
'''
# Filename: test.py
 
from print_some import printSome
import random
import time
from time import time

import insertion_sort
import merge_sort

n=input("Enter a integer that represents the number of elements for the sort problem you want to simulate:")
n=int(n)
arr=[]
for i in range(n):
    arr.append(random.randint(0,n*10))
    
# printSome(arr,str="原始序列")
#深拷贝一份未排序数列
arr_bak=arr[:]
# printSome(arr_bak,str="复制的原始序列")

""" 开始比较计时:这一段可以考虑用函数式编程(函数作为参数) """
#统计插入排序的耗时
start_time1=time()
printSome(arr,str="插入排序之前:")
insertion_sort.insertionSort(arr)
end_time1=time()
printSome(arr,str="插入排序之后:")
print("the insertion sort takes time:%s" % (end_time1-start_time1))

#统计归并排序的耗时
start_time2=time()
printSome(arr_bak,str="归并排序之前:")
#注意,此归并排序的结果以MergeSort()函数返回来获得,并不会直接在参数列表中改动
arr_bak=merge_sort.MergeSort(arr_bak)
end_time2=time()
printSome(arr_bak,str="归并排序之后:")
print("the MergeSort sort takes time:%s" % (end_time2-start_time2))

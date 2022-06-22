# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 14:40:13 2021

@author: zero
"""
#ch6_sort_argsort.py
import numpy as np
a = np.array([[1,4],[3,1]])
print("Original array a:\n",a)
a1=np.sort(a)  # 默认按最后一维排序，每行各自排序             
print("Sorted array a1:\n",a1)

a2=np.sort(a, axis=0)# 按第1维排序 ，每列各自排序  
print("Sorted array a2:\n",a2)

a3=np.sort(a, axis=None) #所有元素排序
print("Sorted array a3:\n",a3)

dtype=[('name', 'S10'), ('height', float), ('age', int)] #自定义数据类型
values=[('Arthur', 1.8, 41),  ('Lancelot', 1.9, 38), ('Galahad', 1.7, 38)]
b=np.array(values, dtype=dtype) #多级排序
a4=np.sort(b, order='height')                        
print("Sorted array a4:\n",a4)


#ch6_sort_argsort.py
import numpy as np
x = np.array([3, 1, 2])#一维数组
print("index:",np.argsort(x))#argsort返回排序后的下标

x = np.array([[2, 3,5], [8, 1,-3]])#二维数组
print("Original array:\n",x,'\n')
print("Sorted array0:\n",np.sort(x,axis=0))
print("index0:\n",np.argsort(x, axis=0))
print()
print("Sorted array1:\n",np.sort(x,axis=1))
print("index1:\n",np.argsort(x, axis=1))


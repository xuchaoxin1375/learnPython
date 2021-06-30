import numpy as np
from numpy import random
from numpy.lib.function_base import average
import pandas as pd
import math
import time
import scipy
from scipy import integrate
import matplotlib.pyplot as plt  

''' 7 '''
''' df = pd.DataFrame([[1, 2], [4, 5], [7, 8]],
     index=['cobra', 'viper', 'sidewinder'],
     columns=['max_speed', 'shield']) '''
data_dict={'dataset':['I','I','I','I','I'],'x':[10,8,13,9,11],'y':[8.04,6.95,7.58,8.81,8.33]}
df=pd.DataFrame(data=data_dict)
''' I found that if use numpy.array to make the dataFrame,the mean() method work uncorrectly!'''
# data_lists=[['I','I','I','I','I'],[10,8,13,9,11],[8.04,6.95,7.58,8.81,8.33]]
# #the common python lists will be priority by line make the parameter for the constractor with specified columns;
#  the numpy.array instance may be is more flexible:
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html?highlight=dataframe#pandas.DataFrame

# df=pd.DataFrame(data=np.array(data_lists).T,columns=['dataset','x','y'])
# print(df)
df.loc[[2,4],'dataset']="II"
# tmp=df[[2,4],['dataset']]
print(df)
''' averages: '''
bool_serial_I=df['dataset']=='I'
# print(df['dataset']=='I')
items_I=df.loc[bool_serial_I]
# print(tmp1.loc[:,['x','y']])
# tmp1=tmp1.loc[:,['x','y']]
# print(tmp1)
print(items_I)
# print(type(items_I))
# print(items_I.mean(1))
average_I=items_I.mean(1)
# print(type(average_I.values))#<class 'numpy.ndarray'>
# print(average_I.values)
average_I_df=average_I.to_frame()
average_I_df.columns=["averages of x+y"]
print(average_I_df)
# print(type(average_I))#<class 'pandas.core.series.Series'>
#note:the mean() there return a Serial rather than a dataFrame!,so the result just has the index tag but no columns!
# print("average of x+y for I:",average_I[:])
# items_I.columns=["index","averages"]
# print(items_I.columns)
# print(items_I.index)
bool_serial_lt=df["x"]>9.5
tmp2=df[bool_serial_lt]
print("the average of y:",end="")
print(tmp2['y'].mean())






""" 6 """
# array_randn=random.normal(-1,1,1000)
# import matplotlib.pyplot as plt
# import time
# plt.ion() #开启interactive mode
# x = np.linspace(0, 50, 1000)

# plt.figure(1) # 创建图表1
# plt.plot(x, np.sin(x))
# plt.show()
# time.sleep(1)
# plt.close(1)

# print ('it is ok')

""" 5 """
# def f(x):
#     return x**2+np.math.sin(x)+math.sqrt(x)+x**(1/3)+1
# print('integration:',integrate.quad(f,1,2)[0])

""" 4 """

# def myfun(x):
#     return math.cos(x)


# def umyfun():
#     # def myfun(x):
#     #     return math.cos(x)
#     return np.frompyfunc(myfun, 1, 1)

# # array = random.randint(1, 100000, size=100000)
# array=np.arange(1,100000)
# # print(umyfun()(np.array([math.pi,0])))

# start_time=time.time()
# result = umyfun()(array)
# print(result)
# print("umyfun() used time:",time.time()-start_time)

# start_time2=time.time()
# result2=np.cos(array)
# print(result2)
# print("np.cos(result) used time:",time.time()-start_time2)



""" 3 """
# a=random.uniform(10,20,(10,5))
# print(a)
# average_array=np.mean(a,axis=1)
# average_matrix=average_array.reshape(average_array.shape[0],1)
# np.savetxt("dat.csv",a,fmt="%.3f",delimiter=',')
# a[[1,2],:]=np.loadtxt("dat.csv",delimiter=",")[[1,2],:]
# index_col=a[:,1]
# indices_col=np.argsort(index_col)

# a=a[indices_col,:]
# print(a)

# print(average_matrix)
# print(a-average_matrix)
# print(np.array([1,2,3]))
''' 2 '''
# A=random.uniform(-1,1,10000)
# # print(A)
# B=random.normal(size=10000)
# print(A+B)
# print("A@B=",A*B)
# print("A/B=",A/B)
# print("exp(A)+exp(B)=",np.exp(A)+np.exp(B))
# print("A*B=",A*B)
# print("averageB,maxB,minB=",np.average(B),np.max(B),np.min(B))

''' 1 '''
# a1=random.randn(9,10)
# print(a1)
# print(a1[a1[:,:]>1])
# array_randn=random.randn(20)
# array_bool=array_randn>1
# print(array_bool)
# filter_result=array_randn[array_bool]
# print(filter_result)

# print(a1[2,5])
# print(a1[6,3])
# print(a1[3:5,4:6])
# print(a1[3:5,[1,2,4]])
# # np.where(random.rand(10)>0.5,10,)
# print(np.where(a1>1,10,-10))
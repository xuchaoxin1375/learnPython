'''
Description: 
Version: 2.0
Author: xuchaoxin
Date: 2021-03-05 23:25:22
LastEditors: xuchaoxin
LastEditTime: 2021-03-07 18:38:09
'''
from time import time
import random
def insertionSort(arr): 
    """ 利用一个二重循环来实现,i表示待插入元素在原数列中的索引"""
    """ 没执行一次for循环,一个元素就被插入到有序区域中,并且有序区的数列仍然保持有序 """
    for i in range(1, len(arr)): #range(n)产生0到n-1的数列,range(m,n)是m到n左闭右开的数列 
        # i=1,2,3,,,len(arr)-1;
        # 保存当前被排序元素(待插入元素)(防止被覆盖而消失)
        key = arr[i] 
        """ 辅助索引变量j定义为:和待插入元素相比较大小的元素的索引,初始化为i元素的前一个元素 """
        j = i-1
        """ 判断当前的数对(number pair)的大小,并决定是否需要对原有序序列的某部分你数做位置的移动(向后覆盖)"""
        """ 每执行一次while循环,可以将数列中的一个元素向后移动(覆盖) """
        while j >=0 and key < arr[j] : 
                """ 将前面一个元素覆盖掉后一个元素,达到元素后移的效果 """
                arr[j+1] = arr[j] 
                # 下标j是在有序区中从后往前遍历,且j>=0才是有效的索引,(当判断到j<0时,就应该停止向前遍历)
                # 索引j-1必须和arr[j+1]=arr[j]绑定在一起,while循环才能正常运行
                j -= 1
        """ 执行插入操作(key元素找到了合适的插入位置)
        arr[j]元素是第一个比key小的元素,所以,key元素要插入到arr[j+1]位置上,"""
        arr[j+1] = key 
  
""" 测试该insert_sort(List) """
""" arr=[]
for i in range(1000):
    arr.append(random.randint(0,20000)) """
#开始计时(time start)
# func_start=time()
# #invoke the insert_sort()
# insertionSort(arr) 
# #time end
# func_end=time()
# print("the function takes time:",func_end-func_start)


""" 经过验证,该算法正确,这里就不打印全部了 """
# print ("排序后的数组:") 
# for i in range(50): 
#     print ("%d" %arr[i],sep="",end=" ")
# print("......")

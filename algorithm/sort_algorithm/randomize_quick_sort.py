'''
Description:
Version: 2.0
Author: xuchaoxin
Date: 2021-03-26 21:00:45
LastEditors: xuchaoxin
LastEditTime: 2021-03-28 18:57:41
'''
import generate_randomInt
import random

""" partition:we need the state that meet the condition:elements in the left part <= pivot_element;and elements in the right part >=pivot_element;the pivot_element is in the proper location of the sequence finally
it's no more than to describe the demand of the function to achieve a certain algorithm!!
unless you are very familiar to what you write (otherwise ,don't overestimate the degree your understand of the algorithm you are writing;it's time for you to formulate a series of regularity/norm
"""


def partition(dataList, pivot_index):  # district
    """这个函数只是为了让quick_sort()内部代码结构更紧凑而提取出来的(不是必须的)

    Args:
        dataList (list): [description]
        pivot_index (Number): [description]
        rightList (List): [description]
        leftList (List): [description]
    """

    size_of_dataList = len(dataList)
    """ set two index variable to partition the sequence """
    i = 0
    j = size_of_dataList-1
    """ save the pivot_element to be compared: """
    pivot_element = dataList[pivot_index]
    """ swap the pivot generated randomly,transform the familiar problem to solve """
    dataList[pivot_index], dataList[0] = dataList[0], dataList[pivot_index]

    # print("debug...\n pivot_element", pivot_element)
    """ 
    sequence_k:contains the elements<=pivot;
    sequence_j:contains the elements>pivot;
    k,j grow in two threads (we can know ,all of them grow continuosly separately)
    """
    k = 0
    for j in range(1, size_of_dataList):
        if dataList[j] <= pivot_element:
            k += 1
            dataList[k], dataList[j] = dataList[j], dataList[k]
    """ insert(swap to) the pivot_element to proper location """
    dataList[0],dataList[k]=dataList[k],dataList[0]
    """ update the pivot_index: """
    pivot_index = k
    return pivot_index


def quick_sort(dataList):
    """利用递归来实现快速排序(随机轴心+置换版)
<<<
    Args:
        dataList (list): 待排序的数列

    Returns:
        list: 排好序的数列!!!>>>

    """
    if len(dataList) >= 2:  # 递归入口及出口(如果(当前深度)传入的列表中只有一个元素,则直接返回结果)
        """ 选取基准值，也可以选取第一个或最后一个元素(注意这里用地板除法)
        这个基准值将要特地取出来,会用来连接左侧序列和右侧序列(也作为关节元素)
        """
        pivot_index = random.randint(0, len(dataList)-1)
        pivot_element = dataList[pivot_index]
        # debug...

        # pivot_index = dataList[len(dataList)//2]
        # pivot_index = len(dataList)//2
        # print("random_pivot_index=", pivot_index)
        # print("random_pivot_element=", pivot_element)

        """ 逐个判断数列中的各个元素和基准值的大小关系,并放到对应侧的子序列中
        可以考虑封装到一个函数中去"""
        pivot_index = partition(dataList, pivot_index)  # 核心算法(代码段)1

        leftList, rightList = dataList[0:pivot_index], dataList[pivot_index+1:]
        pivot_element = dataList[pivot_index]

        # print("debuging..\n\nleftList:", leftList)
        # print("pivot_element:", pivot_element)
        # print("rightList:\n", rightList)
        """ 递归调用:对两侧子序列分别调用quick_sort()处理 """
        return quick_sort(leftList) + [pivot_element] + quick_sort(rightList)  # 核心算法(代码段)2
        # return leftList+pivot_element+rightList
    else:
        return dataList


# 示例：
# array = [2, 3,6,6]
# array= [2,3,5,7,1,4,6,15,5,12]
# array = [2, 3, 5, 7, 1, 4, 6, 15, 5, 2, 7, 9, 10, 15, 9, 17, 12]
array=[2,5,3,6,8,13,10,11]

# array = generate_randomInt.generate()
print("the input sequence:\n", array)
print("the sorted sequence:")
print(quick_sort(array))

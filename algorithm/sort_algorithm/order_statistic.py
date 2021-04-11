'''
Description: 
Version: 2.0
Author: xuchaoxin
Date: 2021-03-26 21:01:11
LastEditors: xuchaoxin
LastEditTime: 2021-03-28 21:10:51
'''
import random


def partition(dataList):  # district
    """partition:
    Args:
        dataList (list): [description]
        pivot_index (Number): [description]
        rightList (List): [description]
        leftList (List): [description]
    """
    pivot_index = random.randint(0, len(dataList)-1)
    size_of_dataList = len(dataList)
    """ set two index variable to partition the sequence """
    j = size_of_dataList-1
    """ save the pivot_element to be compared: """
    pivot_element = dataList[pivot_index]
    """ swap the pivot generated randomly,transform the familiar problem to solve """
    dataList[pivot_index], dataList[0] = dataList[0], dataList[pivot_index]

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
    dataList[0], dataList[k] = dataList[k], dataList[0]
    """ update the pivot_index: """
    pivot_index = k
    return pivot_index


def find(list, i):
    """
    Args:
        list ([list ]): [description]
        i ([int ]): [description]

    Returns:
        [Number]: [element of we we desire ]
    """
    i -= 1
    return rand_select(list, i)


def rand_select(list, i):
    """base on the i is the index  of the list /array 

    Args:
        list (List ): the sequence to be calculate 
        i ([int ]): the index of i_th smallest element count from 0 rather then count from 1  

    Returns:
        [int ]: [result ]
    """    
    # i-=1
    size = len(list)

    if size == 1:
        return list[0]
    """ r :the index of the pivot  """
    r = partition(list)
    """ the pivot is the answer we want to calculate  """
    if i == r:
        return list[r]

    left_list = list[0:r]
    right_list = list[r+1:]
    if i < r:
        return rand_select(left_list, i)
    else:
        """ we need embody the index :substract 1 """
        return rand_select(right_list, i-r-1)


# print(find([10,2,7,3,40],3))
print(find([2, 5, 3, 6, 7, 0, -10, -100, 90], 4))

'''
Description: 
Version: 2.0
Author: xuchaoxin
Date: 2021-03-19 22:11:17
LastEditors: xuchaoxin
LastEditTime: 2021-03-20 08:24:54
'''

""" 
初始化总和变量
	方案一:
		初始化为0总是合适的(累乘变量初始化为1也总是合适的)
			因为0与任何数相加都不会改变被加和的数的大小
	方案二
		初始化为输入数据的第一个元素
			在累加是记得去掉首元素
			所以为了避免忘记去重,初始化为0还是更常用
 """


def cross_subarray(list, low, mid, high):
    """conquer the cross situation
    return a triple tuple

    Args:
        list (List): [description]
        low ([int]): [description]
        mid ([int]): [description]
        high ([int]): [description]

    Returns:
        [tuple]: [triple]
    """    """ """
    sum = 0
    left_sum_to_max = list[mid]
    max_left_indice = mid
    
    for i in range(low, mid):
        sum += list[i]
        if sum > left_sum_to_max:
            left_sum_to_max = sum
            max_left_indice = i
    sum = 0
    right_sum_to_max = list[mid+1]
    max_right_indice=mid+1
    for i in range(mid+1, high):
        sum += list[i]
        if sum > right_sum_to_max:
            right_sum_to_max = sum
            max_right_indice=i
    return max_left_indice,max_right_indice,left_sum_to_max+right_sum_to_max

def max_subarray(list,low,high):
    """conquer the subarray problem

    Args:
        list (List): the list to be find the max subarray
        low (int): left indice
        high (int): right indice

    Returns:
        tuple: triple
    """    
    """ 递归出口(返回) """  
    if high==low:
        return low,high,list[0]
    else:
        mid=(low+high)//2
        left_tuple=max_subarray(list,low,mid)
        right_tuple=max_subarray(list,mid+1,high)
        cross_tuple=cross_subarray(list,low,mid,high)
        if left_tuple[2]>=right_tuple[2] and left_tuple[2]>=cross_tuple[2]:
            return left_tuple
        elif cross_tuple[2]>=left_tuple[2] and cross_tuple[2]>=right_tuple[2]:
            return cross_tuple
        else:
            return right_tuple
    
            
def main():
    list=[13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
    list1=[1,2,-1,5,6,-8,3]
    print("runing..")
    print(max_subarray(list,0,len(list1)-1))
""" start the program """
main()
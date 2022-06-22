'''
Description: 
Version: 2.0
Author: xuchaoxin
Date: 2021-03-07 17:06:52
LastEditors: xuchaoxin
LastEditTime: 2021-03-07 17:54:19
'''
import generate_randomInt


def divide_zone(dataList, midElement, rightList, leftList):  # district
    """这个函数只是为了让quick_sort()内部代码结构更紧凑而提取出来的(不是必须的)

    Args:
        dataList (list): [description]
        midElement (Number): [description]
        rightList (List): [description]
        leftList (List): [description]
    """
    for num in dataList:
        # 大于基准值,则放到右侧序列区
        if num >= midElement:
            rightList.append(num)
        else:
            leftList.append(num)


def quick_sort(dataList):
    """利用递归来实现快速排序
    是一种用空间换时间的方法(类似于归并法,快速法更简单些)
<<<!!!(定义好返回内容(功能)后,再开始递归函数的实现(具体编写依赖于我们对需求的清晰描述)
(先预设定义好功能,哪怕实现不了再回头调整,否则那一进行下去,毕竟递归函数内部要用到调用自己,函数的功能(特别是返回/计算结果)是什么样的很有必要明确)
    Args:
        dataList (list): 待排序的数列

    Returns:
        list: 排好序的数列!!!>>>
        
    """
    if len(dataList) >= 2:  # 递归入口及出口(如果(当前深度)传入的列表中只有一个元素,则直接返回结果)
        """ 选取基准值，也可以选取第一个或最后一个元素(注意这里用地板除法)
        这个基准值将要特地取出来,会用来连接左侧序列和右侧序列(也作为关节元素)
        """
        midElement = dataList[len(dataList)//2]
        """ # 定义基准值左右两侧的列表;随着递归的深入,leftList和rightList区可分配到的元素越来越少(问题规模不断降低)
        对于不超过三个元素的某个序列certainList为参数的quick_sort(),"""
        leftList, rightList = [], []

        dataList.remove(midElement)  # 从原始数组中移除被选定为基准值的元素
        """ 逐个判断数列中的各个元素和基准值的大小关系,并放到对应侧的子序列中
        可以考虑封装到一个函数中去"""
        divide_zone(dataList, midElement, rightList, leftList)#核心算法(代码段)1

        """ 递归调用:对两侧子序列分别调用quick_sort()处理 """
        return quick_sort(leftList) + [midElement] + quick_sort(rightList)#核心算法(代码段)2
    else:
        return dataList


# 示例：
# array = [2,3,5,7,1,4,6,15,5,2,7,9,10,15,9,17,12]
array = generate_randomInt.generate()
print(quick_sort(array))


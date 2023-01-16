'''

Description: 

Version: 2.0

Author: xuchaoxin

Date: 2021-03-07 17:06:52

LastEditors: xuchaoxin

LastEditTime: 2021-03-07 17:54:19

'''

import generate_randomInt
from generate_randomInt import generate


def generate(n=50):
    arr = []
    for i in range(n):
        arr.append(random.randint(0, n * 10))
    return arr

def partion_poor(dataList, midElement, rightList, leftList):  # district
    """这个函数只是为了让quick_sort()内部代码结构更紧凑而提取出来的(不是必须的)


    Args:

        dataList (list): [description]

        midElement (Number): [description]

        rightList (List): [description]

        leftList (List): [description]
    """

    # 非原地排序

    for num in dataList:

        # 大于(等于)基准值,则放到右侧序列区

        if num >= midElement:

            rightList.append(num)
        else:

            leftList.append(num)


def quick_sort_poor(dataList):
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

        midElement = dataList[len(dataList) // 2]
        """ # 定义基准值左右两侧的列表;随着递归的深入,leftList和rightList区可分配到的元素越来越少(问题规模不断降低)

        对于不超过三个元素的某个序列certainList为参数的quick_sort(),"""

        leftList, rightList = [], []

        dataList.remove(midElement)  # 从原始数组中移除被选定为基准值的元素
        """ 逐个判断数列中的各个元素和基准值的大小关系,并放到对应侧的子序列中

        可以考虑封装到一个函数中去"""

        partion_poor(dataList, midElement, rightList, leftList)  #核心算法(代码段)1
        """ 递归调用:对两侧子序列分别调用quick_sort()处理 """

        return quick_sort_poor(leftList) + [midElement] + quick_sort_poor(
            rightList)  #核心算法(代码段)2
    else:

        return dataList


def partion(l, low=0, high=0, pivot=0):
    #简单的指定枢轴为待划分区间的第一个元素 (将这个元素备份到pivot变量中保存)
    pivot = l[low]
    high=len(l)-1
    while (low < high):
        #操作连个区间的指针
        while (low < high and l[high] >= pivot):
            high -= 1
            #离开循环的时候说明high指针所指的元素比pivot小,
            # 需要把它移到low所指的地方(此时l[low]可以被安全覆盖而不会丢失必要数据)
        l[low] = l[high]
        #轮到另一个指针运动,做类似的比较和覆盖操作
        while (low < high and l[low] < pivot):
            low += 1
        l[high] = l[low]
        #覆盖掉可以被覆盖的元素(第一个是区间内的第一个元素原来的位置)
        #直到区间内的元素被划分完毕
    # 最后将枢轴pivot中保存的元素插入到序列中的正确位置,k=low=high
    pivot_postion = low  #low==high
    l[pivot_postion] = pivot
    return pivot_postion

def quick_sort(l,low=0,high=0):
    #快速排序是递归实现的
    #首先编写递归出口逻辑:
    #或者说递归继续深入的条件(包含了出口的意思)
    if(low<high):
        #首先对传入的区间片段做一个partition
        pivot_position=partion(l,low,high)
        quick_sort(l,low,pivot_position-1)
        quick_sort(l,pivot_position+1,high)

# 示例：
if __name__ == "__main__":
    # l = [2,3,5,7,1,4,6,15,5,2,7,9,10,15,9,17,12]
    l = generate()
    print(l)
    len_l = len(l)
    high = len_l - 1
    #测试函数功能
    ## 测试partition()
    # print(quick_sort_poor(l))
    # p = partion(l)
    ##测试quicksort()
    quick_sort(l,low=0,high=len_l-1)
    ##  打印结果
    # print("p=%d;l[p]=%d" %(p,l[p]))
    print("🎈排序结果:")
    print(l)

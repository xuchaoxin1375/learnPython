'''
Description: 
Version: 2.0
Author: xuchaoxin
Date: 2021-03-06 11:25:50
LastEditors: xuchaoxin
LastEditTime: 2021-03-23 22:31:14
'''
""" 归并排序有些类似于二叉树的遍历算法,分为左支递归调用和右支递归调用 
利用递归思想并调用合并算法(递归算法和合并算法是调用和被调用的关系)(而合并算法本身不是用递归方式实现的)"""
from generate_randomInt import generate_by_shuffle


def MergeSort(list):
    """这个运行过程是:当将最初地大问题规模降低到1时,各级深度地递归调用开始回归(出栈)
    将这个递归模型抽象为二叉树递归顺序,则是后根遍历(从叶子到根)"""
    """ 首先明确递归出口 待排序列地元素不超过1个,就直接原样返回(本身就有序)"""
    if len(list) <= 1:
        return list  #能执行到这一步的时候,已经开时递归的回程(最深一级的MergeSort()只执行了if语句就return出来了,开始倒二深度的MergeSort()的回归,也就是回到back处,继续执行(完成该层次的递归调用的所有语句)
    """ 当待排序序列中至少存在两个元素时:(len(list)>=2) """
    """ 将数列分为两部分,使得问题规模下降一半
    应为本函数的递归出口时当问题规模只有一个元素时退出,所以直到一个含n给元素的序列被反复对半分,直到只有一个元素时开始归的过程
    最开始回归时,可以得到一系列有序的二元列表(左小右大),再进一步回归前,会进行merge(),来归并两个二元列表(扑克牌算法),能够分别得到四元素有序列表"""
    num = int(len(list) / 2)
    """ 分别对原来问题规模的一般进行排序计算 """
    #处理左半部分的任务(注意,python切片是左闭右开的,切片的元素个数=rightIndex-leftIndex),rightList缺省值=len(list)+1;
    leftList = MergeSort(list[:num])
    #back
    #在同一层次的递归调用下,处理左半部分的递归函数已经执行完毕后,再处理该层次的右半部分的递归任务
    rightList = MergeSort(list[num:])
    """ 两部分任务都完成后,返回处理的结果(调用Merge(来合并一下))
    因为是二叉树模型,在同一个根节点下,总是有且只有两颗高度相同的树(问题规模)(一个根节点只有两个子根节点)
    对于同一个根节点下的两兄弟子树,总是左边的子树先完成计算(处理),在左子树尚未完整处理(回归)前,(同级且同根节点)的右子树的计算还尚未开始,"""
    return Merge_orderd_list(leftList, rightList)


""" 用于处理合并序列的函数
具体功能是用来合并两队分别已经有序的数列,从而得到一个大的有序数列
这里处理为升序排列
本函数的参数是两个列表(而不是两个整数)!!"""


def Merge_orderd_list(leftList, rightList):
    """ 本函数可以处理的问题规模下限是两个单个元素构成的列表 """
    """ 定义两个索引变量(用来记录并表示两队有序的数列的最值(端点元素)和一个用来存储排序计算结果的列表 """
    r, l = 0, 0  #初始化为0
    result = []  #可见,每次merge(),都需要创建一个result列表来保存排序结果
    """ r,l都是向右遍历(递进的) """
    while l < len(leftList) and r < len(rightList):
        """ 比较两列有序的数列的最小端元素
        每执行一次循环体,两队数列中的某一个(端点的)元素会被取出并插入到存储结果有序序列的列表result中
        这种每次计算出一个元素再结果序列中的位置的现象会持续到当某个队列的所有元素都被安排到结果序列为止,然后如果由某一队的元素还有剩余,那么就将剩余的元素直接按原序接到结果序列中
        这里优先将两者中较小的元素(也就是待插入中的最小元素插入到结果序列中)"""
        if leftList[l] <= rightList[r]:
            """ 执行插入操作,同时绑定一个索引向后移动的操作 """
            result.append(leftList[l])
            l += 1
        else:
            result.append(rightList[r])
            r += 1
    """ 将两队中剩余的元素序列直接追加到结果序列中去(此时至少有一队列中已经没有元素了,故而可以同一地都追加到结果序列;当然也可以判断索引和队列长度后有选择地接入到结果列表中(python中,列表可以直接相加))
    这里调用list()函数,将列表地切片leftList[l:](或rightList[r:])转换为一个列表,再执行列表追加操做"""
    result += list(leftList[l:])
    result += list(rightList[r:])
    """ 返回结果列表result """
    return result


# print (MergeSort([1,100, 7, 90, 21, 23, 45]))
# ---------------new-------------
def merge2(a, b):
    # length = len(a) + len(b)
    res_l = []
    i = j = 0
    while (i < len(a) and j < len(b)):
        if (a[i] <= b[j]):
            # print(a[i])
            res_l.append(a[i])
            i += 1
        else:
            # print(b[j])
            res_l.append(b[j])
            j += 1
    if (i < len(a)):
        # print(a[i:])
        res_l += a[i:]
    else:
        # print(b[j:])
        res_l += b[j:]
    return res_l


def merge_orderd_ranges(l, start=0, mid=0, end=0):
    """合并两个相邻区间内的元素:归并排序适配版
    <相邻有序区间的有序化合并操作>
    由于归并排序是自底向上的,而且合并的两个有序序列区间在同一个序列中且是相邻的
    因此我们用下标参数来描述描述两个待合并序列
    分别表示为l[start:mid];l[mid+1,end]
    Parameters
    ----------
    l : list
        待执行指定区间[start,end]的合并的序列
        为了保证合并后
    start : int, optional
        待合并的第一个区间起点, by default 0
    mid : int, optional
        待合并区间的第一个有序区间的终点下标,用以区分来个有序区间的边界, by default 0
    end : int, optional
        第二个有序区间的终点元素下标索引, by default 0
    Returns
    -------
    list
        两个有序区间有序化合并完的结果(不是必须的)
    """
    # end = end if mid and end > 0 else len(l) - 1
    #复制一份待归并序列
    print("elements to be merged:🎎", l[start:end + 1])
    bak_l = l[:]
    print("\t✨indexes:start,mid, end", start, mid, end)
    # res_l = []
    i = start  #~mid
    j = mid + 1  #~end
    k = i  #指示尚未排序的部分中的最小的元素应该插入到l序列中的那个位置
    # len_a = mid - start + 1
    # len_b = end - mid
    while (i <= mid and j <= end):
        if (bak_l[i] <= bak_l[j]):
            l[k] = bak_l[i]
            i += 1
        else:
            l[k] = bak_l[j]
            j += 1
        #更新下一个要插入的位置
        k += 1
    #将剩余部分直接拷贝到l中
    #c语言中的实现可以是:
    # while(i<=mid) l[k++]=bak_l[i++]
    # while(j<=mid) l[k++]=bak_l[j++]
    if (i <= mid):
        l[k:end + 1] = bak_l[i:mid + 1]
    else:
        l[k:end + 1] = bak_l[j:end + 1]
    print("merge res🎈:", l[start:end + 1])
    return l[start:end + 1]


def merge_sort_binary(l, start=0, end=0):
    """归并排序:基于分支算法的二路归并排序算法
    借助一个合并操作Merge来充当分治递归的主要操作逻辑
    Merge_sort和Merge调用的关系:
        Merge_sort负责划分问题(分治)
        Merge操作负责实际的元素调整,有序化移动序列中的元素
    Parameters
    ----------
    l :list
        待排序列;另外加上闭区间[start,end]
    start : int
         本次归并排序需要处理的区间(开头)
    end : int
        区间的结尾
    Returns
    -------
    list
        返回已经排好序的区间
        当递归调用栈回到最深层的时候,整个序列l已经有序
    """
    # end= end if end else len(l)-1
    #递归调用执行深入下去的条件:(递归入口及出口)
    if (start < end):
        #继续划分的条件是,当前序列区间[start,end]至少包含2个元素
        #(否则(只有0/1个元素,不需要在划分了,Merge操作可以对处理区间长度为2的序列进行有序化(合并))
        sum = (start + end)
        mid = sum // 2
        print("start,mid,end", (start, mid, end))
        merge_sort_binary(l, start, mid)
        merge_sort_binary(l, mid + 1, end)
        #merge调用被安排在划分(递归调用MergeSortBinary)之后,只有当所有任务被划分完毕
        #merge调用才有机会开始执行,递归调用栈开始逐步弹出
        merge_orderd_ranges(l, start, mid, end)
        # print(l[start:end+1])
    #如果只有一个元素,则直接返回
    return l[start:end+1]


def test_merge2():
    a = [1, 3, 5, 7]
    b = [2, 4, 6, 8, 12, 14]
    d = [2, 4, 6, 10]
    e = [0, 2, 9]
    print(merge2(a, d))
    print(merge2(a, e))


def test_merge_orderd_ranges():
    a = [1, 3, 5, 7]
    b = [2, 4, 6, 8, 12, 14]
    l = a + b
    print(merge_orderd_ranges(l, mid=3))


def test_merge_sort_binary(l):
    merge_sort_binary(l, 0, len(l) - 1)
    print(l)


if __name__ == "__main__":
    a = [1, 3, 5, 7]
    b = [2, 4, 6, 8, 12, 14]
    l = generate_by_shuffle(20)
    print("random list:", l)
    # test_merge2()
    # test_merge_orderd_ranges()
    test_merge_sort_binary(l)

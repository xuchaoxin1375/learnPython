import numpy as np
import time 
# import numpy.random as nr

def exchange(A, i, j):
    A[i],A[j]=A[j],A[i]
    # temp = A[i]
    # A[i] = A[j]
    # A[j] = temp


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] < x:
            i = i + 1
            exchange(A, i, j)
    exchange(A, i + 1, r)
    return i + 1


def randomized_partition(A, p, r):
    i = np.random.randint(p, r + 1)
    exchange(A, r, i)
    return partition(A, p, r)


def randomized_selected_ith(A, p, r, i):  # 找出第i小的元素，i>=1
    ''' 仅有一个元素 '''
    if p == r:
        return A[p]
    #继续执行
    q = randomized_partition(A, p, r)
    k = q - p + 1
    if i == k:
        return A[q]
    elif i < k:
        return randomized_selected_ith(A, p, q-1, i)
    else:
        return randomized_selected_ith(A, q+1, r, i-k)



""" optimal version: """
#局部插入排序
def local_sort(A, p, r):  # 对数组A的p to r部分进行插入排序
    for j in range(p + 1, r + 1):
        x = A[j]
        for i in range(j, p - 1, -1):  # 找x的正确位置i；注意不能将x与A[i](i从j-1开始到p)比较,直到遇到A[i]<=x时认为i+1为x的正确
            # 位置。因为若x的正确位置其实是p=i+1,我们需遇到A[i=p-1]<=x,但这超出了i的范围。
            if A[i - 1] > x:
                A[i] = A[i - 1]
            else:
                break
        A[i] = x
    return A


def median(A, p, r):  # 分组并排序,记录每组中位数,并返回中位数对应到A中位置t（即主元位置）

    #  分组并排序,记录每组中位数
    long = r - p + 1  # A[p]到A[r]的长度
    if long // 5 == 0:
        return r
    B = []
    for i in range(1, long // 5 + 1):
        A = local_sort(A, p + 5 * (i - 1), p + 5 * i - 1)  # 逐段对每五个元素进行插入排序delta=4,elements=5=end-start+1
        B.append(A[p + 5 * i - 3])  # 记录每组中位数
    B_0 = B
    mid = optimal_select(B_0, 0, len(B_0) - 1, len(B_0) // 2)  # 用select找出上述所有中位数的中位数
    for i in range(0, len(B)):
        if B[i] == mid:
            t_0 = i
            t = p + 5 * (t_0 + 1) - 3
            break
    return t


def modified_partition(A, p, r):  # 随机划分，返回主元重排后的位置
    t = median(A, p, r)  # 主元
    A[t], A[r] = A[t], A[r]  # 主元放末尾
    x = A[r]
    m = p - 1
    for j in range(p, r):
        if A[j] <= x:
            m = m + 1
            A[m], A[j] = A[j], A[m]
    A[m + 1], A[r] = A[r], A[m + 1]
    return m + 1


def optimal_select(A, p, r, i):
    if p == r:
        return A[p]
    q = modified_partition(A, p, r)
    k = q - p + 1  #
    if k == i:  # 递归基线条件
        return A[q]
    if k > i:
        return optimal_select(A, p, q - 1, i)  # 在q之前得数组中查找
    if k < i:
        return optimal_select(A, q + 1, r, i - k)  # 在q之后得数组中查找

def calculate_time(select_method,method_str):
    ''' 取中位数来实验 '''
    start_time=time.time()
    num_i_th = select_method(A, 0, length-1, int(0.5*length))
    end_time=time.time()
    consume_time=end_time-start_time
    print(len(A),"numbers as input:")
    print_result(method_str,consume_time,num_i_th)
    # print("solved by",method_str,":")
    # print(num_i_th)
    # print("consumed time:",consume_time)
    # return end_time-start_time
    
def print_result(method_str,consume_time,num_i_th):
    print("solved by",method_str,":")
    print(num_i_th)
    print("consumed time:",consume_time)
    
    # calculate_time(select_method,)
    
# test_correctness = [2, 8, 7, 1, 3, 5, 6, 4]
A=np.random.randint(0,100000,size=2000)
length = len(A)
# print(A)


consume_time_random=calculate_time(randomized_selected_ith,"randomized_select")
consume_time_optimal=calculate_time(optimal_select,"optimal_select")


import random as rand

l = list(range(10))
rand.shuffle(l)
rl = l  #random number list
print(rl)


def swap(l, i, j):
    #python支持成组赋值
    l[i], l[j] = l[j], l[i]
    #传统写法如下:
    # tmp = rl[j]
    # rl[j] = rl[j - 1]
    # rl[j - 1] = tmp



def bubble_sort(rl):
    n = len(rl)
    for i in range(n - 1):
        #这里的变量i可以理解为待排序区B的第一个元素
        #在本趟排序前,设立一个标记
        flag = True  #标记:假设本轮排序前是有序的
        #sort_next_round(l,flag, n, i)的逻辑
        #这一趟排序结束后(第i趟),那么位置i上的元素就被最终确定下来
        #当B区元素[首尾闭区间]数量剩余1的时候(也就是闭区间两端重合)就可以结束算法了
        #待排序区域B的下标范围[i,i+1,...,n-1]
        for j in range(n - 1, i, -1):
            #j的取值:n-1,n-2,...,i+1(不直接包括B区的第一个元素下标)
            if (rl[j] < rl[j - 1]):
                flag = False#若发现逆序,修改标记
                #交换序列中的两个元素
                swap(rl,j,j-1)

        #本趟排序结束后,检查标记是否被更改,来判定是否已经得到一个有序序列
        if flag:  #如果本趟排序没有发现逆序(交换),则已经可以认定序列是有序的了,可以结束排序
            break
    return rl


if __name__ == "__main__":
    bubble_sort(rl)
    print(rl)
##
ol=list(range(10))#order list
# import numpy as np
# 你需要的不是ndarray,而是array
# ol=2*np.array(ol)+3
##
print(ol)
##
def binarySearch(ol,k):
    """ 二分查找(参数有序顺序表) """
    l=0
    r=len(ol)-1
    while(l<=r):
        mid=(l+r)//2
        print('indexes:[%d,%d],mid:%d' %(l,r, mid))#log
        if(ol[mid]==ol[k]):
            return mid
        if(k<mid):
            r=mid-1
        if(mid<k):
            l=mid+1
    return -1
print(binarySearch(ol, 7))
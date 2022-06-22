'''
Description: 
Version: 2.0
Author: xuchaoxin
Date: 2021-03-06 20:17:12
LastEditors: xuchaoxin
LastEditTime: 2021-03-07 12:58:14
'''
""" 堆排序

	堆中定义以下几种操作：
		○ 最大堆调整（Max Heapify堆积化）：
			§ 将堆的末端子节点作调整，使得子节点永远小于父节点
		○ 创建最大堆（Build Max Heap）：(核心算法)
			§ 将堆中的所有数据重新排序
		○ 堆排序（HeapSort）：
			§ 移除位在第一个数据的根节点，并做最大堆调整的递归运算 （可以不递归）
"""
import generate_randomInt
def big_endian(arr,start,end):  #big_endian大端法  
    """[设计本函数的初衷的直接目的用来解决:某个已经总体上(由于顶端元素被替换,导致堆结构被破坏)已经满足堆的定义的完全二叉树做调整(将堆顶元素通过调整,放到合适的位置,使得该堆真正满足堆的定义),通过配合循环,合理的逆序调用本函数,可以用来初始换一些杂乱无章的数列,使之满足堆的结构(我们届时用build_heap()函数来组织big_endian()的逆序调用,从而实现初始化建堆的目的)
        这是核心函数,提供按深度（而非广度）调整大根堆的服务,从给定的start节点开始，向深层的节点执行,直到扫描的end(给定终点);
    值得注意的是,从start节点通往end节点的过程中不是逐个遍历的,
    （体现在：一颗满足堆性质的完全二叉树是可以看成两部分（两颗兄弟子树，当其中一颗子树从堆结构被破坏后，该子树就不满足堆的性质；但是另一颗子树并没有受到影响，任然满足堆结构），故而，欲使得该树重新满足堆结构只需要调整被破坏的那一棵子树，而不需要去动另一颗子树。即向深处调整，而不是广度调整。）
    这个函数有两方面的用途。
    那么，一次big_endian调用到底会调整多少次位于不同层次的三元子堆呢（在同一次调用中，不同深度的三元子堆树最多调整一次）
    可以确定的是，这个函数是从给定起点start开始向后遍历到给定的终止节点end，
    
    一方面用途（复杂度较高，反复滚动扫描调整），
    对于最开始建堆，是一个反复滚动调用big_endian()的过程，
    从给定起点start开始向后遍历到最后一个节点end在这时是确定的end=len(arr)-1(即同终点,(是叶子节点))
    这些调用存在先后关系，但不存在嵌套调用的关系，后期的调用要比前期的调用执行更多的判断/对堆的结构可能做出更多的调整行为（滚动）]
    
    另一方面（复杂度较低，一次扫描调整），是基于初始建堆完成之后的完全二叉树，这时的二叉树总体上满足堆定义，但是由于堆顶的调换，导致结构被破坏，这时候只需要重新从堆顶处开始调用big_endian()执行一次扫描调整（该过程会沿着不满足堆结构的子树不断深入深层去调整，每一级调整中（如果需要），都只会调整两棵同级子树中的一颗，另一颗任然是满足二叉树的定义，这一点又该二叉树总体上满足堆定义做出前提保证）

    Args:
        arr (list): [表示待排序数列的堆(列表形式)]
        start (int):[堆的完全二叉树形态下的，需要heapify的节点区间的左边界索引（在arr中的位置索引）,即从那个节点开始heapify调整)]
        end (int): [需要heapify的节点区间的右边界索引（在arr中的位置索引）/可以用来判断何时停止调整循环:child<=end]
    """    
    """ 注意,这里用的是列表(索引从0开始,0,1,2(即左孩子的索引编号是偶数,右孩子节点的编号是奇数(2*i+1))) """
    root=start    #当前级别(深度)的(子)树的根节点（root的值是要被不断更新的）
    child=root*2+1 #child记录兄弟节点中的较大者的索引,初始化为左孩子元素的编号索引（child的值也要不断更新/重新计算）
    """ root的变化趋势是越来越大(child=root*2+(1/2),当然也是变大的趋势) """
    """ 采用循环策略 """
    # while child<=end:#如果一个节点的左子节点的理论标号>end,说明该节点的左子节点不存在，有因为是完全二叉树，右节点更加不会存在。
    #     #child比最后一个节点的编号还大,说明此时的root已经是叶子节点了,就应该退出循环
    #     if child+1<=end :#如果child+1>end,则表明该非叶子节点只有一个孩子节点(左孩子)
    #         #保证大孩子索引child指向正确
    #         if  arr[child]<arr[child+1]:
    #         #为了始终让其跟两个子节点元素中的较大值比较(让较大值当左孩子)，如果右边大就更新child的值(使得它指向右孩子)，左边大的话就默认           
    #             child+=1            
    #     """ 判断是否需要对该三元堆进行节点调整,否则break """
    #     if arr[root]<arr[child]:
    #         #父节点小于子节点中的较大者,则直接交换元素位置，同时坐标也得更新                
    #         arr[root],arr[child]=arr[child],arr[root]  
    #         # 同时更新root值并重新计算child的值，这样下次循环可以准确判断：是否为最底层，             
    #         root=child                
    #         child=root*2+1            
    #     else:               
    #         break
    """ 采用递归的策略 """
    if child<=end:#表明root节点是非叶子节点(其左孩子存在,因为child<=end)
        if  child+1<end :#如果同时存在右孩子节点,则比较处那个孩子节点较大,并将对应节点的索引赋值给child(更新)
            if arr[child]<arr[child+1]:
                child+=1
        if arr[child]>arr[root]:
            """执行调整操作:交换元素位置 """
            arr[child],arr[root]=arr[root],arr[child]
            big_endian(arr,child, end)#所有递归目标同终点end,child是变化的
""" build_heap()不是必须，可以直接写在sort中 """
def build_heap(arr):
    reverse_first=len(arr)//2 - 1  #第一个非叶子节点元素的索引;或则写reverse_first=(len(arr)-1)//2
    # size=len(arr) 
    lastIndex=len(arr)-1
    """ range()步长为-1,产生序列:reverse_first到0,左闭右开 """  
    #初始化建堆:执行逆序heapify()
    for reverse_roll_start in range(reverse_first,-1,-1):#索引变量为reverse_roll_start
        #从下到上，从右到左，对每个节点进行调整，循环调用big,得到非叶子节点        
        #去调整所有的节点;这里的reverse_roll_start跟随着索引变量的前进而前进（变化）;所有调用同终点:lastIndex
        big_endian(arr,reverse_roll_start,lastIndex) 
        
         
def heap_sort(arr): #大根堆排序    

    build_heap(arr)
    lastIndex=len(arr)-1
    """ 每执行一次循环，就有一个元素被正确排入到结果序列
    总共需要排序lastIndex次,即len(arr)-1次
    end>=1,end-1>=0"""
    for end in range(lastIndex,0,-1):  #索引变量为end(表示该趟heapify（）的处理区间[start=0,end]的右边界索引) , 从序列的最后一个元素(叶子节点）开始逆序遍历到第2个位置()  
        arr[0],arr[end]=arr[end],arr[0] #顶部尾部互换位置 ，将为有序区增加一个元素(而在最后一次调换时,次小的元素的有序同时也使得最小的元素放在了合适的位置)       
        #重新调整子节点，使得整个堆仍然满足堆的定义，每次heapify都从顶开始调整（start=0);所有调用同起点start=0
        big_endian(arr,0,end-1)
        #可以考虑仿射big_endian函数
    return arr
     
def main():    
    # l=[111,7,2,9,11,66,22,11]
    l=generate_randomInt.generate(50)
    print(heap_sort(l))
 
# if __name__=="__main__":    
#     main()
main()

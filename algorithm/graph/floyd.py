import numpy as np
import math
import logging as l
# l.basicConfig(level=l.DEBUG)
inf = math.inf


def floyd(d):
    ''' the w is a table(n*n) '''
    # d = w
    n = len(d)
    precursor_table = [[None for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if d[i][j] != inf:
                precursor_table[i][j] = i
    # print_matrix(precursor_table)
    # print("pre 0\n", np.array(precursor_table))

    l.debug(f'd:{d}')

    '''d[i][j] means that weight of a shortest path from i to j with 
    intermediate vertices belonging to the set {1, 2, …, k}. 
    Okay to omit superscripts, since extra relaxations can’t hurt.'''
    #
    # the k is the intermediate vertices' max numbers(upper bound)(number system)(not the size of the intermediate nodes points ).
    for k in range(n):
        ''' traverse the weight matrix in each level subproblem(indicated by k) '''
        # the i is the start node of the path(i,j)
        for i in range(n):
            # the j is the end node of the path(i,j)
            for j in range(n):
                l.debug(f'i,j={i,j}')
                # the classic relax operation:
                if d[i][j] > d[i][k]+d[k][j]:
                    d[i][j] = d[i][k]+d[k][j]
                    precursor_table[i][j] = precursor_table[k][j]

        # print("pre", k+1, "\n", np.array(precursor_table))
    return precursor_table
d = [
    [0, 3, 8, inf, -4],
    [inf, 0, inf, 1, 7],
    [inf, 4, 0, inf, inf],
    [2, inf, -5, 0, inf],
    [inf, inf, inf, 6, 0]

]
 
def print_matrix(d):
    for line in d:
        print(line) 
        
''' 调用floyd算法计算矩阵d(并将保存结果保存在d) (但函数返回值我设置为前驱矩阵)'''
precursor_table=floyd(d)
print_matrix(d)
                  
def print_precurcer(precursor_table,i,j):
    ''' from 0 count the index of the matrix and from 0 number the node in the graph '''
    precursor=precursor_table[i][j]
    # print(np.array(precursor_table).shape)
    # print((i,j))
    l.debug(f'i,j={i,j}')
    # print(f'i,j={i,j}')
    if i==j:
        # print()
        print(i,end=" ")#let it break line
    elif precursor==None:
        print("no path from",i,"to",j,"exists")
    else:
        print_precurcer(precursor_table,i,precursor)
        print(j,end=" ")
                
            

''' 如果是矩阵从1开始计数,那么调用如下函数(直接赋值给print_precurcer函数的引用) '''
def print_precurcer_count_from_1(precursor_table,i,j):
    precursor=precursor_table[i][j]
    # print(np.array(precursor_table).shape)
    # print((i,j))
    l.debug(f'i,j={i,j}')
    # print(f'i,j={i,j}')
    if i==j:
        # print()
        print(i+1,end=" ")#let it break line
    elif precursor==None:
        print("no path from",i+1,"to",j+1,"exists")
    else:
        print_precurcer(precursor_table,i,precursor)
        print(j+1,end=" ")
#
# print_precurcer=print_precurcer_count_from_1


# 打印所有最短路径
def print_paths(precursor_table):
    n=len(precursor_table)
    for i in range(n):
        for j in range(n):
            print()
            print(f'i,j={i,j}') 
            print_precurcer(precursor_table,i,j)
            print()


print_paths(precursor_table)
# print_precurcer(precursor_table,2,0)

''' 打印最短路径权值矩阵 '''
print_matrix(d)

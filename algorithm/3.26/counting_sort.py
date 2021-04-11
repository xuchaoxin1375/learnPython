'''
Description: 
Version: 2.0
Author: xuchaoxin
Date: 2021-03-26 20:58:42
LastEditors: xuchaoxin
LastEditTime: 2021-03-28 12:57:09
'''
""" 
for i ← 1 to k
do C[i] ← 0
for j ← 1 to n
do C[A[ j]] ← C[A[ j]] + 1 ⊳C[i] = |{key = i}|
for i ← 2 to k
do C[i] ← C[i] + C[i–1] ⊳C[i] = |{key ≤ i}|
for j ← n down_to 1
do B[C[A[ j]]] ← A[ j]
C[A[ j]] ← C[A[ j]] – 1
"""


def counting_sort(A):
    """counting_sort(),stable sort algorithm;
    the function apply to natural numbers,but:
    if you want to sort float,then times all the elements a positive integer big enough to make them natural numbers 
    if you want to sort negative numbers,you can plus all of the element a positive big enough to make them natural numbers

    Args:
        A (List): list/array to be sort
    """
    sizeOfA = len(A)  # n
    max_element = max(A)  # k
    count_list = []
    result_list = []
    """ initial the counting list """
    for i in range(0, max_element+1):
        # A[i]=0
        count_list.append(0)
        # result_list.append(0)
    for i in range(0, sizeOfA):
        result_list.append(0)
    """ counting values:(it's ok) """
    for i in range(0, sizeOfA):
        count_list[A[i]] += 1
    """ update the values(element) after the second element in the count_list;
    however,the indice start from 0,so substract 1 at first """
    count_list[0] -= 1
    for i in range(1, max_element+1):
        count_list[i] += (count_list[i-1])
    """ insert the element of A(A[i]) to correct place in the sorting sequence """
    for i in range(sizeOfA-1, -1, -1):
        """ in order to find the cause :IndexError: list assignment index out of range
        I print some value to locate it(comment out the program statement),the cause is that I didn't initial the list:result_list"""
        # print("i=",i)
        # print("A[i]=",A[i])
        # print("len(count_list)=",len(count_list))
        # print("")
        result_list[count_list[A[i]]] = A[i]
        """ update the indice of count_list:namely,the value which indice=A[i]:count_list[A[i]] """
        count_list[A[i]] -= 1
    return result_list


def main():
    """ test the counting_sort() """
    print(counting_sort([4, 2, 2, 6, 9, 0, 1]))


# main()

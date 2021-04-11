'''
Description: 
Version: 2.0
Author: xuchaoxin
Date: 2021-03-26 21:03:37
LastEditors: xuchaoxin
LastEditTime: 2021-03-26 21:20:31
'''
""" The code for radix sort is straightforward. The following procedure assumes that
each element in the n-element array A has d digits, where digit 1 is the lowest-order
digit and digit d is the highest-order digit.

1 for i D 1 to d
2 use a stable sort to sort array A on digit i

the radix need multiple sort passes"""

def radix_sort(A,d):
    """radix_sort

    Args:
        A (list/array): to be sort number sequence
        d (int): [the highest_order digit]
    """    
    
    
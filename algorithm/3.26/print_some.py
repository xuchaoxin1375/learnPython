'''
Description: 
Version: 2.0
Author: xuchaoxin
Date: 2021-03-06 15:38:15
LastEditors: xuchaoxin
LastEditTime: 2021-03-06 19:39:19
'''
def printSome(arr,n=10,str=""):
    """[summary]

    Args:
        n (int): [description]
        arr (list): [description]
    """    
    print(str,end="")
    for i in range(n):
        print("%d" %arr[i],end=" ")
    print("....")



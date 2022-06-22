'''
Description: 
Version: 2.0
Author: xuchaoxin
Date: 2021-01-31 23:24:33
LastEditors: xuchaoxin
LastEditTime: 2021-02-01 09:32:52
'''
def fib(max):
    """计算斐波那契数

    Args:
        max (int): 被计算的第max项

    Returns:
        int: 第max项的值
    """   
    '''
    n 表示地推次数
    a,b表示Fibonacci相邻的两项的值(初始值分别为0,1);每一次地推,将bn的值赋给a(n+1),an+bn的值赋给bn+1;
    ''' 
    n, a, b = 0, 0, 1
    while n < max:
        # print(b)
        """ 作为生成器: """
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
# print(fib(5))
""" 利用循环打印生成器返回的元素 """
for n in fib(5):
    print(n)
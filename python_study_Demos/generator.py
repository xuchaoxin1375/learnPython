'''
Description: 
Version: 2.0
Author: xuchaoxin
Date: 2021-01-31 23:24:33
LastEditors: xuchaoxin
LastEditTime: 2021-02-01 09:32:52
'''
def fib(max):
    """����쳲�������

    Args:
        max (int): ������ĵ�max��

    Returns:
        int: ��max���ֵ
    """   
    '''
    n ��ʾ���ƴ���
    a,b��ʾFibonacci���ڵ������ֵ(��ʼֵ�ֱ�Ϊ0,1);ÿһ�ε���,��bn��ֵ����a(n+1),an+bn��ֵ����bn+1;
    ''' 
    n, a, b = 0, 0, 1
    while n < max:
        # print(b)
        """ ��Ϊ������: """
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
# print(fib(5))
""" ����ѭ����ӡ���������ص�Ԫ�� """
for n in fib(5):
    print(n)
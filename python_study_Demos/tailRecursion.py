'''
Description: 
Version: 2.0
Author: xuchaoxin
Date: 2021-01-31 20:22:49
LastEditors: xuchaoxin
LastEditTime: 2021-01-31 22:12:45
'''

#
""" ���ķ���ʵ�� """
def fact_iter(num, product):
    '''
    description: 
    param {*}
    return {*}
    author: xuchaoxin
    '''
    
    if num == 1:
        """ ���Ĳ���:��ÿһ�εݹ�ļ��������ص���һ�εݹ���õ�(�ڶ���)������,�ﵽֱ�ӷ��غ�������ĵ���,�����ǰ���������ı��ʽ(ʵ��β�ݹ�,���۾��Ǹõݹ麯����Ҫ����һ��������¼ÿ�εݹ���õļ�����.���ʾ���ѭ��) """
        return product
    return fact_iter(num - 1, num * product)


print(fact_iter(6, 1))


def fact(n):

    
    return fact_iter(n, 1)


print(fact(5))

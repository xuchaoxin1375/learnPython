'''
Description: 
Version: 2.0
Author: xuchaoxin
Date: 2021-01-31 20:22:49
LastEditors: xuchaoxin
LastEditTime: 2021-01-31 22:12:45
'''

#
""" 核心方法实现 """
def fact_iter(num, product):
    '''
    description: 
    param {*}
    return {*}
    author: xuchaoxin
    '''
    
    if num == 1:
        """ 核心步骤:将每一次递归的计算结果返回到下一次递归调用的(第二个)参数中,达到直接返回函数本身的调用,而不是包含其他项的表达式(实现尾递归,代价就是该递归函数需要多配一个参数记录每次递归调用的计算结果.本质就是循环) """
        return product
    return fact_iter(num - 1, num * product)


print(fact_iter(6, 1))


def fact(n):

    
    return fact_iter(n, 1)


print(fact(5))

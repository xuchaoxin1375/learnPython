'''
Description: 
Version: 2.0
Author: xuchaoxin
Date: 2021-02-01 09:33:06
LastEditors: xuchaoxin
LastEditTime: 2021-02-01 12:13:17
'''
# -*- coding: utf-8 -*-

def triangles():
    """产生杨辉三角列表行(python生成器的演示)

    Yields:     
        [list]: [description]
    """    
    
    """ 定义列表ret(初始其中的元素化为1),ret中只保存整形数 
    pre列表表示上一行杨辉三角的元素所构成的列表"""
    ret = [1]
    while True:
        """ 每次生成器返回结果的地方 """
        yield ret
        """ 深复制一份ret列表,并作为pre初始引用值 """
        pre=ret[:]
        for i in range(1, len(ret)):
            """ 根据杨辉三角的递推规则来更新列表ret:
            即ret[i]=pre[i]+pre[i-1]
            由于i是列表[1,2,...,len(ret)]中取出的元素,可以作为ret的索引
            注意, list(range(1,1)) 的结果是空列表[];所以第一轮循环不会进入执行
            则有i-1=0,1,2,...,len(ret)-1 """
            ret[i] = pre[i] + pre[i - 1]
        """ 为ret列表的末尾添加一个固定元素:1 """
        ret.append(1)
        """ pre列表表示上一行杨辉三角的元素所构成的列表
        更新pre列表(将ret中的值赋值一份给pre),进行地推(迭代) """
        pre = ret[:]

for n in triangles():
    if(len(n)>7):
        abs()
        break
    print(n)
'''
Description: 
Version: 2.0
Author: xuchaoxin
Date: 2021-02-04 10:05:58
LastEditors: xuchaoxin
LastEditTime: 2021-02-04 10:20:04
'''
""" 导入logging(记录)模块,使得程序在出错后可以继续执行后面的代码 """
import logging
def foo(s):
    return 10 / int(s)
def bar(s):
    return foo(s) * 2
def main():
    try:
        bar('0')
    except Exception as e:
        """ 在except 处使用logging模块的logging变量 """
        logging.exception(e)
main()
# print(logging)
""" >>> 
print(type(logging))
<class 'module'> """
print('END')

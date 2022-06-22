#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
' a test module (a usage demo of module( [ˈmɑːdʒuːl]'

__author__ = 'cxxupy'
""" 导入sys模块 """


def test():
    """自定义的测试模块
    """
    # 获取命令行输入的参数,并存入args列表
    args = sys.argv

    if len(args) == 1:
        print('Hello, world!')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')


"""
在命令行运行该模块文件时，
Python解释器把一个特殊变量__name__置为__main__，
而如果在其他地方(非命令行)导入该hello模块时，if判断将失败，
因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，
最常见的就是运行测试。
 """
if __name__ == '__main__':
    test()
""" 
第1行和第2行是标准注释，
	第1行注释可以让这个hello.py文件直接在Unix/Linux/Mac上运行，
	第2行注释表示.py文件本身使用标准UTF-8编码；
第4行是一个字符串，表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；
第6行使用__author__变量把作者写进去
以上就是Python模块的标准文件模板，
当然也可以全部删掉不写
"""
""" 直接通过命令行执行模块文件:
PS D:\OneDrive - pop.zjgsu.edu.cn\PythonPath> python .\module.py
Hello, world!
"""
""" Python交互调用测试:
>>> import module
>>> module.test()
Hello, world!
"""

'''
Description: 
Version: 2.0
Author: xuchaoxin
Date: 2021-04-13 09:38:06
LastEditors: xuchaoxin
LastEditTime: 2021-04-13 13:30:59
'''
""" use the package :you'd be os chdir() to the directory where the package existed or,embedded the package """
""" 通过import sys模块,对sys.path写入新的环境变量(即要用的那个模块的所在目录),可以调用sys.path.append(方法插入 """
import sys

pack_path_string="d:/OneDrive - pop.zjgsu.edu.cn/pythonPath/exp3"

sys.path.append(pack_path_string)
# for i in sys.path: 
# # for example:filter by environment variable contatins "exp"
#     if "exp" in i:
#         print(i)
""" 插入完毕,可以正常导入模块(或其中的某个函数) """
from test_submodule_package.add import add_func  
print(add_func(1,5))

# module_path_string="D:/OneDrive - pop.zjgsu.edu.cn/PythonPath/exp3/test_submodule_package"
# sys.path.append(module_path_string)
# import add
# print(add.add_func(1,6))
# """inspect the sys.path:added just before:  """
# for i in sys.path: 
# for example:filter by environment variable contatins "exp"
#     if "exp" in i:
#         print(i)
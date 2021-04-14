'''
Description: 
Version: 2.0
Author: xuchaoxin
Date: 2021-04-14 10:43:37
LastEditors: xuchaoxin
LastEditTime: 2021-04-14 10:59:37
'''
import os

path_string_fix = "D:/OneDrive - pop.zjgsu.edu.cn/PythonPath/exp4/"

def fex(dirpwd):
    """return a set contains extension of files without repateing

    Args:
        dirpwd (string): path string

    Returns:
        set: file extension names
    """    
    list_dir=os.listdir(dirpwd)
    file_post_set=set()
    for file in list_dir:
        file_post=os.path.splitext(path_string_fix+file)[-1]
        if(file_post):
            file_post_set.add(file_post)
        # if file_post in 
    return file_post_set

""" 

设定一个递归函数travers_dir()
该函数接收一个目录字符串参数，函数进入改目录打印出所有文件名以及目录名此外，如果被打印的对象时目录时，需要以该目录为参数在调用一次traverse_dir

"""
import os
import os.path as op
from posixpath import dirname

# dirName = "d:/repos/learnPython/ppt_source_code"
dirName = "./../algorithm/"
pathOut = "file_dir_out"


def empyt(obj):
    ...


d = print
d = empyt

if op.exists(pathOut):
    os.remove(pathOut)


def append(content, fileName=pathOut):
    with open(fileName, 'a') as fout:
        fout.write(content+"\n")


out = append
depth = 0


def traverse_dir(dirName):
    d("\t new invoke of traverse_dir()")
    items = os.listdir(dirName)
    # print(items)
    if (items):
        # cwd1=os.getcwd()
        # d('\t'+cwd1)
        # d("now chdir()...")
        # os.chdir(dirName)
        # cwd2=os.getcwd()
        # d("\t"+cwd2)
       
        for item in items:
            # newPath = dirName+"/"+item
            newPath = op.join(dirName, item)
            d(newPath)
            # os.chdir(newDir)
            cwd3 = os.getcwd()
            d("\t"+cwd3)
            # notice the paramter of isdir()
            
            # levelDepth = depth
            if op.isdir(newPath):
                d("dirName:"+item+"\twill be enter by new invoke of traverse_dir")
                dirStr = depth*"\t"+newPath
                print(dirStr)
                out(dirStr)
                # depth += 1
                # newDir=dirName+"/"+item
                d(newPath)
                # os.chdir(newDir)
                # cwd3=os.getcwd()
                d("\t"+cwd3)
                traverse_dir(newPath)
            else:
                print(item)
                out(depth*"\t"+item)

from sys import argv

dirName=argv[1]
depth=argv[2]
if __name__ == "__main__":
    traverse_dir(dirName)

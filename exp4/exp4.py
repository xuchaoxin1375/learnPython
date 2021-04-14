'''
Description:
Version: 2.0
Author: xuchaoxin
Date: 2021-04-14 08:08:56
LastEditors: xuchaoxin
LastEditTime: 2021-04-14 15:06:51
'''
# import time

# import datetime
# datetime.date.today()
''' 2 '''
import os
import random
from typing import AsyncGenerator

path_string_fix = "D:/OneDrive - pop.zjgsu.edu.cn/PythonPath/exp4/"
# text_string = "\ntest data to write"


# def fs(dirname, s):
#     """[to save the string s randomly to the txt file in the dirname path ]

#     Args:
#         dirname (str): file path
#         s (str): data to save
#     """
#     list_dir = os.listdir(path_string_fix)
#     txt_files_list = list(filter(lambda file: file.endswith(".txt"), list_dir))
#     if len(txt_files_list)==0:
#         with open(path_string_fix+"new.txt","w") as file_output_stream:
#             file_output_stream.write(text_string)
#     else:
#         file_random_index=random.randint(0, len(txt_files_list)-1)
#         print(txt_files_list[file_random_index]+" will be written")
#         # print(list(txt_files_list))
#         with open(path_string_fix+txt_files_list[file_random_index],"a") as file_output_stream:
#             file_output_stream.write(text_string)
#     print("append randomly done!")
# fs(path_string_fix, text_string)
''' 3 '''

# import exname
# exname.fex(path_string_fix)
# print(exname.fex(path_string_fix))

# class Student():
#     name=""
#     age=0
#     scores=[]
#     def __init__(self,name,age,scores):
#         self.name=name
#         self.age=age
#         self.scores=scores
#     def get_name(self):
#         return self.name
#     def get_age(self):
#         return self.age
#     def get_course(self):
#         return max(self.scores)
#     def print_all_info(self):
#         print(self.get_name())
#         print(self.get_age())
#         print(self.get_course())

# zm = Student('zhangming', 20, [69,88,100])
# zm.print_all_info()
    
# class Listinfo():
#     list=[]
#     def __init__(self,list_info):
#         Listinfo.list=list_info
#         # self.list=list_info
#     def add_elem(self,elename):
#         Listinfo.list.append(elename)
#         return Listinfo.list
#     def get_elem(self,num):
#         return Listinfo.list[num]
#     def merge_list(self,ls):
#         Listinfo.list=Listinfo.list+ls
#         return Listinfo.list
#     def del_lastone(self):
#         return Listinfo.list.pop()
#     # def print_test_info():
#     #    
# list_info=Listinfo([44,222,111,333,454,'sss','333'])
# # list_info.add_elem(5)
# print("before operation:",list_info.list)
# print("list_info.add_elem(\"test add\") result:",list_info.add_elem("test add"))
# print("list_info.get_elem(5):",list_info.get_elem(5))
# print("list_info.merge_list([\"test merge\"]):",list_info.merge_list(["test merge"]))
# print("list_info.del_lastone() element deleted:",list_info.del_lastone())
        
""" 7 """
class Human():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def get_name(self):
        print(self.name)
    def do_homework(self):
        print("there is no homework from the parent!")
class student(Human):
    def __init__(self,name,age,homework):
        Human.__init__(self,name,age)
        self.homework = homework
    def do_homework(self):
        print("作业为："+self.homework)
        
stu=Stud



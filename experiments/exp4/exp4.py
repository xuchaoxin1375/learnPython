'''
Description:
Version: 2.0
Author: xuchaoxin
Date: 2021-04-14 08:08:56
LastEditors: xuchaoxin
LastEditTime: 2021-04-14 22:41:34
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
        
"10"
import numpy as np
from numpy import random 
import itertools
class HDPoints():
    def __init__(self,HDPoints_list):
        self.points =HDPoints_list
    def centerpoint(self):
        ndarray=np.array(self.points)
        return sum(ndarray)/len(ndarray)
    
    def minkowski(self,x,y,p):
        abs_list= [abs(x-y)**p for x,y in zip(x,y)]
        return sum(abs_list)**(1/p)

    def farthestpoint(self,p):
        centerpoint=self.centerpoint()
        distances_list=[self.minkowski(centerpoint,point,p) for point in self.points ]
        max_distance= max(distances_list)
        return  distances_list.index(max_distance),max_distance
    def farthest2points(self,p):
        points_index_tuple_list=[(point,i)for i,point in enumerate(self.points)]
        point_pairs_tuples=(itertools.combinations(points_index_tuple_list,r=2))
            #element shape:(([point_list1],index2),([point_list2],index2))
            
        distances_list=[(self.minkowski(tuple[0][0],tuple[1][0],p),(tuple[0][1],tuple[1][1])) for tuple in point_pairs_tuples ]
            #element shape:(minkowski_distance,(index1,index2))
        max_distance_point=max(distances_list,key=lambda tuple:tuple[0])
        return max_distance_point[1],max_distance_point[0]

        
        

# a=random.rand(1,0.5,2,3,6,3)
a=random.uniform(0,1,5).tolist()
""" get points list: """
points=[random.uniform(0,1,5).tolist() for i in range(50)]
hd_Points=HDPoints(points)
p=random.randint(1,6)
print("the centerpoint is:",hd_Points.centerpoint())
""" the minkowski method will be test contained in the farthestpoint() method! """
print("the farthest point:",hd_Points.farthestpoint(p))
print(f"the farthest2point: index of the 2 pointes: {hd_Points.farthest2points(p)[0]},the max minkowski distance is {hd_Points.farthest2points(p)[1]}")

# print(hd_points_list)
""" use numpy to deal it """
# ndarray=np.array(points)
""" get combinations by pairwisely: """
# point_pairs_list=itertools.combinations(points,r=2)
# distances_list_iterator=[minkowski(x,y,0) for x in ]

# points_index_tuple_list=[(point,i)for i,point in enumerate(points)]
# print(points_index_tuple_list)
# for tuple in point_pairs_list:
#     print(tuple)
# print(sum(ndarray)/len(ndarray))
# hd_points = HDPoints(hd_points_list)

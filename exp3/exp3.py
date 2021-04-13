'''
Description:
Version: 2.0
Author: xuchaoxin
Date: 2021-04-07 09:47:22
LastEditors: xuchaoxin
LastEditTime: 2021-04-13 09:40:32
'''

import time
import math
import pickle

path_string_fix = "D:/OneDrive - pop.zjgsu.edu.cn/PythonPath/exp3/"

ls = []


def open_file_exp3_toList(fileName):
    """the function read data from a file specified ;however,it generate the list by append the lines(sublist) to the ls[],differently invoke may accumulate the read result,so you should better reset the ls before invoke the function.

    Args:
        fileName ([type]): [description]
    """
    with open(path_string_fix+fileName, "r") as file_input_stream:
        for line in file_input_stream:
            ls.append(line.strip("\n").split(","))

# """ you have to specify the """
# path_string="D:/OneDrive - pop.zjgsu.edu.cn/PythonPath/exp3/test.txt"
# def isprime(n):
#     if n==1 or n==0:
#         return False
#     for i in range(2,n):
#         if n%i==0:
#             return False
#     return n
# def decompose(n):
#     # n=(int)(input("input a positive integer:"))
#     item_factor=[]
#     item_power=[]
#     item=[item_factor,item_power]

#     """ python3:the dict is ordered! """
#     # dict={}
#     """ use the index variable to guide the power update operation """
#     j=-1
#     i=2
#     # for i in range(2,n):
#     while n>1:
#         # if n==1:
#         #     break
#         if n%i==0:
#             if isprime(i):
#                 """ iterate n: """
#                 n=n//i
#                 """ update the prime factor and its correspondent power  """
#                 if(i not in item_factor):
#                     item_factor.append(i)
#                     item_power.append(1)
#                     j+=1
#                 else:
#                     item_power[j]+=1
#             else:
#                 i+=1
#         else:
#             i+=1
#     return item
# """ handle in range(2000,2000) """
# string=""
# f=open(path_string,"w")
# for i in range(2000,2000):
#     # string=(str)(i)+":"
#     f.write(str(i)+":")
#     whether_separator=True
#     for item in decompose(i):
#         # count_separator=0
#         string_item=[str(i) for i in item]
#         # print (string_item)
#         f.write(",".join(string_item))
#         if (whether_separator):
#             f.write(";")
#             whether_separator=False
#     f.write("\n")

# f.close()


# """ open and import file to the list to handle """
# open_file_exp3_toList("info_stocks.txt")
# """ test the read result: """
# # print(ls)

# """ sum the price: """

# def calculate_index(item):
#     shares = int(item[1].split(":")[1])
#     price = float(item[2].split(":")[1])
#     sum_price = shares*price
#     return sum_price


# ls.sort(key=lambda item: calculate_index(item), reverse=True)


# def print_iterable(iterable):
#      for item in iterable:
#         for i in [0, 2]:
#             """ to make the print format tidily each column,we specify a width for the middle column: """
#             print(item[i].strip().ljust(20), end=" ")
#         print("sum_price="+str(calculate_index(item)))

# # print(ls)


# def print_sort_result(ls):
#     print("\nthe sorted result:")
#     print_iterable(ls)


# filter_ls=filter(lambda list:float(list[2].split(":")[1])>80,ls)

# def print_filter_result(filter_ls):
#     print("\nthe filtered result:")
#     print_iterable(filter_ls)
#     # for item in filter_ls:
#     #     for i in [0,2]:
#     #         print(item[i].strip(),end=" ")
#     #     print("sum_price=%s"%calculate_index(item))
# print_sort_result(ls)
# print_filter_result(filter_ls)
""" 3 """
# def calculate_size(ls):
#     size=0
#     for item in ls:
#         for word in item:
#             size+=len(word)
#     return size

# """ out put the sorted result: """
# open_file_exp3_toList("transactions.txt")
# ls.sort(key=lambda list_element: float(list_element[3]))
# """ use the good structure to execute the i/o operations:with as file_stream """
# # print(ls[0])
# with open(path_string_fix+"result3b.txt","w") as f_out:
#     print(ls[0])
#     for list_element in ls:
#         string=""
#         for word in list_element:
#             string+=(word+",")
#         f_out.write(string+"\n")

# print(ls)

# """ open the stransactions.txt """
# with open(path_string_fix+"transactions.txt","r") as file_input_stream:
#     ls=file_input_stream.readlines()
# print("the character numbers=%d"%calculate_size(ls))
""" 4 """

# open_file_exp3_toList("transactions.txt")
# def get_num_list_sorted(ls,i):
#     """ i=2,3,4,5,6(i from 0) """
#     get_num_list=[]
#     for list_element in ls:
#         get_num_list.append(float(list_element[i]))
#     get_num_list.sort()
#     return get_num_list

# def get_middle(list):
#     return list[len(list)//2]
# def get_average(list):
#     return sum(list)/len(list)

# def calculate(i):
#     # string=""
#     num_list=[]
#     # for i in range(2,7):
#     num_list=get_num_list_sorted(ls,i)
#     calculated_list=[]
#     calculated_list.append(get_average(num_list))
#     calculated_list.append(get_middle(num_list))
#     calculated_list.append(num_list[-1])
#     calculated_list.append(num_list[0])
#     return calculated_list
# def get_string(list):
#     string=""
#     for item in list:
#         string+=str("%.4f"%item).ljust(20)
#     return string

# with open(path_string_fix+"result4.txt","w") as file_output_stream:
#     file_output_stream.write("".ljust(20)+"均值".ljust(20)+"中位数".ljust(20)+"最大值".ljust(20)+"最小值".ljust(20)+"\n")
#     i=3
#     for i in range(2,7):
#         num_list=[]
#         file_output_stream.write(("第%d列"%(i+1)).ljust(20)+get_string(calculate(i))+"\n")

# open_file_exp3_toList("points.txt")

# def Euclid_distance(point_list1, point_list2):
#     sum = 0
#     for i in range(0, 3):
#         sum += (point_list1[i]-point_list2[i])**2
#     return sum**0.5


# def Manhattan_distance(point_list1, point_list2):
#     sum = 0
#     for i in range(0, 3):
#         sum += abs(point_list1[i]-point_list2[i])
#     return sum


# def Chebyshev_distance(point_list1, point_list2):
#     list = []
#     for i in range(0, 3):
#         list.append(abs(point_list1[i]-point_list2[i]))
#     return max(list)


# """ fetch all points """


# def get_points_list(ls):
#     # num_list=[]
#     """ turn the digit strings to numbers """
#     for list_element in ls:
#         for i in range(1, 4):
#             list_element[i] = float(list_element[i])

#     # return list_element[1:4]
#     """ append the three kinds of distances:"""
#         # num_list.append(float(list_element[i]))

# """ pairwise calculated points   """
# get_points_list(ls)
# Euclid_distance_list = []
# Manhattan_distance_list = []
# Chebyshev_distance_list = []
# # point_coordinate_list1=[]
# # point_coordinate_list2=[]
# p1=[]
# p2=[]
# p_No1=""
# p_No2=""
# offset=0
# for point_list1 in ls:
#     # for point_list2 in ls:
#     offset+=1
#     for i in range(offset,len(ls)):
#         p1,p2=point_list1[1:4], ls[i][1:4]
#         p_No1,p_No2=point_list1[0],ls[i][0]
#         Euclid_distance_list.append( [Euclid_distance(p1,p2),(p_No1,p_No2)])
#         Manhattan_distance_list.append( [Manhattan_distance(p1,p2),(p_No1,p_No2)])
#         Chebyshev_distance_list.append([Chebyshev_distance(p1,p2),(p_No1,p_No2)])

# Euclid_distance_list.sort(key=lambda list:list[0])
# Manhattan_distance_list.sort(key=lambda list:list[0])
# Chebyshev_distance_list.sort(key=lambda list:list[0])
# # print(Euclid_distance_list)
# with open(path_string_fix+"result5.txt","w") as file_output_stream:
#     Euclid_distance_max=Euclid_distance_list[-1]
#     Manhattan_distance_max=Manhattan_distance_list[-1]
#     Chebyshev_distance_max=Chebyshev_distance_list[-1]
#     file_output_stream.write("欧氏距离最大值:%.3f"%Euclid_distance_max[0]+", 距离最远的两点:%s,%s"%(Euclid_distance_max[1][0],Euclid_distance_max[1][1])+'\n')
#     file_output_stream.write("曼哈顿距离最大值:%.3f"%Manhattan_distance_max[0]+", 距离最远的两点:%s,%s"%(Manhattan_distance_max[1][0],Manhattan_distance_max[1][1])+'\n')
#     file_output_stream.write("欧氏距离最大值:%.3f"%Chebyshev_distance_max[0]+", 距离最远的两点:%s,%s"%(Chebyshev_distance_max[1][0],Chebyshev_distance_max[1][1])+"\n")


# count_result_string = "ID".rjust(6)
# count_dict = {'A': 0, 'R': 0, 'N': 0, 'D': 0, 'C': 0, 'Q': 0, 'E': 0, 'G': 0, 'H': 0,
#               'I': 0, 'L': 0, 'K': 0, 'M': 0, 'F': 0, 'P': 0, 'S': 0, 'T': 0, 'W': 0, 'Y': 0, 'V': 0}
# for character in count_dict.keys():
#     count_result_string += character.rjust(6)
# count_result_string += "\n"

# with open(path_string_fix+"seqs_fasta.txt", "r") as file_input_stream:
#     sequences_list = []
#     sequences_list = file_input_stream.read().split(">")
#     sequences_list.pop(0)
#     # sequence_list=[sequence_list for sequence in sequences_list ]
#     # print(string)
#     result_dict = {}
#     for sequence in sequences_list:
#         count_dict = {'A': 0, 'R': 0, 'N': 0, 'D': 0, 'C': 0, 'Q': 0, 'E': 0, 'G': 0, 'H': 0,
#                       'I': 0, 'L': 0, 'K': 0, 'M': 0, 'F': 0, 'P': 0, 'S': 0, 'T': 0, 'W': 0, 'Y': 0, 'V': 0}
#         sequence = sequence.split("\n")
#         ID_string = ""
#         ID_string = sequence.pop(0)
#         size=0
#         """ count a sequence: """
#         result_dict[ID_string] = count_dict
#         for segment in sequence:
#             size+=len(segment)
#             for character in segment:
#                 count_dict[character] += 1
#         """ make up all counted result(accumulate) """
#         count_result_string += ID_string+" "
#         for character in count_dict.keys():
#             count_result_string += str(round(count_dict[character]/size*100,1)).rjust(6)
#             # print(count_result_string)
#         count_result_string += "\n"

# print(count_result_string)
# with open(path_string_fix+"result6.txt","w") as file_output_stream:
#     file_output_stream.write(count_result_string)

# 格式化成2016-03-20 11:45:39形式


# def get_formatted_time():
#     return (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
# account, pwd = "", ""

# items_list = []


# def get_accounts_existed():
#     with open(path_string_fix+"account.txt", "r") as file_input_stream:
#         for item in file_input_stream:
#             items_list.append(item.strip().split(":"))
# # print(items_list)


# def log_record(account,pwd):
#     with open(path_string_fix+"log.txt", "a") as file_output_stream:
#         file_output_stream.write(account+","+pwd+",time:"+get_formatted_time()+"\n")


# def login():
#     for i in range(5):
#         get_accounts_existed()
#         account, pwd = (input("input account:")), (input("input password:"))
#         log_record(account,pwd)
#         if [account, pwd] in items_list:
#             print("welcome! "+account)
#             return
#         else:
#             print("您的账号或密码有误！")
#         # if i==4:
#         #     print("您的账号将被锁定！")
#     print("您的账号将被锁定！")

# login()



#将特定文件夹下的文件移动到另一个文件夹
import os
import shutil

path_src = path_string_fix
path_des = path_string_fix+"mydir/"
""" create the dir mydir in the proper source path """
if not os.path.exists(path_des):
    os.mkdir(path_src+"mydir")
""" get the files in the path: """
files_list = os.listdir(path_src)
""" get the files start with news_: """
file_news_list=os.listdir(path_des)[:2]

""" move files from source path to destination path:"""
def move_news():    
    for file_name in files_list:
        if file_name.startswith("news_"):
            # print(file_name)
            shutil.move(path_src+file_name,path_des)
""" count the word in specified file """
def wordcount(w,txt_file):
    """the frequency of appearance of word w in the file txt_file(attention ,the txt_file use the absolute path)
    !attention2:the function read files which is encode in gbk,so the open() use the encoding="gbk"(gb18030 is ok too) to read it correctly
    Args:
        w (str): [description]
        txt_file (str): [absolute path]
    """
    # list=[]
    string=""
    with open(txt_file,"r",encoding='gbk') as file_input_stream:
        string= file_input_stream.read()
        # print(string)
    return string.count(w)
# print(wordcount("t",path_src+"log.txt"))
""" use(experience the serialize module pickle too store(dump) and use the object serialized:) """

def pickle_deal():
    # obj_list=obj_list
    with open(path_des+"wc.pkl","wb") as file_output_stream:
        pickle.dump((wordcount,file_news_list),file_output_stream)
    with open(path_des+"wc.pkl","rb") as file_input_stream:
        return pickle.load(file_input_stream)
# print(obj_list)

def print_head(word_list):
    for i in [""]+word_list:
        print(i.center(20),end="")
    print()

def print_result(word_list):
    print_head(word_list)
    for file in obj_list[1]:
        print(file.center(20),end="")
        file_full_path=path_des+file
        for word in word_list:
            frequency=0
            frequency=wordcount(word,file_full_path)
            frequency=str(frequency).center(20)
            print(frequency,end="")
        print()
        
# word_list=["中国","美国","科技","芯片"]
# move_news()
# obj_list=pickle_deal()
# "get the function from pickled file"
# wordcount=obj_list[0]
# print_result(word_list)

##
import os
import pandas as pd
##
#将多个文件有序的拼接为一个大文件(包含文件名解析&排序)
dir_base='d:/repos/pythonLearn/pandasLearn/'
# dir=dir_base+'out_delta/'
dir_input=dir_base+'mini_dicts/'
# dir_out=dir

files=os.listdir(dir_input)
# 按顺序拼接(按数字(而不是ascii))
# 测试提取算法对所有文件的提取效果
# for item in files:
#     p=item.index('~')
#     order_str=item[:p]
#     order=int(order_str)
#     print(order)
def get_order(item):
    index_tilde=item.index('~')
    index_dot=item.index('.')
    order_str=item[index_tilde+1:index_dot]
    order=int(order_str)
    return order

def parser(files_list):
    order_list=[]
    for item in files_list:
        order=get_order(item)       
        order_list.append(order)
    order_list.sort()
    return order_list
sorted_order_list=parser(files)
##
# files.sort(key=lambda item:int(item[:item.index('~')]))
files.sort(key=lambda item:get_order(item))
sorted_file_list=files
# print(sorted_file_list)
# print(files)
os.chdir(dir_input)
dfs=pd.DataFrame()
# dfs=pd.read_excel(sorted_file_list[0])
sample=sorted_file_list[:]
# 处理特殊值(参数)&拼接df
for item in sample:
    
    # item_df=pd.read_excel(item,dtype=str)#NULL还是会被解析为NAN
    item_df=pd.read_excel(item,na_filter=False)#OK
    # print(item_df)
    # df.append()并不会原地修改,而是会返回一个处理好的dataframe(这和sort)函数相反.
    dfs=dfs.append(item_df)#,ignore_index=True仅仅是将index改为0...n
# 查看最终大小
shape=dfs.shape
print(shape)
# 截取去掉索引列:spelling以及之后多所有列
dfs_raw=dfs.loc[:,'spelling':]
# print(dfs)
## drop duplicated row of column value
unique_df=dfs_raw.drop_duplicates(subset=['spelling'],keep='first')
##
unique_df.to_excel(dir_input+"../"+"Integer_delta.xlsx",index=False)

sorted_unique_df=unique_df.sort_values('spelling')
sorted_unique_df.to_excel(dir_input+"../"+"Integer_delta_sorted.xlsx",index=False)

##
# #  convert excel to to csv file
file=dir_input+"../"+"Integer_delta_sorted.xlsx"

old_df=pd.read_excel(file)
## 
old_df.to_csv(dir_input+"to_csv.csv")
##

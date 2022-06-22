## 
from os import chdir
import numpy as np
import os
import pandas as pd
##
# 改变工作路径
dir="d:/repos/pythonLearn/PandasLearn/raw_word_data/"
chdir(dir)

file_old="union_gre_neep.xlsx"
file_cet46="cet46.csv"
file_new="new.xlsx"
# 查看当前工作路径
os.getcwd()


# chdir("./PandasLearn")
##
# 读入一个没有表头的excel;而后修改为(添加)合适的表头)
old_df=pd.read_excel(file_old)
##
new_df=pd.read_csv(file_cet46,header=None)
##
new_df.columns=['spelling']
new_df
# new=pd.DataFrame(old_df,columns=["spelling"])
# gre_df.set_axis(["a","b","c"],axis=1,inplace=True)

##
## specify the header for the df object!
##
## 伪并集操作(不做去重处理)
set_fake_union_df=pd.concat([new_df,old_df])
## 检索某个列中满足特定条件(取值)的所有记录:df[df['column_name']=='column_value']
set_fake_union_df[set_fake_union_df['spelling']=='zoom']


##
# 并集(去重)(得到原生不重复的全集)
set_union_df=pd.concat([old_df,new_df]).drop_duplicates()
set_union_df
# 根据数据列重新产生(重新建立索引并排序:reset_index(drop=True));
# 或者不用drop参数,直接截取指定列(旧有的索引列自然会被去掉!)
# set_union_df=set_union_df.reset_index()[['spelling']]
##
# 注意concat(的参数)&drop_duplicates(的参数keep)
set_diff_df=pd.concat([set_union_df,old_df]).drop_duplicates(keep=False)
set_diff_df=set_diff_df.reset_index()[['spelling']]
set_diff_df
# 本地的两份词库中,只有1700左右是重合的
##
# 排序现有索引(索引可能重复的情况下)
# set_diff_df.sort_index()
##
###  输出delta集
set_diff_df.to_excel('delta_cet46_gre.xlsx',index=False)

## 
# try diff compare(optional):以下是差集和pandas方法的推演
s1=pd.Series([2,3,4,5])
s1
df1=pd.DataFrame(s1)
s2=pd.Series([1,3,4,5])
df2=pd.DataFrame(s2)
set_union_df = pd.concat([df2, df1]).drop_duplicates()
set_union_df
#集合论中: A-B=A-AB
# 我们可以利用concat(A+B,B).drop_duplicates(keep=False)得到类似效果
# df2-df1
set_diff_df=pd.concat([set_union_df,df1]).drop_duplicates(keep=False)
set_diff_df
#df1-df2
set_diff_df=pd.concat([set_union_df,df2]).drop_duplicates(keep=False)
set_diff_df
print(set_union_df)
##

# df1=pd.DataFrame([[2,3,4,5]])
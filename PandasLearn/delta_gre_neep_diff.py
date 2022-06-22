## 
from os import chdir
import numpy as np
import os
import pandas as pd
##
dir="d:/repos/pythonLearn/PandasLearn/raw_word_data/"
chdir(dir)
file_source="gre.xlsx"
file_out="outline5500_sorted.xlsx"
os.getcwd()
# chdir("./PandasLearn")
##
# 读入一个没有表头的excel;而后修改为(添加)合适的表头)
gre_df=pd.read_excel(file_source,header=None).iloc[:,:3]
new=pd.DataFrame(gre_df,columns=["a","b","c"])
# gre_df.set_axis(["a","b","c"],axis=1,inplace=True)

##
## specify the header for the df object!
gre_df.columns=['spelling','phonetic','explains']
gre_df_outline=gre_df['spelling']
##
neep_spelling_df=pd.read_excel(file_out)
gre_spelling_df=gre_df[['spelling']]
## 伪并集操作(不做去重处理)
set_fake_union_df=pd.concat([neep_spelling_df,gre_spelling_df])
## 检索某个列中满足特定条件(取值)的所有记录:df[df['column_name']=='column_value']
set_fake_union_df[set_fake_union_df['spelling']=='zoom']
# 并集(去重)
set_union_df=pd.concat([neep_spelling_df,gre_spelling_df]).drop_duplicates()
#经过比较,两个数据集中的重复数据大概是1700个
# 根据数据列重新产生(建立索引)
# set_union_df=set_union_df.reset_index()[['spelling']]
set_diff_df=pd.concat([set_union_df,neep_spelling_df]).drop_duplicates(keep=False)
set_diff_df=set_diff_df.reset_index()[['spelling']]
set_diff_df
# 本地的两份词库中,只有1700左右是重合的
##
# 排序现有索引(索引可能重复的情况下)
# set_diff_df.sort_index()
##
###  输出delta集
set_diff_df.to_excel('delta_gre_neep.xlsx',index=False)

## 
# try diff compare
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
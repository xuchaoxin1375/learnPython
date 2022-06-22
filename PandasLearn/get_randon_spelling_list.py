##
import pandas as pd
import numpy as np
from datetime import datetime 
# 随机矩阵生成器
import numpy.random as nprand
import random as rand

from pkg_resources import working_set
dir='d:/repos/pythonLearn/pandasLearn/'
dir=dir+'raw_word_data/'
fileSource=dir+"union_gre_neep.xlsx"#Integer_delta_sorted.xlsx"

##
words_df=pd.read_excel(fileSource)
##
words_df

## 
# get randon array
source_size=words_df.size
fetch_size=6000
source_size_list=list(range(source_size))
rand.shuffle(source_size_list)
randon_source_order_list=source_size_list
randon_fetch_order_list=randon_source_order_list[:fetch_size]
# print(randon_list)
##
# get randon number  sequence within [0,4500)(the numbers should not be duplicated!)
##
randon_fetch_order_list.sort()
sorted_fetch_list=randon_fetch_order_list

fetch_df=words_df.iloc[sorted_fetch_list,:]
# words_df.drop(index=words_df.index[randon_size_list])
# words_df[randon_size_list]

##
# words_df.drop(words_df.iloc[[1,2,3]])
# words_df.drop([1,3,4])
# cet4_df=words_df.drop(list(randon_size_sorted_list))
##
fetch_df.to_excel(f"spelling_{fetch_size}.xlsx",index=False)
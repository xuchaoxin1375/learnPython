
##
import numpy as np
from datetime import datetime 
import pandas as pd
# 随机矩阵生成器
import numpy.random as nprand
import random as rand
#demo
#create DataFrame
df = pd.DataFrame(nprand.rand(6,2), index=range(0,18,3), columns=['A', 'B'])
##
# fileSource=dir+"neepSampleOutline.xlsx"
# fileSource=dir+"neep5500.xlsx"
# fileOut=dir+"outline5500.xlsx"

# words_df=pd.read_excel(fileSource)
# words_spelling_df=words_df["spelling"]
# print(words_spelling_df)
# word_list=word_list_df.values.tolist()
# word_series=word_list_df.squeeze()
# word_series=word_series.astype("str")
# word_series.astype(str)
# print(word_series.dtypes)
# word_list=word_series.tolist()
# print(word_list[:10])
# print(word_list[-10:])


# word_sorted_list=word_list.sort()
# word_sorted_series=word_series.sort_values()
# word_sorted_series=pd.Series(word_sorted_list)

# # print(word_list)
# word_sorted_series.to_excel(fileOut)
# # print(type(s))
# # t=type(word_list_df)
# # print(t)
# ##


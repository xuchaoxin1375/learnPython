##
import pandas as pd
# import numpy as np
# from datetime import datetime 
# # 随机矩阵生成器
# import numpy.random as nprand
# import random as rand
##
# dir="c:/users/cxxu/desktop/"
dir="./"
# fileSource=dir+"neepSample.xlsx"
fileSource=dir+"neep5500.xlsx"
fileOut=dir+"outline5500.xlsx"
word_df=pd.read_excel(fileSource,header=[1])
# word_list.columns=word_list.iloc[0]
# sort tuples(row items)by specific key(column value)
""" 排序 """
# word_df=word_df.sort_values(by="spelling")
##
words_spelling_df=word_df["spelling"]
# print(datetime.utcnow())
words_spelling_df.to_excel(fileOut,index=False)
# word_list_spelling
# words_spelling=pd.read_excel(fileOut)
# word_list_spelling_read
##

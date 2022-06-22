##
import os
import pandas as pd

dir_base='d:/repos/pythonLearn/pandasLearn/'

os.chdir(dir_base)

file1='./raw_word_data/'+"union_gre_neep.xlsx"
file2='./integer_delta.xlsx'
df1=pd.read_excel(file1,na_filter=False)
# df1.applymap(lambda x:str(x))
df2=pd.read_excel(file2,na_filter=False)
##
df2=df2[[ "spelling" ]]
df2
##
df3=df1.append(df2)
df3
##
# 字符串中包含了True/False,导致排序故障?(并不是,单独的试验说明pandas不会再这方面出错)
# df4=df3["spelling"].map({True: 'True', False: 'False'})
# df3[df3["spelling"]=='true']="yes"
# df3[df3["spelling"]=='false']="no"
##
df1.sort_values(by='spelling')
df1[df1["spelling"]]
##
df2.sort_values(by='spelling')
##
# 将所有元素类型通过python元素类型强制转化,转换为str类型
df3=df3.applymap(lambda x:str(x))
# 这个时候再执行列上的元素排序不会出现数据类型不同的问题!
df_sorted=df3.sort_values(by='spelling')
##
df_result=df_sorted.reset_index(drop=True)
df_result
##
df_result.to_excel("gre_neep_cet46.xlsx")
##
# pd.DataFrame(df4).sort_values(by='spelling')
##

d={"spelling":["app","True","kite","false","bool","null","true"]}
d={"spelling":["app","True","kite","false",1,"bool","null","true"]}
d={"spelling":[True,"test"]}


dfb=pd.DataFrame(d)
##
dfb
t=dfb.dtypes
t
##
dfb.sort_values(by="spelling")
dfb.convert_dtypes()

##
data = pd.DataFrame({'x1':[True, True, False, True, False],            # Create pandas DataFrame
                     'x2':['a', 'b', 'c', 'd', 'e'],
                     'x3':range(10, 15)})
print(data)   
##
data.dtypes

##
data_new1 = data.copy()                                                # Create copy of pandas DataFrame
data_new1['x1'] = data_new1['x1'].map({True: 'True', False: 'False'})  # Replace boolean by string
print(data_new1)                                                       # Print updated pandas DataFrame
data_new1.dtypes

##
import pandas as pd
df = pd.DataFrame({'A': [1,2,3], 'B': [True, False, False], 'C': ['a', 'b', 'c']})

df.A.dtype
# dtype('int64')
df.B.dtype
# dtype('bool')
df.C.dtype
# dtype('O')

df.dtypes
#A     int64
#B      bool
#C    object
#dtype: object
##

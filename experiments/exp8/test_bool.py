import pandas as pd
import numpy as np
''' 得到dataframe '''
df1 = pd.DataFrame({'left': ['foo', 'bar']})
df2 = pd.DataFrame({'left': [7, 8]})
print(f"df1:\n{df1}\ndf1.type:{type(df1)}")
# test=df1.merge(df2, how='cross')
''' 尝试合并列: '''
test_df=pd.concat([df1,df2])
print(f"test_df:\n{test_df}\ntype(test_df):{type(test_df)}")

''' 得到ndarray '''
test_nd=np.array(test_df)
print(f"test_nd:\n{test_nd}\ntest_nd.shape:{test_nd.shape}\ntype(test_nd):{type(test_nd)}")
''' 得到series: '''
test_series=pd.Series({"a":2,"t":6})
print(f"test_series:\n{test_series}\ntype(test_series):{type(test_series)}")
''' 得到一维ndarray '''
test_nd=np.array(test_series)

print(f"test_nd:\n{test_nd}\ntype(test_nd):{type(test_nd)}\ntest_nd.shape:{test_nd.shape}")
''' 得到二维ndarray: '''
# test_nd2=np.array([test_nd])
test_nd2=test_nd.reshape(test_nd.shape[0],1)
print(f"test_nd2,test_nd2.shape:\n{test_nd2};\n{test_nd2.shape}")
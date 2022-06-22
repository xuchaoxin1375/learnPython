'''
Description: 
Version: 2.0
Author: xuchaoxin
Date: 2021-03-05 23:18:02
LastEditors: xuchaoxin
LastEditTime: 2021-03-05 23:25:39
'''
import datetime

starttime = datetime.datetime.now()
#long running
#do something other
#运行代码
for i in range(1000):
    if i>950:
        print(i)  
endtime = datetime.datetime.now()
print (endtime - starttime)


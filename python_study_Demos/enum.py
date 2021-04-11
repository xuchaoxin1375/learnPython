'''
Description: 
Version: 2.0
Author: xuchaoxin
Date: 2021-02-03 22:02:57
LastEditors: xuchaoxin
LastEditTime: 2021-02-03 22:06:25
'''
from enum import Enum
Month = Enum('Month_', ('Jan', 'Feb', 'Mar', 'Apr', 'May',
                       'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name, member in Month.__members__.items():
    """  """
    print(name, '=>', member, ',', member.value)
""" 
print:
Jan => Month_.Jan , 1
Feb => Month_.Feb , 2
Mar => Month_.Mar , 3
Apr => Month_.Apr , 4
May => Month_.May , 5
Jun => Month_.Jun , 6
Jul => Month_.Jul , 7
Aug => Month_.Aug , 8
Sep => Month_.Sep , 9
Oct => Month_.Oct , 10
Nov => Month_.Nov , 11
Dec => Month_.Dec , 12 """
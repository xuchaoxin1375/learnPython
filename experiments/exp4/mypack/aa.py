'''
Description: 
Version: 2.0
Author: xuchaoxin
Date: 2021-04-14 14:39:58
LastEditors: xuchaoxin
LastEditTime: 2021-04-14 14:44:49
'''

import math

def add(x: float, y: float) -> None:
    # 除了函数注解,您当然可以为某个变量使用类型注解:
    pi: float = 3.142
    
    print(pi)
    print(x+y)
    
if __name__=="__main__":
    add(1,2)
    
 
''' Type Comments[类型注解]:对位置比较严格: '''
def circumference(radius):
    #type: (float) -> float
    return 2 * math.pi * radius
'''
Description: 
Version: 2.0
Author: xuchaoxin
Date: 2021-02-01 16:40:42
LastEditors: xuchaoxin
LastEditTime: 2021-02-01 17:30:25
'''
from functools import reduce
def turnToInteger(x,y):
    """[summary:turn the integer numbers to a big integer in sequence ]

    Args:
        x ([int ]): [integer element in the integer list(the function expression after the first invoke the function)]
        y ([type]):[the integer of the integer list y] 
    Returns:
        [int]: [the turning result of the list y]
    """ 
    print(x*10+y)
    print("\n")
    return x*10+y
print("print the result:"+str(reduce(turnToInteger,[1,2,3,4]))
      )
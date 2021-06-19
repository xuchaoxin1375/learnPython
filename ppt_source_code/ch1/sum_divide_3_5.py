#ch1: sum_divide_3_5.py
#import numpy as np
#s=0
#for i in range(1,1000):
#    if i%3==0 or i%5==0:
#        s+=i
#print(s)

ls=[i for i in range(1,1000) if i%3==0 or i%5==0]
##a=sum(ls)
##print(a)
print(ls)
print("sum:",sum(ls))
# ch2: set.py
a={"peace","peace","rong","rong","nick"}                                         
print("a:",a)                                                                                                                                       
b=set(["peace","peace","rong","rong","hello"])                                               
print("b:",b)  
                                                                                                                                      
print("并集:",a|b)#演示联合                                                                                                                                             
print("交集:",a&b)#演示交                                                                                                                                           
print("差集:",a-b) #演示差                                                                                                                                        
print("对称差:",a^b)#对称差集     


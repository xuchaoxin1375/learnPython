# -*- coding: utf-8 -*-
#ch3:try_except.py
#while 1:
#    name=input("Enter name:")
#    if name=='stop':
#        break
#    age=input("Enter age:")
#    print("age:",age)
#    print('Hello',name,'=>',int(age)**2)


#ch3:try_except.py
while 1:
    name=input("Enter name:")
    if name=='stop':
        break
    age=input("Enter age:")
    try:
        print('Hello',name,'=>',int(age)**2)
    except:
        print('Please input correct age!')


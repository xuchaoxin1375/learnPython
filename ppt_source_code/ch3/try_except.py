# -*- coding: utf-8 -*-
# ch3:try_except.py
# while 1:
#    name=input("Enter name:")
#    if name=='stop':
#        break
#    age=input("Enter age:")
#    print("age:",age)
#    print('Hello',name,'=>',int(age)**2)


# ch3:try_except.py
while 1:
    name = input("Enter name:")
    if name == 'stop':
        break
    age = input("Enter age:")

    try:
        print('Hello', name, '=>', int(age)**2)
    except:
        print('Please input correct age!')
# %%

# 列表推导式中循环嵌套的规律:(观察打印结果中变化最快(最频繁的变量(该变量对应的for就嵌套在最深层)))
L = [(x, y, z) for x in range(3)
     for y in range(5) for z in range(-7, -1)]
# print(L)
for item in L:
    print(item)
''' 相当于:
'''

def verify():
    for x in range(3):
        for y in range(5):
            for z in range(-7, -1):
                print((x+1, y+0.1, z+1))

# %%
verify()

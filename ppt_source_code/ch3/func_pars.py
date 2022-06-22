# -*- coding: utf-8 -*-
# ch3:func_pars.py
# def numcmp(a,b):
#    if a>b: return 1
#    elif a==b: return 0
#    else: return -1
# print(numcmp(8,9),numcmp(12,1),numcmp(23,23))
#
# print(numcmp(a=13,b=78))
#
# print(numcmp(b=78,a=13))

# def func(a=5,b):
#    if a>b: print(a)
# func(5,10)


# def func(a,b=10):
#    if a>b: print(a)
# func(20,10)

# %%
def f(*x):
    if len(x) == 0:
        print('None')
    else:
        print(x)


# test
f(1)
f(1, 2, 3)
f()
f('t', 1, 'hello')
# %%


def fd(**x):
    if len(x) == 0:
        print('None')
    else:
        print(x)


#    test
fd()
fd(x=1, y=2, z='c')

# fd(1, 2)#Expected 0 positional arguments
fd(x=1, y=2)

# %%
# 关键字参数可以使用位置参数的方式来传实参


def test_default(x=6):
    print(x)


test_default(7)
# 位置参数可以通过使用关键字参数的形式传递实参


def test_position(x):
    print(x)


test_position(x=8)
# %%


def test(x, y=1,
         *a,  # 保存位置参数序列的元组(经常以*args)
         **b):  # 保存关键字参数的字典
    print(x, y, a, b)


test(1)
test(1, 2)
test(1, 2, 3, 4)
test(x=1, y=2)
test(1, a=2)
test(1, 2, 3, a=4)
test(1, 2, 3, c=4)
# got multiple values for argument 'y'
# test(1, 2, 3, y=4)

# %%
# 不定位置参数
def positional_args(*x):
    if len(x) == 0:
        print('None')
    else:
        print(x)


# test
positional_args(1)  # (1,)
positional_args(1, 2, 3)  # (1, 2, 3)
positional_args()  # None
positional_args('t', 1, 'hello')  # ('t', 1, 'hello')
# 不定位置参数不接受关键字参数实参
# positional_args(x=1)#TypeError: positional_args() got an unexpected keyword argument 'x'

# %%

# 不定关键字参数


def variables_kwargs(**x):
    if len(x) == 0:
        print('None')
    else:
        print(x)


#    test
variables_kwargs()
variables_kwargs(x=1, y=2, z='c')
variables_kwargs(x=1, y=2)
# 不定关键字参数容器不接受位置参数实参
# fd(1, 2)#Expected 0 positional arguments

# %%
# 关键字参数可以使用位置参数的方式来传实参

print("# 关键字参数可以使用位置参数的方式来传实参")
def test_default(x="default value"):
    print(x)


test_default()  # 6(default value)
test_default("overwrite by positional parameter")  # 7(overwrite)
test_default(x="overwrite by keyword parameter")

# 位置参数可以通过使用关键字参数的形式传递实参
print("# 位置参数可以通过使用关键字参数的形式传递实参 ")
def positional_by_key(x):
    print(x)

positional_by_key(x="by keyword parameter")
# %%
# 位置参数,默认参数(关键字参数),不定位置参数,不定关键字参数


def test(x, y=1,
         *a,  # 保存位置参数序列的元组(经常以*args)
         **b):  # 保存关键字参数的字典
    print(x, y, a, b)


test(1)  # 1 1 () {}
test(1, 2)  # 1 2 () {}
test(1, 2, 3, 4)  # 1 2 (3, 4) {}
test(x=1, y=2)  # 1 2 () {}
# 没有合适关键字形参,关键字实参将被传入到关键字参数容器(字典中)保存(即使关键字实参和不定形参容器名称(元组/字典)重名)
test(1, a=2)  # 1 1 () {'a': 2}
test(1, 2, 3, a=4)  # 1 2 (3,) {'a': 4}
test(1, 2, 3, c=4)  # 1 2 (3,) {'c': 4}
# got multiple values for argument 'y'
# test(1, 2, 3, y=4)

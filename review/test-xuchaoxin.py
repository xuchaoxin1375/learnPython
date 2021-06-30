
import numpy as np
a = [3, 1, 2, 3, 3]
# a.insert(0,3)
a.remove(3)
# print("2\b4\b")
# %%
print("123456789"[1::2])
# "a".format()
"test"


# %%
5*3
print("e")
# %%
dict_test = {1: "str1", 2: "str2"}
# %%
get_type = dict_test.items()
# %%
print(type(get_type))

# %%
for item in get_type:
    # print(item)
    print(type(item))
    1+5
    9
# %%
""" For values exactly halfway between rounded decimal values, NumPy rounds to the nearest even value. Thus 1.5 and 2.5 round to 2.0, -0.5 and 0.5 round to 0.0, etc. """
np.round([2.5, 2.6, 2.4, 1.4])
# %%
""" axisint or None, optional
Axis along which to sort. If None, the array is flattened before sorting. The default is -1, which sorts along the last axis. """
# 快速得到一个随机多维数组
a = np.random.rand(4, 7)*10
a = np.floor(a)
# 也可以,直接,由浮点型得到转换为整型后的数组(新对象\)
b = a.astype(int)

# %%

# dir(np.ndarray)

# %%
b.sort(axis=0)
b

# %%
b.sort()
b
# %%
orderd_array = np.arange(10)
orderd_array.argsort()
# %%
x = np.array([13, 111, 12, 15])
x.argsort()
# x
# %%
str="qweu123"
str[::-5]#3w(逆向索引)
print(str[::5])#q2
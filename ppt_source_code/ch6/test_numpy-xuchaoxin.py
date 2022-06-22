import numpy as np
a = np.array([[[1, 2, 3],
               [11, 3, 4]],
              [[1, 2, 3],
               [11, 3, 4]]])

# %%
# 打印出a的维度数(即嵌套深度)
# 高维数组:嵌套深
print(a.ndim)
print(a.shape)
# 高维点:单个点的坐标的刻画维度多(可以用一个n元组表达)(d0,d1,d2,d3,d4,..dn-1):
''' 
例如:
一维点:(d0)
二维点:(d0,d1)
三维点:(d0,d1,d2):例如(1,2,3),(x=1,y=2,z=3)
...
总之,要区分好两种"维度"的含义
ndarray(多维度数组)对象的shape属性可以体现该数组在各个维度上的度量宽度
    '''
b = np.array(
    [1, 2, 3, 4, 5, 6]
)
print(b.ndim, "\n", b.shape)


# %%
np.random.rand(2, 2, 2)
''' 
 If high is None (the default), then results are from [0, low).
 Return random integers from low (inclusive) to high (exclusive).

Return random integers from the “discrete uniform” distribution of the specified dtype in the “half-open” interval [low, high).'''
print(np.random.randint(10))
print(np.random.randint(10, 99))

# %%
ls = range(120)
c = np.array(ls).reshape(2, 2, 5, 3, 2)
print(c)

# %%
t = np.arange(10)
t[t % 2 == 1]
# %%
x = np.array([[[1], [2], [3]], [[4], [5], [6]]])
x.shape

# %%

x[...,0]
# %%
x[...]
# %%
x=x.reshape(2,1,3)
x[...,1]
# %%
array=np.array([range(i*10,i*10+6) for i in range(6)])
array

# %%
r=range(1,10)
print(type(r))
# %%
array=np.linspace(0,2*np.pi,10)
np.sin(array)
##
import numpy as np
import matplotlib.pyplot as plt
##

x = np.linspace(0, 2, 100)  # Sample data.

# Note that even in the OO-style, we use `.pyplot.figure` to create the Figure.
# ->Tuple[Figure, Axes]
fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
ax.plot(x, x, label='linear@lable=linear')  # Plot some data on the axes.
ax.plot(x, x**2, label='quadratic@label=quadratic')  # Plot more data on the axes...
ax.plot(x, x**3, label='cubic@lable=cubic')  # ... and some more.
# set lables
ax.set_title("Simple Plot@ax.set_title")  # Add a title to the axes.
ax.set_xlabel('x label@ax.set_xlable')  # Add an x-label to the axes.
ax.set_ylabel('y label@ax.set_ylable')  # Add a y-label to the axes.
ax.legend();  # Add a legend.

##
x = np.linspace(0, 2, 100)  # Sample data.

plt.figure()
plt.plot(x, x, label='linear')  # Plot some data on the (implicit) axes.
plt.plot(x, x**2, label='quadratic')  # etc.
plt.plot(x, x**3, label='cubic')
plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Simple Plot")
plt.legend();

##
np.random.seed(19680801)  # seed the random number generator.
data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100
# print(np.random.randn)//默认使用老的RandomState 计算随机数
fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
ax.scatter('a', 'b', c='c', s='d', data=data)
ax.set_xlabel('entry a')
ax.set_ylabel('entry b');


##
""" 仅提供value向量进行画图,不提供其他维度向量,让matplot自动找到一个合适的刻度来绘图 """
rng=np.random.default_rng()
data=rng.random(size=(1000))
values=data*10
# y=x**2
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html
# 调整画布尺寸大小 Width, height in inches.
plt.figure(figsize=(20,20))
plt.tick_params(labelsize=20)
plt.plot(values)
# print("values:",values)
avg=values.mean()
print("avg:",avg)



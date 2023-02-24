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


import numpy as np
import matplotlib.pyplot as plt
##
# 生成数据
x = np.arange(0, 6, 0.1) # 以 0.1为单位，生成 0到 6的数据
y1 = np.sin(x)
y2 = np.cos(x)

# 绘制图形
plt.plot(x, y1, label="sin")#默认实线绘制
plt.plot(x, y2, linestyle = "--", label="cos") # 用虚线绘制
plt.xlabel("x") # x轴标签
plt.ylabel("y") # y轴标签
plt.title('sin & cos') # 标题
plt.legend()
plt.show()
##
import matplotlib.pyplot as plt
from matplotlib.image import imread

img_path=r'D:\org\Ecloud\MyPictures\MIngKing.png'

img = imread(img_path) # 读入图像（设定合适的路径！）
plt.imshow(img)
plt.show()
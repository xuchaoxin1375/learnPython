""" use jupyter notebook to run this file (recommanded!)"""
""" part1:import packages &set the basic sample data set! """
##
import matplotlib.pyplot as plt
import matplotlib.scale as sle
import numpy as np
import matplotlib.ticker as ticker
import math
x_narraw=np.linspace(-10,10,300)
x_wide=np.linspace(-100,100,300)
x_dense=np.linspace(-10,10,1000)
x_nd=x_narraw
xdata=x_nd
data1=np.random.random(300)*10

""" part2:assign the target function in the section"""
##

##
d=2
y1=x_nd
y2=x_nd+d
y3=x_nd-d
##
# 创建显示创建一个绘图对象

fig,axs=plt.subplots(1,1,figsize=(8,8))
axs.plot(x_nd,y1,color='r',label='f(x)=x')
axs.plot(x_nd,y2,color='b',label='f(x+d)=x+d')
axs.plot(x_nd,y3,color='g',label='f(x-d=x-d')
# axs.text(title='d=2')

axs.set_title('f(x)=x @(offset d=2)')
plt.grid()
plt.xticks(np.arange(-10,10,1))
plt.axvline(x = 0, color='black',linestyle='--', label = 'x=0')
plt.axvline(x = -2, color='b',linestyle='dotted', label = 'x=-2')
plt.axvline(x = +2, color='r',linestyle='-.', label = 'x=+2')

axs.legend()
plt.plot()
# # rude line chart
# plt.plot([1, 2, 3, 4], [1, 4, 2, 3])
# plt.show()
##
# plot the quadratic function
# x_nd=np.linspace(-10,10,100)
# y=x_nd**2

##
# y=math.sin(x_nd)
y=[math.sin(x) for x in x_nd]
# print([x for x in x_nd])
##

y=[math.sin(x)/x for x in x_wide]
##
x_nd=x_dense
y=x_nd+1/x_nd
##
e1=np.abs(x_nd+1)
e2=np.abs(2*x_nd-3)
y=np.subtract(e1,e2)
##
e1=np.abs(x_nd+1)
e2=np.abs(2*x_nd-3)

## 
x_nd=np.linspace(-10,10,100)
y=np.divide(
    np.sin(
        np.multiply(
            x_nd,np.sin(1/x_nd)
            )
    ),
    np.multiply(
            x_nd,np.sin(1/x_nd)
            )
    )

y
##
""" part3:show the fucntion image! """
##
y=np.abs(x_nd)/x_nd
## 
y=np.sin(1/x_nd)
## 
# plt.scatter(x_nd,y)
##

##
plt.figure(figsize=(15,15))
# 设定刻度大小
plt.tick_params(labelsize=22)
# 全局字体大小
plt.rc(group='font', size=22)
plt.grid()
##
plt.plot(x_nd,e1,label="e1")
plt.plot(x_nd,e2,label="e2")
##
plt.xticks(np.arange(-10,10,1))
# plt.plot
# plt. .set_minor_locator(ticker.MultipleLocator(0.1))
"""draw by subplot"""
##
fig,axs=plt.subplots(figsize=(10,10))
axs.plot(x_nd,y,label="y")
##
##
# fig.figsize=(35,35)
axs.plot(x_nd,e1,label="e1")
axs.plot(x_nd,e2,label="e2")
plt.axvline(x = -1, color='b',linestyle='dotted', label = 'y=-1')
plt.axvline(x = 3/2, color='r',linestyle='-.', label = 'y=3/2')
##
# axs[0].xaxis.set_minor_locator(ticker.MultipleLocator(0.5))

# axs.show()

##
# plt.xticks(np.arange(-10,10,1))
plt.grid()
plt.legend()
plt.plot(x_nd,y)
plt.show()

##
# fig, axs = plt.subplots(1, 2, figsize=(5, 2.7), layout='constrained')
# data1=x_nd
# xdata = np.arange(len(data1))  # make an ordinal for this
# data = 10**data1
# axs[0].plot(xdata, data)

# axs[1].set_yscale('log')
# axs[1].plot(xdata, data);
##
fig, axs = plt.subplots(2, 1, layout='constrained')
axs[0]  # type: ignore
axs[0].plot(xdata, data1)  # type: ignore
axs[0].set_title('Automatic ticks')
#figure2
axs[1].plot(xdata, data1)
# axs[1].set_xticks(np.arange(0, 100, 30), ['zero', '30', 'sixty', '90'])
axs[1].set_xticks(np.arange(0, 100, 3))
axs[1].set_yticks([ 0, 1.5])  # note that we don't need to specify labels
axs[1].set_title('Manual ticks');
##



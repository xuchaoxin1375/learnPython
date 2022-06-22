""" use jupyter notebook to run this file (recommanded!)"""
""" part1:import packages &set the basic sample data set! """
##
import matplotlib.pyplot as plt
import numpy as np
import math
x_narraw=np.linspace(-10,10,300)
x_wide=np.linspace(-100,100,300)
x_dense=np.linspace(-10,10,1000)
x_nd=x_narraw

""" part2:assign the target function in the section"""
##
# rude line chart
plt.plot([1, 2, 3, 4], [1, 4, 2, 3])
plt.show()
##
# plot the quadratic function
x_nd=np.linspace(-10,10,100)
y=x_nd**2

##
# y=math.sin(x_nd)
y=[math.sin(x) for x in x_nd]
# print([x for x in x_nd])
##

y=[math.sin(x)/x for x in x_wide]
##
x_nd=x_dense
y=x_nd+1/x_nd
""" part3:show the fucntion image! """
##
y=np.abs(x_nd)/x_nd
## 
y=np.sin(1/x_nd)
## 
plt.scatter(x_nd,y)
##
plt.figure(figsize=(50,50))
plt.plot(x_nd,y)
plt.show()

##
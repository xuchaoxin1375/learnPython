
import numpy as np  
import matplotlib.pyplot as plt  
''' to make the chart well,you must set well the graph with the matched axes range
as for the other information,such as the title, the labels of x,y axes;and the formula expression with the appropriate
location(axis value)
then is the color of the chart '''
mu,sigma=-1,1
array_x=mu+sigma*np.random.randn(10000)
# array_x=np.random.normal(-1,1,10000)  

n,bins,patches=plt.hist(array_x,bins=100,density=1)
# print(bins)  
# set the title and x,y lables of the chart:
plt.title('Histogram of normal attributions')  
plt.xlabel('x')  
plt.ylabel('y')  
"""the text() fuction 
    it support the latex syntax to express formula:r"$string#" 
    DESCRIPTION
    Add text to the axes ['æksiːz].

    Add text in string s to axis at location x, y, data coordinates.

    PARAMETERS
    x, y : scalars
    data coordinates
    s : string
    text"""
# Add text in string s to axis at location x, y, data coordinates.
    #it must matched properly with the chart x,y axes range to display,or you couldn't see it in the chart!
plt.text(0,0, r'$\mu=-1,\ \sigma=1$')  
""" Convenience method to get or set axis properties. """
#if you not specify the axis ,then the chart axes will auto adjust to display properly!
# plt.axis([-10,10,0,1])  
''' set if you want to display the grid: '''
plt.grid(True)
# plt.show()
# time.sleep(2)
''' display the chart and the auto close it : '''
plt.pause(3)


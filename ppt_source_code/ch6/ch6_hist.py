# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 20:10:22 2021

@author: zero
"""

#ch6_hist.py
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(19680801)
mu = 100  # mean of distribution
sigma = 15  # standard deviation of distribution
x = mu + sigma * np.random.randn(437)# example data
num_bins = 50
fig, ax = plt.subplots()

# the histogram of the data
n, bins, patches = ax.hist(x, num_bins, density=True)
# add a 'best fit' line
a=1/(np.sqrt(2*np.pi)*sigma)
y = a*np.exp(-0.5*(1/sigma*(bins-mu))**2)
ax.plot(bins, y, '--')
ax.set_xlabel('Smarts')
ax.set_ylabel('Probability density')
ax.set_title(r'Histogram of IQ: $\mu=100$, $\sigma=15$')

fig.tight_layout()
plt.show()


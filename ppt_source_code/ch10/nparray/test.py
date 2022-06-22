# -*- coding: utf-8 -*-

# file: test.py
import cos_doubles
import numpy as np
import matplotlib.pyplot as plt

a = np.linspace(-5, 5, 100)
b = np.empty_like(a)
cos_doubles.cos_doubles_func(a, b)

plt.plot(b)
plt.show()


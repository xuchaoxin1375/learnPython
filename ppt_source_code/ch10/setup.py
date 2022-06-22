# -*- coding: utf-8 -*-
#setup.py
from distutils.core import setup
from Cython.Build import cythonize
import numpy

setup(
    ext_modules = cythonize(["sqrt_cy1.pyx","sqrt_cy2.pyx","sqrt_cy3.pyx"]),
    include_dirs=[numpy.get_include()]
)

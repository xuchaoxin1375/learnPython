# -*- coding: utf-8 -*-
#ch4: ospath.py
import os
from os.path import join 
path1 = os.path.dirname(__file__) 
print('The directory of this .py file is:\n', path1)
print()

newdir=join(path1,'hello')
os.mkdir(newdir)
for f in os.listdir(path1):
    print(f)
    
print()
for f in os.listdir(path1):
    print(os.path.abspath(f))
    


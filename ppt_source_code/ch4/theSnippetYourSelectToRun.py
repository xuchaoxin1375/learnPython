# -*- coding: utf-8 -*-
#ch4: ospath.py

# %%

import os
import os.path as Path
from os.path import join  # 导入函数,以便直接调用
path1 = os.path.dirname(__file__)


def get_file_location():
    print('The directory of this .py file is:\n', path1)

# %%


newdir: str = join(path1, 'hello')
if os.path.exists(newdir) == False:
    os.mkdir(newdir)

# %%


def type_path():
    for file_str in os.listdir(path1):
        type_str = "file" if Path.isfile(file_str) else "dir"
        print(file_str, "type:"+type_str)


def test_abspath():
    for file_str in os.listdir(path1):
        print(os.path.abspath(file_str))
# print()

# %%

# 具体请看官方函数api文档
def test_walk():
    for item in os.walk(path1):
        # item:Tuple[str, List[str], List[str]]
        print(item)
        # print(type(item))
    

# %%
import os
from os.path import join, getsize

# %%
# print(getsize(path1))
# %%

# 请务必正确的传入合适的参数个os.walk()方法
# 一种经典的用法是,将os.walk()返回的三元组直接用一个三元组收集起来(三元组不加括号也可以)
for root, dirs, files in os.walk(path1):
    # be equals: for (root, dirs, files) in os.walk(path1):
    print(root, "consumes", end=" ")
    # pr
    print(sum(getsize(join(root, name)) for name in files), end=" ")
    print("bytes in", len(files), "non-directory files")
    if 'CVS' in dirs:
        dirs.remove('CVS')  # don't visit CVS directories
# %%

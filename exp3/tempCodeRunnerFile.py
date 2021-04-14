pack_path_string="d: / OneDrive - pop.zjgsu.edu.cn/pythonPath/exp3"

sys.path.append(path_string)
""" 插入完毕,可以正常导入模块(或其中的某个函数) """
from test_submodule_package.add import add_func  
print(add_func(1,5))

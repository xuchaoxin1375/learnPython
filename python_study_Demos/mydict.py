'''
Description: 
Version: 2.0
Author: xuchaoxin
Date: 2021-02-04 11:34:28
LastEditors: xuchaoxin
LastEditTime: 2021-02-04 15:28:18
'''
class Dict(dict):
    """ 接受任意关键字参数 """    
    def __init__(self, **kw):
        """ 调用父类的__init__方法 """
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value
d={'a':1,'b':2}
d['test']=6
print(d)
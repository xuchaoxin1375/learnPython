'''
Description: 
Version: 2.0
Author: xuchaoxin
Date: 2021-02-02 11:16:53
LastEditors: xuchaoxin
LastEditTime: 2021-02-02 11:58:11
'''
def log(func):
    # print("executing the log()")
    def wrapper(*args, **kw):
        """ the wrapper function add some functions to the primitive function's invoke temporary/dynamically  """
        print("executing the wrapper()")
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper # when you invoke the primitive function ,the decoration mechanism will invoke the wrapper after that

""" simple decoration """
@log
def now():
    print('hello now!')

#print("do a other thing")
now( )
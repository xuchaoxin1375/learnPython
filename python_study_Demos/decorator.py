'''
Description: 
Version: 2.0
Author: xuchaoxin
Date: 2021-02-02 10:05:09
LastEditors: xuchaoxin
LastEditTime: 2021-03-31 09:50:53
'''
import functools
# def log(func):
#     #将原始函数func的_name_等属性复制到wrapper()函数中:
#     @functools.wraps(func)
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)

#     return wrapper


def log(text):
    print("executing log() and to return/invoke decorator")

    def decorator(func):
        print("executing decorator and to return/invoke wrapper()")
        # 将原始函数func的_name_等属性复制到wrapper()函数中:

        @functools.wraps(func)
        def wrapper(*args, **kw):
            print("executing wrapper() and to return/invoke func()(primitive function())")
            print('\t use(print) the parameter of the decoration log():%s,\n\tprint the primitive funcition name: %s():' % (
                text, func.__name__))
            return func(*args, **kw)
        return wrapper  # 访问被装饰的函数(greet()的独立调用语句)
    return decorator  # 访问被装饰的函数的定义处(这里是def greet(),但并不直接执行greet()),然后回来


""" The decorator is called as a higher-order function """


@log("'test the parameter of the log() decoration'")
def greet():
    print("executing the primitive function:greet()!!!")
    print("hello")


""" if we don't invoke the function which is be decorated by the decoration function log(),it still could execute several statements of the log() decoration:

executing log() and to return/invoke decorator
executing decorator and to return/invoke wrapper()
"""
""" 调用greet()=>log("exec")=>decorator(func=greet)=>wrapper()=>func=greet() """

""" The decorator is called as a higher-order function """
#log("test invoke the log() decoration  along")


def main():
    print("do another thing to observe the consistency of the decorator mechanism")
    greet()


main()

'''
Description: 
Version: 2.0
Author: xuchaoxin
Date: 2021-02-03 10:32:17
LastEditors: xuchaoxin
LastEditTime: 2021-02-03 11:49:45
'''
from types import MethodType

class Student:
    def printName(name):
        print(name+"!!")

s=Student()
def setName(self,name):
    self=name

""" 利用MethodType(),将setName函数绑定到对象s中 """
s.setName=MethodType(setName,s)
s.setName("good")
print(hasattr(s,"setName"))
def set_score(self,score):
    self.score=score
Student.set_score=set_score
print(hasattr(Student,"set_score"))
""" dir()函数返回参数对象的成员名清单 """
print(dir())
#dir(Student)
    
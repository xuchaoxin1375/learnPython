# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 16:21:29 2021

@author: zero
"""

#ch5: class_inherit.py
#class people: #单继承：定义父类
#    name = ''
#    age = 0
#    def __init__(self,n,a):#定义构造方法
#        self.name = n
#        self.age = a
#    def speak(self):
#        print("%s说: 我%d岁。"%(self.name,self.age))
#print('Initial age:',people.age)
#class student(people): #定义子类
#    grade = ''
#    def __init__(self,n,a,g):
#        people.__init__(self,n,a) #调用父类构造函数, 同super().__init__(n,a)
#        self.grade = g
#    def speak(self): #重写(override)父类方法
#        print("%s说: 我%d岁在读%d年级"%(self.name,self.age,self.grade))     
#stu = student('Alice',10,3)
#stu.speak()

#ch5: class_inherit.py
class Fruit():
    def color(self):
        print("Fruits are colorful")
class Apple(Fruit):
    def color(self):
        super().color()
        print("Apple is red")
class Orange(Fruit):
    def color(self):
        super().color()
        print("Orange is orange")
apple = Apple()
orange = Orange()
apple.color()
orange.color()


#ch5: class_inherit.py 
#class people: # 多继承: 定义父类
#    name = ''
#    def __init__(self, n):
#        self.name = n
#    def speak(self):
#        print("我叫%s." % (self.name))
#class student(people): #student类单继承people类
#    age = 0
#    def __init__(self, n, a):
#        people.__init__(self, n)
#    def speak(self):
#        print("我叫%s，我今年%d岁" % (self.name, self.age))
#class speaker():#定义另一个父类
#    topic,name= '',''
#    def __init__(self, n, t):
#        self.name,self.topic = n,t
#    def speak(self):
#        print("我叫%s，我分享的主题是%s" % (self.name, self.topic))
#class sample(speaker, student):#多重继承
#    def __init__(self, n, a, t):
#        student.__init__(self, n, a)
#        speaker.__init__(self, n, t)
#
#test = sample("Alice", 25, "Python与数据科学")
#test.speak()  # 默认调用的是speaker类的方法



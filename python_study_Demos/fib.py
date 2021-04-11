'''
Description:
Version: 2.0
Author: xuchaoxin
Date: 2021-02-03 18:57:17
LastEditors: xuchaoxin
LastEditTime: 2021-02-03 21:33:39
'''


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器a，b

    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己

    def __next__(self):  # 可迭代的关键
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值

        if self.a > 1000:  # 退出循环的条件
            raise StopIteration()  # 抛出异常
        return self.a  # 返回下一个值

    def __getitem__(self, n):
        """ 让Fib对象能够通过Fib[n]的形式访问(可以通过通项公式实现,也可以通过for in结构计算到目标索引对应的项,再将结果返回) 
        此处通过地推公式实现:
        Args:
            n ([type]): [description]

        Returns:
            [type]: [description]
        """        
        if isinstance(n,int):
            a, b = 1, 1
            for x in range(n):
                """ 计算a+b得到的下一个元素的值记录在下一轮的b上(b(n+1)) """
                a, b = b, a + b
                """ a=b=1,b=a+b=2; a=b=2,b=a+b=3 """
            return a
            """ 检验算法:Fib()[0]=1,Fib()[1]=1,Fib()[2]=2,... """
        """ 进一步扩展,使其具有部分切片功能(步长step=1的情况下的切片,即形如[start:stop](以冒号分隔的中括号对,start缺省为None,这里将None处理为start=0)) """ 
        if isinstance(n, slice): # n是切片(切片也是一种对象)
            """ 分别取得切片对象的start和stop(这一步不是必须的,但可以提高灵活性(特别是只读对象)和直观性:start=0) """
            start = n.start
            stop = n.stop
            #处理start缺省的情况;None 类似于null
            if start is None:
                start = 0
            
            a, b = 1, 1# a0=1,b0=1;
            L = []
            for x in range(stop):# x=0,1,2,...,stop-1;
                """ stop-1>=0(stop>=1)时,可以进入循环 """
                """ 当索引x开始落在切片区间中时,将结果插入到L列表中,又由for in中x的取值序列可知,x的取值<=stop-1 """
                """ 0<=start<stop时,执行插入动作 """
                if x >= start:
                    """对于[0:stop], a_i=1,1,2,3,5,...(第一个1是迭代之前,第二个1是第一次迭代之后) """
                    L.append(a)
                """新值和旧值的递推关系:
                a(n+1)=b(n),(①)
                b(n+1)=a(n)+b(n),(②);
                =>a(n+1),b(n+1)=b(n),a(n)+b(n)==>Python中表示为:a,b=b,a+b即可,于是写下: """
                a, b = b, a + b
                
                """ a1=b0=1,a2=b1=2,a3=b2=3,...
                    b1=a0+b0=2,b2=a1+b1=3,..."""
                """a(n)和b(n)分别服从斐波那契数列,a(n+1)=a(n)+a(n-1);或者:联立式1,2,得到: b(n+2)-b(n+1)=a(n+1)=b(n),即b(n+2)=b(n+1)+b(n),a(n)同理 """
                """ b_i=1,2,3,5,... (i=0,1,2,..)"""
            return L
            """ 试探f=Fib();f[3:5]=[f(3),f(4)]=[] """
    
""" 通过索引让某些对象(计算)数据,类似可迭代(具有getitem()方法的)对象方法的隐式调用 """
print(Fib()[3:7])#测试切片[3:7]
# for n in Fib():
#     print(n)

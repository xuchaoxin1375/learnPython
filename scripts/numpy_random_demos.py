import numpy as np
rng = np.random.default_rng()
# x=np.array([13,11,12])
# a = np.arange(16).reshape(4,4)
#rng:random generator
# Construct a new Generator with the default BitGenerator (PCG64).
print(rng.random())
print(type(rng),type(rng.random()))
print(rng.random(size=(4,4)))
##
print(rng.random((5,)))
print(rng.random((5,1)))
print(rng.random((5,2)))
print(rng.random((5,2,3)))
##
c=rng.random(size=(4,4))
# 保留三位小数(可以确保打印的时候每个元素的小数位数不超过3位)
d=c.round(3)
print(d)
##
# 一种可能的实现(存在精度表示问题,仅作为一种理论上的方法)
p=c%0.001
# p=c%1e*3
d=c-p
print(d)
#两种方式在打印的时候都不打印结尾的0串(如果有的话)
##
import numpy as np
rng = np.random.default_rng()
##
m,n=4,5
c = rng.random(size=(m,n))
d=c.round(3)
for i in d:
    # print(i)
    for j in i:
        print(j,end="\t")
    print()
print("translating...","-"*10)
l=len(d)
for i in range(n):
    # print(i)
    for j in range(m):
        print(d[j,i],end="\t")
    print()
##
import numpy as np
rng = np.random.default_rng()
m,l,n=3,4,5
m,l,n=3,1,4
A=rng.integers(1,10,size=(m,l))
B=rng.integers(1,10,size=(l,n))
#使用.dot()方法计算矩阵乘法(内积)
C=A.dot(B)
# 对于二维数组（矩阵）还可以用下列方式计算
# np.matmul(A,B)
# A@B
A,B,C
##
for i in range(m):
    for j in range(n):
        c_ij=0
        for k in range(l):
            # for p in range()
            c_ij+=A[i,k]*B[k,j]
        print("%s\t"%c_ij,end=" ")
    print()
##
for i in range(m):
    for j in range(n):
        c_ij=A[i]*B[:,j]
        print("%s\t"%c_ij[0],end=" ")
        # print("%s\t"%c_ij,end=" ")
    print()
        
##
m,n=3,4
a=rng.random((m,)).round(1)
b=rng.random((m,)).round(1)
c=a.dot(b)
s=0
for i in range(m):
    s+=a[i]*b[i]
a,b,c,s
## 
a2=(rng.random((m,n))*10).round(1)
b2=(rng.random((m,n))*10).round(1)
c2=a*b
s2=0
for i in range(m):
    s+=a[i]*b[i]
a2,b2,c2,s2

##
x1 = np.arange(9.0).reshape((3, 3))
x2 = np.arange(3.0)
x3=np.array([x2,x2,x2])
x1, x2, np.multiply(x1, x2),np.multiply(x1, x3)
##
y1=(10*rng.random((3,4))).round(1)
y2=(10*rng.random(4,)).round(1)
y1,y2,np.multiply(y1, y2)
##np.multiply可以用*号简写
print("x1*x2=\n%s,\ny1*y2=\n%s"%(x1*x2,y1*y2))
##
def get_random_int_mat(l,c):
    rng=np.random.default_rng()
    return rng.integers(1,9,size=(l,c))
##
y1=(10*rng.random((4,6))).round(0)
y2=(10*rng.random((1,1))).round(0)
y1,y2,y1*y2
##
a = np.array([1.0, 2.0, 3.0])
b = np.array([2.0, 2.0, 2.0])
s1=a * b
p = np.array([1.0, 2.0, 3.0])
q = 2.0
s2=p*q
s1,s2

##
import numpy as np
rng = np.random.default_rng()
m=3
n=4
A=rng.integers(1,9,size=(m,1))
B=rng.integers(1,9,size=(1,n))
print("%s@A;\n%s@B;\n%s@A*B;\n"%(A,B,A*B))
##
# matrix broadcasting (m,1)&(1,n)->(m,n)
Amn=np.array([[A[l][0] for c in range(n)] for l in range(m)])
Bmn=np.array([[B[0][c] for c in range(n)] for l in range(m)])
# Bmn=np.array([B[0] for i in range(m)])
print("%s@Amn\n%s@Bmn\n%s@Amn*Bmn\n"%(Amn,Bmn,Amn*Bmn))
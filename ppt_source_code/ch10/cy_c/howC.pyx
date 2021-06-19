
#howC.pyx
cdef extern from "stdio.h":  
    int printf(const char *template, ...)
    int scanf(const char *template, ...)
# from libc.stdio cimport printf, scanf
# 因为函数原型声明已经定义好,见：
# https://github.com/cython/cython/tree/master/Cython/Includes
from libc.stdlib cimport atoi
from libc.math cimport sin
        
cdef struct AB:
    int a
    int b
cpdef myC():
    cdef int A[100],i,n
    cdef int *pn=&n
    cdef AB ab
    
    n,ab.a,ab.b=123,2,3
    printf("%d\n",pn[0])
    for i in range(100):
        A[i]=i**2
    scanf("%d",&n)
    printf("sum:%d\n",A[n]+ab.a+ab.b)
    
    n=atoi("45")
    printf("sin(%d)=%.4f",n,sin(n))
    

        
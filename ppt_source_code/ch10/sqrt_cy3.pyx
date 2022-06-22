
#sqrt_cy3.pyx
cdef extern from "math.h":  
    double sqrt(double x)  

cdef double _fsq(int n):
    cdef int i
    cdef double x
    for i in range(n):
        x = sqrt(i)
cpdef fsq(int n):
    return _fsq(n)
    
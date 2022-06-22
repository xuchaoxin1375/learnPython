#sqrt_cy2.pyx
import math
cdef double _fsq(int n):
    cdef int i
    cdef double x
    for i in range(n):
        x = math.sqrt(i)
cpdef fsq(int n):
    return _fsq(n)

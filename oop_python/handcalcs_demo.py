##
import handcalcs.render
from math import pi,sqrt

%%render
a = 2
b = 3
c = 2*a + b/3
x= -b+sqrt( b**2 +4*a*c )/(2*a)
%%tex
a = 2
b = 3
c = 2*a + b/3
x= -b+sqrt( b**2 +4*a*c )/(2*a)
##

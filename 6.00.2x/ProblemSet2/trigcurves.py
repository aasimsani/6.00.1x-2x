import pylab
from math import *

pi = 4*atan(1.0)

twopi = pi*2

x = []
siny = []
cosy = []
for i in range(0,360):
	x.append((float(i)/360.00)*twopi)


for i in x:
	siny.append(sin(i))
	cosy.append(cos(i))

pylab.plot(x,siny)
pylab.plot(x,cosy)


pylab.show()
﻿#-*- coding:uft-8 -*-

from numpy import *

v=3.14



def f(x,y):
    return 10*x+y
b = fromfunction(f,(5,4),dtype=int)

#????
b.ndim
b.itemsize

#??????×÷
c1=arange(20).reshape(4,5)
print(c1)
print(c1[:,1])

#Shape Manipulation
c1.ravel()#??±?????c±??í??????±??????í??·???????
def method_name():
    a=floor(10*random.random((2,2)))
    return a

a = method_name()
print(a)




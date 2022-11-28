import numpy as np
import matplotlib.pyplot as plt
from polynomials import Polynomial
from differential_equations import ODE
from functions import Function
import pandas as pd
from arrays import Vector

a = ODE([lambda x,y,z: x, lambda x,y,z: x])
y = a.nystrom(y0=[1,0],graphic=False,n=200)
print(y.head())
x = a.euler2(y0=[1,0],graphic=False,n=200)
print(x.head())
x1 = a.euler(y0=[1,0],graphic=False,n=200)
print(x1.head())
x2 = a.heun(y0=[1,0],graphic=False,n=200)
print(x2.head())
x3 = a.rk4(y0=[1,0],graphic=False,n=200)
print(x3.head())
# a = Function(lambda x,y: x**y)
# b = Function(lambda x,y: x-y)
# c = Function(lambda x,y: x/y)
# d = Vector([a,b,c])
# print(type(d([1,2,3],[1,2,3])))
import numpy as np
import matplotlib.pyplot as plt
from polynomials import Polynomial
from differential_equations import ODE
from functions import Function
import pandas as pd
from arrays import Vector

# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1)

# b=lambda x,y,z: x*y*z
# c = lambda x,y,z: x-y+z
# d = np.array([1,2])

a = ODE([lambda x,y,z: x, lambda x,y,z: x])
# print(a.functions)
# print(type(*d))
# print(a.functions(1,*d))
y = a.euler(y0=[1,0],n=200)
x = np.arange(0,1,1/200)
xl = plt.xlabel('x')
yl = plt.ylabel('y')
la = plt.plot(x, y[0], 'r', label='y')
lb = plt.plot(x, y[1], 'b', label='z', linestyle='dotted')
ll=plt.legend(loc = 'upper right')
plt.show()

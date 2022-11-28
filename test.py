import numpy as np
from polynomials import Polynomial
from differential_equations import ODE
from functions import Function
import pandas as pd
from arrays import Vector

# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1)
# ax.spines['left'].set_position('center')
# ax.spines['bottom'].set_position('zero')
# ax.spines['right'].set_color('none')
# ax.spines['top'].set_color('none')
# ax.xaxis.set_ticks_position('bottom')
# ax.yaxis.set_ticks_position('left')

b=lambda x,y,z: x*y*z
c = lambda x,y,z: x-y+z
d = np.array([1,2])

a = ODE([lambda x,y,z: x*y*z, lambda x,y,z: x-y+z])
print(a.functions)
print(type(*d))
# print(a.functions(1,*d))
# a.euler(y0=[0,0],n=5)

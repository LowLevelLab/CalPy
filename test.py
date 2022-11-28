import numpy as np
from polynomials import Polynomial
from differential_equations import ODE
from functions import Function
import pandas as pd

# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1)
# ax.spines['left'].set_position('center')
# ax.spines['bottom'].set_position('zero')
# ax.spines['right'].set_color('none')
# ax.spines['top'].set_color('none')
# ax.xaxis.set_ticks_position('bottom')
# ax.yaxis.set_ticks_position('left')
a = complex(1, 2)
b = complex(3, 4)
c = Polynomial([1,2,3,4])
print(c.derivative(1),c.derivative(2))

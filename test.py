import numpy as np
from polynomials import Polynomial
from differential_equations import ODE

# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1)
# ax.spines['left'].set_position('center')
# ax.spines['bottom'].set_position('zero')
# ax.spines['right'].set_color('none')
# ax.spines['top'].set_color('none')
# ax.xaxis.set_ticks_position('bottom')
# ax.yaxis.set_ticks_position('left')

import pandas

x = np.array([3.45])
y = np.array([1.21,1])
print(Polynomial([-2,1]))
X = Polynomial(x)
X *= Polynomial(y)
print(X)
obj = ODE([lambda x,y: 1, lambda x,y: 2])
print(obj.euler(0,1,[0,0],5))

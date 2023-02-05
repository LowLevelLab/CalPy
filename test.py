from linalg.arrays import *
import numpy as np
import interpolation.regression as lin
from calculus.functions import Function
from poly.polynomials import Polynomial
from linalg.arrays import Vector
from calculus.differential_equations import ODE

# x = [0,1,2,3,4]
# y = [1,2,3/2,4/3,5/4]

# # reg = lin.Regression(x,y)
# # exp = reg('inv')
# # print(exp)

edo = ODE([lambda x,y,z: y,lambda x,y,z:z], [0,1])

sol = edo.euler2([1,1])
print(sol.cross_map(1,2,style='--'))
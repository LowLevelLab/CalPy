from linalg.arrays import *
import numpy as np
import interpolation.regression as lin
from calculus.functions import Function
from poly.polynomials import Polynomial
from linalg.arrays import Vector
from calculus.differential_equations import ODE
from numpy import linspace

# a = Matrix([[1,0,0],[1,1,0],[1,1,1]])

# print(a.validate_ss())

x = [1,2,3,4,5]
y = [1/1,1/2,1/3,1/4,1/5]

reg = lin.Regression(x,y)
exp = reg('opt')
print(exp)
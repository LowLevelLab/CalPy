import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from polynomials import Polynomial
from differential_equations import ODE
from functions import Function
from arrays import Vector
from lin_regression import *


# a = Function(lambda x, y, z: y+z)
# b = Function(lambda x, y, z: z+y)
c = Regression([1,2,3,4], [np.e,np.exp(2),np.exp(3),np.exp(4)])
exp = c('exp')
print(exp)


# sol = ODE([a,b], [0,10])
# table1 = sol.nystrom([2,-1], graphic=True)


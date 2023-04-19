from linalg.arrays import Array
from calculus.ode import ODE
# import numpy as np
# import interpolation.regression as lin
# from calculus.functions import Function
# from poly.polynomials import Polynomial
# from linalg.arrays import Vector, Matrix
# from discrete.boolArr import BoolMatrix
# from discrete.relation import Relation
# from time import time


a = ODE([lambda x, y: y], [0,2])
a.rk4([1],graphic=True)

# a = Matrix(np.array([[1,2,3],[4,5,6],[7,8,9]]))
# print(a[1,0:])
# np.any()

# print(Relation.prob_transitive(4))


# a = np.array([[1,2],[4,5]])
# b = np.array([[1,4],[4,5]])
# c = a==b
# print(c)
# c = c*c
# print(c)
# d = np.array(c, dtype = int)
# print(d)

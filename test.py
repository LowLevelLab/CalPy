from calculus.functions import Function
from poly.polynomials import Polynomial
import numpy as np


# a = Matrix([[1,2],[3,4]])
# print(a.determinant())
# b = Polynomial([1,2,3,4])
# print(b)
# print(32+12+4+1)
# c =b.to_function()
# print(c(2))
aux = lambda x: np.sin(x)
a, b = Function(aux), Function(aux)
print(a(1)-b(1))
print(a)
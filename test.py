from linalg.arrays import *
import numpy as np
import interpolation.lin_regression as lin
from calculus.functions import Function


# a = [1,2,3,4,5,6]
# print(min(a))

# # f = Function(lambda x: x**2)

# # print(f([1,2,3,4]))

pontos_x = [1,2,3,4]
pontos_y = [2,4,8,16]
reg = lin.Regression(pontos_x,pontos_y)

opt = reg('opt')
print(type(opt))



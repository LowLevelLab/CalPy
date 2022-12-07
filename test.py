from functions import Function
import numpy as np
from scipy.special import factorial
from scipy.misc import derivative
import constants as c
from complex import Quaternion
from arrays import Matrix

# a = Function(lambda x: np.sin(x))
# c = a.taylor_series(7,0, 5)
# print(c)


a = Matrix([[1,2],[3,4]])
a.append([5,6], axis=1)
print(a)


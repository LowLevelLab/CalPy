from functions import Function
import numpy as np
from scipy.special import factorial
from scipy.misc import derivative
import constants as c

a = Function(lambda x: np.sin(x))
c = a.taylor_series(7,0, 5)
print(c)




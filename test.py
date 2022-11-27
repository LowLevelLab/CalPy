import numpy as np
from polynomials import Polynomial



x = np.array([3.45])
y = np.array([1.21,1])
print(Polynomial([-2,1]))
X = Polynomial(x)
X *= Polynomial(y)
print(X)


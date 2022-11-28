import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from polynomials import Polynomial
from differential_equations import ODE
from functions import Function
from arrays import Vector


al = np.array([1.00004,2.00004,34.00004])
al = al.round(3)
print(al)

a = lambda x, y, z: y**2 - 2*y*z
b = lambda x, y, z: x*y+y**2*np.sin(z)

sol = ODE([a,b], [0,0.4])
table1 = sol.euler([1,-1])
table2 = sol.nystrom([1,-1])
t = table1.index.get_indexer([0.0016])
print(table1.y1[0.0024])
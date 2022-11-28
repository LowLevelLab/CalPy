import numpy as np
import matplotlib.pyplot as plt
from polynomials import Polynomial
from differential_equations import ODE
from functions import Function
import pandas as pd
from arrays import Vector

a = ODE([lambda x,y,z: x, lambda x,y,z: x])
y = a.euler2(y0=[1,0],graphic=True,n=200)
print(y)


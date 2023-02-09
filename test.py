from linalg.arrays import *
import numpy as np
import interpolation.regression as lin
from calculus.functions import Function
from poly.polynomials import Polynomial
from linalg.arrays import Vector, Matrix
from discrete.boolArr import BoolMatrix


a = BoolMatrix(Matrix([[1,1,1,1],[0,1,0,1],[0,0,1,0],[0,0,0,1]]))
print(a.compare_transitive())


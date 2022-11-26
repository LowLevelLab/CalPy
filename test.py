import numpy as np

g1 = lambda x: x
g2 = lambda x: 2*x

g3 = lambda x: g1*g2

print(g3(3))

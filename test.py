import numpy as np

g1 = lambda x: x
g2 = lambda x: x*2

print(type(g1))
g1 = [g1]
print(g1[0](1))
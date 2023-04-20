
import numpy as np
from discrete.relation import prob_transitives

# a = ODE([lambda x, y: y], [0,2])
# a.rk4([1],graphic=True)

# a = Matrix(np.array([[1,2,3],[4,5,6],[7,8,9]]))
# print(a[1,0:])
# np.any()


print(prob_transitives(5))




# import numpy as np


# class Array:
#     def __init__(self, lista):
#         self.array = np.array(lista)

#     def __len__(self):
#         return len(self.array)
    
#     def __getitem__(self, index):
#         return self.array[index]
#     def __setitem__(self, index, value):
#         self.array[index] = value
    
#     def __call__(self, *args) :
#         aux = np.zeros((len(self),len(self[0])))
#         for i in range(len(self)):
#             for j in range(len(self[0])):
#                 aux[i][j] = self[i][j](*args)
#         return np.linalg.det(aux)


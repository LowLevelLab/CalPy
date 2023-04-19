import numpy as np


# class ArrayCarteado:
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
#         return aux




# a = Array([[lambda x: x, lambda x: 2*x],[lambda x: 3*x, lambda x: 5*x]])
# b = Array([1,2,4,],dtype=np.float64)
# print(b)

# c = BoolArray([[1,2,3],[1,2,6],[2,6,7]])
# d = BoolArray([[3,0,0],[0,2,0],[2,0,7]])
# print(c&d.astype(np.int8))

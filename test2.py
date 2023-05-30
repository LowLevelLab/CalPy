
import subprocess


# a = typeof(np.array([1,2,3], dtype=np.bool_))
# print(a)

# @jitclass(a)
# class Test(np.ndarray):
#     def __new__(cls, input_array, *, dtype=np.bool_, shape=None, order=None):
#         obj = np.asarray(input_array)
#         if dtype is not None:
#             obj = obj.astype(dtype)
#         if shape is not None:
#             obj = obj.reshape(shape)
#         if order is not None:
#             obj = obj.copy(order=order)
#         return obj.view(cls)
#     1 0 
#     1 1
#     - -
# 1 0|1 0
# 1 1|2 1
# t = Test([1,2,3,4])
# print(t)


# a = Array([[lambda x: x, lambda x: 2*x],[lambda x: 3*x, lambda x: 5*x]])
# b = Array([1,2,4,],dtype=np.float64)
# print(b)

# c = BoolArray([[1,2,3],[1,2,6],[2,6,7]])
# d = BoolArray([[3,0,0],[0,2,0],[2,0,7]])
# print(c&d.astype(np.int8))



# try:
#     output = subprocess.check_output(['./test'])
# except FileNotFoundError:
#     subprocess.run("gcc test.c -o test", shell=True)
#     output = subprocess.check_output(['./test'])

# print(output.decode('utf-8'))

# a = np.array([[True,False],[True,True]],dtype=np.bool_)
# print(a)


# import numpy as np
# from numba import jit, njit, typeof, cuda
# from numba.experimental import jitclass



# size = 5  # the size of the matrix
# indices = np.indices((size, size), dtype=int)  # create a 2D array of row and column indices
# matrices = np.bitwise_and(indices[0], indices[1]).astype(bool)  # generate all possible boolean combinations of the indices

# print(matrices)

# print(matrices.size)


from calculus.ode import ODE

ODE([lambda x, y, z: y, lambda x, y, z: z], [0,1]).rk4([1,1], graphic=True)

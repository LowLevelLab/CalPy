import numpy as np
# from imports import *
# from complex import Complex

class Array(np.ndarray):
    def __new__(cls, input_array, *, dtype=None, shape=None, order=None):
        obj = np.asarray(input_array)
        if dtype is not None:
            obj = obj.astype(dtype)
        if shape is not None:
            obj = obj.reshape(shape)
        if order is not None:
            obj = obj.copy(order=order)
        return obj.view(cls)
    
    # def __array_finalize__(self, obj: None | NDArray[Any], /) -> None:
    #     if obj is None:
    #         return
    
    # def __mul__(self, other):
    #     pass

    # def __rmul__(self, other):
    #     pass

    # def __imul__(self, other):
    #     pass
    
    def __call__(self, *args, **kwargs):
        values = [f(*args, **kwargs) for f in self.flat]
        return Array(values).reshape(self.shape)

    def det(self) -> float:
        return np.linalg.det(self.array)
    
    def find_row(self, row: list) -> int:
        for i, element in enumerate(self):
            if all(row[j]==element[j] for j in range(len(row))):
                return i 
        return -1

    def find_column(self, column:list) -> int:
        aux = self.transpose()
        return aux.find_row(column)

    def invert(self): 
        return np.linalg.inv(self)

    def to_frame(self):
        import pandas as pd
        return pd.DataFrame(data=self.array)

    # def append(self,*args: tuple[list | np.ndarray | Array], axis: str | int = 0) -> None:
    #     if axis == 0 or axis =='below':
    #         final = self._below_append(*args)
    #     elif axis == 1 or axis =='right':
    #         final = self._right_append(*args)
    #     else:
    #         raise ValueError
    #     return final

    # def _below_append(self,*args: tuple[list | np.ndarray | Array]):
    #     for element in args:
    #         if not isinstance(element, Union[Vector,list,np.ndarray]):
    #             raise TypeError(f"Invalid type: {type(element)}")
    #         elif len(element) != len(self[0]):
    #             raise DimensionError
    #     original_size = len(self)
    #     final_size = len(self.array) + len(args)
    #     self.array.resize((final_size,len(self[0])))
    #     for i, element in enumerate(args):
    #         self.array[original_size+i] = np.array(element)

    # def _right_append(self,*args: tuple[list | np.ndarray | Array]):
    #     aux = self.transpose().copy()
    #     aux.append(*args)
    #     self.array = aux.array.transpose()



    # """
    # ###LINEAR SYSTEM###
    # """


    # def validate_b(self,b):
    #     if len(b) != self.cols:
    #         raise DimensionError(dim1=self.cols,dim2=len(b))
    #     if isinstance(b, Union[list,np.ndarray,tuple]):
    #         b = Vector(b)
    #     elif not isinstance(b, Vector):
    #         raise TypeError
    #     return b
        
    
    # def validate_gj(self):
    #     for i in range(len(self)):
    #         if sum([abs(aux) for aux in self[i]])/abs(self[i][i])-1 >= 1:
    #             return False
    #     return True

    # def gauss_jacobi(self, b):
    #     if not self.validate_gj():
    #         raise InvalidMethodError(message='gauss-jacobi is an invalid method for this matrix')
        

    # def validate_gs(self):
    #     def beta(i: int):
    #         pass
    #     def term(i):
    #         return abs((abs(sum(beta(j) for j in range(i)))+abs(sum(self[i][j] for j in range(i+1,len(self[i])))))/self[i][i])
    #     for i in range(len(self)):
    #         if term(i) >=1:
    #             return False
    #     return True

    # def gauss_seidel(self, b):
    #     if not self.validate_gs():
    #         raise InvalidMethodError(message='gauss-seidel is an invalid method for this matrix')

    # def validate_ss(self):
    #     for i in range(self.rows):
    #         if not (self[i,:i+1] == Vector(np.zeros(self.cols-i)) and self[i,:i+1] == Vector(np.zeros(self.cols-i, dtype=int))):
    #             return False
    #     return True
    #     # triangular inferior

    # def successive_subs(self, b):
    #     if not self.validate_ss():
    #         raise InvalidMethodError(message='given matrix is not lower triangular')
    #     b = self.validate_b(b)
    #     n = len(b)
    #     x = Vector(np.zeros(n))
    #     for i in range(n):
    #         x[i] = (b[i] -self[i,:i]*x[:i])/self[i,i]
    #     return x


    # def validate_rs(self):
    #     for i in range(self.rows):
    #         if not (self[i,i+1:] == Vector(np.zeros(i)) and self[i,i+1:] == Vector(np.zeros(i, dtype=int))):
    #             return False
    #     return True 
    #     # triangular superior

    # def retroactive_subs(self, b):
    #     if not self.validate_rs():
    #         raise InvalidMethodError(message='given matrix is not upper triangular')
    #     b = self.validate_b(b)
    #     n = len(b)
    #     x = Vector(np.zeros(n))
    #     for i in reversed(range(n)):
    #         x[i] = (b[i] - self[i, i+1:]*x[i+1:])/self[i, i]
    #     return x


    # def gauss_eng(self):
    #     pass

    # def gauss_bigo(self):
    #     pass

    # def gauss_elimination(self, pivot=False):
    #     pass

    # def linear_conjugate_gradient(self): # lcg
    #     pass

    # def LU_decomposition(self):
    #     pass

    # def LU_solution(self):
    #     pass

    # def LDU(self):
    #     pass

    # def choleski(self):
    #     pass

    # def solution_choleski(self):
    #     pass

    # def non_linear_newton(self):
    #     pass

    # def newton_modified(self):
    #     pass


    # """
    # ### AUTOVALORES ###
    # """


    # def leverrier(self):
    #     pass

    # def eigenvector(self):
    #     pass

    # def LR_decomposition(self):
    #     n = self.array.shape[0]
    #     r = np.copy(self.array)
    #     l = np.identity(n) 
    #     rt = r.transpose()

    #     for j in range(n-1):
    #         for i in range(j+1,n):
    #             m = r[i, j]/r[j, j]
    #             r[i, j:] -= m * r[j, j:]
    #             l[i, j] = m
    #     return l, r

    # def LR_method(self, iter=c.ITERATIONS):        
    #     Ak = np.copy(self.array)
    #     for k in range(iter):
    #         L, R = self.LR_decomposition(Ak)
    #         Ak = R@L
    #     eigenvalues = np.diag(Ak)
    #     return eigenvalues

    # def householder(self):
    #     pass

    # def QR_method(self):
    #     pass

    # def QR_eigenvalues(self):
    #     pass


    pass





class BoolArray(Array):
    def __new__(cls, input_array):
        return super().__new__(cls, input_array, dtype=np.bool_)
    
    # def __str__(self) -> str:
    #     return super().__str__()



a = Array([[1,2],[3,4]])
b = np.linalg.inv(a)

print(type(b))
import numpy as np
from error_types import DimensionError
from typing import Union
import pandas as pd


class Array:
    def __init__(self, arg: Union[list,np.ndarray]) -> None:
        self.array = np.array(arg)

    def __len__(self):
        return len(self.array)

    def __contains__(self, item):
        if item in self.array:
            return True
        return False

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < len(self.array):
            result = self.array[self.n]
            self.n += 1
            return result
        else:
            raise StopIteration

    def __eq__(self, other):
        if isinstance(self,Matrix) and isinstance(other,Matrix):
            for i,v in enumerate(self.array):
                if not all((v == other[i]).tolist()):
                    return False
            return True
        elif isinstance(self,Vector) and isinstance(other,Vector):
            for i,v in enumerate(self.array):
                if not (v == other[i]).tolist():
                    return False
            return True
        else:
            return False
    
    def __add__(self, other):
        if isinstance(other, Union[list,np.ndarray]):
            if isinstance(self, Vector):
                return Vector(self.array + np.array(other))
            else:
                return Matrix(self.array + np.array(other))
        if isinstance(other, Union[Vector, Array, Matrix]):
            if isinstance(self, Vector):
                return Vector(self.array + other.array)
            else:
                return Matrix(self.array + other.array)

    def __sub__(self, other):
        if isinstance(other, Union[list,np.ndarray]):
            if isinstance(self, Vector):
                return Vector(self.array - np.array(other))
            else:
                return Matrix(self.array - np.array(other))
        if isinstance(other, Union[Vector, Array, Matrix]):
            if isinstance(self, Vector):
                return Vector(self.array - other.array)
            else:
                return Matrix(self.array - other.array)

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self,other):
        return self.__add__(other)

    def __rsub__(self, other):
        aux = self.__sub__(other)
        aux.array = - aux.array
        return aux

    def __isub__(self,other):
        return self.__sub__(other)
        
    def __rmul__(self, other):
        pass

    def __getitem__(self, item):
        return self.array[item]

    def __setitem__(self, key, value):
        self.array[key] = value

    def __str__(self) -> str:
        return str(self.array)
# MODIFY __str__ : DATAFRAME


class Matrix(Array):

    """
    ### PROPERTIES ###
    """


    def __init__(self, arg: list) -> None:
        super().__init__(arg)

    def __mul__(self, other):
        if isinstance(other, Union[float,int]):
            return Matrix(self.array * other)
        if isinstance(other, Matrix):
            return self._matrix_multiplication(other)
        if isinstance(other, Vector):
            return self._linear_system(other)
        else:
            raise TypeError
    

    """
    ### BASIC METHODS ###
    """


    def _matrix_multiplication(self, other):
        return Matrix(self.array @ other.array)

    def _linear_system(self, other):
        return Vector(self.array @ other.array)

    def is_a_square_matrix(self):
        pass

    def determinant(self):
        self.is_square_matrix()
        row_number = len(self.array)
        for i in range(row_number):
            if self[i][i] != 0:
                pivot = self[i][i]
            else:
                for j in range(i + 1, row_number):
                    if self != 0:
                        ans = self[i]
                        self[i] = -self[j]
                        self[j] = ans
                        pivot = self[i][i]
                        break

            for j in range(i + 1, row_number):
                if self[j][i] == 1:
                    continue
                else:
                    self[j] = self[j] * pivot - self[j][i] * self[i]

        return self.array[row_number - 1][row_number - 1]

    def find_row(self, row: list):
        if len(self[0]) != len(row):
            raise DimensionError('incompatible dimensions')
        for i in range(len(self)):
            if self[i] == row:
                return i
        raise Exception('line not found')

    def findColumn(self):
        pass

    def transpose(self):
        return Matrix(self.array.transpose())

    def invert(self): 
        pass

    def append(self,vector):
        pass

    def to_list(self) -> list:
        pass

    def to_frame(self) -> pd.core.frame.Dataframe:
        pass

    def to_nparray(self) -> np.ndarray:
        return self.array


    """
    ###LINEAR SYSTEM###
    """


    def validate_gj(self):
        for i in range(len(self)):
            if sum([abs(aux) for aux in self[i]])/abs(self[i][i])-1 >= 1:
                return False
        return True

    def gauss_jacobi(self, b):
        pass

    def validate_gs(self):
        pass

    def gauss_seidel(self, b):
        pass

    def successive_subs(self):
        pass

    def retroactive_subs(self):
        pass

    def gauss_eng(self):
        pass

    def gauss_bigo(self):
        pass

    def gauss_elimination(self, pivot=False):
        pass

    def linear_conjugate_gradient(self):
        pass

    def LU_decomposition(self):
        pass

    def LU_solution(self):
        pass

    def LDU(self):
        pass

    def choleski(self):
        pass

    def solution_choleski(self):
        pass

    def tridiagonal(self):
        pass

    def pentadiagonal(self):
        pass

    def non_linear_newton(self):
        pass

    def newton_modified(self):
        pass


    """
    ### AUTOVALORES ###
    """


    def leverrier(self):
        pass

    def eigenvector(self):
        pass

    def LR_decomposition(self):
        pass

    def LR_method(self):
        pass

    def householder(self):
        pass

    def QR_method(self):
        pass

    def QR_eigenvalues(self):
        pass


    pass


class Vector(Array):
    def __init__(self, arg: list) -> None:
        super().__init__(arg)

    def __mul__(self, other):
        if isinstance(other, Union[float,int]):
            return Vector(self.array * other)
        elif isinstance(other, Matrix):
            return self._transpose_linear_system(other)
        elif isinstance(other, Vector):
            return self._dot_product(other)
        else:
            pass
        pass

    def _transpose_linear_system(self, other):
        return Vector((other.array.transpose()@self.array.transpose()).transpose())

    def _dot_product(self, other):
        return Vector(np.dot(self, other))

    def append(self, *args) -> None:
        original_size = len(self)
        final_size = len(self.array) + len(args)
        self.array.resize(final_size, refcheck=False)
        for i in range(len(args)):
            self.array[original_size+i] = args[i]

    def to_list(self) -> list:
        return list(self)

    def to_nparray(self) -> np.ndarray:
        return self.array


    pass

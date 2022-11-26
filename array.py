import numpy as np

class Array:
    def __init__(self, arg: list) -> None:
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

    # def __eq__(self, other):
    #     Array.dimension_comparison(self, other)
    #     for i in range(len(self.array)):
    #         if self.array[i] != other[i]:
    #             return False
    #     return True
    
    def __add__(self, other):
        if type(other) is list or type(other) is np.ndarray:
            aux_other = Array(other)
        if type(other) is Array:
            aux_other = other
        return self.array + aux_other.array

    def __sub__(self, other):
        if type(other) is list or type(other) is np.ndarray:
            aux_other = Array(other)
        if type(other) is Array:
            aux_other = other
        return self.array - aux_other.array

    def __radd__(self, other):
        return self.__add__(other)

    def __rsub__(self, other):
        return -self.__sub__(other)

    def __mul__(self, other):
        if type(other) == float or type(other) == int:
            return self.array * other
        else:
            pass
        #     try:
        #         for i in range(len(self)):
        #             vector.append([])
        #             for j in range(len(self[i])):
        #                 vector[i].append(other*self[i][j])
        #         return vector
        #     except TypeError:
        #         for element in self:
        #             vector.append(other * element)
        #         return vector
        # elif type(other) == Array or type(other) == list:
        #     other = Array(other)
        #     return Array.array_multiplication(self, other)

    def __rmul__(self, other):
        pass

    def __getitem__(self, item):
        return self.array[item]

    def __setitem__(self, key, value):
        self.array[key] = value

    def __str__(self) -> str:
        return str(self.array)



class Matrix(Array):

    def __init__(self, arg: list) -> None:
        super().__init__(arg)

    def __mul__(self, other):
        if type(other) is float or type(other) is int:
            return self.array * other
        if type(other) is Matrix:
            return self.matrix_multiplication(other)
        elif type(other) is Vector:
            return self.linear_system(other)
        else:
            raise TypeError
        pass
    

    def matrix_multiplication(self, other):
        return self.array @ other.array

    def linear_system(self, other):
        return self.array @ other.array

    def validate_gj(self):
        pass

    def validate_gs(self):
        pass



    def gauss_jacobi(self, b):
        pass

    def gauss_seidel(self, b):
        pass


    def determinant(self):
        pass

    def findRow(self):
        pass

    def findColumn(self):
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


    

    
        

    ### AUTOVALORES ###

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
        if type(other) is float or type(other) is int:
            return self.array * other
        if type(other) is Matrix:
            return self.transpose_linear_system(other)
        elif type(other) is Vector:
            return self.dot_product(other)
        else:
            pass
        pass

    def transpose_linear_system(self, other):
        return (other.array.transpose()@self.array.transpose()).transpose()

    def dot_product(self, other):
        return np.dot(self, other)

    
# """Union(int, float)"""
    def append(self, *args) -> None:
        original_size = len(self)
        final_size = len(self.array) + len(args)
        self.array.resize(final_size, refcheck=False)
        for i in range(len(args)):
            self.array[original_size+i] = args[i]

    pass


obj1 = np.array([1,2])
obj2 = np.array([[2,3],[4,5]])
print(len(obj1))
obj = Vector(obj1)
obj_ = Matrix(obj2)
print(obj_*obj)

for i in obj:
    print(i)

# print(obj - obj2)





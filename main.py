import numpy as np
import constants as c
from error_types import DimensionError

"""
FUNÇÕES A SER ADICIONADAS:
- TRIGONOMETRICAS E INVERSAS
- EXPONENCIAIS E INVERSAS
- 
"""


class Array:
    def __init__(self, array: list):
        self.array = array
        self.max = len(array)
        self.list = list(self.array)

    def __len__(self):
        return self.max

    def __contains__(self, item):
        if item in self.array:
            return True
        return False

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < self.max:
            result = self.array[self.n]
            self.n += 1
            return result
        else:
            raise StopIteration

    def __eq__(self, other):
        Array.dimension_comparison(self, other)
        for i in range(len(self.array)):
            if self.array[i] != other[i]:
                return False
        return True

    def __getitem__(self, item):
        return self.array[item]

    def __setitem__(self, key, value):
        self.array[key] = value

    def __add__(self, other):
        Array.dimension_comparison(self, other)
        addition = Array([])
        if type(self[0]) == list:  # Array.dimension_comparison(self, other)
            for i in range(len(self)):
                addition.append([])
                for j in range(len(self[i])):
                    addition[i].append(self[i][j] + other[i][j])
            return addition
        for i in range(len(self)):
            addition.append(self[i] + other[i])
            print(addition[i])
        return addition

    def __sub__(self, other):
        Array.dimension_comparison(self, other)
        subtraction = Array([])
        if Array.dimension_comparison(self, other):
            for i in range(len(self)):
                subtraction.append([])
                for j in range(len(self[i])):
                    subtraction[i].append(self[i][j] - other[i][j])
            return subtraction
        for i in range(len(self)):
            subtraction.append(self[i] - other[i])
            print(subtraction[i])
        return subtraction

    def __rmul__(self, other):
        if type(other) == float or type(other) == int:
            vector = Array([])
            try:
                len(self[0])
                for i in range(len(self)):
                    vector.append([])
                    for j in range(len(self[i])):
                        vector[i].append(other * self[i][j])
                return vector
            except TypeError:
                for element in self:
                    vector.append(other * element)
                return vector

    def __radd__(self, other):
        return self.__add__(other)

    def __rsub__(self, other):
        return self.__sub__(other)

    def __mul__(self, other):
        if type(other) == float or type(other) == int:
            vector = Array([])
            try:
                for i in range(len(self)):
                    vector.append([])
                    for j in range(len(self[i])):
                        vector[i].append(other*self[i][j])
                return vector
            except TypeError:
                for element in self:
                    vector.append(other * element)
                return vector
        elif type(other) == Array or type(other) == list:
            other = Array(other)
            return Array.array_multiplication(self, other)
        else:
            raise Exception(f'Invalid object types: {type(self)} and {type(other)}')

    def __divmod__(self, other):
        self.validation_inverse_matrix()
        self.invert_matrix()

    def __str__(self):
        # breakpoint()
        try:
            len(self[0])
            i = 0
            string = '['
            while True:
                try:
                    string += self[i].__str__()+','
                    i+=1
                except IndexError:
                    string = string.rstrip(',')
                    string+= ']'
                    break
            return string
        except TypeError:
            return str(list(self.array))

    def array_multiplication(self, array2):
        kind = 0
        try:
            len(self[0])
        except TypeError:
            kind -= 2
        try:
            len(array2[0])
        except TypeError:
            kind += 1
        if kind == -1:
            return Array.dot_product(self, array2)
        elif kind == 0:
            return Array.matrix_multiplication(self, array2)
        else:
            return Array.linear_system_multiplication(self, array2)

    def dot_product(self, array2):
        if not Array.dimension_comparison(self, array2):
            raise DimensionError('dot product is not valid for '
                                 'given pair of vectors')
        term = 0
        for i in range(len(array2)):
            term += array2[i] * self[i]
        return term

    def dimension_comparison(self, array2):
        try:
            m1 = len(self[0])
        except TypeError:
            m1 = 1
        finally:
            n1 = len(self)

        try:
            m2 = len(array2[0])
        except TypeError:
            m2 = 1
        finally:
            n2 = len(array2)

        if n1 != n2 or m1 != m2:
            raise DimensionError('Dimensions are incompatible')
        return True

    def matrix_multiplication(self, array2):
        result = Array([])
        for i in range(len(self)):
            result.append(Array.constant_vector(len(array2[0]), 0))
        for i in range(len(self)):
            for j in range(len(array2[0])):
                for k in range(len(array2)):
                    result[i][j] += self[i][k] * array2[k][j]
        return result

    def linear_system_multiplication(self, array2):
        result = Array([])
        try:
            len(array2[0])
            for i in range(len(self)):
                addition = 0
                for j in range(len(array2[i])):
                    addition += array2[j][i] * self[j]
                result.append(addition)
            return result
        except TypeError:
            for i in range(len(self)):
                result.append(Array.dot_product(self[i], array2))
            return result

    def is_transpose_of_lin_syst(self, array2):
        try:
            len(array2[0])
            return False
        except TypeError:
            if len(array2) != len(self):
                return False
            return True

    def transpose(self):
        if not self.is_a_matrix():
            raise Exception
        new_array = [[self[j][i] for j in range(len(self[i]))]
                     for i in range(len(self))]
        return new_array

    def is_a_linear_system(self, b):
        try:
            if len(self[0]) != len(b):
                return False
        except TypeError:
            return False
        return True

    def is_a_matrix(self):
        try:
            for element in self:
                if len(self[0]) != len(element):
                    return False
        except TypeError:
            return False
        return True

    def is_square_matrix(self):
        self.is_a_matrix()
        for i in range(len(self)):
            if len(self) != len(self[i]):
                raise DimensionError('Object is not a square matrix')
        return True

    @staticmethod
    def cross_product(array1, array2):
        pass

    @staticmethod
    def constant_vector(length: int, constant: float = 0.):
        vector = []
        for i in range(length):
            vector.append(constant)
        return Array(vector)

    def invert_matrix(self):
        pass

    def validation_inverse_matrix(self):
        if self.determinant() == 0:
            raise DimensionError('given matrix is not invertible')
        return True

    def append(self, *args):
        list_object = list(self.array)
        list_object.append(*args)
        self.array = Array(list_object)

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

    def find_column(self, column: list):
        # if len(self) != len(column):
        #     raise Exception('incompatible dimensions')
        # for i in range(len(self)):
        #     if self.array[i][j] == vector[i]:
        # raise Exception('line not found')
        pass

    def retro_substitution(self, b):
        pass

    def successive_subs(self, b):
        # n = b_s.size
        # xs = np.zeros(n)
        # for i in range(n):
        #     xs[i] = (b_s[i] - L[i, :i] @ xs[:i]) / L[i, i]
        # return xs
        b = Array(b)
        xs = Array.constant_vector(len(b))
        for i in range((len(b))):
            xs[i] = (b[i] - Array(xs[0:i]) * Array(self[i][0:i]))/self[i][i]
        return xs

    def gauss_elimination(self, b):
        pass

    def lu_decomposition(self):
        pass

    def choleski(self):
        pass

    def choleski_solution(self, b):
        pass

    def solution_jacobi(self, b, x0, iterations: int = 2 * c.ITERATIONS // 10):
        pass

    def gauss_seidel_method(self, b, x0, iterations: int = 2 * c.ITERATIONS // 10):
        pass

    def non_linear_newton(self, b, iterations: int = 2 * c.ITERATIONS // 10, error: float = c.ERROR):
        pass


vetor3 = Array([1, 2, 3, 4])
vetor2 = Array([[1, 2], [0, 3]])
vetor = Array([[1, 2], [4, 3], [1, 5]])
# vetor5 = vetor2.successive_subs(vetor3)
# print(vetor5)
vetor4 = vetor2.transpose()
print(vetor4)
vetor6 = vetor * vetor2
print(vetor6)
print(vetor6[1:3])
print(3*vetor4)
lista = [[1,2],[3,4]]
print(2*lista)
print(vetor4)

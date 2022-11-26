import numpy as np

class Array:
    def __init__(self, arg: list) -> None:
        self.array = np.array(arg)
        self.max = len(arg)

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

    # def __eq__(self, other):
    #     Array.dimension_comparison(self, other)
    #     for i in range(len(self.array)):
    #         if self.array[i] != other[i]:
    #             return False
    #     return True
    
    def __add__(self, other):
        if type(other) == list or type(other) == np.ndarray:
            aux_other = Array(other)
        if type(other) == Array:
            aux_other = other
        return self.array + aux_other.array

    def __sub__(self, other):
        if type(other) == list or type(other) == np.ndarray:
            aux_other = Array(other)
        if type(other) == Array:
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
        super.__mul__(self,other)
        if other == isinstance(Matrix):
            self.matrix_multiplication(other)
        elif other == isinstance(Vector):
            self.linear_system(other)
        else:
            raise TypeError
        pass
    

    def matrix_multiplication(self, other):
        return self.array @ other.array

    def linear_system(self, other):
        pass


    pass


class Vector(Array):
    def __init__(self, arg: list) -> None:
        super().__init__(arg)

    def __mul__(self, other):
        super.__mul__(self,other)
        if other == isinstance(Matrix):
            self.transpose_linear_system(other)
        elif other == isinstance(Vector):
            self.dot_product(other)
        else:
            pass
        pass

    def transpose_linear_system(self, other):
        pass

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


obj1 = np.array([1,2,3])
obj2 = np.array([2,3,4,5, 6])
print(len(obj1))
obj = Array(obj1)
obj.append(1, 2)
print(obj)

print(obj - obj2)





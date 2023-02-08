from imports import *
import linalg.arrays as arr


class BoolMatrix:
    def __init__(self, array: arr.Matrix) -> None:
        self.__aux = arr.Matrix(array)
        self.__matrix = self.convert_type(arr.Matrix(array))
        self.__rows = array.rows
        self.__cols =  array.cols

    @property
    def aux(self):
        return self.__aux

    @property
    def matrix(self):
        return self.__matrix

    @property
    def rows(self):
        return self.__rows

    @property
    def cols(self):
        return self.__cols

    def convert_type(self, array):
        pass
        # aux = np.zeros((array.rows,array.cols), dtype=int)
        # for r in range(array.rows):
        #     for c in range(array.cols):
        #         # if 
                
    def __add__(self,other):
        return self or other

    def __mul__(self,other):
        aux = self.aux*other.aux
        return BoolMatrix(aux)

    def __pow__(self,index):
        if not isinstance(index,int):
            raise TypeError
        if index == 0:
            if len(self) == len(self[0]):
                return BoolMatrix(np.identity(len(self)))
            else:
                raise DimensionError()
        elif index == 1:
            return self
        return self*self.__pow__(index-1)

    def __eq__(self,other):
        if isinstance(self,BoolMatrix) and isinstance(other,BoolMatrix):
            for i,v in enumerate(self.aux):
                if not all((v == other[i]).tolist()):
                    return False
            return True

    def transpose(self):
        return BoolMatrix(self.aux.transpose())


    def compare_transitive(self,other):
        pass

    # and
    # or
    # xor

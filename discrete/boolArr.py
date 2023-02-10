from imports import *
import linalg.arrays as arr


class BoolMatrix:
    def __init__(self, array: Union[arr.Matrix,np.ndarray]) -> None:
        if len(array) != 0:
            self.__aux = arr.Matrix(array)
            self.__rows = array.rows
            self.__cols = array.cols
        else:
            self.__aux = array
            self.__rows = 0
            self.__cols = 0
        self.__matrix = self.convert_type(self.aux)
       

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
        if isinstance(array,arr.Matrix):
            aux = self.aux.copy()
            for i in range(self.rows):
                for j in range(self.cols):
                    if aux[i,j] != 0:
                        aux[i,j] = 1
            return aux
        else:
            return array

    def __str__(self) -> str:
        return str(self.matrix)
                
    def __add__(self,other):
        return BoolMatrix(self.matrix+other.matrix) 

    def __sub__(self,other):
        return BoolMatrix(self.matrix-other.matrix)

    def __mul__(self,other):
        if isinstance(other, BoolMatrix):
            return BoolMatrix(self.matrix*other.matrix)
        else:
            raise TypeError

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
        # return not (self^other).isone()
        pass

    def __and__(self,other):
        if not isinstance(other,BoolMatrix):
            raise TypeError(f"invalid type: {type(other)}. Expected {type(self)}")
        if self.rows == 0 ^ other.rows == 0:
            return False
        if self.cols != other.cols or self.rows != other.rows:
            return False
        return self*other

    def __or__(self,other):
        if not isinstance(other,BoolMatrix):
            raise TypeError(f"invalid type: {type(other)}. Expected {type(self)}")
        if self.rows == 0 ^ other.rows == 0:
            return False
        if self.cols != other.cols or self.rows != other.rows:
            return False
        return self+other

    def __xor__(self,other):
        if not isinstance(other,BoolMatrix):
            raise TypeError(f"invalid type: {type(other)}. Expected {type(self)}")
        if self.rows == 0 ^ other.rows == 0:
            return True
        if self.cols != other.cols or self.rows != other.rows:
            return False
        return self-other
        
    def __getitem__(self,item):
        return BoolMatrix(self.matrix[item])

    def transpose(self):
        return BoolMatrix(self.aux.transpose())

    def isone(self) -> bool:
        if self.rows == 0:
            return False
        for element in self.matrix:
            if not all(element):
                return False
        return True

    def isnull(self) -> bool:
        if self.rows == 0:
            return True
        for element in self.matrix:
            if any(element):
                return False
        return True

    def compare_transitive(self) -> bool:
        m2 = self**2
        aux = m2 ^ self
        return aux.isnull() 

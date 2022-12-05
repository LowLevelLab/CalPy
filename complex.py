import numpy as np
from typing import Union, Optional


class Complex(complex):
    pass

    

class Quaternion:
    def __init__(self,*args) -> None:
        if len(args) != 4:
            raise IndexError    
        self.__real = args[0]
        self.__imag = np.array(args[1:4])

    @property
    def real(self):
        return self.__real

    @ property
    def imag(self):
        return self.__imag

    def __str__(self) -> str:
        return f'{self.__real} + ({self.__imag[0]})i + ({self.__imag[1]})j + ({self.__imag[2]})k'

    def __add__(self, other):
        if isinstance(other, Union[float, int]):
            return Quaternion(self.real+other, *self.imag)    
        if isinstance(other, Quaternion):
            return Quaternion(self.real+other.real, *(self.imag + other.imag))
    
    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        return Quaternion(self.real-other.real, *(self.imag - other.imag))
    
    def __rsub__(self, other):
        return self.__sub__(other)

    def __isub__(self, other):
        return self.__sub__(other)

    def __mul__(self):
        pass

    def __rmul__(self):
        pass

    def __imul__(self):
        pass

    def __truediv__(self):
        pass

    def __rtruediv__(self):
        pass

    def __itruediv__(self):
        pass

    def __floordiv__(self):
        pass

    def __rfloordiv__(self):
        pass

    def __ifloordiv__(self):
        pass

    def __pow__(self, index):
        if index == 0:
            return 1
        elif index == 1:
            return self
        return self*self.__pow__(index-1)

    def __rpow__(self):
        pass

    def __ipow__(self):
        pass

    def __pos__(self):
        pass

    def __neg__(self):
        return Quaternion(-self.real, *(-1*self.imag))

    def __eq__(self, __o: object) -> bool:
        if self.real == __o.real and all([self.imag[i] == __o.imag[i] for i in range(len(self.imag))]):
            return True
        else:
            return False

    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)

    def __abs__(self):
        return self.real**2 + np.sum(self.imag**2)

    def image(self):
        return f"({self.__imag[0]})i + ({self.__imag[1]})j + ({self.__imag[2]})k"

    def conjugate(self):
        return Quaternion(self.real, *(-1*self.imag))
    

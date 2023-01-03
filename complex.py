from imports import *


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
        if isinstance(other, Union[int,float]):
            return Quaternion(self.real+other, *self.imag)
        elif isinstance(other, Quaternion):
            return Quaternion(self.real+other.real, *(self.imag + other.imag))
        else:
            raise TypeError
    
    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Union[int,float]):
            return Quaternion(self.real-other, *self.imag)
        elif isinstance(other, Quaternion):
            return Quaternion(self.real-other.real, *(self.imag - other.imag))
        else:
            raise TypeError
    
    def __rsub__(self, other):
        return self.__sub__(other)

    def __isub__(self, other):
        return self.__sub__(other)

    def __mul__(self,other):
        if isinstance(other, Union[int,float]):
            return Quaternion(self.real*other, *(self.imag*other))
        elif isinstance(other, Quaternion):
            return Quaternion(self.real*other.real-np.dot(self.imag,other.imag),
                              *(self.real*other.imag+other.real*self.imag+np.cross(self.imag,other.imag)))
        else:
            raise TypeError

    def __rmul__(self, other):
        return self.__mul__(other)

    def __imul__(self, other):
        return self.__mul__(other)

    def commutator(self,other):
        return self*other-other*self

    def __truediv__(self, other):
        if isinstance(other, Union[int,float]):
            return Quaternion(self.real/other, *(self.imag/other))
        elif isinstance(other,Quaternion):
            pass
        else:
            raise TypeError

    def __rtruediv__(self,other):
        return self.__truediv__(other)

    def __itruediv__(self,other):
        return self.__truediv__(other)

    def __floordiv__(self,other):
        if isinstance(other, Union[int,float]):
            return Quaternion(self.real/other, *(self.imag/other))
        elif isinstance(other,Quaternion):
            pass
        else:
            raise TypeError

    def __rfloordiv__(self,other):
        return self.__floordiv__(other)

    def __ifloordiv__(self,other):
        return self.__floordiv__(other)

    def __pow__(self, index):
        if isinstance(index, int):
            if index == 0:
                return 1
            elif index == 1:
                return self
            return self*self.__pow__(index-1)
        elif isinstance(index, float):
            pass
        elif isinstance(index, Quaternion):
            pass
        else:
            pass

    def __rpow__(self,other):
        if isinstance(other, Union[int,float]):
            pass
        else:
            return self.__pow__(other)

    def __ipow__(self,other):
        return self.__pow__(other)

    def __pos__(self):
        return self

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
        return Quaternion(self.real, *((-1)*self.imag))
    


    
def commutator(p:Quaternion,q:Quaternion):
    return p.commutator(q)
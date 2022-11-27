import numpy as np
from typing import Union


class Polynomial:

    """
    ### PROPERTIES ###
    """

    def __init__(self, array: Union[np.ndarray, list]) -> None:
        self.__polynomial = np.array(array)

    @property
    def polynomial(self):
        return self.__polynomial

    def __add__(self, other):
        if isinstance(other, Union[float,int]):
            aux = self.polynomial.copy()
            aux[0] += other
            return Polynomial(aux)

        elif isinstance(other, Polynomial):
            aux1, aux2 = np.array(list(reversed(self.polynomial))), np.array(list(reversed(other.polynomial)))
            aux = np.polyadd(aux1,aux2)
            return Polynomial(np.array(list(reversed(aux))))
        else:
            raise TypeError(f"incompatible types: {type(self)} and {type(other)}")

    def __radd__(self,other):
        return self.__add__(other)

    def __iadd__(self,other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Union[float,int]):
            aux = self.polynomial.copy()
            aux[0] -= other
            return Polynomial(aux)

        elif isinstance(other, Polynomial):
            aux1, aux2 = np.array(list(reversed(self.polynomial))), np.array(list(reversed(other.polynomial)))
            aux = np.polysub(aux1,aux2)
            return Polynomial(np.array(list(reversed(aux))))
        else:
            raise TypeError(f"incompatible types: {type(self)} and {type(other)}")

    def __rsub__(self, other):
        aux = self.__sub__(other)
        aux2 = aux.polynomial.copy()
        for i, v in enumerate(aux.polynomial):
            aux2[i] = -v
        return Polynomial(aux2)

    def __isub__(self,other):
        return self.__sub__(other)

    def __mul__(self, other):
        if isinstance(other, Union[float,int]):
            aux = other*self.polynomial
            return Polynomial(aux)
        elif isinstance(other, Polynomial):
            aux1, aux2 = np.array(list(reversed(self.polynomial))), np.array(list(reversed(other.polynomial)))
            aux = np.polymul(aux1,aux2)
            return Polynomial(np.array(list(reversed(aux))))
        else:
            raise TypeError(f"incompatible types: {type(self)} and {type(other)}")

    def __imul__(self, other):
        return self.__mul__(other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __eq__(self, other) -> bool:
        if isinstance(other, Union[float,int]):
            if len(self.polynomial) == 1:
                return self.polynomial[0] == other
            else:
                return False
        elif isinstance(other, Polynomial):
            for element in zip(self.polynomial, other.polynomial):
                if not all(element[0]==element[i] for i in range(2)):
                    return False
            return True
        else:
            raise TypeError(f"incompatible types: {type(self)} and {type(other)}")
    
    def __call__(self, *args) -> Union[float,int]:
        return self._horner_method(*args)

    def __truediv__(self, other):
        if isinstance(other, Union[float,int]):
            aux = self.polynomial/other
            return Polynomial(aux)
        elif isinstance(other,Polynomial):
            aux1, aux2 = np.array(list(reversed(self.polynomial))), np.array(list(reversed(other.polynomial)))
            aux = np.polydiv(aux1,aux2)
            return (Polynomial(np.array(list(reversed(aux[0])))), Polynomial(np.array(list(reversed(aux[1])))))
        else:
            raise TypeError(f"incompatible types: {type(self)} and {type(other)}")

    def __floordiv__(self, other):
        if isinstance(other, Polynomial): 
            aux = self.__truediv__(other)
            return aux[0]

        else:
            raise TypeError(f"incompatible types: {type(self)} and {type(other)}")


    def __str__(self) -> str:
        aux = f'{str(self.polynomial[0])} + '
        for i in range(1,len(self.polynomial)):
            aux += str(self.polynomial[i]) + f'x^{i} + '
        aux = aux.rstrip('+ ')
        return aux
      
    # HORNER METHOD

    def _horner_method(self, x: float) -> Union[float,int]:
        result = self.polynomial[-1]
        for i in range(len(self.polynomial)-2,-1,-1):
            result = result * x + self.polynomial[i]
        return result

    # GRAPHIC

    def plot_graphic(self, x:list) -> None:
        pass

    # DEGREE
    
    def deg(self) -> int:
        return len(self.polynomial)-1


    """
    ### ROOT-FINDING METHODS ###
    """


    pass

obj = Polynomial(np.array([1,2,43,5,3,45,1,5]))
obj1 = Polynomial([1,1,1])
# print(2-obj)
a = np.array([1,2,3])
b = np.array([4,5,6])

print(obj-obj1)
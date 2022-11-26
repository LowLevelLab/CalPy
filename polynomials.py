import numpy as np
from typing import Union


class Polynomial:
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
            aux = []
            if len(self.polynomial) > len(other.polynomial):
                pt = self.polynomial
                ot = other.polynomial
            if len(self.polynomial) < len(other.polynomial):
                pt = other.polynomial
                ot = self.polynomial
            for element in zip(self.polynomial, other.polynomial):
                aux.append(element[0]+element[1])
            for i in range(len(ot),len(pt)):
                aux.append(pt[i])
            return Polynomial(aux)
        else:
            raise TypeError(f"incompatible types: {type(self)} and {type(other)}")

    def __radd__(self,other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Union[float,int]):
            aux = self.polynomial.copy()
            aux[0] -= other
            return Polynomial(aux)

        elif isinstance(other, Polynomial):
            aux = []
            if len(self.polynomial) > len(other.polynomial):
                pt = self.polynomial
                ot = other.polynomial
            if len(self.polynomial) < len(other.polynomial):
                pt = other.polynomial
                ot = self.polynomial
            for element in zip(self.polynomial, other.polynomial):
                aux.append(element[0]-element[1])
            for i in range(len(ot),len(pt)):
                aux.append(pt[i])
            return Polynomial(aux)
        else:
            raise TypeError(f"incompatible types: {type(self)} and {type(other)}")

    def __rsub__(self, other):
        aux = self.__sub__(other)
        aux2 = aux.polynomial.copy()
        for i, v in enumerate(aux.polynomial):
            aux2[i] = -v
        return Polynomial(aux2)

    def __mul__(self, other):
        if isinstance(other, Union[float,int]):
            aux = other*self.polynomial
            return Polynomial(aux)
        elif isinstance(other, Polynomial):
            pass #for i, v in enumerate(self.polynomial)
        else:
            raise TypeError(f"incompatible types: {type(self)} and {type(other)}")

    def __rmul__(self, other):
        return self.__mul__(other)

    def __eq__(self, other):
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
    
    def __call__(self, *args):
        return self._horner_method(*args)

    def __truediv__(self, other):
        if isinstance(other, Union[float,int]):
            aux = self.polynomial/other
            
            return Polynomial(aux)


        elif isinstance(other,Polynomial):
            pass #for i, v in enumerate(self.polynomial)
        else:
            raise TypeError(f"incompatible types: {type(self)} and {type(other)}")

    def __floordiv__(self, other):
        if isinstance(other, Polynomial): 
            return self.__truediv__[0]
        else:
            raise TypeError(f"incompatible types: {type(self)} and {type(other)}")


    def __str__(self) -> str:
        aux = f'{str(self.polynomial[0])} + '
        for i in range(1,len(self.polynomial)):
            aux += str(self.polynomial[i]) + f'x^{i} + '
        aux = aux.rstrip('+ ')
        return aux
      

    # HORNER METHOD
    def _horner_method(self, x: float):
        result = self.polynomial[-1]
        for i in range(len(self.polynomial)-2,-1,-1):
            result = result * x + self.polynomial[i]
        return result

    # GRAPHIC

    def plot_graphic(self, x:list):
        pass


obj = Polynomial(np.array([1,2,3]))
obj1 = Polynomial([1,2,3, 4])
# print(2-obj)
a = np.array([1,2,3])
b = np.array([4,5,6])

print(obj+obj1)
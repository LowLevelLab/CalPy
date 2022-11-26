import numpy as np
import matplotlib.pyplot as plt
from functions import Function
from polynomials import Polynomial
from typing import Union


class Interpolation:
    def __init__(self, x: Union[np.ndarray,list], y: Union[np.ndarray,list] = ['e'], f = lambda x: x) -> None:
        x.sort(), y.sort()
        self.x_interval = x
        self.y_interval = y
        self.function = f



class NewtonInterpolation(Interpolation):
    def __init__(self, x: list, y: list = ['e'], f = lambda x: x) -> None:
        super().__init__(x,y,f)
    
    def diff_div(self):
        pass

    def _Nk(self, k: int) -> Polynomial:
        pass
    
        
    pass

class LagrangeInterpolation(Interpolation):
    def __init__(self, x: list, y: list = ['e'], f = lambda x: x) -> None:
        super().__init__(x,y,f)
        self.__poly = self._interpolate()


    def _Lk(self, k:int) -> Polynomial:
        aux = Polynomial([1])
        for i in range(len(self.x_interval)):
            if i == k:
                continue
            aux = aux*Polynomial([-self.x_interval[i]/(self.x_interval[k]-self.x_interval[i]),
                                   1/(self.x_interval[k]-self.x_interval[i])])
        return aux

    def _interpolate(self) -> Polynomial:
        if self.y_interval[0] != 'e':
            return sum([self.y_interval[i]*self._Lk(i) for i in range(len(self.x_interval))])
        else:
            self.y_interval = [self.function(xk) for xk in self.x_interval]
            return sum([self.y_interval[i]*self._Lk(i) for i in range(len(self.x_interval))])
        
    @property
    def poly(self):
        return self.__poly
            
        
    pass

obj = LagrangeInterpolation([1,2,3,4,5],[1,2,3,5,6])

print(obj.poly)
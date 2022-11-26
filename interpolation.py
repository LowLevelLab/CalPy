import numpy as np
import matplotlib.pyplot as plt
from functions import Function
from polynomials import Polynomial


class Interpolation:
    def __init__(self, x: list, y: list = ['e'], f: function = lambda x: x) -> None:
        self.__x_interval = x
        self.__y_interval = y
        self.__function = f
    pass


class NewtonInterpolation(Interpolation):
    def __init__(self, x: list, y: list = ['e'], f: function = lambda x: x) -> None:
        super.__init__(x,y,f)
    
    def diff_div(self):
        pass

    def _Nk(self, k: int) -> Polynomial:
        pass
    
        
    pass

class LagrangeInterpolation(Interpolation):
    def __init__(self, x: list, y: list = ['e'], f: function = lambda x: x) -> None:
        super.__init__(x,y,f)
        self.__poly = self._interpolate()


    def _Lk(self, k:int) -> Polynomial:
        aux = Polynomial([1])
        for i in range(len(self.__x_interval)):
            if i == k:
                continue
            aux = aux*Polynomial([-self.__x_interval[i]/(self.__x_interval[k]-self.__x_interval[i]),
                                   1/(self.__x_interval[k]-self.__x_interval[i])])
        return aux

    def _interpolate(self) -> Polynomial:
        if self.__y_interval[0] != 'e':
            return sum([self.__y_interval[i]*self._Lk(i) for i in range(len(self.__x_interval))])
        else:
            self.__y_interval = [self.__function(xk) for xk in self.__x_interval]
            return sum([self.__y_interval[i]*self._Lk(i) for i in range(len(self.__x_interval))])
        
    @property
    def poly(self):
        return self.__poly
            
        
    pass
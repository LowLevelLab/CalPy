from imports import *
from poly.polynomials import Polynomial


class Interpolation:
    def __init__(self, x: Union[np.ndarray,list], y: Union[np.ndarray,list] = None, f = lambda x: x) -> None:
        x.sort()
        self.x_interval = np.array(x)
        if y is not None:
            y.sort()
            self.y_interval = np.array(y)
        else:
            self.y_interval = f(self.x_interval)    



class NewtonInterpolation(Interpolation):
    def __init__(self, x: Union[list,np.ndarray], y: Optional[Union[list,np.ndarray]] = None, f = lambda x: x) -> None:
        super().__init__(x,y,f)
        self.__poly = self._interpolate()

    def __str__(self) -> str:
        return self.poly.__str__()
    
    def diff_div(self,i: int,k: int) -> Union[int,float]:
        if i == k:
            return self.y_interval[i]
        else:
            return ((self.diff_div(i+1, k)-self.diff_div(i,k-1))/(self.x_interval[k]-self.x_interval[i]))
        
    def _Nk(self, k: int) -> Polynomial:
        aux = Polynomial([self.diff_div(0, k)])
        for i in range(k):
            aux *= Polynomial([-self.x_interval[i],1])
        return aux

    def _interpolate(self) -> Polynomial:
        return sum([self._Nk(i) for i in range(len(self.x_interval))])

    @property
    def poly(self):
        return self.__poly


class LagrangeInterpolation(Interpolation):
    def __init__(self, x: Union[list,np.ndarray], y: Optional[Union[list,np.ndarray]] = None, f = lambda x: x) -> None:
        super().__init__(x,y,f)
        self.__poly = self._interpolate()

    def __str__(self) -> str:
        return self.poly.__str__()

    def _Lk(self, k:int) -> Polynomial:
        aux = Polynomial([1])
        for i in range(len(self.x_interval)):
            if i == k:
                continue
            aux *=Polynomial([(-self.x_interval[i])/(self.x_interval[k]-self.x_interval[i]),
                                   1/(self.x_interval[k]-self.x_interval[i])])
        return aux

    def _interpolate(self) -> Polynomial:
        return sum([self.y_interval[i]*self._Lk(i) for i in range(len(self.x_interval))])
        
    @property
    def poly(self):
        return self.__poly
            


# TABLE: DATAFRAME

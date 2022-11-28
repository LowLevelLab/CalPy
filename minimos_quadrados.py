import numpy as np
from typing import Union, Optional
from abc import ABCMeta, abstractclassmethod

class Regression(metaclass=ABCMeta):
    def __init__(self, xlist: Union[list,np.ndarray], ylist: Union[list,np.ndarray]) -> None:
        if not isinstance(xlist, Union[list, np.ndarray]):
            raise TypeError
        self.x = np.array(xlist)
        if not isinstance(xlist, Union[list, np.ndarray]): 
            raise TypeError
        self.y = np.array(ylist)
        self.coeff = self.coeff_regression()

    # @property
    # def x(self) -> np.ndarray:
    #     return self.__x
    # @x.setter
    # def x(self,xlist) -> None:
    #     if type(xlist) is not Union[np.ndarray,list]:
    #         raise TypeError
    #     else:
    #         self.__x = xlist

    
    # @property
    # def y(self) -> np.ndarray:
    #     return self.__y
    # @y.setter
    # def y(self,ylist) -> None:
    #     if type(ylist) is not Union[np.ndarray,list]:
    #         raise TypeError
    #     else:
    #         self.__y = ylist

    def __call__(self, kind: str):
        possibilities = {
            'exp' : ExpRegression(self.x, self.y),
            'hpb' : HypRegression(self.x, self.y),
            'lin' : LinRegression(self.x, self.y),
            'log' : LogRegression(self.x, self.y),
            'pol' : PolyRegression(self.x, self.y),
            'pot' : PotRegression(self.x, self.y),
            'inv' : InvRegression(self.x, self.y),
            'lgt' : LogisticRegression(self.x,self.y),
            'gss' : GaussRegression(self.x,self.y),
            'opt' : 0
        }
        return possibilities[kind]

    # @abstractclassmethod
    def S_factor(self) -> float:
        pass

    @abstractclassmethod
    def coeff_regression(self) -> tuple:
        return (0,0)


class LinRegression(Regression):
    def __init__(self, xlist: Union[list,np.ndarray], ylist: Union[list,np.ndarray]) -> None:
        super().__init__(xlist, ylist)
        self.coeff = self.coeff_regression()
    
    def __str__(self) -> str:
        return f"y = {str(self.coeff[1])} + {str(self.coeff[0])}x"

    def coeff_regression(self) -> tuple:
        m = (len(self.y) * sum(self.x*self.y)
                         -sum(self.y) * sum(self.x)) / (
                         len(self.y) * sum(self.x**2) - sum(self.x) ** 2)

        b = (sum(self.x**2) * sum(self.y) - sum(self.x) * sum(
                         self.x*self.y)) / (
                         len(self.y) * sum(self.x**2) - sum(self.x) ** 2)
        return (m,b)
        

    
class ExpRegression(Regression):
    def __init__(self, xlist: Union[list,np.ndarray], ylist: Union[list,np.ndarray]) -> None:
        super().__init__(xlist, ylist)
    
    def __str__(self) -> str:
        return f"y = {str(self.coeff[1])}*e^({str(self.coeff[0])}*x)"

    def coeff_regression(self) -> tuple:
        y_new = np.log(self.y)
        aux = LinRegression(self.x, y_new)
        aux1 = aux.coeff_regression()
        aux = (aux1[0], np.e**(aux1[1]))
        return aux


class LogRegression(Regression):
    def __init__(self, xlist: Union[list,np.ndarray], ylist: Union[list,np.ndarray]) -> None:
        super().__init__(xlist, ylist)

    def __str__(self) -> str:
        return f"y = {str(self.coeff[1])} + {str(self.coeff[0])}log(x)"
    
    def coeff_regression(self) -> tuple:
        x_new = np.log(self.x)
        aux = LinRegression(x_new, self.y)
        aux1 = aux.coeff_regression()
        aux = (aux1[0], aux1[1])
        return aux


class PotRegression(Regression):
    def __init__(self, xlist: Union[list,np.ndarray], ylist: Union[list,np.ndarray]) -> None:
        super().__init__(xlist, ylist)

    def __str__(self) -> str:
        return f"y = {str(self.coeff[1])}*x^({str(self.coeff[0])})"

    def coeff_regression(self) -> tuple:
        x_new = np.log(self.x)
        y_new = np.log(self.y)
        aux = LinRegression(x_new, y_new)
        aux1 = aux.coeff_regression()
        aux = (aux1[0], np.e**(aux1[1]))
        return aux



class PolyRegression(Regression):
    def __init__(self, xlist: Union[list,np.ndarray], ylist: Union[list,np.ndarray]) -> None:
        super().__init__(xlist, ylist)

    def __str__(self) -> str:
        pass #return Polynomial

    def coeff_regression(self) -> tuple:
        pass

class HypRegression(Regression):
    def __init__(self, xlist: Union[list,np.ndarray], ylist: Union[list,np.ndarray]) -> None:
        super().__init__(xlist, ylist)

    def __str__(self) -> str:
        return f"y = 1/({str(self.coeff[1])} + {str(self.coeff[0])}x)"

    def coeff_regression(self) -> tuple:
        y_new = 1/self.y
        aux = LinRegression(self.x, y_new)
        aux1 = aux.coeff_regression()
        aux = (aux1[0], aux1[1])
        return aux



class InvRegression(Regression):
    def __init__(self, xlist: Union[list,np.ndarray], ylist: Union[list,np.ndarray]) -> None:
        super().__init__(xlist, ylist)

    def __str__(self) -> str:
        return f"y = {str(self.coeff[1])} + {str(self.coeff[0])}/x"

    def coeff_regression(self) -> tuple:
        x_new = 1/self.x
        aux = LinRegression(x_new, self.y)
        aux1 = aux.coeff_regression()
        aux = (aux1[0], aux1[1])
        return aux


class LogisticRegression(Regression):
    def __init__(self, xlist: Union[list,np.ndarray], ylist: Union[list,np.ndarray], lim: Optional[Union[float,int]]=1) -> None:
        super().__init__(xlist, ylist)
        if isinstance(lim, Union[float,int]) and lim != 1:
            self.lim = lim
        else:
            self.lim=1

    def __str__(self) -> str:
        return str(self.lim) #f"y = {self.lim}/(1+e^({self.coeff[0]}*(x-{self.coeff[1]})))"

    def coeff_regression(self) -> tuple:
        pass


class GaussRegression(Regression):
    def __init__(self, xlist: Union[list,np.ndarray], ylist: Union[list,np.ndarray]) -> None:
        super().__init__(xlist, ylist)

    def __str__(self) -> str:
        pass 

    def coeff_regression(self) -> tuple:
        pass

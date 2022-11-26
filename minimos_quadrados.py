import numpy as np
from typing import Union
from abc import ABCMeta, abstractclassmethod

class Regression(ABCMeta):
    def __init__(self, xlist: Union[list,np.ndarray], ylist: Union[list,np.ndarray]) -> None:
        if type(xlist) is not Union[list, np.ndarray]:
            raise TypeError
        self.__x = np.array(xlist)
        if type(ylist) is not Union[list, np.ndarray]:
            raise TypeError
        self.__y = np.array(ylist)
        self.__coeff = self.coeff_regression()

    @property
    def x(self) -> Union[list,np.ndarray]:
        return self.__x
    @property
    def x(self,xlist) -> None:
        if type(xlist) is not Union[np.ndarray,list]:
            raise TypeError
        else:
            self.__x = xlist

    
    @property
    def y(self) -> Union[list,np.ndarray]:
        return self.__y
    @property
    def y(self,ylist) -> None:
        if type(ylist) is not Union[np.ndarray,list]:
            raise TypeError
        else:
            self.__y = ylist

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
            'sqrt' : SqrtRegression(self.x,self.y),
            'gss' : GaussRegression(self.x,self.y),
            'opt' : 0
        }
        return possibilities[kind]

    @abstractclassmethod
    def S_factor(self) -> float:
        pass

    @abstractclassmethod
    def coeff_regression(self) -> list[function]:
        pass

    @staticmethod
    def regression(x: list, y: list):
        m = (len(y) * sum(Regression.term_by_term_product(y, x))
             - sum(y) * sum(x)) / (
                    len(y) * sum(Regression.square_pot(x)) - sum(x) ** 2)

        b = (sum(Regression.square_pot(x)) * sum(y) - sum(x) * sum(
            Regression.term_by_term_product(y, x))) / (
                    len(y) * sum(Regression.square_pot(x)) - sum(x) ** 2)

        return m, b

    def exp_regression(self):
        pass

    def poly_regression(self):
        pass

    def inverse_regression(self):
        x_new = Regression.invert_list(self.x)
        m, b = Regression.regression(x_new, self.y)
        return f"y = {str(b)} + {str(m)}/x"

    def hyperbolic_regression(self):
        y_new = Regression.invert_list(self.y)
        m, b = Regression.regression(self.x, y_new)
        return f"y = 1/({str(b)} + {str(m)}x)"

    def log_regression(self):
        pass

    def pot_regression(self):
        pass

    def lin_regression(self):
        m, b = self.regression(self.x, self.y)
        return f"y = {str(b)} + {str(m)}x"


class LinRegression(Regression):
    def __init__(self, xlist: Union[list,np.ndarray], ylist: Union[list,np.ndarray]) -> None:
        super.__init__(xlist, ylist)
    
    def __str__(self) -> str:
        pass #return f"y = {str(b)} + {str(m)}x"
    
class ExpRegression(Regression):
    def __init__(self, xlist: Union[list,np.ndarray], ylist: Union[list,np.ndarray]) -> None:
        super.__init__(xlist, ylist)
    
    def __str__(self) -> str:
        pass # return f"y = {str(b)} +{str(m)}*e^({str(a)}*x)

class LogRegression(Regression):
    def __init__(self, xlist: Union[list,np.ndarray], ylist: Union[list,np.ndarray]) -> None:
        super.__init__(xlist, ylist)

    def __str__(self) -> str:
        pass # return f"y = {str(b)} + {str(m)}log(x)

class PotRegression(Regression):
    def __init__(self, xlist: Union[list,np.ndarray], ylist: Union[list,np.ndarray]) -> None:
        super.__init__(xlist, ylist)

    def __str__(self) -> str:
        pass # return f"y = {str(b)} * {str(a)}x^{str(m)}

class PolyRegression(Regression):
    def __init__(self, xlist: Union[list,np.ndarray], ylist: Union[list,np.ndarray]) -> None:
        super.__init__(xlist, ylist)

    def __str__(self) -> str:
        pass #return Polynomial

class HypRegression(Regression):
    def __init__(self, xlist: Union[list,np.ndarray], ylist: Union[list,np.ndarray]) -> None:
        super.__init__(xlist, ylist)

    def __str__(self) -> str:
        pass #return f"y = 1/({str(b)} + {str(m)}x)"

class InvRegression(Regression):
    def __init__(self, xlist: Union[list,np.ndarray], ylist: Union[list,np.ndarray]) -> None:
        super.__init__(xlist, ylist)

    def __str__(self) -> str:
        pass #return f"y = {str(b)} + {str(m)}/x"

class LogisticRegression(Regression):
    def __init__(self, xlist: Union[list,np.ndarray], ylist: Union[list,np.ndarray]) -> None:
        super.__init__(xlist, ylist)

    def __str__(self) -> str:
        pass

class SqrtRegression(Regression):
    def __init__(self, xlist: Union[list,np.ndarray], ylist: Union[list,np.ndarray]) -> None:
        super.__init__(xlist, ylist)

    def __str__(self) -> str:
        pass #return f"y = {str(b)} + {str(m)}sqrt(x)"

class GaussRegression(Regression):
    def __init__(self, xlist: Union[list,np.ndarray], ylist: Union[list,np.ndarray]) -> None:
        super.__init__(xlist, ylist)

    def __str__(self) -> str:
        pass #return f"y = "
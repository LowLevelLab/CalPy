from imports import *
from interpolation.interpolation import LagrangeInterpolation
from calculus.functions import Function


class Regression(metaclass=ABCMeta):
    def __init__(self, xlist: Union[list,np.ndarray], ylist: Union[list,np.ndarray]) -> None:
        if not isinstance(xlist, Union[list, np.ndarray]):
            raise TypeError
        self.x = np.array(xlist)
        if not isinstance(xlist, Union[list, np.ndarray]): 
            raise TypeError
        self.y = np.array(ylist)
        self.coeff = self.coeff_regression()
        if type(self) == Regression:            
            self.regressions = {
                'exp' : ExpRegression(self.x, self.y),
                'hpb' : HypRegression(self.x, self.y),
                'lin' : LinRegression(self.x, self.y),
                'log' : LogRegression(self.x, self.y),
                'pol' : PolyRegression(self.x, self.y),
                'pot' : PotRegression(self.x, self.y),
                'inv' : InvRegression(self.x, self.y)
            }

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
        # possibilities = {
        #     'exp' : ExpRegression(self.x, self.y),
        #     'hpb' : HypRegression(self.x, self.y),
        #     'lin' : LinRegression(self.x, self.y),
        #     'log' : LogRegression(self.x, self.y),
        #     'pol' : PolyRegression(self.x, self.y),
        #     'pot' : PotRegression(self.x, self.y),
        #     'inv' : InvRegression(self.x, self.y),
        #     'opt' : self.optimize()
        # }
        # !!!! avoid triggering functions before call !!!!
        if type(self) == Regression:
            if kind == 'opt':
                return self.optimize()
            return self.regressions[kind]

    def square_residue(self) -> float:
        f = Function(self.to_function())
        aux = np.array(f(self.x))
        return np.sum((self.y-aux)**2)

    def coeff_regression(self) -> tuple:
        return (0,0)

    def to_function(self):
        pass

    def optimize(self):
        keys = ['exp','hpb','lin','log','pot','inv']

        residues = [ExpRegression(self.x, self.y).square_residue(),
                    HypRegression(self.x, self.y).square_residue(),
                    LinRegression(self.x, self.y).square_residue(),
                    LogRegression(self.x, self.y).square_residue(),
                    PotRegression(self.x, self.y).square_residue(),
                    InvRegression(self.x, self.y).square_residue()]

        # regressions_map = {
        #     'exp' : ExpRegression(self.x, self.y),
        #     'hpb' : HypRegression(self.x, self.y),
        #     'lin' : LinRegression(self.x, self.y),
        #     'log' : LogRegression(self.x, self.y),
        #     'pot' : PotRegression(self.x, self.y),
        #     'inv' : InvRegression(self.x, self.y),
        # }

        # !!!! improve variables keys and residues !!!!
        # !!!! avoid rewriting dictionary !!!!

        residue_map = dict(element for element in zip(residues,keys))
        # print(residue_map[min(residue_map.keys())])
        return self.regressions[residue_map[min(residue_map.keys())]]


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
        
    def to_function(self):
        return lambda x: self.coeff[1] + x*self.coeff[0]

    
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
    
    def to_function(self):
        return lambda x: self.coeff[1] * np.exp(x*self.coeff[0])


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
    
    def to_function(self):
        return lambda x: self.coeff[1] + self.coeff[0]*np.log(x)


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

    def to_function(self):
        return lambda x: self.coeff[1]*x**self.coeff[0]


class PolyRegression(Regression):
    def __init__(self, xlist: Union[list,np.ndarray], ylist: Union[list,np.ndarray]) -> None:
        super().__init__(xlist, ylist)
        self.inter = LagrangeInterpolation(self.x,self.y)

    def __str__(self) -> str:
        return self.inter.poly.__str__()

    def coeff_regression(self) -> tuple:
        self.coeff = [element for element in range(2)] 
    """self.inter.poly"""
    def to_function(self):
        return self.inter.poly.to_function()


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

    def to_function(self):
        return lambda x: 1/(self.coeff[1] + x*self.coeff[0])


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

    def to_function(self):
        return lambda x: self.coeff[1] + self.coeff[0]/x

"""
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

"""
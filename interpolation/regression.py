from imports import *
from interpolation.interpolation import LagrangeInterpolation
from calculus.functions import Function


class Regression:
    def __init__(self, xlist: Union[list,np.ndarray], ylist: Union[list,np.ndarray]) -> None:
        self.na = 'drop'
        if not isinstance(xlist, Union[list, np.ndarray]):
            raise TypeError
        self.x = np.array(xlist)
        if not isinstance(xlist, Union[list, np.ndarray]): 
            raise TypeError
        self.y = np.array(ylist)
        self.coeff = self.coeff_regression()
        if type(self) == Regression:  
            self.keys = ['exp','hpb','lin','log','pot','inv']

            self.regressions = [ExpRegression,
                    HypRegression,
                    LinRegression,
                    LogRegression,
                    PotRegression,
                    InvRegression]     

            self.dict_reg = dict(element for element in zip(self.keys, self.regressions))     

    def __call__(self, kind: str):

        if type(self) == Regression:
            if kind == 'opt':
                return self.optimize()
            elif kind == 'pol':
                return PolyRegression(self.x, self.y)
            return self.dict_reg[kind](self.x, self.y)

    def square_residue(self) -> float:
        f = Function(self.to_function())
        aux = np.array(f(self.x))
        return np.sum((self.y-aux)**2)

    def coeff_regression(self) -> tuple: raise NotImplementedError()

    def to_function(self): raise NotImplementedError()

    def optimize(self):
        residue_map = {}
        for key, element in self.dict_reg.items():
            aux = element(self.x, self.y)
            residue_map[key] = aux.square_residue(), aux
        self.residues = residue_map
        return min(residue_map.items(), key=lambda x: x[1][0])[1][1]

class LinRegression(Regression):
    def __init__(self, xlist: Union[list,np.ndarray], ylist: Union[list,np.ndarray]) -> None:
        super().__init__(xlist, ylist)
        self.coeff = self.coeff_regression()
    
    def __str__(self) -> str:
        return f"y = {str(self.coeff[1])} + {str(self.coeff[0])}x"

    def coeff_regression(self) -> tuple:
        m = (len(self.y) * np.sum(self.x*self.y)
                         -np.sum(self.y) * np.sum(self.x)) / (
                         len(self.y) * np.sum(self.x**2) - np.sum(self.x) ** 2)

        b = (np.sum(self.x**2) * np.sum(self.y) - np.sum(self.x) * np.sum(
                         self.x*self.y)) / (
                         len(self.y) * np.sum(self.x**2) - np.sum(self.x) ** 2)
        return (m,b)
        
    def to_function(self):
        return lambda x: self.coeff[1] + x*self.coeff[0]

    
class ExpRegression(Regression):
    def __init__(self, xlist: Union[list,np.ndarray], ylist: Union[list,np.ndarray]) -> None:
        super().__init__(xlist, ylist)
    
    def __str__(self) -> str:
        return f"y = {str(self.coeff[1])}*e^({str(self.coeff[0])}*x)"

    def coeff_regression(self) -> tuple:
        self.x, self.y = na(self.x,self.y,'exp',self.na)
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
        self.x, self.y = na(self.x,self.y,'log',self.na)
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
        self.x, self.y = na(self.x,self.y,'pot',self.na)
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
        
    def to_function(self):
        return self.inter.poly.to_function().function


class HypRegression(Regression):
    def __init__(self, xlist: Union[list,np.ndarray], ylist: Union[list,np.ndarray]) -> None:
        super().__init__(xlist, ylist)

    def __str__(self) -> str:
        return f"y = 1/({str(self.coeff[1])} + {str(self.coeff[0])}x)"

    def coeff_regression(self) -> tuple:
        self.x, self.y = na(self.x,self.y,'hpb',self.na)
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
        self.x, self.y = na(self.x,self.y,'inv',self.na)
        x_new = 1/self.x
        aux = LinRegression(x_new, self.y)
        aux1 = aux.coeff_regression()
        aux = (aux1[0], aux1[1])
        return aux

    def to_function(self):
        return lambda x: self.coeff[1] + self.coeff[0]/x


class QuadraticRegression(Regression):
    def __init__(self, xlist: Union[list, np.ndarray], ylist: Union[list, np.ndarray]) -> None:
        super().__init__(xlist, ylist)

    def __str__(self) -> str:
        pass
        # return f" y = {str(self.coeff[])}*sin(x) + {str(self.coeff[])}*cos(x)"

    def coeff_regression(self) -> tuple:
        # x_new = 
        pass

    def to_function(self):
        pass
        # return lambda x: {str(self.coeff[])}*np.sin(x) + {str(self.coeff[])}*np.cos(x)


class SinRegression(Regression):
    def __init__(self, xlist: Union[list, np.ndarray], ylist: Union[list, np.ndarray]) -> None:
        super().__init__(xlist, ylist)

    def __str__(self) -> str:
        pass
        # return f" y = {str(self.coeff[])}*sin(x) + {str(self.coeff[])}*cos(x)"

    def coeff_regression(self) -> tuple:
        # x_new = 
        pass

    def to_function(self):
        pass
        # return lambda x: {str(self.coeff[])}*np.sin(x) + {str(self.coeff[])}*np.cos(x)


def na(x: np.ndarray, y: np.ndarray, kind: str, type: str = 'drop', filler: Optional[Union[float,int]] = None):
    if type == 'drop':
        return dropna(x, y, kind)
    elif type == 'fill':
        return fillna(x, y, kind, filler)
    else:
        raise InvalidArgumentError

def dropna(x, y, kind):
    dic = dict((xk,yk) for xk,yk in zip(x,y))
    elim = []
    if kind == 'inv':
        for index, element in dic.items():
            if index == 0:
                elim.append(index)
        for element in elim:
            dic.pop(element)
        nx, ny = np.array([*dic.keys()]), np.array([*dic.values()])
    elif kind == 'log':
        for index, element in dic.items():
            if index <= 0:
                elim.append(index)
        for element in elim:
            dic.pop(element)
        nx, ny = np.array([*dic.keys()]), np.array([*dic.values()])
    elif kind == 'hpb':
        for index, element in dic.items():
            if element == 0:
                elim.append(index)
        for element in elim:
            dic.pop(element)
        nx, ny = np.array([*dic.keys()]), np.array([*dic.values()])
    elif kind == 'exp':
        for index, element in dic.items():
            if element <= 0:
                elim.append(index)
        for element in elim:
            dic.pop(element)
        nx, ny = np.array([*dic.keys()]), np.array([*dic.values()])
    elif kind == 'pot':
        for index, element in dic.items():
            if element <= 0 or index <= 0:
                elim.append(index)
        for element in elim:
            dic.pop(element)
        nx, ny = np.array([*dic.keys()]), np.array([*dic.values()])
    else:
        raise InvalidArgumentError
    elim.clear()
    return nx, ny

def fillna(x, y, kind, filler):
    dic = dict((xk,yk) for xk,yk in zip(x,y))
    new = {}
    if kind == 'inv':
        for index, element in dic.items():
            if index != 0:
                new[index] = element
        nx, ny = np.array([*new.keys()]), np.array([*new.values()])
    elif kind == 'log':
        for index, element in dic.items():
            if index > 0:
                new[index] = element
        nx, ny = np.array([*new.keys()]), np.array([*new.values()])
    elif kind == 'hpb':
        for index, element in dic.items():
            if element != 0:
                new[index] = element
        nx, ny = np.array([*new.keys()]), np.array([*new.values()])
    elif kind == 'exp':
        for index, element in dic.items():
            if element > 0:
                new[index] = element
        nx, ny = np.array([*new.keys()]), np.array([*new.values()])
    elif kind == 'pot':
        for index, element in dic.items():
            if index > 0 and element > 0:
                new[index] = element
        nx, ny = np.array([*new.keys()]), np.array([*new.values()])
    return nx, ny
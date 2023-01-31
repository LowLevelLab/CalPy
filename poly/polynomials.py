from imports import *
from complex import Complex


class Polynomial:

    """
    ### PROPERTIES ###
    """

    def __init__(self, array: Union[np.ndarray, list, tuple]) -> None:
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
        if len(args) == 1 and isinstance(args[0],Union[int,float]):
            return self._horner_method(*args)
        elif len(args) == 1 and not isinstance(args[0],Union[int,float]):
            return np.array([self._horner_method(element) for element in args[0]])
        else:
            return np.array([self._horner_method(element) for element in args])

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
        if len(self.polynomial) == 1:
            return f'{str(self.polynomial[0])}'
        aux = f'{str(self.polynomial[0])} + {str(self.polynomial[1])}x + '
        for i in range(2,len(self.polynomial)):
            aux += str(self.polynomial[i]) + f'x^{i} + '
        aux = aux.rstrip('+ ')
        return aux
      
    # HORNER METHOD

    def _horner_method(self, x: Union[float,int]) -> Union[float,int]:
        result = self.polynomial[-1]
        for i in range(len(self.polynomial)-2,-1,-1):
            result = result * x + self.polynomial[i]
        return result

    # GRAPHIC

    def plot_function(self,x: Union[list,tuple,np.ndarray],
                      x_axis: str = 'x axis',
                      y_axis: str = 'y axis',
                      title: str = 'function',
                      color: str = 'r',
                      label: Optional[str] = None,
                      local_legend: Optional[str] = None) -> None:
        if label is not None:
            l_def = label
        else:
            l_def = 'f(x)'
        y = [self.function(xk) for xk in x]
        xl = plt.xlabel(x_axis)
        yl = plt.ylabel(y_axis)
        ttl = plt.title(title)
        la = plt.plot(x, y, color, label=l_def)
        if local_legend is not None:
            ll=plt.legend(loc=local_legend)
        plt.show()

    # COPY

    def copy(self):
        return Polynomial(self.polynomial.copy())

    # DEGREE
    
    def deg(self) -> int:
        return len(self.polynomial)-1

    def to_frame(self, *args) -> pd.core.frame.DataFrame:
        aux = pd.DataFrame(data= [list(*args),self(*args)],index=['x','f(x)']).T
        aux.set_index('x', inplace=True)
        return aux

    # DERIVATIVE

    def derivative(self, n:int = 1):
        l = [i*self.polynomial[i] for i in range(len(self.polynomial))]
        l.pop(0)
        aux = Polynomial(l)
        if n == 1:
            return aux
        else:
            return aux.derivative(n-1)

    def to_function(self):
        from calculus.functions import Function
        return Function(lambda x: sum(element*x**i for i, element in enumerate(self.polynomial)))

    def graphic(self, x_interval: Union[list,tuple,np.ndarray],
                color: str = 'r', 
                x_label: str = 'x axis', 
                y_label: str ='y axis', 
                title: str= 'p(x)' , 
                style: str= '-'):
        
        y = [self(xk) for xk in x_interval]
        xl = plt.xlabel(x_label)
        yl = plt.ylabel(y_label)
        ttl = plt.title(title)
        la = plt.plot(x_interval, y, color, ls= style)
        plt.show()



    """
    ### ROOT-FINDING METHODS ###
    """
    

    def function_root_finding(self, method: str = 'nr'):
        aux = self.to_function()
        aux_dict = {}
        # nr
        # bis
        # fp
        # st
    
    pass

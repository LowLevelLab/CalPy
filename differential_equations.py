import numpy as np
import matplotlib.pyplot as plt
import constants as c
from typing import Optional, Union
from functions import Function
from arrays import Vector
import pandas as pd



class ODE:
    def __init__(self, functions:list[Function], x:Optional[Union[list,np.ndarray]] =None) -> None:
        if isinstance(x, Union[list,np.ndarray]):
            self.__x_interval = np.array(x)
        else:
            self.__x_interval = np.array([0,1])
        if not isinstance(functions, list):
            l = [functions]
            functions = l
        if not isinstance(functions[0],Function):
            functions = [Function(element) for element in functions]
        self.__functions = Vector(functions)

    @property
    def functions(self):
        return self.__functions
    
    @property
    def x_interval(self):
        return self.__x_interval

    def _limit_check(self, x0: Optional[Union[int,float]], xf: Optional[Union[int,float]]) -> int:
        if x0 is None and xf is None:
            return 0
        elif x0 is not None and xf is not None:
            return 1
        else:
            raise ValueError

    def euler(self,
              y0:Union[list,np.ndarray],
              x0: Optional[Union[int,float]]=None,
              xf: Optional[Union[int,float]]=None,
              graphic: bool = False,
              n: int = 10*c.ITERATIONS) -> list[np.ndarray]:

        if bool(self._limit_check(x0,xf)):
            step = (xf-x0)/n
        else:
            x0 = min(self.__x_interval)
            xf = max(self.__x_interval)
            step = (xf-x0)/n
        
        y = np.array([np.zeros(n) for yk in y0]).transpose()
        y[0] = y0
        aux_x = np.arange(x0, xf, step)
        for i in range(1,n): 
            y[i] = y[i-1] + step*(self.functions(aux_x[i], *y[i-1])).array
        y = y.transpose()
        if graphic:
            self._to_graphic(y,n)
        return self.to_frame(aux_x,y)
            

    def euler2(self,
               y0:Union[list,np.ndarray],
               x0: Optional[Union[int,float]]=None,
               xf: Optional[Union[int,float]]=None,
               graphic: bool = False,
               n: int = 10*c.ITERATIONS) -> list[np.ndarray]:

        if bool(self._limit_check()):
            step = (xf-x0)/n
        else:
            step = (max(self.__x_interval)-min(self.__x_interval))/n
        
    def heun(self,
             y0:Union[list,np.ndarray],
             x0: Optional[Union[int,float]]=None,
             xf: Optional[Union[int,float]]=None,
             graphic: bool = False,
             n: int = 10*c.ITERATIONS) -> list[np.ndarray]:

        if bool(self._limit_check()):
            step = (xf-x0)/n
        else:
            step = (max(self.__x_interval)-min(self.__x_interval))/n
        
    def rk4(self, 
            y0:Union[list,np.ndarray],
            x0: Optional[Union[int,float]]=None,
            xf: Optional[Union[int,float]]=None,
            graphic: bool = False,
            n: int = 10*c.ITERATIONS) -> list[np.ndarray]:

        if bool(self._limit_check()):
            step = (xf-x0)/n
        else:
            step = (max(self.__x_interval)-min(self.__x_interval))/n

    def pvc(self, 
            x0: Union[int,float], 
            xf: Union[int,float], 
            y0: list[Union[int,float]], 
            yf: list[Union[int,float]],
            graphic: bool = False,
            n: int = 10*c.ITERATIONS) -> list[np.ndarray]:

            pass
        

    def _to_graphic(self,
                    y: list,
                    n: int,
                    title: str = 'graphics',
                    x_axis:str='x axis',
                    y_axis: str = 'y axis',
                    color: str = 'r')-> None:

        x = np.arange(self.x_interval[0],self.x_interval[1],(self.x_interval[1]-self.x_interval[0])/n)
        l = []
        xl = plt.xlabel(x_axis)
        yl = plt.ylabel(y_axis)
        ttl = plt.title(title)
        for yk in y:
            l.append(plt.plot(x,yk,color))
        plt.show()

    
    def to_frame(self,x,y):
        d = {}
        d['x']=x
        for i,element in enumerate(y):
            d[f'y{i+1}'] = element
        df = pd.DataFrame(data=d)
        df.set_index('x',inplace=True)
        return df

    


class PDE:
    pass

# MODIFY __str__ : DATAFRAME
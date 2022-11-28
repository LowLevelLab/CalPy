import numpy as np
import matplotlib.pyplot as plt
import constants as c
from typing import Optional, Union
from functions import Function
from arrays import Vector
import pandas as pd



class ODE:
    def __init__(self, functions: Union[list,np.ndarray], x: Optional[Union[list,np.ndarray]]= None) -> None:
        if isinstance(x, Union[list,np.ndarray]):
            self.__x_interval = np.array(x)
        else:
            self.__x_interval = np.array([0,1])
        if not isinstance(functions, list):
            l = [functions]
            functions = l
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
              df: bool = True,
              n: int = 10*c.ITERATIONS):

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
        if df:
            return self.to_frame(aux_x,y)
        else:
            return y
            

    def euler2(self,
               y0:Union[list,np.ndarray],
               x0: Optional[Union[int,float]]=None,
               xf: Optional[Union[int,float]]=None,
               graphic: bool = False,
               df: bool = True,
               n: int = 10*c.ITERATIONS):

        if bool(self._limit_check(x0,xf)):
            step = (xf-x0)/n
        else:
            x0 = min(self.__x_interval)
            xf = max(self.__x_interval)
            step = (xf-x0)/n
        aux_x = np.arange(x0, xf, step)
        aux_y = self.euler(y0,x0,xf,df=False,n=n).transpose()
        y = np.array([np.zeros(n) for yk in y0]).transpose()
        y[0] = y0
        for i in range(1,n-1): 
            y[i] = y[i-1] + step*((aux_y[i]-aux_y[i-1])/step+(aux_y[i+1]-aux_y[i])/step)/2
        y[-1] = aux_y[-1]
        y = y.transpose()
        if graphic:
            self._to_graphic(y,n)
        if df:
            return self.to_frame(aux_x,y)
        else:
            return y
        
    def heun(self,
             y0:Union[list,np.ndarray],
             x0: Optional[Union[int,float]]=None,
             xf: Optional[Union[int,float]]=None,
             graphic: bool = False,
             df: bool = True,
             n: int = 10*c.ITERATIONS):

        if bool(self._limit_check(x0,xf)):
            step = (xf-x0)/n
        else:
            x0 = min(self.__x_interval)
            xf = max(self.__x_interval)
            step = (xf-x0)/n
        aux_x = np.arange(x0, xf, step)
        y = np.array([np.zeros(n) for yk in y0]).transpose()
        y[0] = y0
        for i in range(n-1):
            y[i+1] = y[i] + step*self.functions(aux_x[i],*y[i])
            y[i+1] = y[i] + (step/2)*(self.functions(aux_x[i],*y[i])+self.functions(aux_x[i+1],*y[i+1]))
        y=y.transpose()
        if graphic:
            self._to_graphic(y,n)
        if df:
            return self.to_frame(aux_x,y)
        else:
            return y

    def nystrom(self, 
                y0:Union[list,np.ndarray],
                x0: Optional[Union[int,float]]=None,
                xf: Optional[Union[int,float]]=None,
                graphic: bool = False,
                df: bool = True,
                n: int = 10*c.ITERATIONS):
        
        if bool(self._limit_check(x0,xf)):
            step = (xf-x0)/n
        else:
            x0 = min(self.__x_interval)
            xf = max(self.__x_interval)
            step = (xf-x0)/n
        aux_x = np.arange(x0, xf, step)
        y = np.array([np.zeros(n) for yk in y0]).transpose()
        k1,k2,k3 = y.copy(),y.copy(),y.copy()
        y[0] = y0

        for i in range(n-1):
            k1[i] = self.functions(aux_x[i],*y[i])
            k2[i] = self.functions(aux_x[i]+2*step/3, *(y[i]+2*step*k1[i]/3))
            k3[i] = self.functions(aux_x[i]+2*step/3, *(y[i]+2*step*k2[i]/3))
            y[i+1] = y[i] + (step/4)*(k1[i]+(3/2)*(k2[i]+k3[i]))
        y=y.transpose()
        if graphic:
            self._to_graphic(y,n)
        if df:
            return self.to_frame(aux_x,y)
        else:
            return y
        
    def rk4(self, 
            y0:Union[list,np.ndarray],
            x0: Optional[Union[int,float]]=None,
            xf: Optional[Union[int,float]]=None,
            graphic: bool = False,
            df: bool = True,
            n: int = 10*c.ITERATIONS):

        if bool(self._limit_check(x0,xf)):
            step = (xf-x0)/n
        else:
            x0 = min(self.__x_interval)
            xf = max(self.__x_interval)
            step = (xf-x0)/n
        aux_x = np.arange(x0, xf, step)
        y = np.array([np.zeros(n) for yk in y0]).transpose()
        k1,k2,k3,k4 = y.copy(),y.copy(),y.copy(),y.copy()
        y[0] = y0
        for i in range(n -1):
            k1[i] = step * self.functions(aux_x[i], *y[i])
            k2[i] = step * self.functions(aux_x[i] + step / 2, *(y[i] + k1[i] / 2))
            k3[i] = step * self.functions(aux_x[i] + step / 2, *(y[i] + k2[i] / 2))
            k4[i] = step * self.functions(aux_x[i] + step, *(y[i] + k3[i]))
            y[i+1] = y[i] + (k1[i] + 2 * (k2[i] + k3[i]) + k4[i]) / 6
        y=y.transpose()
        if graphic:
            self._to_graphic(y,n)
        if df:
            return self.to_frame(aux_x,y)
        else:
            return y

    def pvc(self, 
            x0: Union[int,float], 
            xf: Union[int,float], 
            y0: list[Union[int,float]], 
            yf: list[Union[int,float]],
            graphic: bool = False,
            df: bool = True,
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


# NYSTROM

class PDE:
    pass

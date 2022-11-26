import numpy as np
import matplotlib.pyplot as plt
import constants as c
from typing import Optional, Union



class ODE:
    def __init__(self, functions:list, x:Optional[list] =None) -> None:
        if type(x) is list:
            self.__x_interval = x
        else:
            self.__x_interval = [0,1]
        if type(functions) is not list:
            l = [functions]
            functions = l
        self.__functions = functions

    def _limit_check(self, x0: Optional[Union[int,float]], xf: Optional[Union[int,float]]) -> int:
        if type(x0) is None:
            if type(xf) is None:
                return 0
            else:
                raise ValueError
        else:
            if type(xf) is None:
                raise ValueError
            else:
                return 1

    def euler(self,x0: Optional[Union[int,float]],
              xf: Optional[Union[int,float]],
              y0:list,
              n: int = 100*c.ITERATIONS) -> list[np.ndarray]:

        if bool(self._limit_check()):
            step = (xf-x0)/n
        else:
            step = (max(self.__x_interval)-min(self.__x_interval))/n
        
        y = np.array([np.zeros(n) for yk in y0])
        aux_x = np.arange(x0, xf, step) 
        

    def euler2(self,x0: Optional[Union[int,float]],
               xf: Optional[Union[int,float]],
               y0:list,
               n: int = 100*c.ITERATIONS) -> list[np.ndarray]:

        if bool(self._limit_check()):
            step = (xf-x0)/n
        else:
            step = (max(self.__x_interval)-min(self.__x_interval))/n
        
    def heun(self,x0: Optional[Union[int,float]],
             xf: Optional[Union[int,float]],
             y0:list,
             n: int = 100*c.ITERATIONS) -> list[np.ndarray]:

        if bool(self._limit_check()):
            step = (xf-x0)/n
        else:
            step = (max(self.__x_interval)-min(self.__x_interval))/n
        
    def rk4(self,x0: Optional[Union[int,float]],
            xf: Optional[Union[int,float]],
            y0:list,
            n: int = 100*c.ITERATIONS) -> list[np.ndarray]:

        if bool(self._limit_check()):
            step = (xf-x0)/n
        else:
            step = (max(self.__x_interval)-min(self.__x_interval))/n

    def pvc(self, 
            x0: Union[int,float], 
            xf: Union[int,float], 
            y0: list[Union[int,float]], 
            yf: list[Union[int,float]]) -> list[np.ndarray]:

            pass
        

    def _to_graphic(self, y: list)-> None:
        pass
    


class PDE:
    pass


obj = ODE([lambda x,y: 1, lambda x,y: 2])
print(obj.euler(0,1,[0,0],5))
from calculus.functions import Function
from linalg.arrays import Array
import constants as const
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



class ODE:
    def __init__(self,
                 functions: Array,
                 x: list | Array | None = None,
                 iterations: int = 10*const.ITERATIONS,
                 decimals: int = 4) -> None:

        if isinstance(x, list | Array):
            self.__x_interval = Array(x)
        else:
            self.__x_interval = None
        if not isinstance(functions, list):
            l = [functions]
            functions = l
        self.__functions = Array(functions)
        self.__n = iterations
        self.__decimals = decimals

    @property
    def functions(self):
        return self.__functions
    
    @property
    def x_interval(self):
        return self.__x_interval

    @ property
    def n(self):
        return self.__n

    @n.setter
    def n(self, arg):
        if isinstance(arg, int) and arg > 0:
            self.__n = arg
        elif isinstance(arg, int) and arg <= 0:
            raise ValueError
        elif not isinstance(arg, int):
            raise TypeError
        else:
            raise KeyError

    @property    
    def decimals(self):
        return self.__decimals

    @decimals.setter
    def decimals(self, arg):
        if isinstance(arg, int) and arg > 0:
            self.__decimals = arg
        elif isinstance(arg, int) and arg <= 0:
            raise ValueError
        elif not isinstance(arg, int):
            raise TypeError
        else:
            raise KeyError

    def _limit_check(self, x0: int | float, xf: int | float) -> int:
        if x0 is None and xf is None:
            return False
        elif x0 is not None and xf is not None:
            return True
        else:
            raise ValueError

    def euler(self,
              y0: list | np.ndarray | Array,
              x0: int | float | None = None,
              xf: int | float | None = None,
              graphic: bool = False):

        if bool(self._limit_check(x0,xf)):            
            if self.x_interval is None:
                self.x_interval = np.array([x0,xf])
        else:
            x0 = min(self.__x_interval)
            xf = max(self.__x_interval)
        step = (xf-x0)/self.n
        y = np.zeros((len(y0),self.n)).transpose()
        y[0] = y0
        aux_x = np.arange(x0, xf, step)
        for i in range(1,self.n): 
            y[i] = y[i-1] + step*(self.functions(aux_x[i], *y[i-1]))
        y = y.transpose()
        if graphic:
            aux = SolutionODE(y,iterations=self.n,decimals=self.decimals,x_interval=self.x_interval)
            aux.to_graphic()
            return aux
        return SolutionODE(y,iterations=self.n,decimals=self.decimals,x_interval=self.x_interval)
            

    def euler2(self,
              y0: list | np.ndarray | Array,
              x0: int | float | None = None,
              xf: int | float | None = None,
              graphic: bool = False):

        
        if self._limit_check(x0,xf):            
            if self.x_interval is None:
                self.x_interval = np.array([x0,xf])
        else:
            x0 = min(self.__x_interval)
            xf = max(self.__x_interval)
        step = (xf-x0)/self.n
        aux_x = np.arange(x0, xf, step)
        aux_y = self.euler(y0,x0,xf).solutions.transpose()
        y = np.zeros((len(y0),self.n)).transpose()
        y[0] = y0
        for i in range(1,self.n-1): 
            y[i] = y[i-1] + step*((aux_y[i]-aux_y[i-1])/step+(aux_y[i+1]-aux_y[i])/step)/2
        y[-1] = aux_y[-1]
        y = y.transpose()
        if graphic:
            aux = SolutionODE(y,iterations=self.n,decimals=self.decimals,x_interval=self.x_interval)
            aux.to_graphic()
            return aux
        return SolutionODE(y,iterations=self.n,decimals=self.decimals,x_interval=self.x_interval)
        
    def heun(self,
              y0: list | np.ndarray | Array,
              x0: int | float | None = None,
              xf: int | float | None = None,
              graphic: bool = False):

        
        if bool(self._limit_check(x0,xf)):            
            if self.x_interval is None:
                self.x_interval = np.array([x0,xf])
        else:
            x0 = min(self.__x_interval)
            xf = max(self.__x_interval)
        step = (xf-x0)/self.n
        aux_x = np.arange(x0, xf, step)
        y = np.zeros((len(y0),self.n)).transpose()
        y[0] = y0
        for i in range(self.n-1):
            y[i+1] = y[i] + step*self.functions(aux_x[i],*y[i])
            y[i+1] = y[i] + (step/2)*(self.functions(aux_x[i],*y[i])+self.functions(aux_x[i+1],*y[i+1]))
        y=y.transpose()
        if graphic:
            aux = SolutionODE(y,iterations=self.n,decimals=self.decimals,x_interval=self.x_interval)
            aux.to_graphic()
            return aux
        return SolutionODE(y,iterations=self.n,decimals=self.decimals,x_interval=self.x_interval)

    def nystrom(self,
              y0: list | np.ndarray | Array,
              x0: int | float | None = None,
              xf: int | float | None = None,
              graphic: bool = False):
        
        
        if bool(self._limit_check(x0,xf)):            
            if self.x_interval is None:
                self.x_interval = np.array([x0,xf])
        else:
            x0 = min(self.__x_interval)
            xf = max(self.__x_interval)
        step = (xf-x0)/self.n
        aux_x = np.arange(x0, xf, step)
        y = np.zeros((len(y0),self.n)).transpose()
        k1,k2,k3 = y.copy(),y.copy(),y.copy()
        y[0] = y0

        for i in range(self.n-1):
            k1[i] = self.functions(aux_x[i],*y[i])
            k2[i] = self.functions(aux_x[i]+2*step/3, *(y[i]+2*step*k1[i]/3))
            k3[i] = self.functions(aux_x[i]+2*step/3, *(y[i]+2*step*k2[i]/3))
            y[i+1] = y[i] + (step/4)*(k1[i]+(3/2)*(k2[i]+k3[i]))
        y=y.transpose()
        if graphic:
            aux = SolutionODE(y,iterations=self.n,decimals=self.decimals,x_interval=self.x_interval)
            aux.to_graphic()
            return aux
        return SolutionODE(y,iterations=self.n,decimals=self.decimals,x_interval=self.x_interval)
        
    def rk4(self,
            y0: list | np.ndarray | Array,
            x0: int | float | None = None,
            xf: int | float | None = None,
            graphic: bool = False):

        
        if bool(self._limit_check(x0,xf)):            
            if self.x_interval is None:
                self.x_interval = np.array([x0,xf])
        else:
            x0 = min(self.__x_interval)
            xf = max(self.__x_interval)
        step = (xf-x0)/self.n
        aux_x = np.arange(x0, xf, step)
        y = np.zeros((len(y0),self.n)).transpose()
        k1,k2,k3,k4 = y.copy(),y.copy(),y.copy(),y.copy()
        y[0] = y0
        for i in range(self.n-1):
            k1[i] = step * self.functions(aux_x[i], *y[i])
            k2[i] = step * self.functions(aux_x[i] + step / 2, *(y[i] + k1[i] / 2))
            k3[i] = step * self.functions(aux_x[i] + step / 2, *(y[i] + k2[i] / 2))
            k4[i] = step * self.functions(aux_x[i] + step, *(y[i] + k3[i]))
            y[i+1] = y[i] + (k1[i] + 2 * (k2[i] + k3[i]) + k4[i]) / 6
        y=y.transpose()
        if graphic:
            aux = SolutionODE(y,iterations=self.n,decimals=self.decimals,x_interval=self.x_interval)
            aux.to_graphic()
            return aux
        return SolutionODE(y,iterations=self.n,decimals=self.decimals,x_interval=self.x_interval)

    def adams_bashforth(self,
                        y0: list | np.ndarray | Array,
                        x0: int | float | None = None,
                        xf: int | float | None = None,
                        graphic: bool = False):
        
        
        if bool(self._limit_check(x0,xf)):            
            if self.x_interval is None:
                self.x_interval = np.array([x0,xf])
        else:
            x0 = min(self.__x_interval)
            xf = max(self.__x_interval)
        step = (xf-x0)/self.n
        aux_x = np.arange(x0, xf, step)
        y = np.zeros((len(y0),self.n)).transpose()
        k1,k2,k3,k4 = y.copy(),y.copy(),y.copy(),y.copy()
        y[0] = y0
        return SolutionODE(y,iterations=self.n,decimals=self.decimals,x_interval=self.x_interval)

    def adams_moulton(self,
                      y0: list | np.ndarray | Array,
                      x0: int | float | None = None,
                      xf: int | float | None = None,
                      graphic: bool = False):
        
        
        if bool(self._limit_check(x0,xf)):            
            if self.x_interval is None:
                self.x_interval = np.array([x0,xf])
        else:
            x0 = min(self.__x_interval)
            xf = max(self.__x_interval)
        step = (xf-x0)/self.n
        aux_x = np.arange(x0, xf, step)
        y = np.zeros((len(y0),self.n)).transpose()
        k1,k2,k3,k4 = y.copy(),y.copy(),y.copy(),y.copy()
        y[0] = y0
        return SolutionODE(y,iterations=self.n,decimals=self.decimals,x_interval=self.x_interval)

    def adams3(self,
               y0: list | np.ndarray | Array,
               x0: int | float | None = None,
               xf: int | float | None = None,
               graphic: bool = False):
        
        
        if bool(self._limit_check(x0,xf)):            
            if self.x_interval is None:
                self.x_interval = np.array([x0,xf])
        else:
            x0 = min(self.__x_interval)
            xf = max(self.__x_interval)
        step = (xf-x0)/self.n
        aux_x = np.arange(x0, xf, step)
        y = np.zeros((len(y0),self.n)).transpose()
        k1,k2,k3,k4 = y.copy(),y.copy(),y.copy(),y.copy()
        y[0] = y0
        return SolutionODE(y,iterations=self.n,decimals=self.decimals,x_interval=self.x_interval)

    def adams4(self,
               y0: list | np.ndarray | Array,
               x0: int | float | None = None,
               xf: int | float | None = None,
               graphic: bool = False):
        
        
        if bool(self._limit_check(x0,xf)):            
            if self.x_interval is None:
                self.x_interval = np.array([x0,xf])
        else:
            x0 = min(self.__x_interval)
            xf = max(self.__x_interval)
        step = (xf-x0)/self.n
        aux_x = np.arange(x0, xf, step)
        y = np.zeros((len(y0),self.n)).transpose()
        k1,k2,k3,k4 = y.copy(),y.copy(),y.copy(),y.copy()
        y[0] = y0
        return SolutionODE(y,iterations=self.n,decimals=self.decimals,x_interval=self.x_interval)

    def shooting(self,
              y0: list | np.ndarray | Array,
              x0: int | float | None = None,
              xf: int | float | None = None,
              graphic: bool = False):
        
        
        if bool(self._limit_check(x0,xf)):            
            if self.x_interval is None:
                self.x_interval = np.array([x0,xf])
        else:
            x0 = min(self.__x_interval)
            xf = max(self.__x_interval)
        step = (xf-x0)/self.n
        aux_x = np.arange(x0, xf, step)
        y = np.zeros((len(y0),self.n)).transpose()
        k1,k2,k3,k4 = y.copy(),y.copy(),y.copy(),y.copy()
        y[0] = y0
        return SolutionODE(y,iterations=self.n,decimals=self.decimals,x_interval=self.x_interval)

# self,
#               y0: list | np.ndarray | Array,
#               x0: int | float | None = None,
#               xf: int | float | None = None,
#               graphic: bool = False
    def bvp(self,
            y0: list[int | float] | np.ndarray | Array,
            yf: list[int | float],
            x0: int | float | None = None,
            xf: int | float | None = None,
            graphic: bool = False,
            n: int = 10*const.ITERATIONS) -> list[np.ndarray]:

        pass


class PDE:
    pass

class SolutionODE:
    def __init__(self, solutions: list | np.ndarray | pd.core.frame.DataFrame,
                 functions: list | None = None,
                 iterations: int = 10*const.ITERATIONS,
                 decimals: int = 4,
                 x_interval: list = None) -> None:

        self.__x_interval = x_interval
        self.__n = iterations
        self.__decimals = decimals
        self.__exact = functions
        if isinstance(solutions, pd.core.frame.DataFrame):
            self.__frame_format = solutions
            solutions.reset_index(inplace=True)
            aux = solutions.T.to_numpy()
            self.__x = aux[0]
            self.__solutions = aux[1:]
        elif isinstance(solutions, list | np.ndarray):
            self.__x = np.arange(self.x_interval[0],self.x_interval[1],(self.x_interval[1]-self.x_interval[0])/iterations)
            self.__solutions = solutions
            self.__frame_format = self.to_frame()
        else:
            raise TypeError


    @property
    def x_interval(self):
        return self.__x_interval

    @property
    def n(self):
        return self.__n
    
    @property
    def decimals(self):
        return self.__decimals

    @property
    def exact(self):
        return self.__exact

    @exact.setter
    def exact(self, arg):
        self.__exact = arg

    @property
    def x(self):
        return self.__x
    
    @property
    def solutions(self):
        return self.__solutions

    @property
    def frame_format(self):
        return self.__frame_format

    def __str__(self) -> str:
        return str(self.solutions)

    def error(self, n:int = 10*const.ITERATIONS, type: str = 'abs'):
        x = np.arange(self.x_interval[0],self.x_interval[1],(self.x_interval[1]-self.x_interval[0])/n)
        y_ideal = [element(x) for element in self.exact]
        abs_err = y_ideal - self.solutions # self.solutions must be array here !!!!!!!!!!!!!!!
        rel_err = abs_err/y_ideal
        if type == 'abs':
            return [max(element).round(self.decimals) for element in abs_err]
        elif type == 'rel':
            return [max(element).round(self.decimals) for element in rel_err]
        elif type == 'percent':
            return [100*max(element).round(self.decimals) for element in rel_err]
        else: 
            raise ValueError # InvalidArgumentError

    def to_graphic(self,
                    title: str = 'graphic',
                    x_axis:str='x axis',
                    y_axis: str = 'y axis',
                    color: list[str] | None = None,
                    label:list[str] | None= None,
                    style: list[str] | str = None,
                    legend_loc: str | None = None)-> None:

        l = []
        xl = plt.xlabel(x_axis)
        yl = plt.ylabel(y_axis)
        ttl = plt.title(title)
        color_list = ['r','b','k','g','y','c']
        if color is None:
            color = color_list
        if label is None:
            label = [f'y{i+1}' for i in range(len(self.solutions))]
        if legend_loc is None:
            legend_loc = 'upper right'
        for i,yk in enumerate(self.solutions):
            l.append(plt.plot(self.x,yk,color[i], label=label[i]))
        ll = plt.legend(loc= legend_loc)
        plt.show()  
        l.clear()
    
    def cross_map(self, i: int, j: int,
                    title: str = 'graphics',
                    x_axis:str='x axis',
                    y_axis: str = 'y axis',
                    color: str | None = None,
                    label:str | None = None,
                    style: str | None = None,
                    legend_loc: str | None = None)-> None:
        xl = plt.xlabel(x_axis)
        yl = plt.ylabel(y_axis)
        ttl = plt.title(title)
        color_list = 'b'
        if color is None:
            color = color_list
        if label is None:
            label = f'y{i} X y{j}'
        if legend_loc is None:
            legend_loc = 'upper right'
        if style is None:
            style = '-'
        plt.plot(self.solutions[i-1],self.solutions[j-1],color = color,label=label,ls=style)
        ll = plt.legend(loc= legend_loc)
        plt.show()

    def to_frame(self):
        d = {}
        d['x']=self.x.round(self.decimals)
        for i,element in enumerate(self.__solutions):
            d[f'y{i+1}'] = element
        df = pd.DataFrame(data=d)
        df.set_index('x',inplace=True)
        return df    



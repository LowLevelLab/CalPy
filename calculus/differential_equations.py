from imports import *
from calculus.functions import Function
from linalg.arrays import Vector



class ODE:
    def __init__(self,
                 functions: Union[list,np.ndarray],
                 x: Optional[Union[list,np.ndarray]]= None,
                 iterations: int = 10*c.ITERATIONS,
                 decimals: int = 4) -> None:

        if isinstance(x, Union[list,np.ndarray]):
            self.__x_interval = np.array(x)
        else:
            self.__x_interval = None
        if not isinstance(functions, list):
            l = [functions]
            functions = l
        self.__functions = Vector(functions)
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
              df: bool = True):

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
            y[i] = y[i-1] + step*(self.functions(aux_x[i], *y[i-1])).array
        y = y.transpose()
        if graphic:
            self.to_graphic(y=y)
        if df:
            return self.to_frame(aux_x,y)
        else:
            return y
            

    def euler2(self,
               y0:Union[list,np.ndarray],
               x0: Optional[Union[int,float]]=None,
               xf: Optional[Union[int,float]]=None,
               graphic: bool = False,
               df: bool = True):

        
        if bool(self._limit_check(x0,xf)):            
            if self.x_interval is None:
                self.x_interval = np.array([x0,xf])
        else:
            x0 = min(self.__x_interval)
            xf = max(self.__x_interval)
        step = (xf-x0)/self.n
        aux_x = np.arange(x0, xf, step)
        aux_y = self.euler(y0,x0,xf,df=False).transpose()
        y = np.zeros((len(y0),self.n)).transpose()
        y[0] = y0
        for i in range(1,self.n-1): 
            y[i] = y[i-1] + step*((aux_y[i]-aux_y[i-1])/step+(aux_y[i+1]-aux_y[i])/step)/2
        y[-1] = aux_y[-1]
        y = y.transpose()
        if graphic:
            self.to_graphic(y=y)
        if df:
            return self.to_frame(aux_x,y)
        else:
            return y
        
    def heun(self,
             y0:Union[list,np.ndarray],
             x0: Optional[Union[int,float]]=None,
             xf: Optional[Union[int,float]]=None,
             graphic: bool = False,
             df: bool = True):

        
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
            self.to_graphic(y=y)
        if df:
            return self.to_frame(aux_x,y)
        else:
            return y

    def nystrom(self, 
                y0:Union[list,np.ndarray],
                x0: Optional[Union[int,float]]=None,
                xf: Optional[Union[int,float]]=None,
                graphic: bool = False,
                df: bool = True):
        
        
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
            self.to_graphic(y=y)
        if df:
            return self.to_frame(aux_x,y)
        else:
            return y
        
    def rk4(self, 
            y0:Union[list,np.ndarray],
            x0: Optional[Union[int,float]]=None,
            xf: Optional[Union[int,float]]=None,
            graphic: bool = False,
            df: bool = True):

        
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
            self.to_graphic(y=y)
        if df:
            return self.to_frame(aux_x,y)
        else:
            return y

    def adams_bashforth(self,
                        y0:Union[list,np.ndarray],
                        x0: Optional[Union[int,float]]=None,
                        xf: Optional[Union[int,float]]=None,
                        graphic: bool = False,
                        df: bool = True):
        
        
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

    def adams_moulton(self,
              y0:Union[list,np.ndarray],
              x0: Optional[Union[int,float]]=None,
              xf: Optional[Union[int,float]]=None,
              graphic: bool = False,
              df: bool = True):
        
        
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

    def adams3(self,
               y0:Union[list,np.ndarray],
               x0: Optional[Union[int,float]]=None,
               xf: Optional[Union[int,float]]=None,
               graphic: bool = False,
               df: bool = True):
        
        
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

    def adams4(self,
               y0:Union[list,np.ndarray],
               x0: Optional[Union[int,float]]=None,
               xf: Optional[Union[int,float]]=None,
               graphic: bool = False,
               df: bool = True):
        
        
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

    def shooting(self,
                 y0:Union[list,np.ndarray],
                 x0: Optional[Union[int,float]]=None,
                 xf: Optional[Union[int,float]]=None,
                 graphic: bool = False,
                 df: bool = True):
        
        
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

    def bvp(self, 
            y0: list[Union[int,float]], 
            yf: list[Union[int,float]],
            x0: Optional[Union[int,float]]=None,
            xf: Optional[Union[int,float]]=None,
            graphic: bool = False,
            df: bool = True,
            n: int = 10*c.ITERATIONS) -> list[np.ndarray]:

        pass
        

    def to_graphic(self,
                    data = None,
                    y: list = None,
                    title: str = 'graphics',
                    x_axis:str='x axis',
                    y_axis: str = 'y axis',
                    color: Optional[str] = None,
                    label:Optional[list] = None,
                    legend_loc: Optional[str] = None)-> None:

        l = []
        x = np.arange(self.x_interval[0],self.x_interval[1],(self.x_interval[1]-self.x_interval[0])/self.n)
        xl = plt.xlabel(x_axis)
        yl = plt.ylabel(y_axis)
        ttl = plt.title(title)
        color_list = ['r','b','k','g','y','c']
        if y is None:
            pass
        if color is None:
            color = color_list
        if label is None:
            label = [f'y{i+1}' for i in range(len(y))]
        if legend_loc is None:
            legend_loc = 'upper right'
        for i,yk in enumerate(y):
            l.append(plt.plot(x,yk,color[i], label=label[i]))
        ll = plt.legend(loc= legend_loc)
        plt.show()

    
    def to_frame(self, x:np.ndarray, y:np.ndarray) -> pd.core.frame.DataFrame:
        d = {}
        d['x']=x.round(self.decimals)
        for i,element in enumerate(y):
            d[f'y{i+1}'] = element
        df = pd.DataFrame(data=d)
        df.set_index('x',inplace=True)
        return df

    def error(self, functions: list, y:np.ndarray, n:int = 10*c.ITERATIONS, type: str = 'abs'):
        x = np.arange(self.x_interval[0],self.x_interval[1],(self.x_interval[1]-self.x_interval[0])/n)
        y_ideal = [element(x) for element in functions]
        abs_err = y_ideal - y
        rel_err = abs_err/y_ideal
        if type == 'abs':
            return [max(element).round(self.decimals) for element in abs_err]
        elif type == 'rel':
            return [max(element).round(self.decimals) for element in rel_err]
        elif type == 'percent':
            return [100*max(element).round(self.decimals) for element in rel_err]
        else: 
            raise ValueError(f'Invalid argument: {type}. It must be either \'abs\', \'rel\' or \'percent\'')
        


class PDE:
    pass

from imports import *
from interpolation.interpolation import LagrangeInterpolation



class Function:
    def __init__(self, f):
        self.__function = f

    @property
    def function(self):
        return self.__function

    def __add__(self, other):
        if isinstance(other, Function):
            return Function(lambda x: self.function(x) + other.function(x))
        elif isinstance(other,Union[float,int]):
            return Function(lambda x: self.function(x) + other)

    def __radd__(self,other):
        return self.__add__(other)
        
    def __iadd__(self,other):
        return self.__add__(other) 

    def __neg__(self):
        return 0-self

    def __sub__(self, other):
        if isinstance(other, Function):
            return Function(lambda x: self.function(x) - other.function(x))
        elif isinstance(other,Union[float,int]):
            return Function(lambda x: self.function(x) - other)

    def __rsub__(self,other):
        return self.__sub__(other)

    def __mul__(self, other):
        if isinstance(other, Function):
            return Function(lambda x: self.function(x) * other.function(x))
        elif isinstance(other,Union[float,int]):
            return Function(lambda x: self.function(x) * other)

    def __rmul__(self,other):
        return self.__mul__(other)

    def __imul__(self,other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, Function):
            return Function(lambda x: self.function(x) / other.function(x))
        elif isinstance(other,Union[float,int]):
            pass

    def __eq__(self, other):
        x = np.arange(0, 10, 10/1000)
        aux = self-other
        return all(aux(x)==0.0)
    
    def __call__(self, *args: Union[int,float,list,tuple,np.ndarray]):
        if all([isinstance(i,Union[float,int]) for i in args]):
            return self.function(*args)
        else:
            try:
                if all([len(args[0]) == len(args[i]) for i in range(len(args))]):
                    args = [np.array(element) for element in args]
                    return self.function(*args)
            except TypeError:
                raise TypeError("Invalid types")

    """
    ### BASIC METHODS ###
    """


    # FIXED POINT THEOREM

    @staticmethod
    def fixed_point_theorem(iteration_function, interval):
        aux_function = Function(iteration_function)
        for element in interval:
            if abs(aux_function.derivative(element)) >= 1:
                raise Exception('This iteration function is not valid in given interval')

    # DERIVATIVE OF THE FUNCTION

    def derivative(self, x0: Union[float,int], interval: float=c.DELTA) -> float:
        return (self.function(x0 + interval) - self.function(x0)) / interval

    # N-TH DERIVATIVE

    def nth_derivative(self, x0:Union[float,int], n: int, delta_x: float = c.ERROR):
        if n < 0:
            raise ValueError("n must be non-negative")
        if n == 0:
            return self.function(x0)
        if n == 1:
            return self.derivative(x0)
        return derivative(self.function, x0, n=n, order=2*n+1)

    def to_frame(self, *args) -> pd.core.frame.DataFrame:
        aux = pd.DataFrame(data= [list(*args),self(*args)],index=['x','f(x)']).T
        aux.set_index('x', inplace=True)
        return aux


    """
    ### ROOT-FINDING METHODS ###
    """


    # NEWTON-RAPHSON METHOD

    def newton_raphson(self, x: Union[float,int], 
                       iterations: int = c.ITERATIONS, 
                       error: float = c.ERROR) -> float:
        count = 0
        prev = x
        x = x - self.function(x) / self.derivative(x)
        while count < iterations - 1 and abs(x - prev) > error:
            # for i in range(1000):
            prev = x
            x = x - self.function(x) / self.derivative(x)
            count = count + 1
        return x

    # VALIDATION BISECTION METHOD

    def validation_bisection(self, lower: Union[float,int], upper: Union[float,int]) -> bool:
        return self.function(lower) * self.function(upper) < 0

    # BISECTION METHOD

    def bisection(self, 
                  lower: Union[float,int], 
                  upper: Union[float,int], 
                  iterations: int = c.ITERATIONS, 
                  error: float = c.ERROR) -> float:
        if not self.validation_bisection(lower, upper):
            raise Exception('the interval chosen cannot')
        mean_value = (lower + upper) / 2
        if iterations <= 0:
            raise Exception('Insufficient number of iterations')
        if abs(self.function(mean_value)) <= error:
            return mean_value
        elif self.function(lower) * self.function(mean_value) > 0:
            return self.bisection(mean_value, upper, iterations - 1)
        elif self.function(upper) * self.function(mean_value) > 0:
            return self.bisection(lower, mean_value, iterations - 1)

    # FALSE POSITION METHOD

    def false_position(self, lower: Union[float,int],
                       upper: Union[float,int],
                       iterations: int = c.ITERATIONS,
                       error: float = c.ERROR) -> float:
        x_0 = lower
        x_1 = upper
        for i in range(iterations):
            x = x_0 - self.function(x_0) * (x_1 - x_0) / (self.function(x_1) - self.function(x_0))
            x_0 = x_1
            x_1 = x
            if abs(self.function(x)) < error:
                break
        return x_1

    # FIXED POINT METHOD

    @staticmethod
    def fixed_point(iteration_function, x: Union[float,int], interval: list[Union[float,int]],
                    iterations: int = c.ITERATIONS // 100,
                    error: float = c.ERROR) -> float:
        Function.fixed_point_theorem(iteration_function, interval)
        for iteration in range(iterations):
            x1 = iteration_function(x)
            if abs(x1 - x) <= error:
                break
            x = x1
        return x

    def steffensen(self,
                   x0:Union[int,float],
                   error: float = c.ERROR,
                   iter: int = c.ITERATIONS) -> Union[float,int]:
        g = lambda x: self(x+self(x))/self(x) - 1
        i = 0
        xk = [x0]
        yk = [self(x0)]

        while(abs(self(xk[-1])) > error or i > iter):

            x = xk[-1] - self(xk[-1])/g(xk[-1])
            
            xk.append(x)
            yk.append(self(x))
        
        # print(xk)
        # print(yk)

        return xk[-1]


    """
    ### INTEGRAL OF THE FUNCTION ###
    """

    # RECTANGLE RULE

    def rectangle_integration(self,
                              lower: Union[float,int],
                              upper: Union[float,int],
                              factor: int = c.FACTOR) -> float:
        h = (upper - lower) / factor
        x = np.arange(lower + h / 2, upper - h / 2, factor)
        integral = 0
        for element in x:
            integral += self.function(element) * h
        return integral

    # SIMPSON RULE

    def simpson_13_method(self,
                          lower: Union[float,int],
                          upper: Union[float,int],
                          factor: int = 3 * c.FACTOR) -> float:

        h = (upper - lower) / factor
        integration = self.function(lower) + self.function(upper)
        for i in range(1, factor):
            k = lower + i * h
            if i % 2 == 0:
                integration = integration + 2 * self.function(k)
            else:
                integration = integration + 4 * self.function(k)
        integration = integration * h / 3
        return integration

    # ROMBERG METHOD

    def romberg_integration(self,
                            lower: Union[float,int],
                            upper: Union[float,int],
                            error: float = c.ERROR) -> float:
        def richardson(r,k):
            for alfa in range(k-1,0,-1):
                c = 4**(k-alfa)
                r[alfa]=(c * r[alfa + 1] - r[alfa])/(c - 1.0)
            return r
        
        r = np.zeros(21)
        r[1] = self.trapeze_method(lower,upper)
        R = r[1]
        for k in range(2,21):
            r[k] = self.trapeze_method(lower,upper,guess=r[k-1], factor=k)
            r = richardson(r,k)
            if abs(r[1] - R) < error * max(abs(r[1]), 1.0):
                return r[1]
            R=r[1]
        raise ValueError("Romberg method does not converge")
        
    # TRAPEZE METHOD

    def trapeze_method(self,
                       lower: Union[float,int], 
                       upper: Union[float,int],
                       guess: Union[float,int] = 0,
                       factor: float = c.FACTOR/4) -> float:

        if factor == 1:
            I = (self.function(lower)+self.function(upper))*(lower+upper)/2
        else:
            N = 2**(factor-2)
            dx = (upper-lower)/N
            x = lower + dx/2
            s = 0
            for i in range(N):
                s += self.function(x)
                x+= dx
            I = (guess + dx * s)/2.0
        return I


    """
    ### TAYLOR ###
    """

    # TAYLOR SERIES

    def taylor_series(self, order: int, x0: Union[float,int], round: Optional[int] = None):
        from poly.polynomials import Polynomial
        l = np.zeros(order+1)
        for i in range(order+1):
            l[i] = self.nth_derivative(x0,i)/scp.factorial(i)
            if round is not None:
                l[i] = l[i].round(round)
        return Polynomial(l)
        


    """
    ### PLOTTING FUNCTION ###
    """

    def plot_function(self,x: Union[list,tuple,np.ndarray],
                      x_axis: str = 'x axis',
                      y_axis: str = 'y axis',
                      title: str = 'function',
                      color: str = 'r',
                      label: str = 'f(x)',
                      local_legend: str = 'upper right',
                      style: str = '-') -> None:
        
        y = [self.function(xk) for xk in x]
        xl = plt.xlabel(x_axis)
        yl = plt.ylabel(y_axis)
        ttl = plt.title(title)
        la = plt.plot(x, y, color, label=label, ls = style)
        ll=plt.legend(loc = local_legend)
        plt.show()

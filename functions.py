import constants as c
from polynomials import Polynomial
import numpy as np
import scipy.special as scp
import matplotlib.pyplot as plt
from typing import Optional, Union
import pandas as pd


class Function:
    def __init__(self, f):
        self.__function = f

    @property
    def function(self):
        return self.__function

    def __add__(self, other):
        addition = Function(self.function + other.function)
        return addition

    def __sub__(self, other):
        subtraction = Function(self.function - other.function)
        return subtraction

    def __mul__(self, other):
        multiplication = Function(self.function * other.function)
        return multiplication

    def __call__(self, *args: Union[int,float,list,tuple,np.ndarray]):
        if all([isinstance(i,Union[float,int]) for i in args]):
            return np.array(self.function(*args))
        else:
            try:
                if all([len(args[0]) == len(args[i]) for i in range(len(args))]):
                    args = [np.array(element) for element in args]
                    return self.function(*args)
            except TypeError:
                raise TypeError("Invalid types")


    def __eq__(self, other):
        # x = np.arange(0, 10, 1000)
        # if self.function(x) == other.function(x):
        #     return True
        # return False
        pass

    def __truediv__(self, other):
        division = Function(self.function / other.function)
        return division

    def __abs__(self):
        return abs(self.function)

    def __str__(self):
        pass


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

    # N-th DERIVATIVE

    def nth_derivative(self, x0:Union[float,int], n: int, delta_x: float = c.DELTA):
        if n < 0:
            raise ValueError("n must be non-negative")
        if n == 0:
            return self.function(x0)
        if n == 1:
            return self.derivative(x0)
        return ((self.nth_derivative(x0+ delta_x, n-1)-self.nth_derivative(x0-delta_x,n-1))/2*delta_x)

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

    def steffensen(self) -> Union[float,int]:
        g = lambda x: self(x+self(x))/self(x) - 1
        pass

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

    def taylor_series(self, order: int, x0: Union[float,int]) -> Polynomial:
        l = []
        for i in range(order):
            l.append(self.nth_derivative(x0,i)*x0**i/scp.factorial(i))
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
                      local_legend: str = 'upper right') -> None:
        
        y = [self.function(xk) for xk in x]
        xl = plt.xlabel(x_axis)
        yl = plt.ylabel(y_axis)
        ttl = plt.title(title)
        la = plt.plot(x, y, color, label=label)
        if local_legend is not None:
            ll=plt.legend(loc = local_legend)
        plt.show()


    """
    ### TRANSFORMS ###
    """


    def laplace(self):
        pass

    def fourier(self):
        pass

    """
    def steffesen(f, x0, tol, maxIter):

    def g(x):
        return (f(x + f(x))/f(x)) - 1;

    i = 0;
    x_k = [x0];
    y_k = [f(x0)];

    while(abs(f(x_k[-1])) > tol or i > maxIter):

        next_x = x_k[-1] - f(x_k[-1])/g(x_k[-1]);
        
        x_k.append(next_x);
        y_k.append(f(next_x));

    # print(x_k);
    # print(y_k);    

    return x_k[-1];
"""


class MVFunction:
    pass


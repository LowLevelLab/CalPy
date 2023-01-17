from imports import *



class RandomVariable:
    def __init__(self, data = None,
                 mean: Union[float,int] = 0,
                 variance: Union[float,int] = 0) -> None:
        self.__mean = mean 
        self.__var = variance
        self.__data = data
        if isinstance(data, pd.core.frame.DataFrame):
            aux = data.describe()
            self.__mean, self.__var = aux[1][1], (aux[1][2])**2

    @property
    def mean(self):
        return self.__mean

    @property
    def var(self):
        return self.__var

    def describe(self):
        print(f'mean: {self.mean}')
        print(f'std: {np.sqrt(self.var)}')

    def __add__(self, other):
        if isinstance(other, RandomVariable):
            return RandomVariable(mean= self.mean + other.mean,
                                  variance=self.var + other.var)
        elif isinstance(other, Union[float,int]):
            return RandomVariable(mean = self.mean + other,
                                  variance= self.var)
        else:
            raise TypeError
    
    def __sub__(self, other):
        if isinstance(other, RandomVariable):
            return RandomVariable(mean= self.mean - other.mean,
                                  variance=self.var - other.var)
        elif isinstance(other, Union[float,int]):
            return RandomVariable(mean = self.mean - other,
                                  variance= self.var)
        else:
            raise TypeError

    def __mul__(self, other):
        if isinstance(other, RandomVariable):
            pass
        elif isinstance(other, Union[float,int]):
            return RandomVariable(mean = self.mean * other, variance= self.var * np.sqrt(other))
        else:
            raise TypeError

    def __truediv__(self, other):
        if isinstance(other, RandomVariable):
            pass
        elif isinstance(other, Union[float,int]):
            return RandomVariable(mean = self.mean / other, variance= self.var / np.sqrt(other))
        else:
            raise TypeError

    def standardize(self):
        pass

    def weak_law(self):
        pass

    def central_limit(self):
        pass
    

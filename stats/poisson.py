from stats.bernoulli import *



class Poisson:
    def __init__(self, lam: Union[int,float]) -> None:
        self.prob = lam
        pass
    
    def __add__(self,other):
        if isinstance(other, Poisson):
            return Poisson(self.prob+other.prob)
        else: 
            raise TypeError

    def __sub__(self,other):
        if isinstance(other, Poisson):
            return Poisson(self.prob-other.prob)
        else: 
            raise TypeError
            
    def __mul__(self,other):
        if isinstance(other, int):
            return Bernoulli(self.prob*other)
        else:
            raise TypeError

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self,other):
        if isinstance(other, int):
            return Bernoulli(self.prob/other)
        else:
            raise TypeError
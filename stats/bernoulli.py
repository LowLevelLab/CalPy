from imports import *


class Bernoulli:
    def __init__(self, p: float) -> None:
        self.prob = p
        pass

    def __add__(self,other):
        if isinstance(other, Bernoulli):
            return Bernoulli(self.prob+other.prob)
        else: 
            raise TypeError

    def __sub__(self,other):
        if isinstance(other, Bernoulli):
            return Bernoulli(self.prob-other.prob)
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
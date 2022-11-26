import numpy as np
import matplotlib.pyplot as plt
from functions import Function
from polynomials import Polynomial
from array import Matrix, Array, Vector



class ODE:
    def __init__(self, x:list, functions:list[function]) -> None:
        self.__x_interval = x
        self.__functions = functions

    def euler(self, y0:list)-> list:
        pass
    def euler2(self, y0:list)-> list:
        pass
    def rk4(self, y0:list)-> list:
        pass
    def heun(self, y0:list)-> list:
        pass

    def _to_graphic(self, y: list)-> None:
        pass
    


class PDE:
    pass

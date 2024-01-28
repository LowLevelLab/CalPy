# from imports import *
from time import time
from numba import jit, njit, int64, float64
import numpy as np
from linalg.arrays import Array, BoolArray


class Relation:
    def __init__(self, array) -> None:
        self.__matrix_form = BoolArray(array)

    @property
    def matrix_form(self) -> BoolArray:
        return self.__matrix_form

    def verify_reflexive(self) -> bool:
        for i in range(self.matrix_form.rows):
            if not self.matrix_form[i][i]:
                return False
            else:
                return True

    def verify_simmetry(self) -> bool:
        if self.matrix_form == self.matrix_form.transpose():
            return True
        return False

    def verify_transitive(self) -> bool:
        return self.matrix_form.compare_transitive()

    def verify_functional(self) -> bool:
        pass

    def verify_injective(self) -> bool:
        pass

    @staticmethod
    def prob_simmetry(n: int) -> float:
        pass
    
    @staticmethod
    def prob_reflexive(n: int) -> float:
        pass
    
    
    @staticmethod
    @jit(float64(int64), nopython=False)
    def prob_transitive(n: int) -> float:
        temp = time()
        aux = []
        for i in range(2**(n**2)):
            l = list(map(int,np.binary_repr(i, n**2)))
            aux.append(BoolArray(l,shape=(n,n)).compare_transitive())
            l.clear()
        aux = np.array(aux,dtype=np.int8)
        print(time()-temp)
        return (np.sum(aux), np.sum(aux)/aux.shape[0])

@jit(float64(int64),nopython=False)
def prob_transitives(n: int) -> float:
    # t = time()
    aux = np.zeros((2**(n**2),), dtype=np.bool_)
    for i in range(2**(n**2)):
        aux[i] = BoolArray(list(map(int, np.binary_repr(i, n**2))), shape=(n, n)).compare_transitive()
    count = np.sum(aux.astype(np.int32))
    # print(time()-t)
    return count / aux.size # count, prob
from imports import *
import linalg.arrays as arr
from discrete.boolArr import BoolMatrix


class Relation:
    def __init__(self, array) -> None:
        self.__matrix_form = BoolMatrix(array)

    @property
    def matrix_form(self) -> BoolMatrix:
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
    def prob_simmetry(self, n: int) -> tuple:
        pass
    
    @staticmethod
    def prob_reflexive(self, n: int) -> tuple:
        pass

    @staticmethod
    def prob_transitive(n: int) -> tuple:
        temp = time()
        l = []
        aux = []
        e = n**2
        for i in range(2**e):
            a = i
            while a != 0:
                if a%2:
                    l.append(0)
                else:
                    l.append(1)
                a = a>>1
            if len(l) != n**2:
                for element in [0 for element in range(n**2-len(l))]:
                    l.append(element)
            aux.append(int(BoolMatrix(arr.Matrix([l[len(l)//n*k:len(l)//n*(k+1)] for k in range(n)])).compare_transitive()))
            l.clear()
        print(time()-temp)
        return (sum(aux), sum(aux)/len(aux))



        

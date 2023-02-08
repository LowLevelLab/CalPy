from imports import *
import linalg.arrays as arr
from discrete.boolArr import BoolMatrix


class Relation:
    def __init__(self, array) -> None:
        self.__matrix_form = BoolMatrix(array)

    @property
    def matrix_form(self):
        return self.__matrix_form

    def verify_reflexive(self):
        for i in range(self.matrix_form.rows):
            if not self.matrix_form[i][i]:
                return False
            else:
                return True

    def verify_simmetry(self):
        if self.matrix_form == self.matrix_form.transpose():
            return True
        return False

    def verify_transitive(self):
        aux = self.matrix_form**2
        return aux.compare_transitive(self.matrix_form)
        

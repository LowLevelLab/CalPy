class Regression:
    def __init__(self, xlist: list, ylist: list):
        self.x = xlist
        self.y = ylist

    def __call__(self, kind: str):
        self.determine_function(kind)

    def determine_function(self, kind: str):
        if kind == 'exp':
            self.exp_regression()
        if kind == 'hpb':
            self.hyperbolic_regression()
        if kind == 'lin':
            self.lin_regression()
        if kind == 'log':
            self.log_regression()
        if kind == 'poly':
            self.poly_regression()
        if kind == 'pot':
            self.pot_regression()
        if kind == 'inv':
            self.inverse_regression()

    @staticmethod
    def term_by_term_product(array1: list, array2: list):
        vector: list = []
        for i in range(len(array1)):
            vector.append(array2[i] * array1[i])
        return vector

    @staticmethod
    def square_pot(array: list):
        vector: list = []
        for element in array:
            vector.append(element ** 2)
        return vector

    @staticmethod
    def linear_segmentation(lower: float, upper: float, factor: int):
        space = [lower]
        delta = (upper - lower) / factor
        for n in range(factor):
            space.append(space[n] + delta)
        return space

    @staticmethod
    def invert_list(array: list):
        vector = []
        for element in array:
            vector.append(1/element)
        return vector

    @staticmethod
    def log_applier(array: list):
        vector = []
        for element in array:
            vector.append()
        return vector

    @staticmethod
    def regression(x: list, y: list):
        m = (len(y) * sum(Regression.term_by_term_product(y, x))
             - sum(y) * sum(x)) / (
                    len(y) * sum(Regression.square_pot(x)) - sum(x) ** 2)

        b = (sum(Regression.square_pot(x)) * sum(y) - sum(x) * sum(
            Regression.term_by_term_product(y, x))) / (
                    len(y) * sum(Regression.square_pot(x)) - sum(x) ** 2)

        return m, b

    def exp_regression(self):
        pass

    def poly_regression(self):
        pass

    def inverse_regression(self):
        x_new = Regression.invert_list(self.x)
        m, b = Regression.regression(x_new, self.y)
        return f"y = {str(b)} + {str(m)}/x"

    def hyperbolic_regression(self):
        y_new = Regression.invert_list(self.y)
        m, b = Regression.regression(self.x, y_new)
        return f"y = 1/({str(b)} + {str(m)}x)"

    def log_regression(self):
        pass

    def pot_regression(self):
        pass

    def lin_regression(self):
        m, b = self.regression(self.x, self.y)
        return f"y = {str(b)} + {str(m)}x"

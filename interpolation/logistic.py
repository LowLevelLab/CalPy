from interpolation.regression import *



class LogisticRegression:
    def __init__(self) -> None:
        pass


"""
class LogisticRegression(Regression):
    def __init__(self, xlist: Union[list,np.ndarray], ylist: Union[list,np.ndarray], lim: Optional[Union[float,int]]=1) -> None:
        super().__init__(xlist, ylist)
        if isinstance(lim, Union[float,int]) and lim != 1:
            self.lim = lim
        else:
            self.lim=1

    def __str__(self) -> str:
        return str(self.lim) #f"y = {self.lim}/(1+e^({self.coeff[0]}*(x-{self.coeff[1]})))"

    def coeff_regression(self) -> tuple:
        pass

"""
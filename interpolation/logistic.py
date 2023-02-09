from interpolation.regression import *



class LogisticRegression(Regression):
    def __init__(self, xlist: Union[list,np.ndarray], ylist: Union[list,np.ndarray], lim: Optional[Union[float,int]]=1) -> None:
        super().__init__(xlist, ylist)
        self.lim = lim 
        if not isinstance(lim, Union[float,int]):
            raise TypeError("invalid type for arg: lim") 

    def __str__(self) -> str:
        return f"y = {self.lim}/(1+e^(-(x-{self.coeff[1]})/{self.coeff[0]}))"

    def coeff_regression(self) -> tuple:
        pass

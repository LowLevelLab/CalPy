from collections import OrderedDict

class Model:
    '''
    Base class for all neural network modules.
    '''

    def __init__(self):
        self._parameters = OrderedDict()
        self._modules = OrderedDict()
        self._buffers = OrderedDict()
        self.training = True

    def forward(self, *input): raise NotImplementedError()
    def backward(self, *gradwrtoutput): raise NotImplementedError()
    def reset_parameters(self): raise NotImplementedError()
    
    
    def parameters(self): pass
    def summary(self): pass
    def train(self): self.training = True
    def eval(self): self.training = False
    def fit(self): pass
    def compile(self): pass

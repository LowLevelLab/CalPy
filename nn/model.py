from collections import OrderedDict


class Model:
    '''
    Base class for all neural network modules.
    '''

    def __init__(self):
        self._parameters = OrderedDict()
        self._modules = OrderedDict()
        self._buffers = OrderedDict()
        self._hooks = OrderedDict()
        self.training = True

    def forward(self, *input): raise NotImplementedError()

    def backward(self, *gradwrtoutput):
        pass
        # grad_input = gradwrtoutput[0]
        # for hook in self._hooks.values():
        #     grad_input = hook(grad_input)

        # if not self._hooks:
        #     return
        # return grad_input

    def reset_parameters(self): raise NotImplementedError()

    def parameters(self): pass

    def summary(self): pass

    def train(self):
        self.training = True
        for module in self.children():
            module.train()

    def eval(self):
        self.training = False
        for module in self.children():
            module.eval()

    def children(self):
        if len(self._modules) == 0:
            for name, att in self.__dict__.items():
                if isinstance(att, Model):
                    self._modules[name] = att
        for name, module in self._modules.items():
            yield module
    def training_step(self): raise NotImplementedError()
    def on_training_epoch(self): pass
    def log(self): pass

    __call__ = forward

print(Model().__dict__)
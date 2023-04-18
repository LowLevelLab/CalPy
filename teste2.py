import numpy as np


class ArrayCarteado:
    def __init__(self, lista):
        self.array = np.array(lista)

    def __len__(self):
        return len(self.array)
    
    def __getitem__(self, index):
        return self.array[index]
    def __setitem__(self, index, value):
        self.array[index] = value
    
    def __call__(self, *args) :
        aux = np.zeros((len(self),len(self[0])))
        for i in range(len(self)):
            for j in range(len(self[0])):
                aux[i][j] = self[i][j](*args)
        return aux



class Array(np.ndarray):
    def __new__(cls, input_array, *, dtype=None, shape=None, order=None):
        obj = np.asarray(input_array)
        if dtype is not None:
            obj = obj.astype(dtype)
        if shape is not None:
            obj = obj.reshape(shape)
        if order is not None:
            obj = obj.copy(order=order)
        return obj.view(cls)
    
    
    # def __array_finalize__(self, obj: None | NDArray[Any], /) -> None:
    #     if obj is None:
    #         return
    
    def __call__(self, *args, **kwargs):
        values = [f(*args, **kwargs) for f in self.flat]
        return Array(values).reshape(self.shape)
    
    pass

class BoolArray(Array):
    def __new__(cls, input_array):
        return super().__new__(cls, input_array, dtype=np.bool_)
    
    # def __str__(self) -> str:
    #     return super().__str__()

# a = Array([[lambda x: x, lambda x: 2*x],[lambda x: 3*x, lambda x: 5*x]])
b = Array([1,2,4,],dtype=np.float64)
print(b)

c = BoolArray([1,2,4,])

print(c.astype(np.int8))
from imports import *
from complex import Complex


class Array:
    def __init__(self, arg: Union[list,np.ndarray]) -> None:
        self.array = np.array(arg)

    def __len__(self):
        return len(self.array)

    def __contains__(self, item):
        if item in self.array:
            return True
        return False

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < len(self.array):
            result = self.array[self.n]
            self.n += 1
            return result
        else:
            raise StopIteration

    def __eq__(self, other):
        if isinstance(self,Vector) and isinstance(other,Vector):
            for i,v in enumerate(self.array):
                if not (v == other[i]).tolist():
                    return False
            return True
        elif isinstance(self,Vector) and isinstance(other, Union[np.int32,np.int64,np.float32,np.float64,int,float]) and self.size != 0:
            return self[0] == other
        elif isinstance(self,Vector) and isinstance(other, Union[np.int32,np.int64,np.float32,np.float64,int,float]) and self.size == 0:
            return self.array == other
        else:
            return False
    
    def __add__(self, other):
        if isinstance(other, Union[list,np.ndarray]):
            if isinstance(self, Vector):
                return Vector(self.array + np.array(other))
        if isinstance(other, Union[Vector, Array]):
            if isinstance(self, Vector):
                return Vector(self.array + other.array)

    def __sub__(self, other):
        if isinstance(other, Union[list,np.ndarray]):
            if isinstance(self, Vector):
                return Vector(self.array - np.array(other))
        if isinstance(other, Union[Vector, Array]):
            if isinstance(self, Vector):
                return Vector(self.array - other.array)

    def __iadd__(self,other):
        self = self.__add__(other)

    def __isub__(self,other):
        self = self.__sub__(other)
    


    # !!!!!!!!!!!!! UPDATE !!!!!!!!!!!!!!!!!!

    def __getitem__(self, item):
        return Vector(self.array[item])

    def __setitem__(self, key, value):
        self.array[key] = value

    def __str__(self) -> str: 
        return str(self.array) ### !!! ###

    def copy(self):
        return Array(self.array.copy())


class Vector(Array):
    def __init__(self, arg: Union[list, slice, np.ndarray]) -> None:
        if not self.validate_entry(arg):
            raise ValueError
        super().__init__(arg)
        self.size = len(arg) if isinstance(arg,Union[list,np.ndarray]) else 0

    def validate_entry(self, arg):
        if isinstance(arg, Union[np.int32,np.int64,np.float32,np.float64,int,float]):
            return True
        try:
            arg[0][0]
            return False
        except:
            return True

    def __mul__(self, other):
        if isinstance(other, Union[float,int, Complex]):
            return Vector(self.array * other)
        elif isinstance(other, Vector):
            return self._dot_product(other)
        else:
            raise TypeError

    def __call__(self, *args):
        aux = [element(*args) for element in self.array]
        return Vector(aux)

    def __neg__(self):
        return self*(-1)

    def __abs__(self):
        return np.sqrt(np.sum(self.array**2))

    def __getitem__(self, item):
        return self.array[item]

    def _transpose_linear_system(self, other):
        return Vector((other.array.transpose()@self.array.transpose()).transpose())

    def _dot_product(self, other):
        return Vector(np.dot(self, other))

    def cross_product(self,other):
        return Vector(np.cross(self.array, other))

    def append(self, *args) -> None:
        for element in args:
            if not isinstance(element, Union[float,int,complex,Complex]):
                raise DimensionError
        original_size = len(self)
        final_size = self.size + len(args)
        self.array.resize(final_size, refcheck=False)
        for i in range(len(args)):
            self.array[original_size+i] = args[i]

    def to_list(self) -> list:
        return self.array.tolist()

    def to_numpy(self) -> np.ndarray:
        return self.array


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
        if isinstance(self,Matrix) and isinstance(other,Matrix):
            for i,v in enumerate(self.array):
                if not all((v == other[i]).tolist()):
                    return False
            return True
        elif isinstance(self,Vector) and isinstance(other,Vector):
            for i,v in enumerate(self.array):
                if not (v == other[i]).tolist():
                    return False
            return True
        else:
            return False
    
    def __add__(self, other):
        if isinstance(other, Union[list,np.ndarray]):
            if isinstance(self, Vector):
                return Vector(self.array + np.array(other))
            else:
                return Matrix(self.array + np.array(other))
        if isinstance(other, Union[Vector, Array, Matrix]):
            if isinstance(self, Vector):
                return Vector(self.array + other.array)
            else:
                return Matrix(self.array + other.array)

    def __sub__(self, other):
        if isinstance(other, Union[list,np.ndarray]):
            if isinstance(self, Vector):
                return Vector(self.array - np.array(other))
            else:
                return Matrix(self.array - np.array(other))
        if isinstance(other, Union[Vector, Array, Matrix]):
            if isinstance(self, Vector):
                return Vector(self.array - other.array)
            else:
                return Matrix(self.array - other.array)

    def __iadd__(self,other):
        return self.__add__(other)

    def __isub__(self,other):
        return self.__sub__(other)
    
    def __getitem__(self, item):
        return Vector(self.array[item])

    def __setitem__(self, key, value):
        self.array[key] = value

    def __str__(self) -> str: 
        return str(self.array) ### !!! ###



class Matrix(Array):

    """
    ### PROPERTIES ###
    """


    def __init__(self, arg: list) -> None:
        if not self.validate_entry(arg):
            raise ValueError
        super().__init__(arg)
        self.rows = len(self)
        self.cols = len(self[0])

    def validate_entry(self, arg):
        try:
            return all(len(arg[0])==len(arg[i]) for i in range(len(arg)))
        except:
            return False
        

    def __mul__(self, other):
        if isinstance(other, Union[float,int]):
            return Matrix(self.array * other)
        if isinstance(other, Matrix):
            return self._matrix_multiplication(other)
        if isinstance(other, Vector):
            return self._linear_system(other)
        else:
            raise TypeError

    def __rmul__(self, other):
        if isinstance(other, Union[int,float,Complex, complex]):
            return self.__mul__(other)

    def __imul__(self,other):
        return self.__mul__(other)

    def __pow__(self, index):
        if not isinstance(index,int):
            raise TypeError
        if index == 0:
            if len(self) == len(self[0]):
                return Matrix(np.identity(len(self)))
            else:
                raise DimensionError()
        elif index == 1:
            return self
        return self*self.__pow__(index-1)

    def __neg__(self):
        return self*(-1)


    """
    ### BASIC METHODS ###
    """


    def _matrix_multiplication(self, other):
        return Matrix(self.array @ other.array)

    def _linear_system(self, other):
        return Vector(self.array @ other.array)

    def det(self) -> float: ### !!!!!! ###
        return np.linalg.det(self.array)
    
    def find_row(self, row: list) -> int:
        for i, element in enumerate(self.array):
            if all(row[j]==element[j] for j in range(len(row))):
                return i 
        return -1

    def find_column(self, column:list) -> int:
        aux = Matrix(self.transpose())
        return aux.find_row(column)

    def transpose(self):
        return Matrix(self.array.transpose())

    def invert(self): 
        aux = np.linalg.inv(self.array)
        return Matrix(aux)

    def copy(self):
        return Matrix(self.array.copy())

    def append(self,*args: Union[list,np.ndarray], axis: Union[int,str]=0) -> None:
        if axis == 0 or axis =='below':
            final = self._below_append(*args)
        elif axis == 1 or axis =='right':
            final = self._right_append(*args)
        else:
            raise ValueError
        if not final.validate_entry():
            raise ValueError
        return final

    def _below_append(self,*args: Union[list,np.ndarray]):
        for element in args:
            if not isinstance(element, Union[Vector,list,np.ndarray]):
                raise TypeError(f"Invalid type: {type(element)}")
            elif len(element) != len(self[0]):
                raise DimensionError
        original_size = len(self)
        final_size = len(self.array) + len(args)
        self.array.resize((final_size,len(self[0])))
        for i, element in enumerate(args):
            self.array[original_size+i] = np.array(element)

    def _right_append(self,*args: Union[list,np.ndarray]):
        aux = self.transpose().copy()
        aux.append(*args)
        self.array = aux.array.transpose()
        
        
    def to_list(self) -> list:
        return self.array.tolist()

    def to_frame(self) -> pd.core.frame.DataFrame:
        return pd.DataFrame(data=self.array)

    def to_nparray(self) -> np.ndarray:
        return self.array


    """
    ###LINEAR SYSTEM###
    """


    @staticmethod
    def validate_b(b):
        if isinstance(b, Union[list,np.ndarray,tuple]):
            b = Vector(b)
        elif not isinstance(b, Vector):
            raise TypeError
        return b
        
    
    def validate_gj(self):
        for i in range(len(self)):
            if sum([abs(aux) for aux in self[i]])/abs(self[i][i])-1 >= 1:
                return False
        return True

    def gauss_jacobi(self, b):
        if not self.validate_gj():
            raise InvalidMethodError(message='gauss-jacobi is an invalid method for this matrix')
        

    def validate_gs(self):
        def beta(i: int):
            pass
        def term(i):
            return abs((abs(sum(beta(j) for j in range(i)))+abs(sum(self[i][j] for j in range(i+1,len(self[i])))))/self[i][i])
        for i in range(len(self)):
            if term(i) >=1:
                return False
        return True

    def gauss_seidel(self, b):
        if not self.validate_gs():
            raise InvalidMethodError(message='gauss-seidel is an invalid method for this matrix')

    def validate_ss(self):
        for i in range(len(self)):
            if not self[:i+1] == Vector(np.zeros(self.cols-i)) and self[:i+1] == Vector(np.zeros(self.cols-i, dtype=int)):
                return False
        return True
        # triangular inferior

    def successive_subs(self, b):
        if not self.validate_ss():
            raise InvalidMethodError(message='given matrix is not lower triangular')
        b = Matrix.validate_b(b)
        n = len(b)
        x = Vector(np.zeros(n))
        for i in range(n):
            x[i] = (b[i] -self[i,:i]*x[:i])/self[i,i]
        return x


    def validate_rs(self):
        for i in range(len(self)):
            if not self[i+1:] == Vector(np.zeros(i)) and self[i+1:] == Vector(np.zeros(i, dtype=int)):
                return False
        return True 
        # triangular superior

    def retroactive_subs(self, b):
        if not self.validate_rs():
            raise InvalidMethodError(message='given matrix is not upper triangular')
        b = Matrix.validate_b(b)
        n = len(b)
        x = Vector(np.zeros(n))
        for i in reversed(range(n)):
            x[i] = (b[i] - self[i, i+1:]*x[i+1:])/self[i, i]
        return x


    def gauss_eng(self):
        pass

    def gauss_bigo(self):
        pass

    def gauss_elimination(self, pivot=False):
        pass

    def linear_conjugate_gradient(self):
        pass

    def LU_decomposition(self):
        pass

    def LU_solution(self):
        pass

    def LDU(self):
        pass

    def choleski(self):
        pass

    def solution_choleski(self):
        pass

    def non_linear_newton(self):
        pass

    def newton_modified(self):
        pass


    """
    ### AUTOVALORES ###
    """


    def leverrier(self):
        pass

    def eigenvector(self):
        pass

    def LR_decomposition(self):
        n = self.array.shape[0]
        r = np.copy(self.array)
        l = np.identity(n) 
        rt = r.transpose()

        for j in range(n-1):
            for i in range(j+1,n):
                m = r[i, j]/r[j, j]
                r[i, j:] -= m * r[j, j:]
                l[i, j] = m
        return l, r

    def LR_method(self, iter=c.ITERATIONS):        
        Ak = np.copy(self.array)
        for k in range(iter):
            L, R = self.LR_decomposition(Ak)
            Ak = R@L
        eigenvalues = np.diag(Ak)
        return eigenvalues

    def householder(self):
        pass

    def QR_method(self):
        pass

    def QR_eigenvalues(self):
        pass


    pass


class Vector(Array):
    def __init__(self, arg: list) -> None:
        if not self.validate_entry(arg):
            raise ValueError
        super().__init__(arg)
        self.size = len(self)

    def validate_entry(self, arg):
        try:
            arg[0][0]
            return False
        except:
            return True

    def __mul__(self, other):
        if isinstance(other, Union[float,int, Complex]):
            return Vector(self.array * other)
        elif isinstance(other, Matrix):
            return self._transpose_linear_system(other)
        elif isinstance(other, Vector):
            return self._dot_product(other)
        else:
            raise TypeError

    def __call__(self, *args):
        aux = [element(*args) for element in self.array]
        if not isinstance(aux[0], Union[float,int]):
            return Matrix(aux)
        else:
            return Vector(aux)

    def __neg__(self):
        return self*(-1)

    def __abs__(self):
        return np.sum(self.array**2)

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


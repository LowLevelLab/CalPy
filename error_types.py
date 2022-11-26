class DimensionError(Exception):
    def __init__(self, message='', dim1: int = 0, dim2: int = 0):
        self.dim1 = dim1
        self.dim2 = dim2
        msg = f'dimensions are incompatible: array1 {dim1}, '\
              f'array2 {dim2}'
        super(DimensionError, self).__init__(message or msg)

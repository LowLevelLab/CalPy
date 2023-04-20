from linalg.oldarrays import *


def tridiagonal(a11:Union[int,float],
                a12:Union[int,float],
                a13:Union[int,float], 
                dim:Union[int,float]):

        for i in range(dim-1):
            pass
        pass

def pentadiagonal(a11: Union[int,float],
                  a12:Union[int,float],
                  a13:Union[int,float], 
                  a14:Union[int,float], 
                  a15:Union[int,float], 
                  dim:Union[int,float]):
        
        for i in range(dim-2):
            pass
        pass



"""
###LINEAR SYSTEM###
"""
    

def validate_gj(A: Array):
    for i in range(A.shape[0]):
        if np.sum([abs(aux) for aux in A[i]])/abs(A[i,i])-1 >= 1:
            return False
    return True

def gauss_jacobi(A: Array, b: Array):
    if not validate_gj(A,b):
        raise InvalidMethodError(message='gauss-jacobi is an invalid method for this matrix')
    

def validate_gs(A: Array):
    def beta(i: int):
        pass
    def term(i):
        return abs((abs(sum(beta(j) for j in range(i)))+abs(sum(A[i,j] for j in range(i+1,len(A[i])))))/A[i,i])
    for i in range(A.shape[0]):
        if term(i) >=1:
            return False
    return True

def gauss_seidel(A: Array, b: Array):
    if not validate_gs(A,b):
        raise InvalidMethodError(message='gauss-seidel is an invalid method for this matrix')

def validate_ss(A: Array):
    for i in range(A.rows):
        if not (A[i,:i+1] == Array(np.zeros(A.cols-i)) and A[i,:i+1] == Array(np.zeros(A.cols-i, dtype=int))):
            return False
    return True
    # triangular inferior

def successive_subs(A: Array, b: Array):
    if not validate_ss(A, b):
        raise InvalidMethodError(message='given matrix is not lower triangular')
    x = Array(np.zeros(b.shape[0]))
    for i in range(b.shape[0]):
        x[i] = (b[i] -A[i,:i]*x[:i])/A[i,i]
    return x


def validate_rs(A: Array):
    for i in range(A.rows):
        if not (A[i,i+1:] == Array(np.zeros(i)) and A[i,i+1:] == Array(np.zeros(i, dtype=int))):
            return False
    return True 
    # triangular superior

def retroactive_subs(A: Array, b: Array):
    if not validate_rs(A, b):
        raise InvalidMethodError(message='given matrix is not upper triangular')
    # b = A: Array, b: Array.validate_b(b)
    n = len(b)
    x = Array(np.zeros(n))
    for i in reversed(range(n)):
        x[i] = (b[i] - A[i, i+1:]*x[i+1:])/A[i, i]
    return x


def gauss_eng(A: Array, b: Array):
    pass

def gauss_bigo(A: Array, b: Array):
    pass

def gauss_elimination(A: Array, b: Array, pivot=False):
    pass

def linear_conjugate_gradient(A: Array, b: Array): # lcg
    pass

def LU_decomposition(A: Array, b: Array):
    pass

def LU_solution(A: Array, b: Array):
    pass

def LDU(A: Array, b: Array):
    pass

def choleski(A: Array, b: Array):
    pass

def solution_choleski(A: Array, b: Array):
    pass

def non_linear_newton(A: Array, b: Array):
    pass

def newton_modified(A: Array, b: Array):
    pass


"""
### AUTOVALORES ###
"""


def leverrier(A: Array, b: Array):
    pass

def eigenvector(A: Array):
    pass

def LR_decomposition(A: Array):
    n = A.shape[0]
    r = np.copy(A)
    l = np.identity(n) 
    rt = r.transpose()

    for j in range(n-1):
        for i in range(j+1,n):
            m = r[i, j]/r[j, j]
            r[i, j:] -= m * r[j, j:]
            l[i, j] = m
    return l, r

def LR_method(A: Array, iter=c.ITERATIONS):        
    Ak = np.copy(A)
    for k in range(iter):
        L, R = A.LR_decomposition(Ak)
        Ak = R@L
    eigenvalues = np.diag(Ak)
    return eigenvalues

def householder(A: Array, b: Array):
    pass

def QR_method(A: Array, b: Array):
    pass

def QR_eigenvalues(A: Array, b: Array):
    pass



# def newton_raphson_sist(list_functions,
#                         jacobian: Array,
#                         x0: list[float],
#                         tol: list[float]=[1e-6, 1e-6],
#                         max_iter: int = 10000):
    
#     x = x0
#     iter = 0
#     while np.any([np.absolute(f_x:=f(*x)) > tol for f in list_functions]) and iter < max_iter:
#         f_prime_x = jacobian(*x)
#         x = x - f_x / f_prime_x
#         iter += 1
#     return x, iter
    




if __name__ == "__main__":
    pass
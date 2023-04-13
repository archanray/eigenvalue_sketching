import numpy as np
from numpy.linalg import matrix_power as mpow

def multiplier(B, AP):
    """
    Inputs:
    B -- n times n matrix
    AP -- n times k matrix

    Outputs:
    C -- n times k matrix
    """
    
    C = B @ AP
    return C

def block_krylov_iter(A, eps, k):
    """
    Inputs:
    A -- n times d matrix
    eps -- tolerance
    k -- number of iterations

    Outputs:
    Z -- n times k matrix
    """
    d = A.shape[1]
    n = A.shape[0]
    q = np.log(d) / np.sqrt(eps)
    q = int(np.ceil(q))

    Pi = np.random.randn(d, k)
    Pi = Pi / np.linalg.norm(Pi, axis=0)

    APi = A @ Pi
    AAT = A @ A.T

    K = APi
    for i in range(q):
        quotient = i+1
        K = np.concatenate((K, multiplier(AAT, APi, quotient)), axis = 1)




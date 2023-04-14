import numpy as np
from numpy.linalg import matrix_power as mpow
from numpy.linalg import eig
from copy import deepcopy
from numpy.linalg import qr
from numpy.linalg import svd
from tqdm import tqdm

def block_krylov_iter(A, eps, k):
    """
    Inputs:
    A -- n times d matrix
    eps -- tolerance
    k -- number of iterations

    Outputs:
    Z -- n times k matrix
    """
    matvecs = 0
    d = A.shape[1]
    n = A.shape[0]
    q = np.log(d) / np.sqrt(eps)
    q = int(np.ceil(q))

    Pi = np.random.randn(d, k)
    Pi = Pi / np.linalg.norm(Pi, axis=0)

    APi = A @ Pi
    AAT = A @ A.T
    matvecs += 2

    S = deepcopy(AAT)
    K = deepcopy(APi)
    # generating the Krylov Subspace
    for i in tqdm(range(1,q+1)):
        K = np.concatenate((K, S @ APi), axis = 1)
        S = S @ AAT

    # orthonormalizing columns of K to obtain K
    Q, R = qr(K)

    # compute M
    M = Q.T @ AAT @ Q


    # compute SVD of M
    U, S, V = svd(M, full_matrices=True, compute_uv=True)
    Uk = U[:, :k]

    return Q @ Uk, matvecs

# test
matvals = np.random.randn(100, 100)
eigvec_approx, matvecs = block_krylov_iter(matvals, 1e-2, 10)


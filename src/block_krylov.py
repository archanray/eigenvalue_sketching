import numpy as np
from copy import deepcopy
from numpy.linalg import qr
from numpy.linalg import svd
from tqdm import tqdm

def block_krylov_iter(A, eps, k, return_var="Q"):
    """
    Inputs:
    A -- n times d matrix
    eps -- tolerance
    k -- number of iterations

    Outputs:
    Z -- n times k matrix
    matvecs -- number of matrix vector products on A, the input matrix
    """
    matvecs = 0
    d = A.shape[1]
    n = A.shape[0]
    q = np.log(d) / np.sqrt(eps)
    q = int(np.ceil(q))

    Pi = np.random.randn(d, k)
    Pi = Pi / np.linalg.norm(Pi, axis=0)

    APi = A @ Pi
    matvecs += k

    S = A @ (A.T @ APi)
    K = deepcopy(APi)
    # generating the Krylov Subspace
    for i in tqdm(range(1,q+1)):
        K = np.concatenate((K, S), axis = 1)
        S = A @ (A.T @ S)
        matvecs += 2*k

    # orthonormalizing columns of K to obtain K
    Q, R = qr(K)

    if return_var == "Q":
        return Q, matvecs

    # compute M
    M = (Q.T @ A) @ (A.T @ Q)
    matvecs += Q.shape[1]

    # compute SVD of M
    U, S, V = svd(M, full_matrices=True, compute_uv=True)
    Uk = U[:, :k]

    if return_var != "Q":
        return Q @ Uk, matvecs

# test
matvals = np.random.randn(100, 100)
eigvec_approx, matvecs = block_krylov_iter(matvals, 1e-2, 10, return_var="Z")


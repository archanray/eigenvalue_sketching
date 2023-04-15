import numpy as np
from src.block_krylov import block_krylov_iter as bki

def eigval_approx_bki_adaptive(A, eps, mode="krylov"):
    """
    Inputs:
    A -- n times n matrix
    eps -- tolerance

    Outputs:
    alpha -- n sized array containing eigenvalue approximates
    """
    if mode == "krylov":
        mode = "Q"
    else:
        mode = "Z"
    n = A.shape[0]
    Z, matvecs = bki(A, 1, 1/eps**2, return_var=mode)

    Atilde = Z.T @ (A @ Z)
    matvecs += Z.shape[1]

    alpha = np.linalg.eigvals(Atilde)
    zeros = np.zeros(n - Z.shape[1])
    alpha = np.concatenate((alpha, zeros))
    alpha = np.sort(alpha)

    return alpha, matvecs

def eigval_approx_othro_adaptive(A, k):
    """
    Inputs:
    A -- n times n matrix
    k -- number of eigenvalue approximates

    Outputs:
    alpha -- k sized array containing eigenvalue approximates
    """
    matvecs = 0
    G = np.random.randn(A.shape[0], k)
    V, _, _ = np.linalg.svd(A @ G)
    matvecs += G.shape[1]

    Atilde = V.T @ (A @ V)
    matvecs += V.shape[1]

    alpha = np.linalg.eigvals(Atilde)
    zeros = np.zeros(n - V.shape[1])
    alpha = np.concatenate((alpha, zeros))
    alpha = np.sort(alpha)

    return alpha, matvecs

def eigval_approx_ortho_nonadaptive(A, k):
    """
    Inputs:
    A -- n times n matrix
    k -- number of eigenvalue approximates

    Outputs:
    alpha -- k sized array containing eigenvalue approximates
    """
    # this algorithm in its current state is incorrect and needs to be fixed
    # fix: Btilde is not the correctly computed

    matvecs = 0
    S = np.random.randn(A.shape[0], k)
    T = np.random.randn(A.shape[0], k)
    AS = A @ S
    AT = A @ T
    matvecs += 2 * k

    Btilde = (np.lingalg.inv(AS.T @ T @ T.T @ AS)) @ AS.T @ T @ AT.T
    Abar = AS @ Btilde
    Atilde = (Abar + Abar.T) / 2

    alpha = np.linalg.eigvals(Atilde)
    zeros = np.zeros(n - Btilde.shape[1])
    alpha = np.concatenate((alpha, zeros))
    alpha = np.sort(alpha)

    return alpha, matvecs

def eigval_approx_SW_nonadaptive(A, eps, delta, k):
    """
    Inputs:
    A -- n times n matrix
    eps -- tolerance
    delta -- probability of failure
    k -- number of eigenvalue approximates

    Outputs:
    alpha -- k sized array containing eigenvalue approximates
    """
    G = np.random.randn(k, A.shape[0])
    matvecs = 0
    T = G @ (A @ G.T)
    matvecs += G.shape[0]

    alpha = np.linalg.eigvals(T) - np.sum(np.diag(T)) / k
    zeros = np.zeros(n - G.shape[0])
    alpha = np.concatenate((alpha, zeros))
    alpha = np.sort(alpha)
    
    return alpha, matvecs


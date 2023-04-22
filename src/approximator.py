import numpy as np
from src.block_krylov import block_krylov_iter as bki
from src.utils import sort_abs_descending as sad

def eigval_approx_bki_adaptive(A, epsilon=1, c1=1, c2=1, k=1, mode="Q", k_given=False, q=1, q_given=False, sr=[]):
    """
    Inputs:
    A -- n times n matrix
    eps -- tolerance
    mode -- "Q" or "Z" for returning Q or Z from block Krylov iteration

    Outputs:
    alpha -- n sized array containing eigenvalue approximates
    """
    n = A.shape[0]
    if k_given == False:
        k = c1*int(1/epsilon**2)
    else:
        k = c1*k
    
    if q_given == False:
        Z, matvecs = bki(A, eps=epsilon, k=k, c=c2, return_var=mode)
    else:
        Z, matvecs = bki(A, eps=epsilon, k=k, c=c2, return_var=mode, q=q, q_given=True)

    Atilde = Z.T @ (A @ Z)
    matvecs += Z.shape[1]

    alpha = np.linalg.eigvals(Atilde)
    zeros = np.zeros(n - Z.shape[1])
    alpha = np.concatenate((alpha, zeros))
    alpha = sad(alpha)

    if sr != []:
        alpha = alpha[sr]

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

    matvecs = 0
    S = np.random.randn(A.shape[0], k)
    T = np.random.randn(A.shape[0], k)
    AS = A @ S
    AT = A @ T
    matvecs += 2 * k

    Btilde = (np.lingalg.inv(AS.T @ T @ T.T @ AS)) @ AS.T @ T @ AT.T
    Abar = AS.T @ Btilde.T
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


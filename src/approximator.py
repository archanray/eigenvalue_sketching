import numpy as np
from src.block_krylov import block_krylov_iter as bki
from src.utils import sort_abs_descending as sad

def compute_alpha(A, n, sub_trace=False):
    """
    Inputs:
    A -- k times k matrix

    Outputs:
    alpha -- n sized array containing eigenvalue approximates
    """

    alpha, _ = np.linalg.eig(A)
    #print("max A:", np.max(A))
    #print("sad alphas:", alpha)
    alpha = np.real(alpha)
    if sub_trace == True:
        alpha = alpha - (np.trace(A) / A.shape[0])
    zeros = np.zeros(n - A.shape[0])
    alpha = np.concatenate((alpha, zeros))
    alpha = sad(alpha)
    return alpha

def eigval_approx_bki_adaptive(A, epsilon=1, c1=1, c2=1, k=1, mode="Q", k_given=True, q=3, q_given=True, sr=[]):
    """
    Inputs:
    A -- n times n matrix
    eps -- tolerance
    mode -- "Q" or "Z" for returning Q or Z from block Krylov iteration

    Outputs:
    alpha -- n sized array containing eigenvalue approximates
    """
    if k_given == False:
        k = c1*int(1/epsilon**2)
    else:
        k = c1*k
    
    if q_given == False:
        Z, matvecs = bki(A, eps=epsilon, k=k, c=c2, return_var=mode)
    else:
        Z, matvecs = bki(A, eps=epsilon, k=k, c=c2, return_var=mode, q=q, q_given=q_given)

    Atilde = Z.T @ (A @ Z)
    if mode == "Q":
        matvecs += Z.shape[1]

    alpha = compute_alpha(Atilde, A.shape[1])

    if sr != []:
        alpha = alpha[sr]

    print(alpha)
    return alpha, matvecs

def eigval_approx_othro_adaptive(A, k=1, sr=[]):
    """
    Inputs:
    A -- n times n matrix
    k -- number of eigenvalue approximates

    Outputs:
    alpha -- k sized array containing eigenvalue approximates
    """
    matvecs = 0
    G = np.random.normal(0,1/k, (A.shape[0], k))
    V, _, _ = np.linalg.svd(A @ G)
    matvecs += G.shape[1]

    Atilde = V.T @ (A @ V)
    #matvecs += V.shape[1]

    alpha = compute_alpha(Atilde, A.shape[1])
    if sr !=[]:
        alpha = alpha[sr]

    print(alpha)
    return alpha, matvecs

def eigval_approx_ortho_nonadaptive(A, k=1, sr=[]):
    """
    Inputs:
    A -- n times n matrix
    k -- number of eigenvalue approximates

    Outputs:
    alpha -- k sized array containing eigenvalue approximates
    """

    matvecs = 0
    S = np.random.normal(0,1/k, (A.shape[0], k))
    T = np.random.normal(0,1/k, (A.shape[0], k))
    AS = A @ S
    AT = A @ T
    matvecs += 2 * k

    Btilde = (np.linalg.inv(AS.T @ T @ T.T @ AS)) @ AS.T @ T @ AT.T
    Abar = AS.T @ Btilde.T
    Atilde = (Abar + Abar.T) / 2

    alpha = compute_alpha(Atilde, A.shape[1])
    if sr !=[]:
        alpha = alpha[sr]
    
    return alpha, matvecs

def eigval_approx_SW_nonadaptive(A, k=1, sr=[]):
    """
    Inputs:
    A -- n times n matrix
    k -- number of eigenvalue approximates

    Outputs:
    alpha -- k sized array containing eigenvalue approximates
    """
    G = np.random.normal(0,1/np.sqrt(k), (k, A.shape[0]))
    matvecs = 0
    S = G @ (A @ G.T)
    matvecs += G.shape[0]

    alpha = compute_alpha(S, A.shape[1], sub_trace=True)

    if sr !=[]:
        alpha = alpha[sr]

    return alpha, matvecs

def eigval_approx_random_sample(A, k=1, sr=[]):
    """
    Inputs:
    A -- n times n matrix
    k -- number of eigenvalue approximates

    Outputs:
    alpha -- k sized array containing eigenvalue approximates
    """
    matvecs = 0
    norm = np.ones(A.shape[0]) / A.shape[0]
    list_of_available_indices = range(A.shape[0])
    sample_indices = np.sort(np.random.choice(list_of_available_indices, k, replace=True))
    chosen_p = norm[sample_indices]

    SAS = A[sample_indices][:, sample_indices]
    matvecs += k
    sqrt_chosen_p = np.sqrt(chosen_p*k)
    D = np.diag(1/ sqrt_chosen_p)
    SAS = D @ SAS @ D

    alpha = compute_alpha(SAS, A.shape[1])

    if sr !=[]:
        alpha = alpha[sr]
    
    #print("checks:", alpha)
    #print("checks:", SAS.shape, A.shape)
    return alpha, matvecs

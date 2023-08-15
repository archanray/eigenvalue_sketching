import numpy as np
from src.block_krylov import block_krylov_iter as bki
# from src.utils import sort_abs_descending as sad
from src.utils import sort_descending as sd
from numpy.linalg import qr

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
    if A.shape[0] != n:
        zeros = np.zeros(n - A.shape[0])
        alpha = np.concatenate((alpha, zeros))
    alpha = sd(alpha) # sort alphas descending
    return alpha

def eigval_approx_bki_adaptive(A, epsilon=1, c1=1, c2=1, k=1, mode="Q", k_given=True, iters=3, q_given=True, sr=[]):
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
        Z, matvecs = bki(A, eps=epsilon, k=k, c=c2, return_var=mode, q=iters, q_given=q_given)

    Atilde = Z.T @ (A @ Z)
    if mode == "Q":
        matvecs += Z.shape[1]

    alpha = compute_alpha(Atilde, A.shape[1])

    if sr != []:
        alpha = alpha[sr]

    return alpha, matvecs

def eigval_approx_othro_adaptive(A, k=1, sr=[], mode=None):
    """
    Inputs:
    A -- n times n matrix
    k -- number of eigenvalue approximates

    Outputs:
    alpha -- k sized array containing eigenvalue approximates
    """
    matvecs = 0
    G = np.random.normal(0,1/np.sqrt(k), (A.shape[0], k))
    # V, _, _ = np.linalg.svd(A @ G)
    Q, R = qr(A @ G)
    matvecs += G.shape[1]

    Atilde = Q.T @ (A @ Q)
    #matvecs += V.shape[1]

    alpha = compute_alpha(Atilde, A.shape[1])
    if sr !=[]:
        alpha = alpha[sr]

    # print(alpha)
    return alpha, matvecs

def eigval_approx_ortho_nonadaptive(A, k=1, sr=[], mode=None):
    """
    Inputs:
    A -- n times n matrix
    k -- number of eigenvalue approximates

    Outputs:
    alpha -- k sized array containing eigenvalue approximates
    """

    matvecs = 0
    S = np.random.normal(0,1/np.sqrt(k), (A.shape[0], k))
    T = np.random.normal(0,1/np.sqrt(10*k), (A.shape[0], 10*k))
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

def eigval_approx_ortho_nonadaptive_2(A, k=1, c=2, sr=[], mode=None):
    """
    Inputs:
    A -- n times n matrix
    k -- number of eigenvalue approximates

    Outputs:
    alpha -- n sized array containing eigenvalue approximates
    """
    matvecs = 0
    n = A.shape[1]
    k1 = k
    k2 = int(c*k1)
    S = np.random.normal(0,1/np.sqrt(k1), (k1, n))
    T = np.random.normal(0,1/np.sqrt(k2), (k2, n))
    AST = A @ S.T
    ATT = A @ T.T
    matvecs += k1+k2

    Btilde = (np.linalg.inv(AST.T @ T.T @ T @ AST)) @ AST.T @ T.T @ ATT.T
    Abar = AST @ Btilde
    Atilde = (Abar + Abar.T) / 2

    alpha = compute_alpha(Atilde, n)
    if sr !=[]:
        alpha = alpha[sr]
    
    return alpha, matvecs    

def eigval_approx_SW_nonadaptive(A, k=1, sr=[], mode=None):
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

def eigval_approx_random_sample(A, k=1, sr=[], method=None):
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

def EigenGameUnloaded(M, k=2, iters=100, eta=1e2, sr=[], mode=None):
    n = M.shape[1]
    k = k//2
    V = np.random.randn(M.shape[0], k)
    V /= np.linalg.norm(V, axis=0, keepdims=True)
    k = V.shape[1]

    matvecs = 0
    mask = np.tril(np.ones((k, k)), k=-1)
    for _ in range(iters//2):
        VTMV = np.dot(V.T, M.dot(V))
        matvecs += k
        penalties = np.dot(V, (VTMV * mask).T)
        ojas = np.dot(M, V)
        grad = ojas - penalties
        V += eta * grad
        V /= np.linalg.norm(V, axis=0)

    VTMV = np.dot(V.T, M.dot(V))
    if mode == "d":
        a1 = compute_alpha(VTMV, n//2)
        pass
    if mode == "f":
        a1 = np.diag(VTMV)
    matvecs += k

    if mode == "d":
        # deflate
        Mbar = V @ (V.T @ M) - M
    if mode == "f":
        # flip with max eigval
        lambs = np.max(np.diag(VTMV))
        Mbar = 1.05 * lambs*np.eye(M.shape[1]) - M

    V = np.random.randn(M.shape[0], k)
    V /= np.linalg.norm(V, axis=0, keepdims=True)

    for _ in range(iters//2):
        VTMV = np.dot(V.T, Mbar.dot(V))
        matvecs += k
        penalties = np.dot(V, (VTMV * mask).T)
        ojas = np.dot(Mbar, V)
        grad = ojas - penalties
        V += eta * grad
        V /= np.linalg.norm(V, axis=0)
    
    VTMV = np.dot(V.T, M.dot(V))
    if mode == "d":
        a2 = compute_alpha(VTMV, n//2)
    if mode == "f":
        a2 = np.diag(VTMV)
    matvecs += k

    alpha = np.concatenate((a1, a2), axis=0)
    if len(alpha) != n:
        alpha = np.pad(alpha, pad_width=(0,n-len(alpha)), \
                        mode="constant", constant_values=0)
    alpha = sd(alpha)

    if sr !=[]:
        alpha = alpha[sr]
    return alpha, matvecs

    return V

def EigenGamesUnloadedForEigs(M, k=2, iters=100, eta=1e2, sr=[], mode=None):
    V = np.random.randn(M.shape[0], k)
    V /= np.linalg.norm(V, axis=0, keepdims=True)

    matvecs = 0
    mask = np.tril(np.ones((k, k)), k=-1)

    for _ in range(1,iters):
        ojas = M.dot(np.dot(M.T, M.dot(V)))
        VTMV = np.dot(V.T, ojas)
        penalties = np.dot(V, (VTMV * mask).T)
        grad = ojas - penalties
        V += eta * grad
        V /= np.linalg.norm(V, axis=0)
        matvecs += 3*k

    VTMV = np.dot(V.T, M.dot(np.dot(M.T, M.dot(V))) )
    matvecs += 2*k

    alpha = compute_alpha(VTMV, M.shape[1])

    if sr !=[]:
        alpha = alpha[sr]
    return alpha, matvecs

    return V
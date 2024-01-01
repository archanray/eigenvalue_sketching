import numpy as np
from src.block_krylov import block_krylov_iter_opt as bki
# from src.utils import sort_abs_descending as sad
from src.utils import sort_descending as sd
from numpy.linalg import qr
import sys
from copy import copy

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
    matvecs += Q.shape[1]

    alpha = compute_alpha(Atilde, A.shape[1])
    if sr !=[]:
        alpha = alpha[sr]

    # print(alpha)
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

    Btilde = (np.linalg.pinv(AST.T @ T.T @ T @ AST)) @ AST.T @ T.T @ ATT.T
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

def EigenGameUnloadedOptions(M, k=2, iters=500, eta=2e3, sr=[], mode="EGUN"):
    """
    This function implements several variations of eigengames
    1. Eigengames naive (EGUN) -- this is the base eigengames function on 
    input matrix M
    2. Eigengames + subspace approximation (EGQR) -- this requires saving 
    the subspace at each iteration and then computing a QR of this is the
    approximate subspace
    3. Sketch eigengames (SEG) -- compute a sketch of the input matrix and
    then run eigengames. Notably, only one MV query is required
    4. Sketch eigengames + subspace approximation (SEGQR) -- compute a 
    sketch of the input matrix and then run EGQR. Notably, only one MV 
    query is required
    """
    # create and store a copy of input
    inputM = copy(M)
    
    if mode not in ["EGUN", "EGQR", "SEGUN", "SEGQR"]:
        print("mode not set correctly")
        sys.exit(1)
    if mode in ["SEGUN", "SEGQR"]:
        # skethcing matrix
        V = np.random.normal(0, 1/np.sqrt(k), (M.shape[1], k))
        # first compute a sketch of the input matrix
        # so M become k\times k
        M = np.dot(V.T, M.dot(V))
        matvecs = k
    n = inputM.shape[0]
    V = np.random.randn(M.shape[1], k)
    V /= np.linalg.norm(V, axis=0, keepdims=True)

    if mode in ["EGUN", "EGQR"]:
        # initialize matvecs for eigengames-naive or eigengames-QR
        matvecs = 0
    if "QR" in mode:
        K = np.empty_like(V)
    mask = np.tril(np.ones((k, k)), k=-1)
    
    for _ in range(iters):
        MV = np.dot(M, V)
        VTMV = np.dot(V.T, MV)
        penalties = np.dot(V, (VTMV * mask).T)
        ojas = MV
        grad = ojas - penalties
        V += eta * grad
        V /= np.linalg.norm(V, axis=0)
        if mode in ["EGUN", "EGQR"]:
            # increase matvecs for eigengames-naive or eigengames-QR
            # one k for MV. The ojas step is free since MV is computed in VTMV
            matvecs += k
        if "QR" in mode:
            # if we need to do QR, we save the subspace first
            # this is a free MV step
            K = np.concatenate((K, V), axis = 1)    

    if "QR" in mode:
        # compute QR decomposition of K
        V, R = qr(K)
    if "S" in mode:
        # in sketch mode the matrix is not of the right size!
        # V is now k\times k
        V, R = qr(np.dot(M,V))
        # now V is n \times k
    VTMV = np.dot(V.T, inputM.dot(V))
    matvecs += k
    alpha = compute_alpha(VTMV, n)
    if sr != []:
        alpha = alpha[sr]
    return alpha, matvecs

def EigenGameFeatsOptions(X, k=1, iters=500, eta=5e3, sr=[], mode="EGFUN"):
    """
    This function implements several variations of eigengames where
    the input is a set of features instead of the input covariance matrix
    1. Eigengames naive (EGFUN) -- this is the base eigengames function on 
    input matrix M
    2. Eigengames + subspace approximation (EGFQR) -- this requires saving 
    the subspace at each iteration and then computing a QR of this is the
    approximate subspace
    3. Sketch eigengames (SEGF) -- compute a sketch of the input matrix and
    then run eigengames. Notably, only one MV query is required
    4. Sketch eigengames + subspace approximation (SEGFQR) -- compute a 
    sketch of the input matrix and then run EGQR. Notably, only one MV 
    query is required
    """
    # create a store a copy of input
    inputX = copy(X)
    
    if mode not in ["EGFUN", "EGFQR", "SEGFUN", "SEGFQR"]:
        print("mode not set correctly")
        sys.exit(1)
    if mode in ["SEGFUN", "SEGFQR"]:
        # sketching matrix
        V = np.random.normal(0, 1/np.sqrt(k), (X.shape[1], k))
        # compute a sketch of the input matrix
        # so X becomes n\times k
        Vtilde = copy(V)
        X = np.dot(X, V)
        matvecs = k
    n = X.shape[0]
    V = np.random.randn(X.shape[1], k)
    V /= np.linalg.norm(V, axis=0, keepdims=True)
    
    if mode in ["EGFUN", "EGFQR"]:
        # initialize matvecs for eigengames-naive or eigengames-QR
        matvecs = 0
    if "QR" in mode:
        K = np.empty_like(V)
    mask = np.tril(np.ones((k,k)), k=-1)
    
    for _ in range(iters):
        XV = np.dot(X, V)
        VTMV = np.dot(XV.T, XV)
        penalties = np.dot(V, (VTMV*mask).T)
        ojas = np.dot(X.T, XV)
        grad = ojas-penalties
        V+= eta * grad
        V /= np.linalg.norm(V, axis=0)
        if mode in ["EGFUN, EGFQR"]:
            # increase matvecs by 2*k for XV and X^TXV
            matvecs += 2*k
        if "QR" in mode:
            # if we need to do QR, we save the subspace first
            # this is a free MV step
            K = np.concatenate((K, V), axis = 1)
    
    if "QR" in mode:
        # compute QR decomposition of K
        V, R = qr(K)
    if "S" in mode:
        # in sketch mode the matrix is not of the right size!
        # V is now k\times k
        # V, R = qr(np.dot(X,V))
        # instead of the QR above, project Vtilde on the subspace spanned
        # by the V's computed using eigengames
        V = np.dot(Vtilde, V.dot(V.T))
        # now V is n \times k
    VTMV = np.dot(V.T, inputX.dot(V))
    matvecs += k
    alpha = compute_alpha(VTMV, n)
    if sr !=[]:
        alpha = alpha[sr]
    return alpha, matvecs

def EigenGameFeats(X, k=1, iters=100, eta=5e3, sr=[], mode=None):
    n = X.shape[0]
    V = np.random.randn(X.shape[0], k)
    # V = np.random.normal(0,1/np.sqrt(k), (X.shape[0], k))
    V /= np.linalg.norm(V, axis=0, keepdims=True)

    matvecs = 0
    mask = np.tril(np.ones((k,k)), k=-1)
    for _ in range(iters):
        XV = np.dot(X, V)
        matvecs += k
        VTMV = np.dot(XV.T, XV)
        penalties = np.dot(V, (VTMV*mask).T)
        ojas = np.dot(X.T, XV)
        matvecs += k
        grad = ojas-penalties
        V+= eta * grad
        V /= np.linalg.norm(V, axis=0)

    VTMV = np.dot(V.T, X.dot(V))
    matvecs += k
    alpha = compute_alpha(VTMV, n)
    if sr !=[]:
        alpha = alpha[sr]
    return alpha, matvecs

def EigenGameQR(X, k=1, iters=100, eta=5e3, sr=[], mode=None):
    n = X.shape[0]
    V = np.random.randn(X.shape[0], k)
    # V = np.random.normal(0,1/np.sqrt(k), (X.shape[0], k))
    V /= np.linalg.norm(V, axis=0, keepdims=True)

    matvecs = 0
    mask = np.tril(np.ones((k,k)), k=-1)

    # additional data structure to store the updates at each step
    K = np.empty_like(V)

    for _ in range(iters):
        XV = np.dot(X, V)
        matvecs += k
        VTMV = np.dot(XV.T, XV)
        penalties = np.dot(V, (VTMV*mask).T)
        ojas = np.dot(X.T, XV)
        matvecs += k
        grad = ojas-penalties
        V+= eta * grad
        V /= np.linalg.norm(V, axis=0)

        # add the update to the lib    
        K = np.concatenate((K, V), axis = 1)

    # QR of the lib to get the top-k subspace
    Q, R = qr(K)

    # actual approximation
    VTMV = np.dot(Q.T, X.dot(Q))
    matvecs += k

    alpha = compute_alpha(VTMV, n)
    
    if sr !=[]:
        alpha = alpha[sr]
    return alpha, matvecs

def EigenGameUnloaded2(M, k=2, iters=100, eta=1e3, sr=[], mode=None):
  n = M.shape[1]
  vtop = np.random.randn(M.shape[0])
  matvecs = 0
  for _ in range(iters):
    ojas = M.dot(vtop)
    matvecs += 1
    grad = ojas
    vtop += eta * grad
    vtop /= np.linalg.norm(vtop)
  
  lam_top = np.dot(vtop, M.dot(vtop))
  matvecs += 1

  # print('lam_top', lam_top)

  Mbar = M + abs(lam_top) * np.eye(M.shape[0])

  k = k // 2

  V = np.random.randn(M.shape[0], k)
  V /= np.linalg.norm(V, axis=1, keepdims=True)

  k = V.shape[1]
  mask = np.tril(np.ones((k, k)), k=-1)
  for _ in range(iters // 2):
    VTMV = np.dot(V.T, Mbar.dot(V))
    matvecs += k
    penalties = np.dot(V, (VTMV * mask).T)
    ojas = Mbar.dot(V)
    grad = ojas - penalties
    V += eta * grad
    V /= np.linalg.norm(V, axis=0)

  VTMV = np.dot(V.T, M.dot(V))
  matvecs += k
  lams_pos = np.diag(VTMV)
  lam_max = lams_pos.max()
  Mbar = 1.05 * (lam_max + lam_top) * np.eye(M.shape[0]) - Mbar

  V = np.random.randn(M.shape[0], k)
  V /= np.linalg.norm(V, axis=1, keepdims=True)

  for _ in range(iters // 2):
    VTMV = np.dot(V.T, Mbar.dot(V))
    matvecs += k
    penalties = np.dot(V, (VTMV * mask).T)
    ojas = Mbar.dot(V)
    grad = ojas - penalties
    V += eta * grad
    V /= np.linalg.norm(V, axis=0)

  VTMV = np.dot(V.T, M.dot(V))
  matvecs += k
  lams_neg = np.diag(VTMV)

  lams = np.concatenate((lams_pos, lams_neg), axis=0)
  if len(lams) != n:
    lams = np.pad(lams, pad_width=(0,n-len(lams)), \
                        mode="constant", constant_values=0)
  lams = sd(lams)
  if sr !=[]:
    lams = lams[sr]
  return lams, matvecs
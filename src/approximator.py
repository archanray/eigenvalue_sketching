import numpy as np
from src.block_krylov import block_krylov_iter as bki

def eigval_approx_bki(A, eps, mode="krylov"):
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
    Z, matvecs = bki(A, 1, 1/eps**2, return_var=mode)

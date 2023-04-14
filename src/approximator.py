import numpy as np
from src.block_krylov import block_krylov_iter as bki

def eigval_approx_bki(A, eps, mode="Q"):
    """
    Inputs:
    A -- n times n matrix
    eps -- tolerance

    Outputs:
    alpha -- n sized array containing eigenvalue approximates
    """



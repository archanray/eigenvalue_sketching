import numpy as np
from src.approximator import eigval_approx_bki_adaptive as bki_adp
from src.approximator import eigval_approx_othro_adaptive as oth_adp
from src.approximator import eigval_approx_ortho_nonadaptive as oth_nonadp
from src.approximator import eigval_approx_SW_nonadaptive as sw_nonadp

def approximation(A, params, mv_method):
    """
    Wrapper function for the approximation methods
    :param A: matrix
    :param params: parameters, contains: "search_rank",
    "trials", "min_samples", "max_samples"
    :param mv_method: method for matrix-vector approximation

    :return: eigenvalues across trials
    """
    eps = 1e-2
    approx_eigvals = np.zeros((params['trials'], len(params['search_rank'])))
    matvecs_all = np.zeros(params['trials'])
    for t in range(params['trials']):
        if mv_method.__name__ == "eigval_approx_bki_adaptive":
            returned_approx_eigvals, matvecs = mv_method(A, eps, "Q")
            approx_eigvals[t, :] = returned_approx_eigvals[params["search_rank"]]
            matvecs_all[t] = matvecs
        else:
            raise ValueError('Approximation method not supported')

    return approx_eigvals, matvecs_all

import numpy as np
from src.approximator import eigval_approx_bki_adaptive as bki_adp
from src.approximator import eigval_approx_othro_adaptive as oth_adp
from src.approximator import eigval_approx_ortho_nonadaptive as oth_nonadp
from src.approximator import eigval_approx_SW_nonadaptive as sw_nonadp
from tqdm import tqdm

def approximation(A, params):
    """
    Wrapper function for the approximation methods
    :param A: matrix
    :param params: parameters

    :return: eigenvalues across trials and matvecs
    """
    approx_eigvals = {}
    matvecs_all = {}
    for mv_mthd in params["approx_mthds"]:
        approx_ev_per_method = np.zeros(( len(params["ks"]), params["trials"], \
                len(params["search_rank"]) ))
        matvecs_per_method = np.zeros(( len(params["ks"]), params["trials"] ))
        try:
            for t in tqdm(range(params["trials"])):
                for k in range(len(params["ks"])):
                    R = mv_mthd(A, k=params["ks"][k], sr=params["search_rank"])
                    approx_ev_per_method[k, t, :] = R[0]
                    matvecs_per_method[k, t] = R[1]

            approx_eigvals[mv_mthd.__name__] = approx_ev_per_method
            matvecs_all[mv_mthd.__name__] = matvecs_per_method
        
        except:
            raise ValueError('Approximation method not supported')

    return approx_eigvals, matvecs_all

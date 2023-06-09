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

def approx_unified(A, params, algos, algo_params):
    """
    Wrapper for all
    """
    if len(algo_params["iters"]) == 1:
        iterator = algo_params["iters"][0]
        len_rows = len(iterator)
    else:
        import itertools
        iterator = itertools.product(algo_params["iters"][0], algo_params["iters"][1])
        len_rows = len(algo_params["iters"][0] * algo_params["iters"][1])
    len_cols = len(params["sr"])

    #######################log vars####################################################
    save_dict = {}
    avg_errors = np.zeros((len_rows, len_cols))
    std_errors = np.zeros((len_rows, len_cols))
    avg_lies = np.zeros(len_rows)
    std_lies = np.zeros(len_rows)
    matvecs_all = np.zeros(len_rows)
    ##################################################################################

    for a in algos:
        if a == "bki_adp_Q":
            algo = bki_adp
            return_mode = Q
        if a == "bki_adp_Z":
            algo = bki_adp
            return_mode = Z
        if a == "oth_adp":
            algo = oth_adp
        if a == "oth_nonadp":
            algo = oth_nonadp
        if a == "sw_nonadp":
            algo = sw_nonadp
        pass

        count = 0
        for i in iterator:
            pass

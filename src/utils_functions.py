from src.approximator import eigval_approx_bki_adaptive as bki_adp
from src.approximator import eigval_approx_othro_adaptive as oth_adp
from src.approximator import eigval_approx_ortho_nonadaptive_2 as oth_nonadp
from src.approximator import eigval_approx_SW_nonadaptive as sw_nonadp
from src.approximator import EigenGameUnloaded as egu
from src.approximator import eigval_approx_random_sample as ears

def StrToFunc(name: str):
    dict_of_funcs = {
                    "bki": bki_adp,
                    "oth_adp": oth_adp,
                    "oth_nonadp": oth_nonadp,
                    "sw_nonadp": sw_nonadp, 
                    "eg_unldd": egu,
                    "rand_samp": ears
                    }

    if "bki" in name:
        return dict_of_funcs["bki"]
    else:
        return dict_of_funcs[name]
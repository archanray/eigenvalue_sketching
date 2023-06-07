import numpy as np
from src.approximator import eigval_approx_bki_adaptive as bki_adp
from src.approximator import eigval_approx_othro_adaptive as oth_adp
from src.approximator import eigval_approx_ortho_nonadaptive_2 as oth_nonadp
from src.approximator import eigval_approx_SW_nonadaptive as sw_nonadp
from src.approx_wrapper import approximation
from src.get_dataset import get_data
from src.utils import sort_abs_descending as sad
import pickle
from tqdm import tqdm

"""
code needs fixing the range so the plots overlap
"""

##################################### PARAMETERS #####################################
# Dataset
dataset_name = "facebook"
# Search parameters
search_rank = [0,1,2,3,4,5]
# Approximation parameters
trials = 10
# Approximation methods, check approximator for options
approx_mthds = [bki_adp, oth_nonadp, sw_nonadp, oth_adp]
######################################################################################

################################### GRAB THE MATRICES ################################
true_mat, dataset_size, min_samples, max_samples = get_data(dataset_name)

true_spectrum, _ = np.linalg.eig(true_mat)
true_spectrum = sad(np.real(true_spectrum))

print("loaded datasets")
print("A_infty:", np.max(true_mat))
print("true eigvals:", true_spectrum[search_rank])
print("search ranks:", search_rank)

######################################################################################

################################### SEARCH PARAMETERS ################################
ks = np.arange(min_samples, int(max_samples/10)+10)
#ks = np.arange(min_samples, min_samples+1)
# Parameters
# fix the approx_methods later
params = {"search_rank": search_rank, "trials": trials, \
        "min_samples": min_samples, "max_samples": max_samples, \
        "approx_mthds": approx_mthds, "dataset_size": dataset_size, \
        "true_spectrum": true_spectrum, "true_mat": true_mat, \
        "dataset_name": dataset_name, "ks": ks}
######################################################################################

################################### APPROXIMATION ####################################
# Run approximation
approx_results, matvec_results = approximation(true_mat, params)
print(approx_results)

save_vars = {"params": params, "approx_results": approx_results, "matvec_results": matvec_results}
# Save the results
with open("results/"+dataset_name+".pkl", "wb") as f:
    pickle.dump(save_vars, f)
######################################################################################

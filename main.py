import numpy as np
from src.approximator import eigval_approx_bki_adaptive as bki_adp
from src.approximator import eigval_approx_othro_adaptive as oth_adp
from src.approximator import eigval_approx_ortho_nonadaptive as oth_nonadp
from src.approximator import eigval_approx_SW_nonadaptive as sw_nonadp
from src.approx_wrapper import approximation
from src.get_dataset import get_data
import pickle
from tqdm import tqdm

##################################### PARAMETERS #####################################
# Dataset
dataset_name = "random_random"
# Search parameters
search_rank = [0,1,2,3,4,5]
# Approximation parameters
trials = 10
# Approximation methods, check approximator for options
approx_mthds = [bki_adp]
######################################################################################

################################### GRAB THE MATRICES ################################
true_mat, dataset_size, min_samples, max_samples = get_data(dataset_name)

true_spectrum, _ = np.linalg.eig(true_mat)
#true_spectrum = np.diag(true_spectrum)

abs_true_spectrum = np.abs(true_spectrum)
abs_true_spectrum_ordered_indices = np.argsort(-abs_true_spectrum)

search_rank = abs_true_spectrum_ordered_indices[search_rank]

print("loaded datasets")
print("A_infty:", np.max(true_mat))
print("true eigvals:", true_spectrum[search_rank])
print("search ranks:", search_rank)

params = {"search_rank": search_rank, "trials": trials, \
        "min_samples": min_samples, "max_samples": max_samples}
######################################################################################

################################### APPROXIMATION ####################################
# Initialize the results
results = {}
# Run approximation
for mthd in approx_mthds:
    mv_method = mthd
    print(mv_method.__name__)
    results[mv_method.__name__] = approximation(A, params, mv_method)

# Save the results
with open("results/"+dataset_name+".pkl", "wb") as f:
    pickle.dump(results, f)
######################################################################################

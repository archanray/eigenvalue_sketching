import numpy as np
from src.approximator import eigval_approx_bki_adaptive as bki_adp
from src.approximator import eigval_approx_othro_adaptive as oth_adp
from src.approximator import eigval_approx_ortho_nonadaptive as oth_nonadp
from src.approximator import eigval_approx_SW_nonadaptive as sw_nonadp
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
######################################################################################

################################### APPROXIMATION ####################################
# Initialize the results
c1s = np.logspace(0,8,num=8, base=10, endpoint=False) / 1e+05
c2s = np.logspace(0,8,num=8, base=10, endpoint=False) / 1e+05

ks = np.arange(50,90,5)

approx_results = np.zeros((len(c1s), len(c2s), len(ks), trials, len(search_rank)))
matvec_results = np.zeros((len(c1s), len(c2s), len(ks), trials))

for i in tqdm(range(len(c1s))):
    for j in range(len(c2s)):
        c1l = c1s[i]
        c2l = c2s[j]
        for t in range(len(ks)):
            for l in range(trials):
                for mthd in approx_mthds:
                    R = approx_mthds[0](true_mat, c1=c1l, c2=c2l, k=ks[t], k_given=True, mode="Q")
                    approx_results[i,j,t,l,:] = (R[0])[search_rank]
                    matvec_results[i,j,t,l] = R[1]

filename = dataset_name+"_"+approx_mthds[0].__name__+"_"+str(k_given)+"_"+mode

# Save the results
with open("single_results/"+filename+".pkl", "wb") as f:
    pickle.dump([approx_results, matvec_results], f)
######################################################################################

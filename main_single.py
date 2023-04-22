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
qs = np.logspace(0,6,num=6, base=2, endpoint=False)
ks = np.arange(50,90,5)
k_given = True
q_given = True
mode = "Q"

approx_results = np.zeros((len(qs), len(ks), trials, len(search_rank)))
matvec_results = np.zeros((len(qs), len(ks), trials))

for i in tqdm(range(len(qs))):
    for j in range(len(ks)):
        for l in range(trials):
            for mthd in approx_mthds:
                R = approx_mthds[0](true_mat, k=ks[j], k_given=k_given, q=qs[i], q_given=q_given, mode=mode)
                approx_results[i,j,l,:] = (R[0])[search_rank]
                matvec_results[i,j,l] = R[1]

filename = dataset_name+"_"+approx_mthds[0].__name__+"_"+str(k_given)+"_"+str(q_given)+"_"+mode

# Save the results
with open("single_results/"+filename+".pkl", "wb") as f:
    pickle.dump([true_spectrum[search_rank], approx_results, matvec_results, true_mat, ks, qs,\
            dataset_name, approx_mthds, k_given, q_given, mode], f)
######################################################################################

############################## AGGREGATE RESULTS #####################################
# Load the results
with open("single_results/"+filename+".pkl", "rb") as f:
    data = pickle.load(f)
    true_spectrum = data[0]
    approx_results = data[1]
    matvec_results = data[2]
    true_mat = data[3]
    ks = data[4]
    qs = data[5]
    dataset_name = data[6]
    approx_mthds = data[7]
    k_given = data[8]
    q_given = data[9]
    mode = data[10]

# Aggregate the results
true_spectrum1 = np.expand_dims(true_spectrum, axis=0)
true_spectrum1 = np.expand_dims(true_spectrum1, axis=0)
true_spectrum1 = np.expand_dims(true_spectrum1, axis=0)

error = np.abs(approx_results - true_spectrum1) / float(np.sqrt(np.count_nonzero(true_mat)))
error = np.log(error)

mean_approx_results = np.mean(error, axis=2)
mean_matvec_results = np.mean(matvec_results, axis=2)

std_approx_results = np.std(approx_results, axis=2)
std_matvec_results = np.std(matvec_results, axis=2)
######################################################################################

################################## PLOTS #############################################
import matplotlib.pyplot as plt
# Plot the results

for j in range(len(true_spectrum)):
    filename = dataset_name+"_"+approx_mthds[0].__name__+"_"+str(k_given)+"_"+str(q_given)+"_"+mode+"_eigval"+str(j)
    plt.gcf().clear()
    fig, ax = plt.subplots(1,1, figsize=(10,10))
    # plot approximation by 0
    ax.plot(ks, np.log(np.abs(np.zeros_like(mean_approx_results[i,:,0]) - true_spectrum[j])/\
            float(np.sqrt(np.count_nonzero(true_mat))) ), label="approx by 0")
    for i in range(len(qs)):
        # plot the mean errors
        ax.plot(ks, mean_approx_results[i,:,0], label="q="+str(qs[i]))

        ax.set_xlabel("k")
        ax.set_ylabel("error")
        ax.set_title("error vs k for different q")
        ax.legend()
    plt.savefig("figures/single_results/"+filename+"_"+str(j)+".pdf")
######################################################################################

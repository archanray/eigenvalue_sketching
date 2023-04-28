import numpy as np
from src.approximator import eigval_approx_bki_adaptive as bki_adp
from src.approximator import eigval_approx_othro_adaptive as oth_adp
from src.approximator import eigval_approx_ortho_nonadaptive as oth_nonadp
from src.approximator import eigval_approx_SW_nonadaptive as sw_nonadp
from src.approximator import eigval_approx_random_sample as rnd_smp
from src.get_dataset import get_data
import pickle
from tqdm import tqdm
from src.utils import sort_abs_descending as sad

##################################### PARAMETERS #####################################
# Dataset
dataset_name = "facebook"
# Search parameters
search_rank = [0,1,2,3,4,5]
# Approximation parameters
trials = 50
# Approximation methods, check approximator for options
approx_mthds = [oth_nonadp]
######################################################################################

################################### GRAB THE MATRICES ################################
print("loading datasets")
true_mat, dataset_size, min_samples, max_samples = get_data(dataset_name)

true_spectrum, _ = np.linalg.eig(true_mat)
#true_spectrum = np.diag(true_spectrum)

true_spectrum = sad(np.real(true_spectrum))

print("loaded datasets")
print("A_infty:", np.max(true_mat))
print("true eigvals:", true_spectrum[search_rank])
print("search ranks:", search_rank)
######################################################################################

################################### APPROXIMATION ####################################
# Initialize the results
#qs = np.logspace(0,6,num=6, base=2, endpoint=False)
#ks = np.arange(50,90,5)
#qs = [1,2,4,8,16,32]
#ks = [6,10,15,20,30]
ks = np.arange(min_samples, max_samples, 10)
#ks = [min_samples, max_samples, max_samples+2000, true_mat.shape[0]]
#k_given = True
#q_given = True
#mode = "Z"

"""
approx_results = np.zeros((len(qs), len(ks), trials, len(search_rank)))
matvec_results = np.zeros((len(qs), len(ks), trials))
"""

approx_results = np.zeros((len(ks), trials, len(search_rank)))
matvec_results = np.zeros((len(ks), trials))
"""
# for bki_adp
for i in tqdm(range(len(qs))):
    for j in range(len(ks)):
        for l in range(trials):
            for mthd in approx_mthds:
                # bki_adp
                #R = approx_mthds[0](true_mat, k=ks[j], k_given=k_given, q=qs[i], q_given=q_given, mode=mode, sr=search_rank)
                #print("outputs:", R)
                # sw_nonadp
                R = approx_mthds[0](true_mat, k=ks[j], sr=search_rank)
                approx_results[i,j,l,:] = R[0]
                matvec_results[i,j,l] = R[1]
"""

# for bki_adp
for j in tqdm(range(len(ks))):
    for l in range(trials):
        for mthd in approx_mthds:
            # sw_nonadp
            R = approx_mthds[0](true_mat, k=ks[j], sr=search_rank)
            approx_results[j,l,:] = R[0]
            matvec_results[j,l] = R[1]

#filename = dataset_name+"_"+approx_mthds[0].__name__+"_"+str(k_given)+"_"+str(q_given)+"_"+mode

filename = dataset_name+"_"+approx_mthds[0].__name__

save_vals = {}
save_vals["true_spectrum"] = true_spectrum[search_rank]
save_vals["approx_results"] = approx_results
save_vals["matvec_results"] = matvec_results
save_vals["true_mat"] = true_mat
save_vals["ks"] = ks
#save_vals["qs"] = qs
save_vals["dataset_name"] = dataset_name
save_vals["approx_mthds"] = approx_mthds
#save_vals["k_given"] = k_given
#save_vals["q_given"] = q_given
#save_vals["mode"] = mode

# Save the results
with open("single_results/"+filename+".pkl", "wb") as f:
    pickle.dump(save_vals, f)

######################################################################################


############################## AGGREGATE RESULTS #####################################
# Load the results
with open("single_results/"+filename+".pkl", "rb") as f:
    data = pickle.load(f)
    true_spectrum = data["true_spectrum"]
    approx_results = data["approx_results"]
    matvec_results = data["matvec_results"]
    true_mat = data["true_mat"]
    ks = data["ks"]
    #qs = data["qs"]
    dataset_name = data["dataset_name"]
    approx_mthds = data["approx_mthds"]
    #k_given = data["k_given"]
    #q_given = data["q_given"]
    #mode = data["mode"]

eps = 1e-32

# Aggregate the results
true_spectrum1 = np.expand_dims(true_spectrum, axis=0)
true_spectrum1 = np.expand_dims(true_spectrum1, axis=0)
# add below for bki_adp
#true_spectrum1 = np.expand_dims(true_spectrum1, axis=0)

nnzA = float(np.sqrt(np.count_nonzero(true_mat)))
error = np.abs(approx_results - true_spectrum1) / nnzA
error = np.log(error+eps)

mean_approx_results = np.mean(error, axis=1)
mean_matvec_results = np.mean(matvec_results, axis=1)

std_approx_results = np.std(approx_results, axis=1)
std_matvec_results = np.std(matvec_results, axis=1)
######################################################################################

################################## PLOTS #############################################
import matplotlib.pyplot as plt
# Plot the results

for j in range(len(true_spectrum)):
    plt.gcf().clear()
    fig, ax = plt.subplots(1,1, figsize=(10,10))
    """
    # uncomment block for bki_adp
    # plot approximation by 0
    #ax.plot(ks, np.log(np.abs(np.zeros_like(mean_approx_results[i,:,0]) - true_spectrum[j])/\
    #        float(np.sqrt(np.count_nonzero(true_mat))) ), label="approx by 0")
    for i in range(len(qs)):
        # plot the mean errors
        # print(mean_approx_results[i,:,j])
        ax.plot(np.log(ks), mean_approx_results[i,:,j], label="q="+str(qs[i]))

        ax.set_xlabel("log k")
        ax.set_ylabel("log error")
        ax.set_title("Approximation of eigval "+str(true_spectrum[j])+" of "+dataset_name+" dataset")
        ax.legend()
    plt.savefig("figures/single_results/"+filename+"_"+str(j)+".pdf")
    """
    # plot the mean errors
    ax.plot(np.log(np.array(ks) / true_mat.shape[0]), mean_approx_results[:,j])
    ax.set_xlabel("log k")
    ax.set_ylabel("log error")
    ax.set_title("Approximation of eigval "+str(true_spectrum[j])+" of "+dataset_name+" dataset")
    #ax.legend()
    plt.savefig("figures/single_results/"+filename+"_"+str(j)+".pdf")
######################################################################################


import numpy as np
from src.approximator import eigval_approx_bki_adaptive as bki_adp
from src.approximator import eigval_approx_othro_adaptive as oth_adp
from src.approximator import eigval_approx_ortho_nonadaptive_2 as oth_nonadp
from src.approximator import eigval_approx_SW_nonadaptive as sw_nonadp
from src.get_dataset import get_data
from src.utils import sort_abs_descending as sad
from src.utils import sort_descending as sd
from src.utils import l_infty_error as lie
import pickle
from tqdm import tqdm
import sys

##################################### PARAMETERS #####################################
# Dataset
dataset_name = sys.argv[1]
print(dataset_name)
# Search parameters
search_ranks = [0,1,2,3,4,-5,-4,-3,-2,-1]
# Approximation parameters
trials = int(sys.argv[2])
eps = 1e-32 # tolerance
# Approximation methods, check approximator for options
# approx_mthds = [bki_adp, oth_nonadp, sw_nonadp, oth_adp]
mthds = sys.argv[3]
# print(approx_mthds)
if not mthds:
    print("no methods selected; please choose among: bki_adp_Q, bki_adp_Z, oth_nonadp, sw_nonadp, oth_adp without spaces")
    sys.exit()
else:
    if "full" in mthds:
        approx_mthds = "bki_adp_Q,bki_adp_Z,oth_nonadp,sw_nonadp,oth_adp"
    else:
        approx_mthds = mthds
approx_mthds = approx_mthds.split(",")
print(approx_mthds)
######################################################################################

################################### GRAB THE MATRICES ################################
true_mat, dataset_size, min_samples, max_samples = get_data(dataset_name)

true_spectrum, _ = np.linalg.eig(true_mat)
true_spectrum = sd(np.real(true_spectrum)) # sort eigvals in descending order
# true_spectrum = true_spectrum[search_ranks]
max_abs_eigval = max(np.abs(true_spectrum[0]), np.abs(true_spectrum[-1]))

print("loaded datasets")
print("A_infty:", np.max(true_mat))
print("top true eigvals:", true_spectrum[search_ranks])
print("true eigvals len:", len(true_spectrum))
print("search ranks:", search_ranks)
print("trials:", trials)
######################################################################################

##################################### SAVERS #########################################
params = {"sr": search_ranks, "eps": eps, "A_infty": np.max(true_mat), \
            "true_eigs": true_spectrum}
save_dict = {}
######################################################################################

########################### Approximator -- bki_adp ##################################
if "bki_adp_Q" in approx_mthds:
    print("Approximator: Block Krylov Adaptive: Q")
    all_ks = list(range(20,100,100))
    all_qs = list(range(0,11,2))
    avg_errors = np.zeros((len(all_ks)*len(all_qs), len(search_ranks)))
    p20_errors = np.zeros((len(all_ks)*len(all_qs), len(search_ranks)))
    p80_errors = np.zeros((len(all_ks)*len(all_qs), len(search_ranks)))
    avg_lies = np.zeros(len(all_ks)*len(all_qs))
    p20_lies = np.zeros(len(all_ks)*len(all_qs))
    p80_errors = np.zeros(len(all_ks)*len(all_qs))
    matvecs_all = np.zeros(len(all_ks)*len(all_qs))
    count = 0
    for i in tqdm(range(len(all_ks)), position=0):
      k = all_ks[i]
      for j in range(len(all_qs)):
            q = all_qs[j]
            errors = np.zeros((trials, len(search_ranks)))
            lies = np.zeros(trials)
            for t in range(trials):
                alpha, matvecs = bki_adp(true_mat, k=k, k_given=True, \
                                        q=q, q_given=True, mode="Q", sr=[])
                errors[t,:] = np.abs(true_spectrum[search_ranks] - alpha[search_ranks]) / max_abs_eigval
                lies[t] = lie(true_spectrum, alpha, max_abs_eigval)

            avg_errors[count, :] = np.log(np.abs(np.mean(errors, axis=0)) + eps)
            p20_errors[count, :] = np.log(np.abs(np.percentile(errors,q=20, axis=0)) + eps)
            p80_errors[count, :] = np.log(np.abs(np.percentile(errors,q=80, axis=0)) + eps)
            avg_lies[count] = np.log(np.abs(np.mean(lies)) + eps)
            p20_lies[count] = np.log(np.abs(np.percentile(lies, q=20)) + eps)
            p80_lies[count] = np.log(np.abs(np.percentile(lies, q=80)) + eps)
            matvecs_all[count] = matvecs
            count += 1
    save_dict["bki_adp_Q"] = []
    save_dict["bki_adp_Q"].append(avg_errors)  #0
    save_dict["bki_adp_Q"].append(p20_errors)  #1
    save_dict["bki_adp_Q"].append(p80_errors)  #2
    save_dict["bki_adp_Q"].append(avg_lies)    #3 
    save_dict["bki_adp_Q"].append(p20_lies)    #4
    save_dict["bki_adp_Q"].append(p80_lies)    #5
    save_dict["bki_adp_Q"].append(matvecs_all) #6
######################################################################################

########################### Approximator -- bki_adp ##################################
if "bki_adp_Z" in approx_mthds:
    print("Approximator: Block Krylov Adaptive: Z")
    all_ks = list(range(20,100,100))
    all_qs = list(range(0,11,2))
    avg_errors = np.zeros((len(all_ks)*len(all_qs), len(search_ranks)))
    p20_errors = np.zeros((len(all_ks)*len(all_qs), len(search_ranks)))
    p80_errors = np.zeros((len(all_ks)*len(all_qs), len(search_ranks)))
    avg_lies = np.zeros(len(all_ks)*len(all_qs))
    p20_lies = np.zeros(len(all_ks)*len(all_qs))
    p80_lies = np.zeros(len(all_ks)*len(all_qs))
    matvecs_all = np.zeros(len(all_ks)*len(all_qs))
    count = 0
    for i in tqdm(range(len(all_ks)), position=0):
        k = all_ks[i]
        for j in range(len(all_qs)):
            q = all_qs[j]
            errors = np.zeros((trials, len(search_ranks)))
            lies = np.zeros(trials)
            for t in range(trials):
                alpha, matvecs = bki_adp(true_mat, k=k, k_given=True, q=q, q_given=True, mode="Z", sr=[])
                errors[t,:] = np.abs(true_spectrum[search_ranks] - alpha[search_ranks]) / max_abs_eigval
                lies[t] = lie(true_spectrum, alpha, max_abs_eigval)

            avg_errors[count, :] = np.log(np.abs(np.mean(errors, axis=0)) + eps)
            p20_errors[count, :] = np.log(np.abs(np.percentile(errors, q=20, axis=0)) + eps)
            p80_errors[count, :] = np.log(np.abs(np.percentile(errors, q=80, axis=0)) + eps)
            avg_lies[count] = np.log(np.abs(np.mean(lies)) + eps)
            p20_lies[count] = np.log(np.abs(np.percentile(lies, q=20)) + eps)
            p20_lies[count] = np.log(np.abs(np.percentile(lies, q=80)) + eps)
            matvecs_all[count] = matvecs
            count += 1
    save_dict["bki_adp_Z"] = []
    save_dict["bki_adp_Z"].append(avg_errors)
    save_dict["bki_adp_Z"].append(p20_errors)
    save_dict["bki_adp_Z"].append(p80_errors)
    save_dict["bki_adp_Z"].append(avg_lies)
    save_dict["bki_adp_Z"].append(p20_lies)
    save_dict["bki_adp_Z"].append(p80_lies)
    save_dict["bki_adp_Z"].append(matvecs_all)
######################################################################################

########################### Approximator -- oth_adp ##################################
if "oth_adp" in approx_mthds:
    print("Approximator: Orthogonal Subspace Adaptive")
    all_ks = list(range(40,500,50))
    avg_errors = np.zeros((len(all_ks), len(search_ranks)))
    p20_errors = np.zeros((len(all_ks), len(search_ranks)))
    p80_errors = np.zeros((len(all_ks), len(search_ranks)))
    avg_lies = np.zeros(len(all_ks))
    p20_lies = np.zeros(len(all_ks))
    p80_lies = np.zeros(len(all_ks))
    matvecs_all = np.zeros(len(all_ks))
    count = 0
    for i in tqdm(range(len(all_ks)), position=0):
        k = all_ks[i]
        errors = np.zeros((trials, len(search_ranks)))
        lies = np.zeros(trials)
        for t in range(trials):
            alpha, matvecs = oth_adp(true_mat, k=k, sr=[])
            errors[t,:] = np.abs(true_spectrum[search_ranks] - alpha[search_ranks]) / max_abs_eigval
            lies[t] = lie(true_spectrum, alpha, max_abs_eigval)

        avg_errors[count, :] = np.log(np.abs(np.mean(errors, axis=0)) + eps)
        p20_errors[count, :] = np.log(np.abs(np.percentile(errors, q=20, axis=0)) + eps)
        p80_errors[count, :] = np.log(np.abs(np.percentile(errors, q=80, axis=0)) + eps)
        avg_lies[count] = np.log(np.abs(np.mean(lies)) + eps)
        p20_lies[count] = np.log(np.abs(np.percentile(lies, q=20)) + eps)
        p80_lies[count] = np.log(np.abs(np.percentile(lies, q=80)) + eps)
        matvecs_all[count] = matvecs
        count += 1
    save_dict["oth_adp"] = []
    save_dict["oth_adp"].append(avg_errors)
    save_dict["oth_adp"].append(p20_errors)
    save_dict["oth_adp"].append(p80_errors)
    save_dict["oth_adp"].append(avg_lies)
    save_dict["oth_adp"].append(p20_lies)
    save_dict["oth_adp"].append(p80_lies)
    save_dict["oth_adp"].append(matvecs_all)
######################################################################################

######################### Approximator -- sw_nonadp ##################################
if "sw_nonadp" in approx_mthds:
    print("Approximator: Sketching with Trace Subtraction")
    all_ks = list(range(50,500,50))
    avg_errors = np.zeros((len(all_ks), len(search_ranks)))
    p20_errors = np.zeros((len(all_ks), len(search_ranks)))
    p80_errors = np.zeros((len(all_ks), len(search_ranks)))
    avg_lies = np.zeros(len(all_ks))
    p20_lies = np.zeros(len(all_ks))
    p80_lies = np.zeros(len(all_ks))
    matvecs_all = np.zeros(len(all_ks))
    count = 0
    for i in tqdm(range(len(all_ks)), position=0):
        k = all_ks[i]
        errors = np.zeros((trials, len(search_ranks)))
        lies = np.zeros(trials)
        for t in range(trials):
            alpha, matvecs = sw_nonadp(true_mat, k=k, sr=[])
            errors[t,:] = np.abs(true_spectrum[search_ranks] - alpha[search_ranks]) / max_abs_eigval
            lies[t] = lie(true_spectrum, alpha, max_abs_eigval)

        avg_errors[count, :] = np.log(np.abs(np.mean(errors, axis=0)) + eps)
        p20_errors[count, :] = np.log(np.abs(np.percentile(errors, q=20, axis=0)) + eps)
        p80_errors[count, :] = np.log(np.abs(np.percentile(errors, q=80, axis=0)) + eps)
        avg_lies[count] = np.log(np.abs(np.mean(lies)) + eps)
        p20_lies[count] = np.log(np.abs(np.percentile(lies, q=20)) + eps)
        p80_lies[count] = np.log(np.abs(np.percentile(lies, q=80)) + eps)
        matvecs_all[count] = matvecs
        count += 1
    save_dict["sw_nonadp"] = []
    save_dict["sw_nonadp"].append(avg_errors)
    save_dict["sw_nonadp"].append(p20_errors)
    save_dict["sw_nonadp"].append(p80_errors)
    save_dict["sw_nonadp"].append(avg_lies)
    save_dict["sw_nonadp"].append(p20_lies)
    save_dict["sw_nonadp"].append(p80_lies)
    save_dict["sw_nonadp"].append(matvecs_all)
######################################################################################

######################### Approximator -- oth_nonadp #################################
if "oth_nonadp" in approx_mthds:
    print("Approximator: Orthogonal Subspace Non-adaptive")
    all_ks = list(range(20,500,50))
    all_cs = list(range(2,3,1))
    avg_errors = np.zeros((len(all_ks)*len(all_cs), len(search_ranks)))
    p20_errors = np.zeros((len(all_ks)*len(all_cs), len(search_ranks)))
    p80_errors = np.zeros((len(all_ks)*len(all_cs), len(search_ranks)))
    avg_lies = np.zeros(len(all_ks)*len(all_cs))
    p20_lies = np.zeros(len(all_ks)*len(all_cs))
    p80_lies = np.zeros(len(all_ks)*len(all_cs))
    matvecs_all = np.zeros(len(all_ks)*len(all_cs))
    count = 0
    for i in tqdm(range(len(all_ks)), position=0):
        k = all_ks[i]
        for j in range(len(all_cs)):
            c = all_cs[j]
            errors = np.zeros((trials, len(search_ranks)))
            lies = np.zeros(trials)
            for t in range(trials):
                alpha, matvecs = oth_nonadp(true_mat, k=k, c=c, sr=[])
                errors[t,:] = np.abs(true_spectrum[search_ranks] - alpha[search_ranks]) / max_abs_eigval
                lies[t] = lie(true_spectrum, alpha, max_abs_eigval)

            avg_errors[count, :] = np.log(np.abs(np.mean(errors, axis=0)) + eps)
            p20_errors[count, :] = np.log(np.abs(np.percentile(errors, q=20, axis=0)) + eps)
            p80_errors[count, :] = np.log(np.abs(np.percentile(errors, q=80, axis=0)) + eps)
            avg_lies[count] = np.log(np.abs(np.mean(lies)) + eps)
            p20_lies[count] = np.log(np.abs(np.percentile(lies, q=20)) + eps)
            p80_lies[count] = np.log(np.abs(np.percentile(lies, q=80)) + eps)
            matvecs_all[count] = matvecs
            count += 1
    save_dict["oth_nonadp"] = []
    save_dict["oth_nonadp"].append(avg_errors)
    save_dict["oth_nonadp"].append(p20_errors)
    save_dict["oth_nonadp"].append(p80_errors)
    save_dict["oth_nonadp"].append(avg_lies)
    save_dict["oth_nonadp"].append(p20_lies)
    save_dict["oth_nonadp"].append(p80_lies)
    save_dict["oth_nonadp"].append(matvecs_all)
######################################################################################

############################# SAVE VALS ##############################################
adder = ""
if mthds == "full":
    adder = "_"+mthds
else:
    for i in approx_mthds:
        adder = adder+"_"+i
save_vars = {"params": params, "save_vals": save_dict}
with open("results/"+dataset_name+adder+".pkl", "wb") as f:
    pickle.dump(save_vars, f)
######################################################################################
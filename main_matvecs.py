import numpy as np
from src.approximator import eigval_approx_bki_adaptive as bki_adp
from src.approximator import eigval_approx_othro_adaptive as oth_adp
from src.approximator import eigval_approx_ortho_nonadaptive_2 as oth_nonadp
from src.approximator import eigval_approx_SW_nonadaptive as sw_nonadp
from src.get_dataset import get_data
from src.utils import sort_abs_descending as sad
import pickle
from tqdm import tqdm
import sys
# import matplotlib.pyplot as plt

##################################### PARAMETERS #####################################
# Dataset
dataset_name = sys.argv[1]
print(dataset_name)
# Search parameters
search_ranks = [0,1,2,3,4,5]
# Approximation parameters
trials = int(sys.argv[2])
eps = 1e-32 # tolerance
# Approximation methods, check approximator for options
# approx_mthds = [bki_adp, oth_nonadp, sw_nonadp, oth_adp]
######################################################################################

################################### GRAB THE MATRICES ################################
true_mat, dataset_size, min_samples, max_samples = get_data(dataset_name)

true_spectrum, _ = np.linalg.eig(true_mat)
true_spectrum = sad(np.real(true_spectrum))
true_spectrum = true_spectrum[search_ranks]

print("loaded datasets")
print("A_infty:", np.max(true_mat))
print("true eigvals:", true_spectrum[search_ranks])
print("search ranks:", search_ranks)
print("trials:", trials)
######################################################################################

##################################### SAVERS #########################################
params = {"sr": search_ranks, "eps": eps, "A_infty": np.max(true_mat), "true_eigs": true_spectrum}
save_dict = {}
######################################################################################

########################### Approximator -- bki_adp ##################################
print("Approximator: Block Krylov Adaptive: Q")
all_ks = list(range(200,1000,100))
all_qs = list(range(0,11,3))
avg_errors = np.zeros((len(all_ks)*len(all_qs), len(search_ranks)))
std_errors = np.zeros((len(all_ks)*len(all_qs), len(search_ranks)))
matvecs_all = np.zeros(len(all_ks)*len(all_qs))
count = 0
for i in tqdm(range(len(all_ks)), position=0):
  k = all_ks[i]
  for j in range(len(all_qs)):
      q = all_qs[j]
      errors = np.zeros((trials, len(search_ranks)))
      for t in range(trials):
          alpha, matvecs = bki_adp(true_mat, k=k, k_given=True, q=q, q_given=True, mode="Q", sr=search_ranks)
          errors[t,:] = np.abs(true_spectrum - alpha)
      avg_errors[count, :] = np.log(np.abs(np.mean(errors, axis=0)) + eps)
      std_errors[count, :] = np.log(np.abs(np.std(errors, axis=0)) + eps)
      matvecs_all[count] = matvecs
      count += 1
P1 = avg_errors - std_errors
P2 = avg_errors + std_errors
save_dict["bki_adp_Q"] = []
save_dict["bki_adp_Q"].append(avg_errors)
save_dict["bki_adp_Q"].append(std_errors)
save_dict["bki_adp_Q"].append(P1)
save_dict["bki_adp_Q"].append(P2)
save_dict["bki_adp_Q"].append(matvecs_all)
######################################################################################

########################### Approximator -- bki_adp ##################################
print("Approximator: Block Krylov Adaptive: Z")
all_ks = list(range(200,1000,100))
all_qs = list(range(0,11,3))
avg_errors = np.zeros((len(all_ks)*len(all_qs), len(search_ranks)))
std_errors = np.zeros((len(all_ks)*len(all_qs), len(search_ranks)))
matvecs_all = np.zeros(len(all_ks)*len(all_qs))
count = 0
for i in tqdm(range(len(all_ks)), position=0):
  k = all_ks[i]
  for j in range(len(all_qs)):
      q = all_qs[j]
      errors = np.zeros((trials, len(search_ranks)))
      for t in range(trials):
          alpha, matvecs = bki_adp(true_mat, k=k, k_given=True, q=q, q_given=True, mode="Z", sr=search_ranks)
          errors[t,:] = np.abs(true_spectrum - alpha)
      avg_errors[count, :] = np.log(np.abs(np.mean(errors, axis=0)) + eps)
      std_errors[count, :] = np.log(np.abs(np.std(errors, axis=0)) + eps)
      matvecs_all[count] = matvecs
      count += 1
P1 = avg_errors - std_errors
P2 = avg_errors + std_errors
save_dict["bki_adp_Z"] = []
save_dict["bki_adp_Z"].append(avg_errors)
save_dict["bki_adp_Z"].append(std_errors)
save_dict["bki_adp_Z"].append(P1)
save_dict["bki_adp_Z"].append(P2)
save_dict["bki_adp_Z"].append(matvecs_all)
######################################################################################

########################### Approximator -- oth_adp ##################################
print("Approximator: Orthogonal Subspace Adaptive")
all_ks = list(range(50,3000,50))
avg_errors = np.zeros((len(all_ks), len(search_ranks)))
std_errors = np.zeros((len(all_ks), len(search_ranks)))
matvecs_all = np.zeros(len(all_ks))
count = 0
for i in tqdm(range(len(all_ks)), position=0):
    k = all_ks[i]
    errors = np.zeros((trials, len(search_ranks)))
    for t in range(trials):
        alpha, matvecs = oth_adp(true_mat, k=k, sr=search_ranks)
        errors[t,:] = np.abs(true_spectrum - alpha)
    avg_errors[count, :] = np.log(np.abs(np.mean(errors, axis=0)) + eps)
    std_errors[count, :] = np.log(np.abs(np.std(errors, axis=0)) + eps)
    matvecs_all[count] = matvecs
    count += 1
P1 = avg_errors - std_errors
P2 = avg_errors + std_errors
save_dict["oth_adp"] = []
save_dict["oth_adp"].append(avg_errors)
save_dict["oth_adp"].append(std_errors)
save_dict["oth_adp"].append(P1)
save_dict["oth_adp"].append(P2)
save_dict["oth_adp"].append(matvecs_all)
######################################################################################

######################### Approximator -- sw_nonadp ##################################
print("Approximator: Sketching with Trace Subtraction")
all_ks = list(range(50,5000,100))
avg_errors = np.zeros((len(all_ks), len(search_ranks)))
std_errors = np.zeros((len(all_ks), len(search_ranks)))
matvecs_all = np.zeros(len(all_ks))
count = 0
for i in tqdm(range(len(all_ks)), position=0):
  k = all_ks[i]
  errors = np.zeros((trials, len(search_ranks)))
  for t in range(trials):
      alpha, matvecs = sw_nonadp(true_mat, k=k, sr=search_ranks)
      errors[t,:] = np.abs(true_spectrum - alpha)
  avg_errors[count, :] = np.log(np.abs(np.mean(errors, axis=0)) + eps)
  std_errors[count, :] = np.log(np.abs(np.std(errors, axis=0)) + eps)
  matvecs_all[count] = matvecs
  count += 1
P1 = avg_errors - std_errors
P2 = avg_errors + std_errors
save_dict["sw_nonadp"] = []
save_dict["sw_nonadp"].append(avg_errors)
save_dict["sw_nonadp"].append(std_errors)
save_dict["sw_nonadp"].append(P1)
save_dict["sw_nonadp"].append(P2)
save_dict["sw_nonadp"].append(matvecs_all)
######################################################################################

######################### Approximator -- oth_nonadp #################################
print("Approximator: Orthogonal Subspace Non-adaptive")
all_ks = list(range(25,400,25))
all_cs = list(range(1,11,3))
avg_errors = np.zeros((len(all_ks)*len(all_cs), len(search_ranks)))
std_errors = np.zeros((len(all_ks)*len(all_cs), len(search_ranks)))
matvecs_all = np.zeros(len(all_ks)*len(all_cs))
count = 0
for i in tqdm(range(len(all_ks)), position=0):
  k = all_ks[i]
  for j in range(len(all_cs)):
      c = all_cs[j]
      errors = np.zeros((trials, len(search_ranks)))
      for t in range(trials):
          alpha, matvecs = oth_nonadp(true_mat, k=k, c=c, sr=search_ranks)
          errors[t,:] = np.abs(true_spectrum - alpha)
      avg_errors[count, :] = np.log(np.abs(np.mean(errors, axis=0)) + eps)
      std_errors[count, :] = np.log(np.abs(np.std(errors, axis=0)) + eps)
      matvecs_all[count] = matvecs
      count += 1
P1 = avg_errors - std_errors
P2 = avg_errors + std_errors
save_dict["oth_nonadp"] = []
save_dict["oth_nonadp"].append(avg_errors)
save_dict["oth_nonadp"].append(std_errors)
save_dict["oth_nonadp"].append(P1)
save_dict["oth_nonadp"].append(P2)
save_dict["oth_nonadp"].append(matvecs_all)
# ######################################################################################

############################# SAVE VALS ##############################################
save_vars = {"params": params, "save_vals": save_dict}
with open("results/"+dataset_name+".pkl", "wb") as f:
    pickle.dump(save_vars, f)
######################################################################################
import numpy as np
import pickle as pkl
import matplotlib.pyplot as plt
import os

dataset_name = "random_random"

with open("results/"+dataset_name+".pkl", "rb") as f:
    results = pkl.load(f)

params = results["params"]
approx_results = results["approx_results"]

true_spectrum = params["true_spectrum"][params["search_rank"]]
true_spectrum = np.expand_dims(true_spectrum, axis=0)
true_spectrum = np.expand_dims(true_spectrum, axis=0)

eps = 1e-32

for mv in params["approx_mthds"]:
    if mv.__name__ == "eigval_approx_SW_nonadaptive":
        approx_eigvals = approx_results[mv.__name__]
        errors = np.abs(approx_eigvals - true_spectrum) / float(np.sqrt(np.count_nonzero(params["true_mat"])))

        mean_errors = np.log(np.mean(errors, axis=1)+eps)
        p20_errors = np.log(np.percentile(errors, 20, axis=1))
        p80_errors = np.log(np.percentile(errors, 80, axis=1))

        all_k = np.log(params["ks"])

        plt.gcf().clear()
        plt.rcParams.update({'font.size': 12})
        for sr in params["search_rank"]:
            plt.plot(all_k, mean_errors[:, sr], label="log(mean errors)")
            plt.fill_between(all_k, p20_errors[:, sr], p80_errors[:, sr], alpha=0.2)
            plt.xlabel("log(k)")
            plt.ylabel("log(errors)")
            plt.title(mv.__name__+" with rank "+str(sr))
            plt.legend()
            filename = "results/"+dataset_name+"/"+mv.__name__+"_rank_"+str(sr)+".png"
            if not os.path.exists(os.path.dirname(filename)):
                os.makedirs(os.path.dirname(filename))
            plt.savefig(filename)
            pass
        pass
    pass


import numpy as np
from src.display_codes import plot_errors
import pickle as pkl

dataset_name = "facebook"

with open("results/"+dataset_name+".pkl", "rb") as f:
    results = pkl.load(f)

params = results["params"]
approx_results = results["approx_results"]
matvec_results = results["matvec_results"]

# aggregate results
eps = 1e-32

true_spectrum = params["true_spectrum"][params["search_rank"]]
true_spectrum = np.expand_dims(true_spectrum, axis=0)
true_spectrum = np.expand_dims(true_spectrum, axis=0)

errors = {}
p20 = {}
p80 = {}
avg_matvecs = {}
for mv in params["approx_mthds"]:
    errs = np.abs(approx_results[mv.__name__] - true_spectrum) \
            / float(np.sqrt(np.count_nonzero(params["true_mat"])))
    errs = np.log(errs+eps)

    errors[mv.__name__] = np.mean(errs, axis=1)

    p20[mv.__name__] = np.percentile(errs, 20, axis=1)
    p80[mv.__name__] = np.percentile(errs, 80, axis=1)

    avg_matvecs[mv.__name__] = np.log(np.mean(matvec_results[mv.__name__], axis=1))

# plot results
plot_errors(params, errors, p20, p80, avg_matvecs)

import numpy as np
import pickle

files = "results/facebook/single_eval_method_egfqr_10.pkl"
with open(files, "rb") as f:
    load_vars = pickle.load(f)
plot_vars = load_vars["plt_vals"]
xvals = plot_vars["log_matvecs"]
yvals = plot_vars["mean_log_errors"]

print(load_vars["params"]["iters"])
print(load_vars["params"]["block_sizes"])
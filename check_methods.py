import numpy as np
import pickle as pkl

dataset_name = "random_random"

with open("results/"+dataset_name+".pkl", "rb") as f:
    results = pkl.load(f)

params = results["params"]
approx_results = results["approx_results"]

true_spectrum = params["true_spectrum"]
print(true_spectrum)

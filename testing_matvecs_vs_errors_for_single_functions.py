import numpy as np
from src.utils import StrToFunc
import sys
import os
from tqdm import tqdm
from src.utils import l_infty_error as lie
from src.get_dataset import get_data
from src.utils import sort_descending as sd
import pickle as pkl

def plotter(dataset, plot_vals, mode="fix_ks"):
    dir_ = "figures/"
    filedir = dataset
    filepath = os.path.join(dir_, filedir, mode)
    if not os.path.isdir(filepath):
        os.makedirs(filepath)
    if mode == "fix_ks":
        for i in range(len(plot_vals["ks"])):
            k = plot_vals["ks"][i]
            plt.gcf.clf()
            for j in range(len(plot_vals["iters"])):
                ite = plot_vals["iters"][j]
                if len(plot_vals["iters"]) == 1:
                    plt.plot(plot_vals["log_matvecs"][k,:,1],\
                             plot_vals["mean_log_lies"][j])
                    plt.fill_between(
                                     plot_vals["log_matvecs"],\
                                     plot_vals["p20_log_lies"][j],\
                                     plot_vals["p80_log_lies"][j]
                                    )
                else:
                    plt.plot(plot_vals["log_matvecs"],\
                             plot_vals["mean_log_lies"][j],\
                             label=str(j))
                    plt.fill_between(
                                     plot_vals["log_matvecs"],\
                                     plot_vals["p20_log_lies"][j],\
                                     plot_vals["p80_log_lies"][j]
                                    )


        pass
    if mode == "fix_iters":
        plt.gcf.clf()
        pass
    return None

def processor(dataset, outputs, params):
    eps = 1e-32
    # get true eigenvalues for the search ranks
    true_spectrum = outputs["true_spectrum"][params["search_rank"]]
    # get the max magnitude eigenvalue
    max_abs_eigval = max(np.abs(true_spectrum[0]), np.abs(true_spectrum[-1]))
    # expand dims to match shape of approx_eigvals
    true_spectrum = np.expand_dims(true_spectrum, axis=(0,1,2))
    # compute log absolute errors
    abs_errors = np.abs(outputs["approx_eigvals"] - true_spectrum) / max_abs_eigval
    log_lies = np.log(np.max(abs_errors, axis=3)+eps)
    # now compute avg and percentiles
    mean_log_lies = np.mean(log_lies, axis=0)
    p20_log_lies = np.percentile(log_lies, p=20, axis=0)
    p80_log_lies = np.percentile(log_lies, p=80, axis=0)
    log_matvecs = np.log(outputs["matvecs"])

    # values to send to the plotter function
    plot_vals = {
                 "mean_log_lies": mean_log_lies,
                 "p20_log_lies": p20_log_lies,
                 "p80_log_lies": p80_log_lies,
                 "log_matvecs": log_matvecs,
                 "max_abs_eigval": max_abs_eigval
                 "ks": params["ks"],
                 "iters": params["iters"]
                }

    # save these in a file so as to avoid recomputing
    save_dict = {"plt_vals": plot_vals, "outputs": outputs, "params": params}
    dir_path = os.path.join("results", dataset)
    if not os.path.isdir(dir_path):
        os.makedirs(dir_path)
    file_path = os.path.join(dir_path, params["method"]+".pkl")
    with open(file_path, "wb") as f:
        pickle.dump(save_vars, f)

    # plot: fix iters
    if not params["iters"]:
        pass
    else:
        plotter(dataset, plot_vals, mode="fix_iters")
    # plot: fix ks
    plotter(dataset, plot_vals, mode="fix_ks")
    return None

def computer(dataset, params):
    true_mat, dataset_size, _, _ = get_data(dataset)
    true_spectrum, _ = np.linalg.eig(true_mat)
    true_spectrum = sd(np.real(true_spectrum))

    method = StrToFunc(params["method"])

    ts = len(range(params["trials"]))
    ks = len(range(params["ks"]))
    srs = len(params["sr"])
    if not params["iters"]:
        qs = len(params["iters"])
    else:
        qs = 1
    outputs = {"approx_eigvals": np.zeros((ts, ks, qs, srs)),
               "matvecs": np.zeros((ts, ks, qs, 1))}
    for t in tqdm(range(params["trials"])):
        for i in range(len(params["ks"])):
            k = params["ks"][i]
            if not params["iters"]:
                for j in range(len(params["iters"])):
                    q = params["iters"][j]
                    eigvals, matvecs = method(data_mat, k=k, iters=q, sr=params["search_rank"])
                    outputs["approx_eigvals"][t,i,j,:] = eigvals
                outputs["matvecs"][t,i,j,:] = matvecs
            else:
                eigvals, matvecs = method(data_mat, k=k, sr=params["search_rank"])
                outputs["approx_eigvals"][t,i,qs,:] = eigvals
                outputs["matvecs"][t,i,qs,:] = matvecs
    outputs["true_spectrum"] = true_spectrum
    return outputs

def main():
    # general setup
    dataset = sys.argv[1] 
    method = sys.argv[2]
    trials = int(sys.argv[3])

    # set up parameters
    sr = [0,1,2,3,4,-5,-4,-3,-2,-1]
    if "bki" in method or "egu" in method:
        ks = list(range(10,160,20))
        iters = list(range(0,1005,5))
        algo_params = {
                       "ks": ks, "iters": iters
                       }
    else:
        ks = list(range(10,150,10))
        algo_params = {"ks": ks, "iters": None}
    algo_params["trials"] = trials
    algo_params["search_rank"] = sr
    algo_params["method"] = method

    outputs = computer(dataset, algo_params)
    processor(dataset, outputs, params)
    return None

if __name__ == "__main__":
    main()
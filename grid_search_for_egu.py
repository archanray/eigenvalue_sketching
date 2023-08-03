import numpy as np
from src.utils_functions import StrToFunc
import sys
import os
from tqdm import tqdm
from src.utils import l_infty_error as lie
from src.get_dataset import get_data
from src.utils import sort_descending as sd
import pickle
import matplotlib.pyplot as plt
from src.utils import sorter

def looper(V, Vlow, Vhigh, xaxis, range_v1, \
           range_v2, filepath, titleval, method, labels="k"):
    fig = plt.figure()
    plt.gcf().clf()
    # fix v1s plot v2s
    # use v1s as labels
    for i in range(len(range_v1)):
        fix_v1 = range_v1[i]
        if len(range_v2) == 1:
            # just a single point, so makes no sense plotting,
            # come back with reversed agruments
            return None
        else:
            xvals, yvals = sorter(xaxis[i,:], V[i,:])
            plt.plot(xvals, yvals, label=labels+"="+str(float("{:.5f}".format(fix_v1))))
            xvals, y1vals, y2vals = sorter(xaxis[i,:], Vlow[i,:], Vhigh[i,:])
            plt.fill_between(xvals, y1vals, y2vals, alpha=0.2)
    plt.xlabel("log matvecs")
    plt.ylabel("log absolute errors")
    plt.legend()
    plt.title("max eigval="+str(titleval))
    plt.savefig(os.path.join(filepath, "grid_search_"+method+" "+labels+".pdf"))
    return None


def plotter(dataset, plot_vals, mode="fix_ks"):
    dir_ = "figures/"
    filedir = dataset
    filepath = os.path.join(dir_, filedir, mode)
    if not os.path.isdir(filepath):
        os.makedirs(filepath)
    if mode == "fix_ks":
        looper(
               plot_vals["mean_log_lies"],\
               plot_vals["p20_log_lies"],\
               plot_vals["p80_log_lies"],\
               plot_vals["log_matvecs"],\
               plot_vals["ks"],\
               plot_vals["lrs"],\
               filepath, plot_vals["max_abs_eigval"],\
               method=plot_vals["method"],\
               labels = "k"
              )
        pass
    if mode == "fix_lrs":
        looper(
               plot_vals["mean_log_lies"].T,\
               plot_vals["p20_log_lies"].T,\
               plot_vals["p80_log_lies"].T,\
               plot_vals["log_matvecs"].T,\
               plot_vals["lrs"],\
               plot_vals["ks"],\
               filepath, plot_vals["max_abs_eigval"],\
               method=plot_vals["method"],\
               labels = "lr"
              )
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
    p20_log_lies = np.percentile(log_lies, q=20, axis=0)
    p80_log_lies = np.percentile(log_lies, q=80, axis=0)
    log_matvecs = np.log(outputs["matvecs"]+eps)

    # values to send to the plotter function
    plot_vals = {
                 "mean_log_lies": mean_log_lies,
                 "p20_log_lies": p20_log_lies,
                 "p80_log_lies": p80_log_lies,
                 "log_matvecs": log_matvecs,
                 "max_abs_eigval": max_abs_eigval,
                 "ks": params["ks"],
                 "lrs": params["lrs"],
                 "method": params["method"]
                }

    # save these in a file so as to avoid recomputing
    save_dict = {"plt_vals": plot_vals, "outputs": outputs, "params": params}
    dir_path = os.path.join("results", dataset)
    if not os.path.isdir(dir_path):
        os.makedirs(dir_path)
    file_path = os.path.join(dir_path, "grid_search_"+params["method"]+".pkl")
    with open(file_path, "wb") as f:
        pickle.dump(save_dict, f)

    # plot: fix lrs
    plotter(dataset, plot_vals, mode="fix_lrs")
    return None

def computer(dataset, params):
    true_mat, dataset_size, _, _ = get_data(dataset)
    true_spectrum, _ = np.linalg.eig(true_mat)
    true_spectrum = sd(np.real(true_spectrum))

    method = StrToFunc(params["method"])

    ts = params["trials"]
    ks = len(params["ks"])
    lrs = len(params["lrs"])
    srs = len(params["search_rank"])
    ite = params["iters"][0]

    outputs = {"approx_eigvals": np.zeros((ts, ks, lrs, srs)),
               "matvecs": np.zeros((ks, lrs))}
    for t in tqdm(range(params["trials"])):
        for i in range(len(params["ks"])):
            k = params["ks"][i]
            for j in range(len(params["lrs"])):
                lr = params["lrs"][j]
                eigvals, matvecs = method(true_mat, \
                                          k=k, iters=ite, eta=lr,\
                                          sr=params["search_rank"])
                outputs["approx_eigvals"][t,i,j,:] = eigvals
                outputs["matvecs"][i,j] = matvecs
    outputs["true_spectrum"] = true_spectrum[params["search_rank"]]
    return outputs

def main():
    # general setup
    dataset = sys.argv[1] 
    trials = int(sys.argv[2])

    # set up parameters
    sr = [0,1,2,3,4,-5,-4,-3,-2,-1]
    ks = list(range(10,210,10))
    iters = [20]
    lr = list(np.arange(0.00051, 0.00060, 0.00001))
    algo_params = {
                    "ks": ks, "iters": iters,\
                    "trials": trials,\
                    "search_rank": sr,\
                    "method": "eg_unldd",\
                    "lrs": lr
                  }

    outputs = computer(dataset, algo_params)
    processor(dataset, outputs, algo_params)
    return None

if __name__ == "__main__":
    main()
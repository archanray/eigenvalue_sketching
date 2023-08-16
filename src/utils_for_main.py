import numpy as np
from src.utils import sort_descending as sd
from src.approximator import eigval_approx_bki_adaptive as bki_adp
from src.approximator import eigval_approx_othro_adaptive as oth_adp
from src.approximator import eigval_approx_ortho_nonadaptive_2 as oth_nonadp
from src.approximator import eigval_approx_SW_nonadaptive as sw_nonadp
from src.approximator import EigenGameUnloaded as egu
from src.approximator import EigenGameUnloaded2 as egu2
from src.approximator import eigval_approx_random_sample as ears

def StrToFunc(name: str):
    dict_of_funcs = {
                    "bki": bki_adp,
                    "oth_adp": oth_adp,
                    "oth_nonadp": oth_nonadp,
                    "sw_nonadp": sw_nonadp, 
                    "egu": egu,
                    "rand_samp": ears,
                    "e2": egu2
                    }

    if "bki" in name:
        return dict_of_funcs["bki"], name.split("_")[-1]
    elif "egu" in name:
        return dict_of_funcs["egu"], name.split("_")[-1]
    else:
        return dict_of_funcs[name], None

def saver(save_dict, name_adder="single_eval_method_"):
    import pickle
    import os
    dir_path = os.path.join("results", save_dict["args"].dataset)
    if not os.path.isdir(dir_path):
        os.makedirs(dir_path)
    if "single_eval_method_" in name_adder:
        file_path = os.path.join(dir_path, \
                             name_adder+str(save_dict["args"].method)+\
                             "_"+save_dict["args"].block_size+".pkl")
    with open(file_path, "wb") as f:
        pickle.dump(save_dict, f)
    return None

def get_eigs(true_mat, search_ranks):
    spectrum, _ = np.linalg.eig(true_mat)
    spectrum = sd(np.real(spectrum))
    return spectrum[search_ranks]

def computer(args, params, true_mat, method, mode, m1, m2):
    from tqdm import tqdm
    for t in tqdm(range(args.trials)):
        for i in tqdm(range(len(params["block_sizes"]))):
            k = params["block_sizes"][i]
            for j in tqdm(range(len(params["iters"]))):
                if "egu" in args.method or "bki" in args.method \
                                        or "e2" in args.method:
                    ite = params["iters"][j]
                    eigvals, matvecs = method(true_mat, \
                                              k=k, iters=ite,\
                                              sr=args.search_ranks, mode=mode)
                else:
                    eigvals, matvecs = method(true_mat, \
                                              k=k,\
                                              sr=args.search_ranks, mode=mode)
                m1[t,i,j,:] = eigvals
                m2[i,j] = matvecs
    return m1, m2

def processor(outputs, params, args):
    eps = 1e-32
    # get true eigenvalues for the search ranks
    true_spectrum = outputs["true_spectrum"]
    # get the max magnitude eigenvalue
    max_abs_eigval = max(np.abs(true_spectrum[0]), np.abs(true_spectrum[-1]))
    # expand dims to match shape of approx_eigvals
    true_spectrum = np.expand_dims(true_spectrum, axis=(0,1,2))
    # compute log absolute errors
    abs_errors = np.abs(outputs["approx_eigvals"] - true_spectrum) / max_abs_eigval
    log_abs_errors = np.log(abs_errors + eps)
    mean_log_errors = np.mean(log_abs_errors, axis=0)
    p20_log_errors = np.percentile(log_abs_errors, q=20, axis=0)
    p80_log_errors = np.percentile(log_abs_errors, q=80, axis=0)
    # # sort by log_matvecs
    # # no point in sorting as these values are sorted. 
    # # If they are not sorted, use the following line
    # # only required when using multiple ks and iters
    # log_matvecs, mean_log_errors = sorter(log_matvecs, mean_log_errors)
    log_lies = np.log(np.max(abs_errors, axis=3)+eps)
    # now compute avg and percentiles
    mean_log_lies = np.mean(log_lies, axis=0)
    # now compute avg and percentiles
    p20_log_lies = np.percentile(log_lies, q=20, axis=0)
    p80_log_lies = np.percentile(log_lies, q=80, axis=0)
    # flatten the first two dims
    # arr1, arr2, arr3: k*iters x sr
    # arr2: k*iters
    mean_log_errors = mean_log_errors.reshape(-1, mean_log_errors.shape[-1])
    p20_log_errors = p20_log_errors.reshape(-1, p20_log_errors.shape[-1])
    p80_log_errors = p80_log_errors.reshape(-1, p80_log_errors.shape[-1])
    mean_log_lies = mean_log_lies.flatten()
    p20_log_lies = p20_log_lies.flatten()
    p80_log_lies = p80_log_lies.flatten()
    log_matvecs = np.log(outputs["matvecs"]+eps).flatten()

    # values to send to the plotter function
    plot_vals = {
                 "mean_log_errors": mean_log_errors,
                 "p20_log_errors": p20_log_errors,
                 "p80_log_errors": p80_log_errors,
                 "mean_log_lies": mean_log_lies,
                 "p20_log_lies": p20_log_lies,
                 "p80_log_lies": p80_log_lies,
                 "log_matvecs": log_matvecs,
                 "max_abs_eigval": max_abs_eigval,
                 "block_sizes": params["block_sizes"],
                 "iters": params["iters"],
                 "method": args.method
                }

    # save these in a file so as to avoid recomputing
    save_dict = {"plt_vals": plot_vals, "outputs": outputs, "params": params,\
                "args": args}
    saver(save_dict)
    return None

def sorter(xvals, y1vals, y2vals=None):
    ids = np.argsort(xvals)
    xvals = xvals[ids]
    if len(y1vals.shape) == 1:
        y1vals = y1vals[ids]
    else:
        y1vals = y1vals[ids, :]
    if y2vals is None:
        return xvals, y1vals
    else:
        if len(y2vals.shape) == 1:
            y2vals = y2vals[ids]
        else:
            y2vals = y2vals[ids, :]
        return xvals, y1vals, y2vals
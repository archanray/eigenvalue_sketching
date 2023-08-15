import matplotlib.pyplot as plt
import numpy as np
import os

def display_image(image):
    """
    Display the image
    """
    plt.gcf().clear()
    plt.rcParams.update({'font.size': 12})
    plt.imshow(image, cmap="gray")
    plt.xlabel("x co-ordinates", fontsize=16)
    plt.ylabel("y co-ordinates", fontsize=16)
    
    plt.title("Original image", fontsize=16)
    filename = "./figures/kong/"
    if not os.path.isdir(filename):
        os.makedirs(filename)
    filename = filename+"kong-original.pdf"
    plt.savefig(filename)
    return None


def plot_errors(params, errors, p20, p80, matvecs):
    """
    Plot the errors for each method
    """
    for sr in params["search_rank"]:
        plt.gcf().clear()
        plt.rcParams.update({'font.size': 12})
        for mv in params["approx_mthds"]:
            E = errors[mv.__name__][:][:, sr]
            P1 = p20[mv.__name__][:][:, sr]
            P2 = p80[mv.__name__][:][:, sr]
            plt.plot(matvecs[mv.__name__], E, label=mv.__name__)
            plt.fill_between(matvecs[mv.__name__], P1, P2, alpha=0.2)
        plt.xlabel("log(Number of matrix-vector products)", fontsize=16)
        plt.ylabel("log(Error)", fontsize=16)
        plt.title(params["dataset_name"], fontsize=16)
        plt.legend()
        filename = "./figures/"+params["dataset_name"]+"/"
        if not os.path.isdir(filename):
            os.makedirs(filename)
        filename = filename+str(sr)+"-error.pdf"
        plt.savefig(filename)
    return None

def plotErrorForAll(names, datasets=["random"], \
                    default_load_path="results", \
                    adder="single_eval_method_",
                    plot_ranks=["lie"],
                    dest_="figures/",
                    legend=True):
    import pickle
    from matplotlib.pyplot import cm
    import colorcet as cc

    names.sort()

    for dataset in datasets:
        dir_ = os.path.join(default_load_path, dataset)
        path_root = os.path.join(dir_,adder)
        for plot_rank in plot_ranks:
            # n=len(names)
            plt.gcf().clf()
            color = iter(cc.cm.glasbey(np.linspace(0, 1, 10)))
            for name in names:
                c = next(color)
                path = path_root+name+".pkl"
                with open(path, "rb") as f:
                    load_vars = pickle.load(f)
                plot_vars = load_vars["plt_vals"]
                xvals = plot_vars["log_matvecs"]
                if plot_rank != "lie":
                    yvals = plot_vars["mean_log_errors"][:,plot_rank]
                    ylow = plot_vars["p20_log_errors"][:,plot_rank]
                    yhigh = plot_vars["p80_log_errors"][:,plot_rank]
                else:
                    yvals = plot_vars["mean_log_lies"]
                    ylow = plot_vars["p20_log_lies"]
                    yhigh = plot_vars["p80_log_lies"]
                plt.plot(xvals, yvals, label=name, color=c)
                plt.fill_between(xvals, ylow, yhigh, alpha=0.2, color=c)
            # plt.ylim([-8,0])
            plt.xlabel("log matvecs")
            plt.ylabel("log l_infty errors")
            if legend:
                plt.legend()
            else:
                # code for separate legend plot
                pass
            if plot_rank != "lie":
                plt.title("eigval="+\
                    str(load_vars["outputs"]["true_spectrum"][plot_rank]))
            else:
                plt.title("max eigval="+str(plot_vars["max_abs_eigval"]))

            filename = "_".join(names)
            filename = filename+"_"+str(plot_rank)

            dest_now = dest_+dataset+"/"
            if not os.path.isdir(dest_now):
                os.makedirs(dest_now)

            plt.savefig(dest_now+filename+".pdf")
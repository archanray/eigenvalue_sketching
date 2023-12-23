import matplotlib.pyplot as plt
import numpy as np
import os

def getMoreColors(n=10):
    import colorcet as cc
    color = iter(cc.cm.glasbey(np.linspace(0, 1, n)))
    for i in range(n):
        print(next(color))
    return None

def method2color(method):
    if method == "bki_adp_Q_10":
        color = [0.843137,0.,0.,1]
    if method == "bki_adp_Q_20":
        color = [0.352941,0.,0.643137,1]
    if method == "oth_adp_full" : 
        color = [0.462745,0.345098,0.239216,1]
    if method == "oth_nonadp_full" : 
        color = [1.,0.372549,0.580392,1]
    if method == "sw_nonadp_full" : 
        color = [0.537255,0.529412,0.74902,1]
    if method == "bki_adp_Q_40" : 
        color = [0.623529,0.623529,0.27451,1.]
    if method == "bki_adp_Q_80" : 
        color = [0.894118,0.,0.890196,1.]
    if method == "bki_adp_Q_1":
        color = [0.47451,0.623529,0.690196,1.]
    if method == "e3_10":
        color = [0.352941,0.345098,0.545098,1.]
    if method == "bki_adp_Q_1":
        color = [0.184314,0.243137,0.658824,1.]
    if method == "e3_20":
        color = [0.788235,0.478431,0.866667,1.]
    if method == "true_spectrum":
        color = [0.223529,0.431373,0.392157,1.]
    return color

def sixColors(method):
    if method == "bki_adp_Q_10":
        color="red" 
    if method == "bki_adp_Q_20":
        color="blue" 
    if method == "oth_adp_full":
        color="green" 
    if method == "oth_nonadp_full":
        color="goldenrod" 
    if method == "sw_nonadp_full":
        color="magenta" 
    if method == "true_spectrum":
        color="k"
    if method == "bki_adp_Q_40":
        color = "brown"
    if method == "e4_10":
        color = "darkturquoise"
    if method == "e4_20":
        color = "chocolate"
    return color

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

def plotEigvals(names, datasets=["random"],\
                default_load_path="results",\
                adder="single_eval_method_",\
                dest_="figures/",
                legend=True,matvecs=10):
    import pickle

    names.sort()
    font_size = 16

    markers = ["o", "*", "D", "^", "v", "1", "2", "3", "4", "x"]
    break_rank = 700
    plot_ranks = list(range(break_rank))+list(range(-break_rank,0,1))
    for dataset in datasets:
        dir_ = os.path.join(default_load_path, dataset)
        path_root = os.path.join(dir_,adder)    
        # n=len(names)
        plt.gcf().clf()
        # added lines
        # fig = plt.figure()
        # ax = fig.add_subplot()
        fig, (ax1, ax2) = plt.subplots(1, 2, sharey=True, \
                          facecolor='w')
        fig.subplots_adjust(wspace=0.15)
        plt.grid()
        ax1.set_axisbelow(True)
        ax1.yaxis.grid(color='gray', linestyle='dashed')
        ax1.xaxis.grid(color='gray', linestyle='dashed')
        ax2.set_axisbelow(True)
        ax2.yaxis.grid(color='gray', linestyle='dashed')
        ax2.xaxis.grid(color='gray', linestyle='dashed')
        plt.rcParams.update({'font.size': font_size-5})
        # color = iter(cc.cm.glasbey(np.linspace(0, 1, 10)))
        count=0
        for name in names:
            print(name)
            # c = next(color)
            path = path_root+name+".pkl"
            with open(path, "rb") as f:
                load_vars = pickle.load(f) #<-- contains all info
            trial_ID = 0
            approx_eigvals = load_vars["outputs"]["approx_eigvals"]
            matvecs_req = load_vars["outputs"]["matvecs"]
            if name == "oth_adp_full":
                matvecs_req = 2*matvecs_req
                # print(matvecs_req)
            xvals = np.array(list(range(approx_eigvals.shape[-1])))
            matvecs_ID = np.intersect1d(matvecs_req[np.where(matvecs_req \
                                                    <= matvecs+20)]\
                                        , \
                                        matvecs_req[np.where(matvecs_req \
                                                    >= matvecs-20)])
            if matvecs_req.shape[0] == 1:
                matvecs_ID = np.where(matvecs_req[0,:] == matvecs_ID[0])[0]
            if matvecs_req.shape[1] == 1:
                matvecs_ID = np.where(matvecs_req[:,0] == matvecs_ID[0])[0]

            if matvecs_req.shape[0] == 1:
                approx_eigvals = approx_eigvals[trial_ID,\
                                            0,\
                                            matvecs_ID[0],\
                                            plot_ranks]
            if matvecs_req.shape[1] == 1:
                approx_eigvals = approx_eigvals[trial_ID,\
                                            matvecs_ID[0],\
                                            0,\
                                            plot_ranks]
            ax1.plot(xvals[plot_ranks], \
                        approx_eigvals, color=sixColors(name),\
                        label=name)
            ax2.plot(xvals[plot_ranks], \
                        approx_eigvals, color=sixColors(name),\
                        label=name)
            # ax1.plot(xvals[plot_ranks], \
            #             approx_eigvals, color=method2color(name),\
            #             label=name)
            # ax2.plot(xvals[plot_ranks], \
            #             approx_eigvals, color=method2color(name),\
            #             label=name)
            count += 1
            # print(matvecs_req[0,int(matvecs_ID[0])])
            # print(approx_eigvals.shape[-1])
            # proportion_of_matvecs = matvecs_req[0,matvecs_ID[0]] / \
            #                         approx_eigvals.shape[-1]
            # print(proportion_of_matvecs)
    true_spectrum = load_vars["outputs"]["true_spectrum"]
    # with np.printoptions(threshold=np.inf):
    #     print(true_spectrum)
    ax1.plot(xvals[plot_ranks], \
                    true_spectrum[plot_ranks], \
                    color=sixColors("true_spectrum"),\
                    label="true")
    ax2.plot(xvals[plot_ranks], \
                    true_spectrum[plot_ranks], \
                    color=sixColors("true_spectrum"),\
                    label="true")
    # ax1.plot(xvals[plot_ranks], \
    #                 true_spectrum[plot_ranks], \
    #                 color=method2color("true_spectrum"),\
    #                 label="true")
    # ax2.plot(xvals[plot_ranks], \
    #                 true_spectrum[plot_ranks], \
    #                 color=method2color("true_spectrum"),\
    #                 label="true")
    # merge the plots
    ax1.set_xlim(0,break_rank)
    ax2.set_xlim(xvals[-break_rank],xvals[-1])
    ax1.spines['right'].set_visible(False)
    ax2.spines['left'].set_visible(False)
    ax1.yaxis.tick_left()
    ax2.yaxis.tick_right()
    d = .015  # how big to make the diagonal lines in axes coordinates
    # arguments to pass plot, just so we don't keep repeating them
    kwargs = dict(transform=ax1.transAxes, color='k', clip_on=False)
    ax1.plot((1-d, 1+d), (-d, +d), **kwargs)
    ax1.plot((1-d, 1+d), (1-d, 1+d), **kwargs)

    kwargs.update(transform=ax2.transAxes)  # switch to the bottom axes
    ax2.plot((-d, +d), (1-d, 1+d), **kwargs)
    ax2.plot((-d, +d), (-d, +d), **kwargs)
    # beautification, naming axes, labels, etc.
    # ax.set_xticks(xvals[plot_ranks])
    fig.supxlabel("Eigenvalue indices", fontsize=font_size)
    fig.supylabel("Eigenvalues", fontsize=font_size)
    if legend:
        plt.legend()
    else:
        # code for separate legend plot
        handles,labels = ax1.get_legend_handles_labels()
        pass
    # compress y range
    plt.ylim([-25,50]) # facebook
    # plt.ylim(-10,20) # facebook full methods
    # plt.ylim([-75,100]) # erdos
    # plt.ylim([-75,75]) # random
    # save the plot first
    filename = "_".join(names)
    filename = filename+"_approx_eigvals_"+str(matvecs)
    dest_now = dest_+dataset+"/"
    if not os.path.isdir(dest_now):
        os.makedirs(dest_now)
    plt.savefig(dest_now+dataset+"_"+filename+".pdf")

    if not legend:
        plt.gcf().clf()
        # print(handles)
        # print(labels)
        fig_legend = plt.figure()
        leg = fig_legend.legend(handles, labels, ncol=3, fontsize=font_size)
        leg_lines = leg.get_lines()
        plt.setp(leg_lines, linewidth=2)
        # for line in leg.legendHandles:
        #     leg.width(4.0)
        # axi.xaxis.set_visible(False)
        # axi.yaxis.set_visible(False)
        # fig_legend.canvas.draw()
        fig_legend.savefig(dest_now+"legend_"+\
            "_".join(names)+"_eigvals_legend_"+str(matvecs)+".pdf", bbox_inches='tight')
    return None

def plotErrorForAll(names, datasets=["random"], \
                    default_load_path="results", \
                    adder="single_eval_method_",
                    plot_ranks=["lie"],
                    dest_="figures/",
                    legend=True):
    import pickle
    from matplotlib.pyplot import cm
    # import colorcet as cc

    names.sort()
    font_size = 16

    #markers = ["o", "*", "D", "^", "v", "1", "2", "3", "4", "x"]
    for dataset in datasets:
        dir_ = os.path.join(default_load_path, dataset)
        path_root = os.path.join(dir_,adder)
        for plot_rank in plot_ranks:
            # n=len(names)
            plt.gcf().clf()
            # added lines
            fig = plt.figure()
            ax = fig.add_subplot()
            plt.rcParams.update({'font.size': font_size-5})
            # color = iter(cc.cm.glasbey(np.linspace(0, 1, 10)))
            count=0
            for name in names:
                # c = next(color)
                path = path_root+name+".pkl"
                with open(path, "rb") as f:
                    load_vars = pickle.load(f)
                plot_vars = load_vars["plt_vals"]
                xvals = plot_vars["log_matvecs"]
                if name == "oth_adp_full":
                    xvals = np.log(2)+xvals
                if plot_rank != "lie":
                    yvals = plot_vars["mean_log_errors"][:,plot_rank]
                    ylow = plot_vars["p20_log_errors"][:,plot_rank]
                    yhigh = plot_vars["p80_log_errors"][:,plot_rank]
                else:
                    yvals = plot_vars["mean_log_lies"]
                    ylow = plot_vars["p20_log_lies"]
                    yhigh = plot_vars["p80_log_lies"]
                # plt.plot(xvals, yvals, label=name, color=c)
                # plt.fill_between(xvals, ylow, yhigh, alpha=0.2, color=c)
                ax.plot(xvals, yvals, label=name, color=sixColors(name))#, \
                    #marker=markers[count])
                count += 1
                ax.fill_between(xvals, ylow, yhigh, alpha=0.2, 
                    color=sixColors(name))
            if plot_rank == "lie":
                if dataset == "facebook":
                    plt.ylim([-6,0])
                    # # for adaptive
                    # plt.ylim([-4.5,-0.5])
                    # # # for nonadaptive
                    # plt.ylim([-5.0,0])
                if dataset == "erdos":
                    pass
                    # plt.ylim([-6,0])
                    # # for adaptive
                    # plt.ylim([-4.2,0])
                    # # for nonadaptive
                    # plt.ylim([-4.0,0])
                if dataset == "random":
                    # plt.ylim([-10,-0.5])
                    # # for adaptive
                    # plt.ylim([-6,-3.5])
                    # for nonadaptive
                    plt.ylim([-6,-0.5])
                if dataset == "eye":
                    pass
                if dataset == "eye_block":
                    pass
                if dataset == "wishart_100":
                    plt.ylim([-10,2.0])
                if dataset == "wishart_200":
                    plt.ylim([-10,2.5])
                if dataset == "wishart_500":
                    plt.ylim([-10,2.5])
                if dataset == "wishart_1000":
                    plt.ylim([-10,2.5])
                pass
            plt.grid()
            plt.xlabel("Log matvecs", fontsize=font_size)
            plt.ylabel("Mean log abs errors", fontsize=font_size)
            if legend:
                plt.legend()
            else:
                # code for separate legend plot
                handles,labels = ax.get_legend_handles_labels()
                pass
            if plot_rank != "lie":
                plt.title("Eigval="+\
                    str(round(load_vars["outputs"]["true_spectrum"]\
                        [plot_rank],3)), fontsize=font_size)
            else:
                plt.title("Maximum eigval="+str(round(\
                    plot_vars["max_abs_eigval"],3)),fontsize=font_size)
            if "wishart" in dataset:
                rank = int(dataset.split("_")[-1])
                rank_x_axis_val = np.log(rank)
                # plot a vertical line
                plt.axvline(x=rank_x_axis_val, color="cyan")
            if "eye_block" in dataset:
                rank = 100
                rank_x_axis_val = np.log(rank)
                # plot a vertical line
                plt.axvline(x=rank_x_axis_val, color="cyan")

            filename = "_".join(names)
            filename = filename+"_"+str(plot_rank)

            dest_now = dest_+dataset+"/"
            if not os.path.isdir(dest_now):
                os.makedirs(dest_now)

            plt.savefig(dest_now+dataset+"_"+filename+".pdf")
            
            plt.close()
            if not legend:
                plt.gcf().clf()
                # print(handles)
                # print(labels)
                fig_legend = plt.figure()
                leg = fig_legend.legend(handles, labels, ncol=4, fontsize=font_size)
                leg_lines = leg.get_lines()
                plt.setp(leg_lines, linewidth=2)
                # for line in leg.legendHandles:
                #     leg.width(4.0)
                # axi.xaxis.set_visible(False)
                # axi.yaxis.set_visible(False)
                # fig_legend.canvas.draw()
                fig_legend.savefig(dest_now+"legend_"+\
                    "_".join(names)+".pdf", bbox_inches='tight')

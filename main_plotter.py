import numpy as np
import matplotlib.pyplot as plt
import pickle
import os
import sys
from matplotlib.pyplot import cm

dataset_name = sys.argv[1]
mthds = sys.argv[2]
if not mthds:
    print("no methods selected; please choose among: bki_adp_Q, bki_adp_Z, \
           oth_nonadp, sw_nonadp, oth_adp without spaces")
    sys.exit()
else:
    if "full" in mthds:
        approx_mthds = "bki_adp_Q,bki_adp_Z,oth_nonadp,sw_nonadp,oth_adp,eg_unldd"
    else:
        approx_mthds = mthds
approx_mthds = approx_mthds.split(",")
print(approx_mthds)

def sorter(xvals, y1vals, y2vals=None):
    ids = np.argsort(xvals)
    xvals = xvals[ids]
    y1vals = y1vals[ids]
    if y2vals is None:
        return xvals, y1vals
    else:
        y2vals = y2vals[ids]
        return xvals, y1vals, y2vals

########################## load data #######################
if "full" in mthds:
    with open("results/"+dataset_name+"_"+"full"+".pkl", "rb") as f:
        save_vars = pickle.load(f)
elif "eg_unldde" in mthds:
    with open("results/"+dataset_name+"_"+"bki_adp_Q_bki_adp_Z_eg_unldde"+".pkl", "rb") as f:
        save_vars = pickle.load(f)
print(save_vars["save_vals"].keys())
############################################################
# CHANGE THIS TO "" IF NOT TESTING
dataset_name_addr = ""#"test"
if dataset_name_addr == "":
    pass
else:
    dataset_name = dataset_name+"_"+dataset_name_addr

if not os.path.isdir("figures/"+dataset_name+"/"):
    os.makedirs("figures/"+dataset_name+"/")

######################### plots ############################
n = len(save_vars["save_vals"].keys())
for i in save_vars["params"]["sr"]:
    plt.gcf().clf()
    color = iter(cm.rainbow(np.linspace(0, 1, n)))
    for mthd in save_vars["save_vals"].keys():
        if mthd in approx_mthds:
            c = next(color)
            xvals, yvals = sorter(np.log(save_vars["save_vals"][mthd][6]), \
                                    save_vars["save_vals"][mthd][0][:,i])
            plt.plot(xvals, yvals, label=mthd, c=c)

            xvals, y1vals, y2vals = sorter(np.log(save_vars["save_vals"][mthd][6]), \
                                    save_vars["save_vals"][mthd][1][:,i], \
                                    save_vars["save_vals"][mthd][2][:,i])
            plt.fill_between(xvals, y1vals, y2vals, alpha=0.2, color=c)
    plt.xlabel("log matvecs")
    plt.ylabel("log absolute errors")
    plt.legend()
    plt.title("eigval="+str(save_vars["params"]["true_eigs"][i]))
    plt.savefig("figures/"+dataset_name+"/"+str(i)+"_"+mthds+".pdf")
############################################################

######################### plots lies ############################
plt.gcf().clf()
color = iter(cm.rainbow(np.linspace(0, 1, n)))
for mthd in save_vars["save_vals"].keys():
    if mthd in approx_mthds:
        c = next(color)
        xvals, yvals = sorter(np.log(save_vars["save_vals"][mthd][6]), \
                                save_vars["save_vals"][mthd][3])
        plt.plot(xvals, yvals, label=mthd, c=c)

        xvals, y1vals, y2vals = sorter(np.log(save_vars["save_vals"][mthd][6]), \
                                    save_vars["save_vals"][mthd][4], \
                                    save_vars["save_vals"][mthd][5])

        plt.fill_between(xvals, y1vals, y2vals, alpha=0.2, color=c)
# plt.ylim([-4,9])
plt.xlabel("log matvecs")
plt.ylabel("log l_infty errors")
plt.legend()
plt.title("max eigval="+str(save_vars["params"]["true_eigs"][0]))
plt.savefig("figures/"+dataset_name+"/"+"lIE_plots"+"_"+mthds+".pdf")
############################################################

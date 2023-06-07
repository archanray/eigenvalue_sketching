import numpy as np
import matplotlib.pyplot as plt
import pickle
import os

dataset_name = "random_random"

def sorter(xvals, yvals):
	ids = np.argsort(xvals)
	xvals = xvals[ids]
	yvals = yvals[ids]
	return xvals, yvals

########################## load data #######################
with open("results/"+dataset_name+".pkl", "rb") as f:
    save_vars = pickle.load(f)
print(save_vars["save_vals"].keys())
############################################################

######################### plots ############################
for i in save_vars["params"]["sr"]:
	print(i)
	plt.gcf().clf()
	for mthd in save_vars["save_vals"].keys():
		plt.plot(np.log(save_vars["save_vals"][mthd][4]), \
			save_vars["save_vals"][mthd][0][:,i], label=mthd)
		plt.fill_between(np.log(save_vars["save_vals"][mthd][4]), \
			save_vars["save_vals"][mthd][2][:,i], \
			save_vars["save_vals"][mthd][3][:,i], alpha=0.2)
	plt.xlabel("log matvecs")
	plt.ylabel("log absolute errors")
	plt.legend()
	plt.title("eigval="+str(save_vars["params"]["true_eigs"][i]))
	plt.savefig("figures/"+dataset_name+"/"+str(i)+".pdf")
############################################################
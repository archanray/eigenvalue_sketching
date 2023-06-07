import numpy as np
import matplotlib.pyplot as plt
import pickle
import os

dataset_name = "facebook"

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
with open("results/"+dataset_name+".pkl", "rb") as f:
    save_vars = pickle.load(f)
print(save_vars["save_vals"].keys())
############################################################

######################### plots ############################
for i in save_vars["params"]["sr"]:
	print(i)
	plt.gcf().clf()
	for mthd in save_vars["save_vals"].keys():
		xvals, yvals = sorter(np.log(save_vars["save_vals"][mthd][4]), \
								save_vars["save_vals"][mthd][0][:,i])
		plt.plot(xvals, yvals, label=mthd)

		xvals, y1vals, y2vals = sorter(np.log(save_vars["save_vals"][mthd][4]), \
								save_vars["save_vals"][mthd][2][:,i], \
								save_vars["save_vals"][mthd][3][:,i])
		plt.fill_between(xvals, y1vals, y2vals, alpha=0.2)
	plt.xlabel("log matvecs")
	plt.ylabel("log absolute errors")
	plt.legend()
	plt.title("eigval="+str(save_vars["params"]["true_eigs"][i]))
	plt.savefig("figures/"+dataset_name+"/"+str(i)+".pdf")
############################################################
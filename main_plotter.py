import numpy as np
import matplotlib.pyplot as plt
import pickle

dataset_name = "random_random"

########################## load data #######################
with open("results/"+dataset_name+".pkl", "rb") as f:
    save_vars = pickle.load(f)
print(save_vars["save_vals"].keys())
############################################################

######################### plots ############################
for i in save_vars["params"]["sr"]:
	print(i)
	plt.gcf.clear()
	for mthd in save_vars["save_vals"].keys():
		plt.plot(np.log(save_vars["save_vals"][mthd][4]), \
			save_vars["save_vals"][mthd][0], label=mthd)
		plt.fill_between(np.log(save_vars["save_vals"][mthd][4]), \
			save_vars["save_vals"][mthd][2], \
			save_vars["save_vals"][mthd][3], alpha=0.2)
	plt.xlabel("log matvecs")
	plt.ylabel("log absolute errors")
	plt.legend()
	plt.title("eigval="+str(save_vars["params"]["true_eigs"][i]))
	plt.savefig("figures/"+dataset_name+"/"str(i)+".pdf")
############################################################
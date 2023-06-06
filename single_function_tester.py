import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
from src.get_dataset import get_data

# def get_data(name):
# 	if name == "random_random":
# 		n = 500
# 		A = np.random.random((n,n))
# 		A = (A+A.T) / 2
# 	return A

def sort_descending(v):
	v = -v
	v = np.sort(v)
	v = -v
	return v

def eigval_approx(A, k, c):
	S = np.random.randn(k, A.shape[1])
	T = np.random.randn(int(c*k), A.shape[1])
	AST = A @ (S.T)
	ATT = A @ (T.T)
	Btilde = (np.linalg.inv(AST.T @ T.T @ T @ AST)) @ AST.T @ T.T @ ATT.T
	Atilde = AST @ Btilde
	Abar = (Atilde+Atilde.T) / 2
	alpha, _ = np.linalg.eig(Abar)
	alpha = sort_descending(np.real(alpha))
	return alpha

# A = get_data("random_random")
A,_,_,_ = get_data("facebook")
lambda_A, _= np.linalg.eig(A)
lambda_A = sort_descending(np.real(lambda_A)) # these are the original eigenvalues
n = A.shape[1] # shape of the data matrix

c = np.arange(0.5,3,0.25)
all_ks = list(range(10,80,10))
trials = 10

for j in tqdm(range(len(c)), position=0):
	avg_errors = np.zeros((len(all_ks), n))
	# run eigval approx across multiple k and each for t trials
	for i in tqdm(range(len(all_ks)), position=1):
		k_now = all_ks[i]
		errors = np.zeros((trials, n))
		# trials
		for t in range(trials): 
			alpha = eigval_approx(A, k_now, c[j]) # these are the approximate eigvals at each round
			errors[t,:] = lambda_A - alpha # error at a single round

		avg_errors[i,:] = np.log(np.abs(np.mean(errors, axis=0)))


	print(avg_errors.shape, avg_errors[:,0].shape)
	plt.plot(np.log(np.array(all_ks)/n), avg_errors[:,0], label=str(c[j]))
# plt.ticklabel_format(axis='y', style='sci', scilimits=(4,4))
plt.ylim([-5,20])
plt.xlabel("log samples")
plt.ylabel("log absolute errors")
plt.legend()
plt.title("RSM, eigval="+str(lambda_A[0]))
plt.savefig("figures/non_adaptive_checks_facebook_data.pdf")
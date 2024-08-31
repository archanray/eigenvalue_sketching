import numpy as np
import argparse, os, pickle
from src.get_dataset import get_data
from src.approximator import *
from tqdm import tqdm

def get_error(A, B):
    l2_error = np.linalg.norm(A-B, ord=2)
    fro_error = np.linalg.norm(A-B, ord="fro")
    return l2_error, fro_error
    

def main(args):
    true_mat, n, _, _ = get_data(args.dataset)
    
    step_size = 20
    max_matvecs = n // 2
    
    save_vals = {}
    
    eigvals = np.linalg.eigvals(true_mat)
    
    for method in args.methods:
        save_vals = {}
        save_vals["eigvals"] = eigvals
        print("current method:", method)
        if "bki_adp_Q" in method:
            block_size = int(method.rsplit("_")[-1])
            qs = np.arange(1, (max_matvecs//block_size)+1, step_size//2).astype(int)
            errors_2Norm = np.zeros((args.trials, len(qs)))
            errors_FroNorm = np.zeros((args.trials, len(qs)))
            matvecs = np.zeros((args.trials, len(qs)))
            for i in tqdm(range(len(qs))):
                for t in range(args.trials):
                    approx_matrix, matvecs[t, i] = eigval_approx_bki_adaptive(true_mat, k=block_size, iters=qs[i], return_type="full matrix")
                    errors_2Norm[t, i], errors_FroNorm[t, i] = get_error(approx_matrix, true_mat)
        if method == "oth_adp":
            # max matvecs is divided by 2 since total matvecs used here is 2k
            block_sizes = np.arange(args.smallest_block_size, (max_matvecs/2)+1, step_size).astype(int)
            errors_2Norm = np.zeros((args.trials, len(block_sizes)))
            errors_FroNorm = np.zeros((args.trials, len(block_sizes)))
            matvecs = np.zeros((args.trials, len(block_sizes)))
            for i in tqdm(range(len(block_sizes))):
                for t in range(args.trials):
                    approx_matrix, matvecs[t, i] = eigval_approx_othro_adaptive(true_mat, k=block_sizes[i], return_type="full matrix")
                    errors_2Norm[t, i], errors_FroNorm[t, i] = get_error(approx_matrix, true_mat)
        if method == "oth_nonadp":
            block_sizes = np.arange(args.smallest_block_size, (max_matvecs/3)+1, step_size).astype(int)
            errors_2Norm = np.zeros((args.trials, len(block_sizes)))
            errors_FroNorm = np.zeros((args.trials, len(block_sizes)))
            matvecs = np.zeros((args.trials, len(block_sizes)))
            for i in tqdm(range(len(block_sizes))):
                for t in range(args.trials):
                    approx_matrix, matvecs[t, i] = eigval_approx_ortho_nonadaptive_2(true_mat, k=block_sizes[i], return_type="full matrix")
                    errors_2Norm[t, i], errors_FroNorm[t, i] = get_error(approx_matrix, true_mat)
        if method == "sw_nonadp":
            block_sizes = np.arange(args.smallest_block_size, max_matvecs+1, step_size).astype(int)
            errors_2Norm = np.zeros((args.trials, len(block_sizes)))
            errors_FroNorm = np.zeros((args.trials, len(block_sizes)))
            matvecs = np.zeros((args.trials, len(block_sizes)))
            for i in tqdm(range(len(block_sizes))):
                for t in range(args.trials):
                    approx_matrix, matvecs[t, i] = eigval_approx_SW_nonadaptive(true_mat, k=block_sizes[i], return_type="full matrix")
                    errors_2Norm[t, i], errors_FroNorm[t, i] = get_error(approx_matrix, true_mat)
        ############# Store the values computed above ######################
        save_vals[method] = {}
        save_vals[method]["two_norm_error"] = errors_2Norm
        save_vals[method]["fro_norm_error"] = errors_FroNorm
        save_vals[method]["matvecs"] = matvecs
        ####################################################################
    
        save_folder = "./results/"+args.dataset
        if not os.path.isdir(save_folder):
            os.makedirs(save_folder)
        savefilename = os.path.join(save_folder, "LRA"+"_"+method+".pkl")
        file_handler = open(savefilename, "wb")
        pickle.dump(save_vals, file_handler)
        file_handler.close()
        
    
    return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Matvecs eval variables")
    parser.add_argument('--dataset', '-d', dest='dataset', 
                        type=str,  default="random", 
                        required=False, help="choose datasets here")
    parser.add_argument('--trials', '-t', dest='trials', type=int, 
                        default=3, required=False,
                        help="number of trials to average out performance")
    parser.add_argument('--methods', '-m', dest='methods', 
                        type=list, default=["bki_adp_Q_10", "bki_adp_Q_20", "oth_adp", "oth_nonadp", "sw_nonadp"], 
                        required=False,
                        help="list of algorithms to compare")
    parser.add_argument('--smallest_block_size', '-sb', dest='smallest_block_size', 
                        type=int, default=10, required=False,
                        help="size of the largest block all algorithms")
    args = parser.parse_args()
    print(args)
    main(args)
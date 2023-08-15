import numpy as np
import os
import argparse
from src.utils_for_main import StrToFunc, saver, get_eigs, computer, processor
from src.get_dataset import get_data

def mapper(block_size, n, multiplier=1):
    iters_high = n//(multiplier*block_size)
    return iters_high  

def main(args):
    method, mode = StrToFunc(args.method)
    true_mat, n, _, _ = get_data(args.dataset)

    # set up the parameters
    if args.block_size == "full":
        block_sizes = list(range(10,n+10,50))
    else:
        block_sizes = [int(args.block_size)]
    if "egu" in args.method:
        iters = list(range( 0, mapper(int(args.block_size),n), 20 ))
    elif "bki" in args.method:
        iters = list(range( 0, mapper(int(args.block_size),n,20) ))
    else:
        iters = [0]
    params = {"block_sizes": block_sizes, "iters": iters, "mode": mode}

    # grab the true spectrum
    true_spectrum = get_eigs(true_mat, args.search_ranks)

    # save variable for outputs
    outputs = {"approx_eigvals": np.zeros((
                                           args.trials,\
                                           len(params["block_sizes"]),\
                                           len(params["iters"]),\
                                           len(args.search_ranks)
                                          ), dtype=np.double),
               "matvecs": np.zeros((
                                    len(params["block_sizes"]),\
                                    len(params["iters"])
                                  ), dtype=np.double)
               }
    # start accumulating values
    outputs["approx_eigvals"], outputs["matvecs"] = \
                computer(args, params, true_mat, method, params["mode"], \
                    outputs["approx_eigvals"], outputs["matvecs"])
    # save the true spectrum
    outputs["true_spectrum"] = true_spectrum
    processor(outputs, params, args)
    return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Matvecs eval variables")
    parser.add_argument('--dataset', '-d',
                        dest='dataset', 
                        type=str, 
                        default="random", 
                        choices=["random", "facebook", "erdos", \
                        "arxiv", "kong_ht", "kong_tps", "eye"],
                        required=False,
                        help="choose datasets here")
    parser.add_argument('--method', '-m',
                        dest='method', 
                        type=str, 
                        default="bki_Q", 
                        choices=["bki_adp_Q", "bki_adp_Z", "oth_adp", \
                        "oth_nonadp", "sw_nonadp", "egu_d",\
                        "egu_f"],
                        required=False, 
                        help="choose matvec method")
    parser.add_argument('--trials', '-t',
                        dest='trials', 
                        type=int, 
                        default=5, 
                        required=False,
                        help="number of trials to average out performance")
    parser.add_argument('--block_size', '-b',
                        dest='block_size', 
                        type=str, 
                        default="full", 
                        required=False,
                        help="block size for ther algos to run on")
    parser.add_argument('--search_ranks', "-s",
                        dest='search_ranks', 
                        type=str, 
                        default=[0,1,2,3,4,-5,-4,-3,-2,-1], 
                        required=False,
                        help="eigenvalues to check performance; input as a,b,c")
    args = parser.parse_args()
    # preprocess for search ranks
    if set(args.search_ranks) == set([0,1,2,3,4,-5,-4,-3,-2,-1]):
        pass
    else:
        args.search_ranks = [int(x) for x in args.search_ranks.split(",")]
        args.search_ranks = list(set(args.search_ranks))
    print(args)
    # args is a Namespace variable. To grab the deets use args.dest-name
    # send args to the main function
    main(args)
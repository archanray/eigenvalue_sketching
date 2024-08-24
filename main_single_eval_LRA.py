import numpy as np
import argparse
from src.get_dataset import get_data
from src.approximator import *

def main(args):
    true_mat, n, _, _ = get_data(args.dataset)
    
    max_matvecs = n // 2
    for t in range(args.trials):
        pass
    
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
                        type=list, default=["bki_adp_Q", "oth_adp", "oth_nonadp", "sw_nonadp"], 
                        required=False,
                        help="list of algorithms to compare")
    parser.add_argument('--largest_block_size', '-lb', dest='block_size', 
                        type=int, default=10, required=False,
                        help="size of the largest block all algorithms")
    args = parser.parse_args()
    main(args)
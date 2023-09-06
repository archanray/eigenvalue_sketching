from src.display_codes import plotErrorForAll as PFA
from src.display_codes import plotEigvals as PE
import argparse

def parse_splitter(variable, type_=int):
    if type(variable) == list:
        return variable
    variable = [type_(x) for x in variable.split(",")]
    variable = list(set(variable))
    return variable

def main(args):
    if args.plot_mode == "eigvals":
        PE(names=args.methods, datasets=args.datasets, \
           legend=args.legend, matvecs=args.matvecs)
    if args.plot_mode == "errors":
        PFA(names=args.methods, datasets=args.datasets, \
            plot_ranks=args.plot_ranks, legend=args.legend)
    return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Matvecs eval plotter variables")
    parser.add_argument('--datasets', '-d',
                        dest='datasets', 
                        type=str, 
                        default=["random", "facebook", "erdos"], 
                        required=False,
                        help="choose datasets here; input as a,b,c")
    parser.add_argument('--methods', '-m',
                        dest='methods', 
                        type=str, 
                        default="bki_adp_Q_10", 
                        required=False, 
                        help="choose matvec methods")
    parser.add_argument('--plot_mode', "-o",
                        dest='plot_mode', 
                        type=str, 
                        default="errors", 
                        required=False,
                        choices=["errors", "eigvals"],
                        help="choose to plot error or eigvals")
    parser.add_argument('--plot_ranks', "-p",
                        dest='plot_ranks', 
                        type=str, 
                        default=[0,1,2,3,4,-5,-4,-3,-2,-1], 
                        required=False,
                        help="eigenvalues to check performance; input as a,b,c")
    parser.add_argument('--matvecs', "-v",
                        dest='matvecs', 
                        type=int, 
                        default=20, 
                        required=False,
                        help="matvecs for plotting eigenvalues")
    parser.add_argument('--legend', "-l",
                        dest='legend', 
                        type=int, 
                        default=True,
                        choices=[1,0],
                        required=False,
                        help="display legend within image; enter as 1 or 0")

    args = parser.parse_args()
    args.datasets = parse_splitter(args.datasets, type_=str)
    args.methods = parse_splitter(args.methods, type_=str)
    args.plot_ranks = parse_splitter(args.plot_ranks, type_=int)
    args.plot_ranks = args.plot_ranks+["lie"]
    print(args)
    main(args)
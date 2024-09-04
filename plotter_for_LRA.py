import numpy as np
import argparse, os, pickle
import matplotlib.pyplot as plt
from src.display_codes import sixColors

def plotter(results_dict, args, error_mode="2-norm"):
    plt.gcf().clf()
    fig, ax = plt.subplots(figsize=(6,4))
    for key in results_dict.keys():
        if key not in ["bki_adp_Q_10", "bki_adp_Q_20"]:
            plot_color = sixColors(key+"_full")
        else:
            plot_color = sixColors(key)
    
        ax.plot(results_dict[key]["mean_matvecs"], results_dict[key]["mean_"+error_mode+"_error"], color=plot_color, label=key)
        ax.fill_between(results_dict[key]["mean_matvecs"], \
                            results_dict[key]["p10_"+error_mode+"_error"], \
                            results_dict[key]["p90_"+error_mode+"_error"], \
                            alpha=0.2, color=plot_color)
    
    plt.xlim([-5.7,-0.4])
    plt.xlabel("log relative matvecs", fontsize=16)
    plt.ylabel("relative log "+ error_mode+" error", fontsize=16)
    # plt.legend()
    plt.grid()
    # plt.title(args.dataset, fontsize=16)
    
    save_path = args.save_directory + "/" + args.dataset
    save_filename = save_path + "/" + args.dataset + "_LRA_" + error_mode + ".pdf"
    plt.savefig(save_filename, bbox_inches='tight')
    
    return None

def main(args):
    header = "LRA"
    filePath = os.path.join(args.directory, args.dataset)
    files = []
    for i in os.listdir(filePath):
        if os.path.isfile(os.path.join(filePath,i)) and header in i:
            files.append(os.path.join(filePath,i))
            
    results_dict = {}
    for filename in files:
        method_name = filename.split(header+"_")[-1]
        method_name = method_name.split(".")[0]
        # use method_name as label to storte summaries in dictionary
        file_handler = open(filename, "rb")
        save_vals = pickle.load(file_handler)
        file_handler.close()
        # errors_2Norm = save_vals[method_name]["two_norm_error"]
        # errors_FNorm = save_vals[method_name]["fro_norm_error"]
        # matvecs = save_vals[method_name]["matvecs"]
        
        true_2_norm = max(np.abs(save_vals["eigvals"]))
        true_f_norm = np.linalg.norm(save_vals["eigvals"])
        
        summaries = {}
        summaries["mean_2-norm_error"] = np.mean(np.log(save_vals[method_name]["two_norm_error"] / true_2_norm), axis=0) # mean of columns
        summaries["p10_2-norm_error"] = np.percentile(np.log(save_vals[method_name]["two_norm_error"] / true_2_norm), q = 10, axis=0) # p10 of columns
        summaries["p90_2-norm_error"] = np.percentile(np.log(save_vals[method_name]["two_norm_error"] / true_2_norm), q = 90, axis=0) # p90 of columns
        
        summaries["mean_F-norm_error"] = np.mean(np.log(save_vals[method_name]["fro_norm_error"] / true_f_norm), axis=0) # mean of columns
        summaries["p10_F-norm_error"] = np.percentile(np.log(save_vals[method_name]["fro_norm_error"] / true_f_norm), q = 10, axis=0) # p10 of columns
        summaries["p90_F-norm_error"] = np.percentile(np.log(save_vals[method_name]["fro_norm_error"] / true_f_norm), q = 90, axis=0) # p90 of columns
        
        summaries["mean_matvecs"] = np.mean(np.log(save_vals[method_name]["matvecs"] / len(save_vals["eigvals"])), axis=0) # mean of columns
        
        results_dict[method_name] = summaries
    
    plotter(results_dict, args, error_mode="2-norm")
    plotter(results_dict, args, error_mode="F-norm")
    return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Matvecs eval variables")
    parser.add_argument('--dataset', '-d', dest='dataset', 
                        type=str,  default="random", 
                        required=False, help="choose datasets here")
    parser.add_argument('--dir', '-r', dest='directory', 
                        type=str,  default="./results/", 
                        required=False, help="default directory of results")
    parser.add_argument('--savedir', '-s', dest='save_directory', 
                        type=str,  default="./figures/", 
                        required=False, help="default save directory of plots")
    args = parser.parse_args()
    print(args)
    main(args)
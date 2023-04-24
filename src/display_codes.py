import matplotlib.pyplot as plt
import numpy as np
import os

def display_image(image):
    """
    Display the image
    """
    plt.gcf().clear()
    plt.rcParams.update({'font.size': 12})
    plt.imshow(image, cmap="gray")
    plt.xlabel("x co-ordinates", fontsize=16)
    plt.ylabel("y co-ordinates", fontsize=16)
    
    plt.title("Original image", fontsize=16)
    filename = "./figures/kong/"
    if not os.path.isdir(filename):
        os.makedirs(filename)
    filename = filename+"kong-original.pdf"
    plt.savefig(filename)
    return None


def plot_errors(params, errors, p20, p80, matvecs):
    """
    Plot the errors for each method
    """
    for sr in params["search_rank"]:
        plt.gcf().clear()
        plt.rcParams.update({'font.size': 12})
        for mv in params["approx_mthds"]:
            E = errors[mv.__name__][:][:, sr]
            print(E.shape, errors[mv.__name__].shape)
            P1 = p20[mv.__name__][:][:, sr]
            P2 = p80[mv.__name__][:][:, sr]
            plt.plot(matvecs[mv.__name__], E, label=mv.__name__)
            plt.fill_between(matvecs[mv.__name__], P1, P2, alpha=0.2)
        plt.xlabel("log(Number of matrix-vector products)", fontsize=16)
        plt.ylabel("log(Error)", fontsize=16)
        plt.title(params["dataset_name"], fontsize=16)
        plt.legend()
        filename = "./figures/"+params["dataset_name"]+"/"
        if not os.path.isdir(filename):
            os.makedirs(filename)
        filename = filename+str(sr)+"-error.pdf"
        plt.show()
        plt.savefig(filename)
    return None

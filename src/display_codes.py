import matplotlib.pyplot as plt
import numpy as np
import os

def display_image(image):
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
    pass

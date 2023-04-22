import numpy as np

def sort_abs_descending(x):
    """
    Sort array by absolute value in descending order.
    """
    abs_x = np.abs(x)
    idx = np.argsort(-abs_x)
    return x[idx]

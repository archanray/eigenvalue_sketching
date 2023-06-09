import numpy as np
from sklearn.metrics import pairwise_distances as euclid

def hyperbolic_tangent(data1, data2, sigma=1):
    """
    hyperbolic_tangent = tanh(xy/sigma+1.0)
    """
    similarity_matrix = np.matrix(data1) * np.matrix(data2.T)
    similarity_matrix = (similarity_matrix / sigma) + 1.0
    similarity_matrix = np.tanh(similarity_matrix)
    similarity_matrix = np.asarray(similarity_matrix)
    return similarity_matrix

def thin_plane_spline(data1, data2, sigma=1.0):
    """
    Ds = |x-y|^2 / sigma^2
    tps = Ds * ln(Ds)
    """
    eps=1e-16
    similarity_matrix = np.square(euclid(data1, data2))+eps
    similarity_matrix = similarity_matrix / (sigma**2)
    similarity_matrix = similarity_matrix * np.log(similarity_matrix)
    return similarity_matrix

def sort_abs_descending(x):
    """
    Sort array by absolute value in descending order.
    """
    abs_x = np.abs(x)
    idx = np.argsort(-abs_x)
    return x[idx]


def sort_descending(x):
    """
    Sort array in descending order.
    """
    idx = np.argsort(-x)
    return x[idx]

def sorter(xvals, y1vals, y2vals=None):
    ids = np.argsort(xvals)
    xvals = xvals[ids]
    y1vals = y1vals[ids]
    if y2vals is None:
        return xvals, y1vals
    else:
        y2vals = y2vals[ids]
        return xvals, y1vals, y2vals

def l_infty_error(list1, list2, normalizer=1):
    return np.max(np.abs(list1 - list2))/normalizer
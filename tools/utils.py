from ast import literal_eval
import random

import numpy as np

def random_position(x1, y1, x2, y2):
    """ Return a random (x, y) coordinate from a square """

    return random.randint(x1, x2), random.randint(y1, y2)


def dynamic_coordinate_converter(parent, child, operator):

    if operator == '-':
        return [child[0] - parent[0], child[1] - parent[1], child[2], child[3]]
    else:
        child = literal_eval(child)
        return child[0] + parent[0], child[1] + parent[1], child[2], child[3]


def blockshaped(arr, nrows, ncols):
    """
    Return an array of shape (n, nrows, ncols) where
    n * nrows * ncols = arr.size

    If arr is a 2D array, the returned array should look like n subblocks with
    each subblock preserving the "physical" layout of arr.
    """
    h, w = arr.shape
    return (arr.reshape(h//nrows, nrows, -1, ncols)
               .swapaxes(1,2)
               .reshape(-1, nrows, ncols))
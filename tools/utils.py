from ast import literal_eval
import random


def random_position(x1, y1, x2, y2):
    """ Return a random (x, y) coordinate from a square """

    print(x1, y1, x2, y2)
    print(random.randint(x1, x2), random.randint(y1, y2))

    return random.randint(x1, x2), random.randint(y1, y2)


def dynamic_coordinate_converter(parent, child, operator):

    if operator == '-':
        return [child[0] - parent[0], child[1] - parent[1], child[2], child[3]]
    else:
        child = literal_eval(child)
        return child[0] + parent[0], child[1] + parent[1], child[2], child[3]



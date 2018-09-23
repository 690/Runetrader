import random


def random_position(x1, y1, x2, y2):
    """ Return a random (x, y) coordinate from a square """

    # TODO Convert function to not be input order dependant

    return random.randint(x1, x2), random.randint(y1, y2)
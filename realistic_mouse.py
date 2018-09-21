import random
import time
import pyautogui

from config import DELAY_RANGE


def random_path(x1, y1, x2, y2):
    """ Create a random mouse movement path from one coordinate to another """

    # TODO Convert function to not be input order dependant

    path = []
    pass


def random_position(x1, y1, x2, y2):
    """ Return a random (x, y) coordinate from a square """

    # TODO Convert function to not be input order dependant

    return random.randint(x1, x2), random.randint(y1, y2)


def click(x, y, **kwargs):
    """ Click a point with a random delay """

    time.sleep(random.uniform(*DELAY_RANGE))
    pyautogui.click(x, y, kwargs)


if __name__ == "__main__":
    """ Run unit tests """

    pass
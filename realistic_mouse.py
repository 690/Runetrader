import random
import time
import pyautogui

from config import SMALL_DELAY_RANGE
from utils import random_position


def random_path(x1, y1, x2, y2):
    """ Create a random mouse movement path from one coordinate to another """

    # TODO Convert function to not be input order dependant

    return x2, y2


def click(x, y):
    """ Click a point with a random delay """

    time.sleep(random.uniform(*SMALL_DELAY_RANGE))
    pyautogui.click(x, y,)


def move(target_x, target_y, **kwargs):
    """ Move the mouse to a given point, using a random path and delays """

    time.sleep(random.uniform(*SMALL_DELAY_RANGE))

    current_x, current_y = pyautogui.position()
    path = random_path(current_x, current_y, target_x, target_y)

    distance = int(((target_x - current_x) ** 2 + (target_y - current_y) ** 2) ** 0.5)
    pyautogui.moveTo(target_x, target_y, (distance * random.random() / 2000) + 0.5, pyautogui.easeInQuad)  # https://github.com/lukegarbott


def all_in_one(x, y, z, w):
    random_x, random_y = random_position(x, y, x + z, y + w)
    move(random_x, random_y)
    click(*pyautogui.position())


if __name__ == "__main__":
    """ Run unit tests """

    move(500, 500)
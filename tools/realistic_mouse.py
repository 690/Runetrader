import random
import time
import pyautogui
import scipy

from scipy import interpolate
from config import SMALL_DELAY_RANGE
from tools.utils import random_position


pyautogui.MINIMUM_SLEEP = 0
pyautogui.MINIMUM_DURATION = 0g

def move(target_x, target_y):
    """ Move mouse according to random bezier curve
    credit : DJV : https://stackoverflow.com/a/44666798 """

    current_x, current_y = pyautogui.position()

    control_points = 3

    x = scipy.linspace(current_x, target_x, control_points, dtype="int")
    y = scipy.linspace(current_y, target_y, control_points, dtype="int")

    seed = random.randint(5, 55)

    xr = scipy.random.randint(-seed, seed, size=control_points)
    yr = scipy.random.randint(-seed, seed, size=control_points)

    xr[0] = yr[0] = xr[-1] = yr[-1] = 0
    x += xr
    y += yr

    degree = 3 if control_points > 3 else control_points - 1  # Degree of b-spline. 3 is recommended.
    tck, u = scipy.interpolate.splprep([x, y], k=degree)
    u = scipy.linspace(0, 1, num=max(pyautogui.size()))
    points = scipy.interpolate.splev(u, tck)

    duration = 0.0001
    timeout = duration / len(points[0])

    for point in zip(*(i.astype(int) for i in points)):
        pyautogui.moveTo(*point)
        if random.randint(1, 10) == 2:
            time.sleep(timeout)

def click(x, y):
    """ Click a point with a random delay """

    time.sleep(random.uniform(*SMALL_DELAY_RANGE))
    pyautogui.click(x, y)


def all_in_one(x, y, z, w):
    random_x, random_y = random_position(x, y, x + z, y + w)
    move(random_x, random_y)
    click(*pyautogui.position())


import pyautogui
import random
import string
import time

from config import SMALL_DELAY_RANGE
from config import REACTION_DELAY
from config import SPELLING_MISTAKE_RATIO


def typeerror(type=None):
    """ Creates random typeerrors and fixes them afterwards """

    if type == int:
        chars = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    else:
        chars = string.ascii_letters

    n = random.randint(1, 4)

    for i in range(1, n):
        time.sleep(random.uniform(*REACTION_DELAY)*0.75)
        write(random.choice(chars))

    for i in range(1, n):
        time.sleep(random.uniform(*REACTION_DELAY))
        pyautogui.press('backspace')


def write(text, type=None):
    """ Writes text to highlighted window with random delays and typing errors """

    time.sleep(random.uniform(*SMALL_DELAY_RANGE))

    for i in str(text):

        if random.randint(1, SPELLING_MISTAKE_RATIO) == 1:
            if not type:
                typeerror(str)
            else:
                typeerror(int)

        time.sleep(random.uniform(*REACTION_DELAY)*0.25)
        pyautogui.typewrite(i, 0.1)


def press(key):
    time.sleep(random.uniform(*SMALL_DELAY_RANGE))
    pyautogui.press(key)

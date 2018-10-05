import pyautogui
import random
import string
import time

from config import *


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

    #time.sleep(random.uniform(*LONG_DELAY_RANGE))

    reset = False

    if random.randint(1, MISTAKE_RATIO) == 1:
        pyautogui.press('capslock')
        reset = True

    for i in str(text):
        if random.randint(1, MISTAKE_RATIO) == 1:
            if not type:
                typeerror(int)
            else:
                typeerror(str)

        time.sleep(random.uniform(*REACTION_DELAY)*0.1)
        pyautogui.typewrite(i, 0.1)

    if reset:
        pyautogui.press('capslock')


def press(key):
    time.sleep(random.uniform(*SMALL_DELAY_RANGE))
    pyautogui.press(key)

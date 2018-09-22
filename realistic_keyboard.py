import pyautogui
import random
import string
import time
from config import SMALL_DELAY_RANGE
from config import REACTION_DELAY
from config import SPELLING_MISTAKE_RATIO


def typeerror():
    """ Creates random typeerrors only containing ascii letters both cases, and fixes them afterwards """
    n = random.randint(1, 4)

    for i in range(1, n):
        time.sleep(random.uniform(*REACTION_DELAY))
        write(random.choice(string.ascii_letters))

    for i in range(1, n):
        time.sleep(random.uniform(*REACTION_DELAY)*0.75)
        pyautogui.press('backspace')


def integer_typeerror():
    """ Creates random typeerrors only containing integer numbers, and fixes them afterwards """

    n = random.randint(1, 4)

    for i in range(1, n):
        time.sleep(random.uniform(*REACTION_DELAY))
        write(random.choice([0, 1, 2, 3, 4, 5, 6 ,7 ,8 ,9]))

    for i in range(1, n):
        time.sleep(random.uniform(*REACTION_DELAY) * 0.75)
        pyautogui.press('backspace')


def write(text, type=None):
    """ Writes text to highlighted window with random delays and typing errors """

    time.sleep(random.uniform(*SMALL_DELAY_RANGE))

    for i in str(text):

        if random.randint(1, SPELLING_MISTAKE_RATIO) == 1:
            if not type:
                typeerror()
            else:
                integer_typeerror()

        time.sleep(random.uniform(*REACTION_DELAY))
        pyautogui.typewrite(i, 0.1)


def press(key):
    pyautogui.press(key)


if __name__ == "__main__":
    typeerror()


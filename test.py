import pytesseract
from PIL import Image
import cv2
import PIL
import numpy as np
import pyautogui

img = np.array(pyautogui.screenshot(region = (200,200,300,50)))
image = cv2.resize(img, (0,0), fx=2, fy=2)
image = PIL.Image.fromarray(image)
image.show()
txt = pytesseract.image_to_string(image, config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
txt_list = list(txt)

CTN_DICT = {'o': '0',
            'O': '0',
            'l': '1',
            'I': '1',
            'i': '1',
            'M': '000000',
            "B": '8',
            'K': '000',
            'm': '000000',
            'k': '000',
            's': '5',
            'S': '5',
            'W': '40',
            '.': ' ',
            ',': ''}


txt_list = [CTN_DICT[t] if t in list(CTN_DICT.keys()) else t for t in txt_list]
print(txt_list)
txt_list = ''.join(txt_list).split()
print(txt_list)
txt_list = [int(x) for x in txt_list if x.isdigit()]
print(list(txt_list))
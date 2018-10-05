from PIL import Image
import numpy as np
import pytesseract
import pyautogui
import cv2
import PIL

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


def recognize_int(region):
    image = pyautogui.screenshot(region=region)
    image = np.array(image)
    image = cv2.resize(image, (0, 0), fx=2, fy=2)
    image = PIL.Image.fromarray(image)
    txt = pytesseract.image_to_string(image, config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')

    txt_list = [CTN_DICT[t] if t in list(CTN_DICT.keys()) else t for t in txt]
    print(txt_list)
    txt_list = [int(x) for x in txt_list if x.isdigit()]

    image.show()
    input()
    t = list(txt_list)[0]
    return t


def get_order_info(exchange):
    quantity = recognize_int(exchange.quantity_info)
    price = recognize_int(exchange.price_info)
    return quantity, price

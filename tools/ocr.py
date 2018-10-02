import pyautogui
import PIL
def get_order_info(coordinates):
    image = pyautogui.screenshot(*coordinates)

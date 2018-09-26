import pyautogui
from PIL import Image

image = Image.open("./resources/items/1935.png")

x, y, z, w = pyautogui.locateOnScreen(image)
print(x, y, z, w)


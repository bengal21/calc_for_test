import pyautogui
import os
import time
from calc_path import path_of_calc

os.startfile(path_of_calc)

list_of_buttons = ['img/1.jpg', 'img/2.jpg', 'img/plus.jpg', 'img/7.jpg', 'img/eq.jpg']


class Button:
    def __init__(self, path):
        self.button = pyautogui.locateOnScreen(path, confidence=0.9)

    def find_center(self):
        self.center_button = pyautogui.center(self.button)
        return self.center_button

    def click(self):
        pyautogui.click(self.find_center())


def twelve_plus_seven(list_of_path: list, pause: int):
    time.sleep(pause)
    for path in list_of_path:
        button = Button(path)
        button.find_center()
        button.click()


twelve_plus_seven(list_of_buttons, 2)

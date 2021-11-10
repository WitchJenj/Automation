from contextlib import ExitStack
from time import time
import pyautogui
import time

from win32 import win32api

from threading import Timer

from dataclasses import dataclass

@dataclass
class Direction:
    forward = 'W'
    back = 'S'
    left = 'A'
    right = 'D'

# # class Planer:
# #     def __init__(self):
# #         self.a = 15

# #     def get_twenty(self):
# #         return 20

# #     def __calculate(self):
# #         return self.a + self.get_twenty()

# #     def calculate(self):
# #         return self.__calculate()

# planer = Planer()
# print(planer.a)
# print(planer.get_twenty())
# print(planer.calculate())

middleCellMoveSeconds = 0.08
oneCellMoveSeconds = 0.5

def moveFor(direction, seconds, finalizationSeconds=0.2):
    pyautogui.keyDown(direction)
    time.sleep(seconds)
    pyautogui.keyUp(direction)
    time.sleep(finalizationSeconds)

def moveBy(direction, count, finalizationSeconds=0.2):
    moveFor(direction, count * oneCellMoveSeconds + (count - 1) * middleCellMoveSeconds, finalizationSeconds)

screenWidth, sreenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()

time.sleep(5)

# pyautogui.click()
pyautogui.press("esc")

time.sleep(0.5)

win32api.mouse_event(1, -100, 0, 0, 0)


# pyautogui.move(-350, 0, duration=2, tween=pyautogui.easeInCubic)
# pyautogui.moveTo(500, 500, duration=2)
# print(pyautogui.position().x)
# def go():
#     moveBy(Direction.right, 1)
#     moveBy(Direction.left, 1)
# t = Timer(5, go)  
# t.start()
# moveBy(Direction.left, 1)
# moveBy(Direction.forward, 14)
# moveBy(Direction.right, 6)
# moveBy(Direction.forward, 2)


# pyautogui.move(-350, 0, duration=2, tween=pyautogui.easeOutExpo)

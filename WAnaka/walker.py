from time import time
import pyautogui
import time

from win32 import win32api

from dataclasses import dataclass

@dataclass
class Direction:
    forward = 'W'
    back = 'S'
    left = 'A'
    right = 'D'

class Walker:
    def __init__(self):
        self.__middleCellMoveSeconds = 0.08
        self.__oneCellMoveSeconds = 0.5

    def moveFor(self, direction, seconds, finalizationSeconds=0.2):
        pyautogui.keyDown(direction)
        time.sleep(seconds)
        pyautogui.keyUp(direction)
        time.sleep(finalizationSeconds)

    def moveBy(self, direction, count, finalizationSeconds=0.2):
        self.moveFor(direction, count * self.__oneCellMoveSeconds + (count - 1) * self.__middleCellMoveSeconds, finalizationSeconds)

    def rotateBy(self, point):
        win32api.mouse_event(1, point.x, point.y, 0, 0)

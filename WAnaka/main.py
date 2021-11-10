from point import Point

from time import time
import pyautogui
import time

from walker import Walker, Direction

# from threading import Timer

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


screenWidth, sreenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()


time.sleep(5)

# pyautogui.click()
pyautogui.press("esc")

time.sleep(0.5)


# pyautogui.move(-350, 0, duration=2, tween=pyautogui.easeInCubic)
# pyautogui.moveTo(500, 500, duration=2)
# print(pyautogui.position().x)
# def go():
#     moveBy(Direction.right, 1)
#     moveBy(Direction.left, 1)
# t = Timer(5, go)  
# t.start()

walker = Walker()

walker.rotateBy(Point(-100, 0))

walker.moveBy(Direction.left, 1)
walker.moveBy(Direction.forward, 14)
walker.moveBy(Direction.right, 6)
walker.moveBy(Direction.forward, 2)


# pyautogui.move(-350, 0, duration=2, tween=pyautogui.easeOutExpo)

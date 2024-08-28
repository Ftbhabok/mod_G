from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

# needs to be mine update it

# Tile 1 Position: X:  469 Y: 1096 RGB: ( 78,  81, 115)
# Tile 2 Position: X:  584 Y: 1096 RGB: ( 78,  81, 115)
# Tile 3 Position: X:  741 Y: 1096 RGB: ( 77,  80, 115)
# Tile 4 Position: X:  845 Y: 1096 RGB: ( 77,  80, 115)

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1)  # This pauses the script for 0.1 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


while keyboard.is_pressed('q') == False:

    if pyautogui.pixel(469, 1096)[0] == 0:
        click(469, 1096)
    if pyautogui.pixel(584, 1096)[0] == 0:
        click(584, 1096)
    if pyautogui.pixel(741, 1096)[0] == 0:
        click(741, 1096)
    if pyautogui.pixel(845, 1096)[0] == 0:
        click(845, 1096)
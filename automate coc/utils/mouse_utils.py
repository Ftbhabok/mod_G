# File: utils/mouse_utils.py
import pyautogui
import random
import time


class MouseController:
    @staticmethod
    def human_move(x, y):
        """Move mouse in a human-like manner"""
        # Add slight randomness to position
        x += random.randint(-5, 5)
        y += random.randint(-5, 5)

        # Random movement duration
        duration = random.uniform(0.3, 0.7)

        # Move mouse with random curve
        pyautogui.moveTo(x, y, duration=duration, tween=pyautogui.easeOutQuad)
        time.sleep(random.uniform(0.1, 0.3))

    @staticmethod
    def human_click():
        """Click in a human-like manner"""
        pyautogui.click()
        time.sleep(random.uniform(0.1, 0.3))
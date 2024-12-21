# File: training/troop_trainer.py
import pyautogui
import logging
import time
import random
from ..utils.mouse_utils import MouseController
from ..config import IMAGE_PATHS


class TroopTrainer:
    def __init__(self):
        self.mouse = MouseController()

    def train_troops(self, troop_types):
        """
        Train specified troops
        troop_types = [('barbarian', 5), ('archer', 3)]
        """
        if self._open_training_menu():
            time.sleep(random.uniform(0.5, 1.0))

            for troop_type, quantity in troop_types:
                self._train_troop(troop_type, quantity)
                time.sleep(random.uniform(0.3, 0.6))

            self._close_training_menu()

    def _open_training_menu(self):
        """Open the troop training menu"""
        try:
            location = pyautogui.locateOnScreen(
                IMAGE_PATHS['training']['train_button'],
                confidence=0.8
            )
            if location:
                center = pyautogui.center(location)
                self.mouse.human_move(center.x, center.y)
                self.mouse.human_click()
                return True
            return False
        except Exception as e:
            logging.error(f"Error opening training menu: {str(e)}")
            return False

    def _train_troop(self, troop_type, quantity):
        """Train a specific quantity of a troop type"""
        try:
            troop_image = IMAGE_PATHS['training']['troops'][troop_type]
            location = pyautogui.locateOnScreen(troop_image, confidence=0.8)

            if location:
                center = pyautogui.center(location)
                self.mouse.human_move(center.x, center.y)

                for _ in range(quantity):
                    self.mouse.human_click()
                    time.sleep(random.uniform(0.1, 0.2))

                logging.info(f"Trained {quantity} {troop_type}")
                return True
            return False
        except Exception as e:
            logging.error(f"Error training {troop_type}: {str(e)}")
            return False

    def _close_training_menu(self):
        """Close the training menu"""
        try:
            # Usually clicking an empty space works to close
            pyautogui.press('esc')
            time.sleep(random.uniform(0.5, 1.0))
        except Exception as e:
            logging.error(f"Error closing training menu: {str(e)}")

# File: collectors/resource_collector.py
import pyautogui
import logging
import time
import random
from datetime import datetime
import os
import sys

# Add parent directory to path to make imports work
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.mouse_utils import MouseController
from config import IMAGE_PATHS, COOLDOWNS

class ResourceCollector:
    def __init__(self):
        self.last_collection = {}
        self.mouse = MouseController()

    def collect_resources(self):
        """Collect all available resources"""
        current_time = datetime.now().timestamp()

        for resource_type, image_path in IMAGE_PATHS['collectors'].items():
            # Check cooldown
            if self._can_collect(resource_type, current_time):
                if self._collect_resource(resource_type, image_path):
                    self.last_collection[resource_type] = current_time
                    # Random delay between collections
                    time.sleep(random.uniform(1.0, 2.0))

    def _can_collect(self, resource_type, current_time):
        """Check if enough time has passed since last collection"""
        return (resource_type not in self.last_collection or
                current_time - self.last_collection[resource_type] >= COOLDOWNS['collection'])

    def _collect_resource(self, resource_type, image_path):
        """Attempt to collect a specific resource type"""
        try:
            location = pyautogui.locateOnScreen(image_path, confidence=0.8)
            if location:
                center = pyautogui.center(location)
                self.mouse.human_move(center.x, center.y)
                self.mouse.human_click()
                logging.info(f"Collected {resource_type}")
                return True
            return False
        except Exception as e:
            logging.error(f"Error collecting {resource_type}: {str(e)}")
            return False
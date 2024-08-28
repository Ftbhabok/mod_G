import pyautogui
import cv2
import numpy as np


def locate_on_screen(image_path, confidence=0.8):
    # Take a screenshot
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    # Read the template image
    template = cv2.imread(image_path, 0)

    if template is None:
        print(f"Failed to load image {image_path}. Make sure the path is correct.")
        return None

    # Perform template matching
    result = cv2.matchTemplate(cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY), template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    if max_val >= confidence:
        return max_loc
    return None


def click_image(image_path, confidence=0.8):
    location = locate_on_screen(image_path, confidence)
    if location:
        template = cv2.imread(image_path, 0)
        center_x = location[0] + template.shape[1] // 2
        center_y = location[1] + template.shape[0] // 2
        pyautogui.click(center_x, center_y)
        print(f"Clicked on {image_path}")
    else:
        print(f"Couldn't find {image_path}")


if __name__ == "__main__":
    click_image('images/train_troops_icon.png')

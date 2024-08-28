import pyautogui
import time
import keyboard
import win32api, win32con

# Tile positions on the screen
tiles = [
    (469, 1096),
    (584, 1096),
    (741, 1096),
    (845, 1096),
]

# Function to click on a specific (x, y) position
def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)  # Very short delay to ensure the click is registered
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

# Main loop that continuously checks tile positions and clicks if necessary
while not keyboard.is_pressed('q'):  # Stop script when 'q' is pressed
    for x, y in tiles:
        if pyautogui.pixel(x, y)[0] == 0:  # Check if the pixel is black
            click(x, y)
    # time.sleep(0.01)  # Short delay to prevent excessive CPU usage

import pyautogui
import time

# Move the mouse to the search bar and click
pyautogui.moveTo(1101, 2090, duration=1)
pyautogui.click()

# Type in the search query
pyautogui.write('yt')
time.sleep(2)

# Click on the search result
pyautogui.click(1188, 539, duration=1)
time.sleep(2)
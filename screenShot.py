# Taking screenshot

import pyautogui

def screenShot():
    """
    Taking screenshot
    """
    # Taking screenshot
    myScreenshot = pyautogui.screenshot()
    # Saving file
    myScreenshot.save(r'GoogleMapsRoute.png')
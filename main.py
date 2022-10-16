from selenium.webdriver.common.by import By
import time as t
import browserOpen as bO
import dataInput as dI
import screenShot as sS
from selenium.common.exceptions import NoSuchElementException

# Launching browser
browser = bO.browserOpen()

# Maximize browser window
browser.maximize_window()

# Redirecting to Google Maps page
browser.get(f"https://www.google.com/maps/place/{dI.dataInput()}")
t.sleep(10)

# Clicking "designate the route"
route = browser.find_element(By.CLASS_NAME, 'EgL07d')
route.click()
t.sleep(10)

# Clicking "From your current location"
# if there is not set this option
try:
    your_loc = browser.find_element(By.CLASS_NAME, 'sbsb_c')
    your_loc.click()
    t.sleep(10)
except NoSuchElementException:
    pass

# Taking screenshot and saving
sS.screenShot()


# Launching browser

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def browserOpen():
    """
    Launching Google Chrome browser
    """
    # Launching the Chrome browser
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    return browser

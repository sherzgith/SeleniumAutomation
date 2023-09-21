
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys


# Automation Test steps
print("# Google search manual test cases ( needs to be automated)")
print("# Launch the Chrome browser")

# created the object for chromedriver that talks to Chrome Browser
chr_options = Options()
chr_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chr_options)
# driver = webdriver.Chrome()
print('maximizing the browser window')
driver.maximize_window()
time.sleep(1)

# Sample of different Locators:
driver.get('https://demoqa.com/links')
time.sleep(2)
driver.find_element(By.LINK_TEXT, 'Created').click()
time.sleep(5)
print('clicking the No Content link partial text')
driver.find_element(By.PARTIAL_LINK_TEXT, 'No').click()
time.sleep(5)
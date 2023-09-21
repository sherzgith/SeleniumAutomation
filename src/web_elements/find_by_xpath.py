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

driver.get("https://www.walmart.com/search?q=pc")
all_add_buttons = driver.find_elements(By.XPATH, '//button[@data-automation-id="add-to-cart"]')
all_add_buttons[0].click()
print(all_add_buttons)
print()
time.sleep(10)

driver.get("https://www.walmart.com/search?q=pc")
first_add_button = driver.find_element(By.XPATH, '//div[@data-item-id="2FVFTLL9KIKV"]//button[@data-automation-id="add-to-cart"]').click()
print('first_add-button ***\n', first_add_button)
time.sleep(10)


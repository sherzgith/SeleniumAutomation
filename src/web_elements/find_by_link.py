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

print('Clicking the Created...')
driver.find_element(By.LINK_TEXT, 'Created').click()
# or XPATH with text
# created_xpath = '//a[text()="Created"]'  # '//a[@id="Created"]'
# driver.find_element(By.XPATH, created_xpath.click())
time.sleep(5)

print('clicking the No Content link partial text')
driver.find_element(By.PARTIAL_LINK_TEXT, 'Conte').click()
time.sleep(5)

#  XPATH with text
print('Clicking the Created...')
created_xpath = '//a[text()="Created"]'  # '//a[@id="Created"]'
driver.find_element(By.XPATH, created_xpath.click())
time.sleep(5)

print('Clicking the Bad Request...')
bad_request_xpath = '//a[contains(text(), "Request")]'  # finds 'Bad Request' link
driver.find_element(By.XPATH, bad_request_xpath).click()
time.sleep(5)

print('Clicking the Unauthorized...')
unauthorized_xpath = '//a[contains(@id, "unauthor")]'
driver.find_element(By.XPATH, unauthorized_xpath).click()
time.sleep(5)

# CSS Selector example
all_add_buttons_css = 'button[data-automation-id=add-to-cart'  # vs xpath example below
all_add_id_xpath = '//button[@data-automation-id="add-to-cart"]'

all_add_id_css = 'button#add-to-cart'  # vs xpath example below
all_add_id_xpath = '//button[@id="add-to-cart"]'

all_add_class_css = 'button.add-to-cart'  # vs xpath example below
all_add_class_xpath = '//button[@class="add-to-cart"]'


element_parent_xpath = '//button[@class="add-to-cart"]/..'  # parent element of the button

import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from src.utilities import *

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
driver.implicitly_wait(20)

# Variables
host = "https://demoqa.com/alerts"


driver.get(host)
disable_google_ads(driver)

# promt_button = driver.find_element(By.ID, 'promtButton')
wdwait = WebDriverWait(driver, 10)
promt_button = wdwait.until(EC.presence_of_element_located((By.ID, 'promtButton')))


print("Clicking the promtButton...")
promt_button.click()
time.sleep(1)

print('create an object of alert class')
prompt_alert = driver.switch_to.alert
prompt_alert.send_keys('Sherzod')
prompt_alert.accept()
result_msg = driver.find_element(By.ID, 'promptResult').text
print(f'Checkpoint of the result: {result_msg}')

print("2. Clicking the promtButton...")
promt_button.click()

print('create an object of alert class')
prompt_alert = driver.switch_to.alert
prompt_alert.send_keys('Canceel')
prompt_alert.dismiss()


# Explicit wait
# WebDriverWait, expected_conditions
# result_status = driver.find_element(By.ID, 'promptResult').is_displayed()
# result_status = WebDriverWait(driver, 10).until_not(
#     expected_conditions.presence_of_element_located((By.ID, 'promptResult')))

wdwait = WebDriverWait(driver, 10)
result_status = wdwait.until_not(EC.presence_of_element_located((By.ID, 'promptResult')))



print(f'Checkpoint of the result: {result_status}')

time.sleep(20)








print('closing the tab')
driver.close()

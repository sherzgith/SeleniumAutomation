from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from src.utilities import *

# TEST DATA
host = "https://demoqa.com/droppable"
host2 = "https://jqueryui.com/tooltip/"

timestamp = time.strftime("%Y%m%d-%H%M")
drag_drop_before_screenshot = f"{ROOT_DIR}/reports/screenshots/{timestamp}_drag_drop_before_screenshot.png"
drag_drop_after_screenshot = f"{ROOT_DIR}/reports/screenshots/{timestamp}_drag_drop_after_screenshot.png"
# drag_drop_after_screenshot = ROOT_DIR + '/reports/screenshots/drag_drop_after_screenshot.png'
# hoverover_screenshot = ROOT_DIR + '/reports/screenshots/hoverover_screenshot.png'
hoverover_screenshot = f"{ROOT_DIR}/reports/screenshots/{timestamp}_hoverover_screenshot.png"

# LOCATORS
droppable_xpath = "//div[@id='droppable']"
tooltip_xpath = "//div[contains(@id, 'ui-id-')]/div"

# Automation Test steps :
print("# Mouse Movements - drag and drop action")
print("# Launch the Chrome browser")

# created the object for chromedriver that talks to Chrome Browser
chr_options = Options()
chr_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chr_options)
# driver = webdriver.Chrome()
print('maximizing the browser window')
driver.maximize_window()
driver.implicitly_wait(5)

print("# open the host webpage (default Simple tab)")
driver.get(host)
disable_google_ads(driver)

print("# verify the message in the droppable box 'Drop here'")
before_msg = driver.find_element(By.XPATH, droppable_xpath).text
print(f"Before message: '{before_msg}'")
time.sleep(2)

print('taking the screenshot...')
driver.save_screenshot(drag_drop_before_screenshot)

print("# hold the Drag Me object and drop it to droppable box")
actions = ActionChains(driver)
draggable_elem = driver.find_element(By.ID, 'draggable')
droppable_elem = driver.find_element(By.ID, 'droppable')

print('performing the action ...')
actions.drag_and_drop(draggable_elem, droppable_elem).perform()

print("# verify the message in the droppable box 'Dropped!'")
after_msg = driver.find_element(By.XPATH, droppable_xpath).text
print(f"After message: '{after_msg}'")

print('taking the screenshot...')
driver.save_screenshot(drag_drop_after_screenshot)

print("Scenarios is completed. ")

print("****** hover over scenario started *************************")
driver.get(host2)
disable_google_ads(driver)

print("switching to the frame and finding the age elem")
driver.switch_to.frame(driver.find_element(By.CLASS_NAME, 'demo-frame'))
age_elem = driver.find_element(By.ID, 'age')

print("performing the actions ...")
actions = ActionChains(driver)
actions.move_to_element(age_elem).perform()

print("getting the text of tooltip...")
tooltip_msg = driver.find_element(By.XPATH, tooltip_xpath).text
print(f"Tooltip message: '{tooltip_msg}' .")

print('taking the screenshot...')
driver.save_screenshot(hoverover_screenshot)

print("Closing the browser...")
time.sleep(2)


driver.quit()
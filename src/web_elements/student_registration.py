# Test case
# Enter name, last name, email,
# Enter Mobile, Subjects, current address
# Select Gender: Male (radio buttons)
# Select/Enter DOB
# Select Checkboxes ( multi select)
# picture upload ( input, type=file)
# Select State(first), then select City (Click the visible container)
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

# test data:
host = 'https://demoqa.com/automation-practice-form'
fname = 'john'
lname = 'doe'
email = 'johndoe@email.com'
gender = 'Male'
dob = '01/01/2000'
subjects = 'john doe registry form'
picture_path = '../../data/Lionel-Messi-PNG-Picture.png'
state = 'NCR'
city = 'Delhi'

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
print('clicking the No Content link partial part :conte')
driver.find_element(By.PARTIAL_LINK_TEXT, 'Conte').click()
time.sleep(10)


print("# Open the student registration form.")
driver.get(host)
print("Zoom the page to 55 %")
driver.execute_script("document.body.style.zoom='55%'")

print("# Enter name...")
fname_input = driver.find_element(By.ID, 'firstName')
fname_input.send_keys('djvdkvddklv')
time.sleep(2)
fname_input.clear()
fname_input.send_keys(fname)

print("# Enter last name...")
driver.find_element(By.ID, 'lastName').send_keys(lname)
time.sleep(2)

# or
# lname_input = driver.find_element(By.ID, 'lastName')
# lname_input.send_keys('flglammvdvm')
# time.sleep(2)
# lname_input.clear()
# lname_input.send_keys(lname)
print("# Enter the email...")
driver.find_element(By.ID, 'userEmail').send_keys(email)
time.sleep(5)


# Enter Mobile, Subjects, current address
# Select Gender: Male (radio buttons)
# Select/Enter DOB
# Select Checkboxes ( multi select)
# picture upload ( input, type=file)
# Select State(first), then select City (Click the visible container)
print('*************COMPLETED, Closing the BROWSER!!!!')
driver.close()


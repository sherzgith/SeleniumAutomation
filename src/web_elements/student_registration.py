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
mobile_num = '7024097877'
gender = 'Male'
dob = '01/01/2000'
subjects = 'john doe registry form'
picture_path = '../../data/Lionel-Messi-PNG-Picture.png'
state = 'NCR'
city = 'Delhi'

# LOCATORS:
mobile_xpath = '//input[@id="userNumber"]'
subject_xpath = '//input[@id="subjectsInput"]'
male_xpath = '//input[@id="gender-radio-1"]/..'
# male_xpath = "//label[contains(text(), 'Male')/..]"
female_xpath = "//input[@id='gender-radio-2']/.."
sports_xpath = '//input[@id="hobbies-checkbox-1"]/..'
# sports_css_selector = 'input#hobbies-checkbox-1'
reading_xpath = '//input[@id="hobbies-checkbox-2"]/..'
# reading_css_selector = 'input#hobbies-checkbox-2'
music_xpath = '//input[@id="hobbies-checkbox-3"]/..'
# music_css_selector = 'input#hobbies-checkbox-3'




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
driver.implicitly_wait(10)
# time.sleep(1)


print("# Open the student registration form.")
driver.get(host)
# print("Zoom the page to 55 %")
# driver.execute_script("document.body.style.zoom='55%'")

print("#1 Enter name...")
fname_input = driver.find_element(By.ID, 'firstName')
fname_input.send_keys('djvdkvddklv')
time.sleep(2)
fname_input.clear()
fname_input.send_keys(fname)

print("#2 Enter last name...")
driver.find_element(By.ID, 'lastName').send_keys(lname)
time.sleep(2)

# or
# lname_input = driver.find_element(By.ID, 'lastName')
# lname_input.send_keys('flglammvdvm')
# time.sleep(2)
# lname_input.clear()
# lname_input.send_keys(lname)

print("#3 Enter the email...")
driver.find_element(By.ID, 'userEmail').send_keys(email)
time.sleep(5)

# Enter Mobile, Subjects, current address
print('Entering the mobile number')
driver.find_element(By.XPATH, mobile_xpath).send_keys(mobile_num)
time.sleep(5)
print('Entering the subject ')
driver.find_element(By.XPATH, '//input[@id="subjectsInput"]').send_keys(subjects)


# Select Gender: Male (radio buttons)
elem = driver.find_element(By.XPATH, male_xpath)
elem.click()
# Alternative way of clicking with javascript code executor
# driver.execute_script("arguments[0].click;", elem)


# Select/Enter DOB
print()


# Select Checkboxes ( multi select)
driver.find_element(By.XPATH, sports_xpath).click()
driver.find_element(By.XPATH, reading_xpath).click()
driver.find_element(By.XPATH, music_xpath).click()
time.sleep(5)

# picture upload ( input, type=file)
# Select State(first), then select City (Click the visible container)
print('*************COMPLETED, Closing the BROWSER!!!!')
driver.close()


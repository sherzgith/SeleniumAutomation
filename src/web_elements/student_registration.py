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
from selenium.webdriver.support.select import Select

from src.utilities import *

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
male_box_xpath = '//input[@id="gender-radio-1"]'
male_xpath = f'{male_box_xpath}/..'  # xpath parent element of male_box input element
# male_xpath = "//label[contains(text(), 'Male')/..]"
female_xpath = "//input[@id='gender-radio-2']/.."
sports_box_xpath = '//input[@id="hobbies-checkbox-1"]'
sports_xpath = f'{sports_box_xpath}/..'
# sports_css_selector = 'input#hobbies-checkbox-1'
reading_xpath = '//input[@id="hobbies-checkbox-2"]/..'
# reading_css_selector = 'input#hobbies-checkbox-2'
music_xpath = '//input[@id="hobbies-checkbox-3"]/..'
# music_css_selector = 'input#hobbies-checkbox-3'
month_select_xpath = '//select[@class="react-datepicker__month-select"]'
year_select_xpath = '//select[@class="react-datepicker__year-select"]'

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


print("#1 Open the student registration form.")
driver.get(host)
# print("Zoom the page to 55 %")
# driver.execute_script("document.body.style.zoom='55%'")
disable_google_ads(driver)

print("#2 Enter name...")
fname_input = driver.find_element(By.ID, 'firstName')
fname_input.send_keys('djvdkvddklv')
time.sleep(0.5)
fname_input.clear()
fname_input.send_keys(fname)

print("#3 Enter last name...")
driver.find_element(By.ID, 'lastName').send_keys(lname)
# time.sleep(2)

# or
# lname_input = driver.find_element(By.ID, 'lastName')
# lname_input.send_keys('flglammvdvm')
# time.sleep(2)
# lname_input.clear()
# lname_input.send_keys(lname)

print("#4 Enter the email...")
driver.find_element(By.ID, 'userEmail').send_keys(email)
time.sleep(0.5)

print("#5 Select Gender: Male (radio buttons)")
elem = driver.find_element(By.XPATH, male_xpath)
male_box = driver.find_element(By.XPATH, male_box_xpath)
print(f"Is male gender selected-before: {male_box.is_selected()}")
elem.click()
print(f"Is male gender selected-After: {male_box.is_selected()}")
# Alternative way of clicking with javascript code executor
# driver.execute_script("arguments[0].click;", elem)


print("#6 Enter Mobile, Subjects, current address")
print('Entering the mobile number')
driver.find_element(By.XPATH, mobile_xpath).send_keys(mobile_num)
time.sleep(5)
print('Entering the subject ')
driver.find_element(By.XPATH, '//input[@id="subjectsInput"]').send_keys(subjects)

# Select/Enter DOB
print(" #7 Select/Enter date of birth - drop down list")
print("# Click on Date of Birth")
driver.find_element(By.ID, 'dateOfBirthInput').click()
print("# select month")
select_month = Select(driver.find_element(By.XPATH, month_select_xpath))
select_month.select_by_visible_text('May')
# select_month.select_by_index(4)  # ['January', 'February', 'March', 'April', 'May', 'June' ...]

print("# select year")
select_year = Select(driver.find_element(By.XPATH, year_select_xpath))
select_year.select_by_value('1986')

print("# click on Day = 27")
day = '027'  # always pass 3 digits, with leading zeros if needed
day_xpath = f"//div[contains(@class, 'react-datepicker__day--{day}') and not(contains(@class, 'outside-month'))]"
driver.find_element(By.XPATH, day_xpath).click()

time.sleep(10)

print("#8 Select Hobbies Checkboxes ( multi select)")
sport_checkbox = driver.find_element(By.XPATH, sports_xpath)
sport_input = driver.find_element(By.XPATH, sports_box_xpath)
print('check if selected: before and after checking')
print(f"Is sport selected-before: {sport_input.is_selected()}")
sport_checkbox.click()
print(f"Is sport selected-after: {sport_input.is_selected()}")

driver.find_element(By.XPATH, reading_xpath).click()
driver.find_element(By.XPATH, music_xpath).click()
time.sleep(0.5)

# 9 picture upload ( input, type=file)

# 10 Select State(first), then select City (Click the visible container)


# 11 check if enabled then click Submit, scrolling might be needed
# driver.execute_script("arguments[0].scrollIntoView();", elem)
# driver.execute_script("arguments[0].click;", elem)

print('*************COMPLETED, Closing the BROWSER!!!!')
driver.close()
# driver.quit() # close the browser

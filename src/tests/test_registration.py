# Test case
# Enter name, last name, email,
# Enter Mobile, Subjects, current address
# Select Gender: Male (radio buttons)
# Select/Enter DOB
# Select Checkboxes ( multi select)
# picture upload ( input, type=file)
# Select State(first), then select City (Click the visible container)
import time

import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from src.pages.forms_page import FormsPage
from src.utilities import *
from src.pages.registration_page import *

logfile = f"{ROOT_DIR}/logs/{get_str_day()}_student_registration.log"
log = create_logger(logfile)

config_file = f"{ROOT_DIR}/data/registration.yml"
data = load_yaml_file(config_file)

# test data:
# host = 'https://demoqa.com/automation-practice-form'
# fname = 'john'
# lname = 'doe'
# email = 'johndoe@email.com'
mobile_num = '7024444444'
gender = 'Male'
dob = '01/01/2000'
subjects = 'john doe registry form'
# picture_path = '../../data/Lionel-Messi-PNG-Picture.png'
# picture_path = 'C:\dev\SeleniumAutomation\data\Lionel-Messi-PNG-Picture.png'
picture_path = ROOT_DIR + '\data\Lionel-Messi-PNG-Picture.png'
state = 'NCR'
city = 'Delhi'
birth_day = '027'
birth_month = 'May'
birth_year = '1986'
hobbies_list = ['sports', 'reading']

# print("# Student Registration Form - Automated steps)")
log.info("# Student Registration Form - Automated steps)")
log.info("# Launch the Chrome browser")
log.warning("This was the warning message")
log.error("Test case failed!!!")

@pytest.mark.forms1
def test_form_case1(driver):

    # test data:
    host = data['case1']['host']
    fname = data['case1']['first_name']
    lname = data['case1']['last_name']
    email = data['case1']['email']
    # Automation Test steps
    # mobilenum1 = data['scenario1']['mobilenumber']
    form_page = FormsPage(driver)

    log.info("#1 Open the student registration form.")
    driver.get(host)
    # print("Zoom the page to 55 %")
    # driver.execute_script("document.body.style.zoom='55%'")
    disable_google_ads(driver)

    form_page.enter_name(fname)
    form_page.enter_last_name(lname)
    form_page.enter_email(email)
    form_page.select_gender('male')
    form_page.enter_mobile_number(mobile_num)
    form_page.enter_subject(subjects)
    form_page.set_date_of_birth(birth_day, birth_month, birth_year)
    form_page.select_hobbies(['sports', 'reading'])
    form_page.upload_picture(picture_path)
    form_page.enter_current_address('560 Shell Road, 89119')
    form_page.select_state_city('NCR', 'Delhi')

    form_page.click_submit()
    time.sleep(5)




# def test_scenario2():
#     mobilenum2 = data['scenario2']['mobilenumber']
#     print(mobilenum2)

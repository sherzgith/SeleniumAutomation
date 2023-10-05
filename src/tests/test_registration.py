# Test case
# Enter name, last name, email,
# Enter Mobile, Subjects, current address
# Select Gender: Male (radio buttons)
# Select/Enter DOB
# Select Checkboxes ( multi select)
# picture upload ( input, type=file)
# Select State(first), then select City (Click the visible container)
import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

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
    try:
        # test data:
        host = data['case1']['host']
        fname = data['case1']['first_name']
        lname = data['case1']['last_name']
        email = data['case1']['email']
        # Automation Test steps
        # mobilenum1 = data['scenario1']['mobilenumber']
        registration_page = RegistrationPage(driver)

        log.info("#1 Open the student registration form.")
        driver.get(host)
        # print("Zoom the page to 55 %")
        # driver.execute_script("document.body.style.zoom='55%'")
        disable_google_ads(driver)

        registration_page.enter_name(fname)
        registration_page.enter_last_name(lname)
        registration_page.enter_email(email)
        registration_page.select_gender('male')
        registration_page.enter_mobile_number(mobile_num)
        registration_page.enter_subject(subjects)
        registration_page.set_date_of_birth(birth_day, birth_month, birth_year)
        registration_page.select_hobbies(hobbies_list)
        registration_page.upload_picture(picture_path)

        # 10 Select State(first), then select City (Click the visible container)

        registration_page.submit_form()

    except (NoSuchElementException, TimeoutException) as err:
        log.error(f"Selenium error occured: {err}")
        screenshot = ROOT_DIR + '/reports/screenshots/student_regist_error.png'
        driver.save_screenshot(screenshot)
        log.warning(f"please check the screenshot here: {screenshot}")
    # finally:
    #     log.info('*************COMPLETED, Closing the BROWSER!!!!')
    #     # driver.close()  # close the current tab
    #     driver.quit() # close the browser


# def test_scenario2():
#     mobilenum2 = data['scenario2']['mobilenumber']
#     print(mobilenum2)

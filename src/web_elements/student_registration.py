# Test case
# Enter name, last name, email,
# Enter Mobile, Subjects, current address
# Select Gender: Male (radio buttons)
# Select/Enter DOB
# Select Checkboxes ( multi select)
# picture upload ( input, type=file)
# Select State(first), then select City (Click the visible container)


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

# test data:
host = 'https://demoqa.com/automation-practice-form'
fname = 'john'
lname = 'doe'
email = 'johndoe@email.com'
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

# # LOCATORS:
# mobile_xpath = '//input[@id="userNumber"]'
# subject_xpath = '//input[@id="subjectsInput"]'
# male_box_xpath = '//input[@id="gender-radio-1"]'
# male_xpath = f'{male_box_xpath}/..'  # xpath parent element of male_box input element
# # male_xpath = "//label[contains(text(), 'Male')/..]"
# female_xpath = "//input[@id='gender-radio-2']/.."
# sports_box_xpath = '//input[@id="hobbies-checkbox-1"]'
# sports_xpath = f'{sports_box_xpath}/..'
# # sports_css_selector = 'input#hobbies-checkbox-1'
# reading_xpath = '//input[@id="hobbies-checkbox-2"]/..'
# # reading_css_selector = 'input#hobbies-checkbox-2'
# music_xpath = '//input[@id="hobbies-checkbox-3"]/..'
# # music_css_selector = 'input#hobbies-checkbox-3'
# month_select_xpath = '//select[@class="react-datepicker__month-select"]'
# year_select_xpath = '//select[@class="react-datepicker__year-select"]'
# # Element : <input id="uploadPicture" type="file" lang="en" class="form-control-file">
# upload_picture_xpath = '//input[@id="uploadPicture"]'
# submit_xpath = '//button[@id="submit"]'

# print("# Student Registration Form - Automated steps)")
log.info("# Student Registration Form - Automated steps)")
log.info("# Launch the Chrome browser")
log.warning("This was the warning message")
log.error("Test case failed!!!")


# created the object for chromedriver that talks to Chrome Browser
chr_options = Options()
chr_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chr_options)
# driver = webdriver.Chrome()
log.info('maximizing the browser window')
# driver.maximize_window()
driver.implicitly_wait(10)
# time.sleep(1)
try:
    # Automation Test steps
    wdwait = WebDriverWait(driver, 15)
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
    screenshot = ROOT_DIR+'/reports/screenshots/student_regist_error.png'
    driver.save_screenshot(screenshot)
    log.warning(f"please check the screenshot here: {screenshot}")
finally:
    log.info('*************COMPLETED, Closing the BROWSER!!!!')
    # driver.close()  # close the current tab
    driver.quit() # close the browser


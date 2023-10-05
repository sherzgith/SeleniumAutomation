from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from src.pages.base_page import BasePage
from src.utilities import *

logfile = f"{ROOT_DIR}/logs/{get_str_day()}.log"
log = create_logger(logfile)


class FormsPage(BasePage):
    """ Page Object Model of forms page, defines all attributes and methods of the page(Building blocks).
    """

    # LOCATORS(Attributes)

    mobile_xpath = '//input[@id="userNumber"]'
    subject_xpath = '//input[@id="subjectsInput"]'
    male_box_xpath = '//input[@id="gender-radio-1"]'
    male_xpath = f'{male_box_xpath}/..'  # xpath parent element of male_box input element
    # male_xpath = "//label[contains(text(), 'Male')/..]"
    female_box_xpath = '//input[@id="gender-radio-2"]'
    female_xpath = f'{female_box_xpath}/..'
    gender_other_xpath = '//input[@id="gender-radio-3"]/..'
    sports_box_xpath = '//input[@id="hobbies-checkbox-1"]'
    sports_xpath = f'{sports_box_xpath}/..'
    # sports_css_selector = 'input#hobbies-checkbox-1'
    reading_xpath = '//input[@id="hobbies-checkbox-2"]/..'
    # reading_css_selector = 'input#hobbies-checkbox-2'
    music_xpath = '//input[@id="hobbies-checkbox-3"]/..'
    # music_css_selector = 'input#hobbies-checkbox-3'
    month_select_xpath = '//select[@class="react-datepicker__month-select"]'
    year_select_xpath = '//select[@class="react-datepicker__year-select"]'
    # Element : <input id="uploadPicture" type="file" lang"en" class="form-control-file">
    upload_picture_xpath = '//input[@id="uploadPicture"]'
    address_textarea = 'currentAddress'
    state_input = 'react-select-3-input'
    city_list = 'city'
    city_input = 'react-select-4-input'
    confirmation_msg = 'example-modal-sizes-title-lg'
    close_cm_button = 'closeLargeModal'
    submit_button = 'submit'

    # methods
    def enter_name(self, first_name):
        log.info("#2 Enter name...")
        self.enter_text_by_id('firstName', first_name)

    def enter_last_name(self, last_name):
        log.info("#3 Enter last name...")
        self.enter_text_by_id('lastName', last_name)

    def enter_email(self, email):
        log.info("#4 Enter the email...")
        self.enter_text_by_id('userEmail', email)
        time.sleep(0.5)

    def select_gender(self, gender: str):
        log.info("Selecting the gender...")
        if gender.lower() == 'male':
            log.info("#5 Select Gender: Male (radio)")
            self.click_element_by_xpath(self.male_xpath)
        elif gender.lower() == 'female':
            log.info("#5 Select Gender: Female (radio)")
            self.click_element_by_xpath(self.female_xpath)

        elif gender.lower() == 'other':
            log.info("#5 Select Gender: Other (radio)")
            self.click_element_by_xpath(self.gender_other_xpath)

        else:
            log.error("Incorrect option was given!! No gender selected")

    def enter_mobile_number(self, mobile_number):
        log.info('Entering the mobile number')
        self.enter_text_by_xpath(self.mobile_xpath, mobile_number)

    def set_date_of_birth(self, day: str, month: str, year: str):
        log.info(" #7 Select/Enter date of birth - drop down list")
        log.info("# Click on Date of Birth")
        self.click_element_by_id('dateOfBirthInput')

        log.info("# select month")
        select_month = Select(self.driver.find_element(By.XPATH, self.month_select_xpath))
        select_month.select_by_visible_text(month.title())
        # select_month.select_by_index(4)  # ['January', 'February', 'March', 'April', 'May', 'June' ...]

        log.info("# select year")
        select_year = Select(self.driver.find_element(By.XPATH, self.year_select_xpath))
        select_year.select_by_value(year)

        log.info(f"# click on Day = {day}")
        day_xpath = f"//div[contains(@class, 'react-datepicker__day--{day}') and not(contains(@class, 'outside-month'))]"
        self.click_element_by_xpath(day_xpath)

    def enter_subject(self, subject):
        log.info('Entering the subject ')
        self.enter_text_by_xpath(self.subject_xpath, subject)

    def select_hobbies(self, hobbies: list):
        for hobby in hobbies:
            if hobby.lower() == 'sports':
                self.click_element_by_xpath(self.sports_xpath)
            elif hobby.lower() == 'reading':
                self.click_element_by_xpath(self.reading_xpath)
            elif hobby.lower() == 'music':
                self.click_element_by_xpath(self.music_xpath)

            else:
                log.error("No hobbies entered, hobbies selection was not made.")

    def enter_current_address(self, address):
        log.info('Entering the address... ')
        self.enter_text_by_id(self.address_textarea, address)

    def select_state_city(self, state, city):
        log.info('Is City list is enabled before selecting state?',
                 self.driver.find_element(By.ID, self.city_list).is_selected())
        log.info('Is State list is enabled before selecting state?',
                 self.driver.find_element(By.ID, self.state_list).is_selected())

        self.enter_text_by_id(self.state_input, ('NCR' + Keys.TAB))
        log.info("state is entered.")
        time.sleep(2)
        log.info('Is City list is enabled after selecting state?',
                 self.driver.find_element(By.ID, self.city_list).is_enabled())
        self.enter_text_by_id(self.city_input, ('Delhi' + Keys.TAB))
        log.info("city is entered")

    def upload_picture(self, file_path):
        log.info("# 9 picture upload ( input, type=file)")
        log.info(f"File absolute path: '{file_path}'")
        select_picture = self.driver.find_element(By.XPATH, self.upload_picture_xpath)
        select_picture.send_keys(file_path)

    def click_submit(self):
        self.click_element_by_id(self.submit_button)

    def close_confirmation_page(self):
        log.info("Is Confirmation message displayed?", self.driver.find_element(By.ID, self.confirmation_msg))
        self.click_element_by_id(self.close_cm_button)

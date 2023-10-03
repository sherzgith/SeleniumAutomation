from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.utilities import *

logfile = f"{ROOT_DIR}/logs/{get_str_day()}.log"
log = create_logger(logfile)


class BasePage:
    """Abstract class that defines shared browser and all necessary/mostly used selenium methods.
    """

    def __init__(self, driver):
        self.driver = driver
        self.wdwait = WebDriverWait(driver, 15)


    # enter text
    def enter_text_by_id(self, locator_id, text_to_enter):
        try:
            log.info('Entering the text by ID..')
            # element = self.driver.find_element(By.ID, locator_id)
            element = self.wdwait.until(EC.presence_of_element_located((By.ID, locator_id)))
            element.clear()
            element.send_keys(text_to_enter)
        except (NoSuchElementException, TimeoutException) as err:
            log.error(f"Selenium error occured: {err}")
            screenshot = ROOT_DIR + '/reports/screenshots/enter_text_by_id_error.png'
            self.driver.save_screenshot(screenshot)
            log.warning(f"please check the screenshot here: {screenshot}")

    def enter_text_by_xpath(self, xpath, text_to_enter):
        try:
            log.info('Entering the text by XPATH..')
            element = self.wdwait.until(EC.presence_of_element_located((By.XPATH, xpath)))
            element.clear()
            element.send_keys(text_to_enter)
        except (NoSuchElementException, TimeoutException) as err:
            log.error(f"Selenium error occurred: {err}")
            screenshot = ROOT_DIR + '/reports/screenshots/enter_text_by_xpath_error.png'
            self.driver.save_screenshot(screenshot)
            log.warning(f"please check the screenshot here: {screenshot}")


    # click element

    def click_element_by_xpath(self, xpath):
        try:
            log.info('Clicking the element by XPATH..')
            element = self.wdwait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            element.click()
        except (NoSuchElementException, TimeoutException) as err:
            log.error(f"Selenium error occurred: {err}")
            screenshot = ROOT_DIR + '/reports/screenshots/click_element_by_xpath_error.png'
            self.driver.save_screenshot(screenshot)
            log.warning(f"please check the screenshot here: {screenshot}")

    def click_element_by_id(self, locator_id):
        try:
            log.info('Clicking the element by ID..')
            element = self.wdwait.until(EC.element_to_be_clickable((By.XPATH, locator_id)))
            element.click()
        except (NoSuchElementException, TimeoutException) as err:
            log.error(f"Selenium error occurred: {err}")
            screenshot = ROOT_DIR + '/reports/screenshots/click_element_by_id_error.png'
            self.driver.save_screenshot(screenshot)
            log.warning(f"please check the screenshot here: {screenshot}")

    # get text
    def get_text_by_xpath(self, xpath):
        try:
            log.info('Getting the text by XPATH..')
            element = self.wdwait.until(EC.presence_of_element_located((By.XPATH, xpath)))
            return element.text
        except (NoSuchElementException, TimeoutException) as err:
            log.error(f"Selenium error occurred: {err}")
            screenshot = ROOT_DIR + '/reports/screenshots/click_element_by_xpath_error.png'
            self.driver.save_screenshot(screenshot)
            log.warning(f"please check the screenshot here: {screenshot}")

    def get_text_by_id(self, locator_id):
        try:
            log.info('Getting the text by ID..')
            element = self.wdwait.until(EC.presence_of_element_located((By.XPATH, locator_id)))
            return element.text
        except (NoSuchElementException, TimeoutException) as err:
            log.error(f"Selenium error occurred: {err}")
            screenshot = ROOT_DIR + '/reports/screenshots/click_element_by_id_error.png'
            self.driver.save_screenshot(screenshot)
            log.warning(f"please check the screenshot here: {screenshot}")
# This is a shared fixture modules
import time

import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from src.pages.base_page import *


@pytest.fixture(scope='module')
def driver():
    print("-\n---------------------SetUp-------------------")
    print('Initializing a webdriver for the browser...')
    # created the object for chromedriver that talks to Chrome Browser
    chr_options = Options()
    chr_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chr_options)
    # driver = webdriver.Chrome()
    log.info('maximizing the browser window')
    driver.maximize_window()
    driver.implicitly_wait(10)
    time.sleep(0)

    yield driver
    print("\n-------------------TearDown-------------------")
    log.info('*************TEST COMPLETED, Closing the BROWSER!!!!')
    # driver.close()  # close the current tab
    driver.quit()  # close the browser
    print("fixture steps are completed here.")

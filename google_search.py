import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Variable
host = 'https://www.google.com/'
keyword = input('Enter the keyword to search:')

# Test Steps start here
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

print("# Open the google.com page")
driver.get(host)
# time.sleep(1)dsc

print("# search for 'ai' and hit enter")
# identifier used to search that element from HTML document
search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys(keyword)
search_box.send_keys(Keys.ENTER)

print("# save the search result")
search_result = driver.find_element(By.ID,'result-stats' )
print(f'Search result of ai : {search_result.text}')
# Sample : About 23,080,000,000 results (0.51 seconds)

print("# close the browser")
driver.close()  # closes the tab

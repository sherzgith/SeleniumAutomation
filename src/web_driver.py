import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

# test data:
host = 'https://demoqa.com/browser-windows'
temp_host = 'https://demoqa.com/automation-practice-form'


# created the object for chromedriver that talks to Chrome Browser
chr_options = Options()
chr_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chr_options)
# driver = webdriver.Chrome()
print('maximizing the browser window')
driver.maximize_window()
driver.implicitly_wait(10)


print("# open the host, name (name of the browser)")
driver.get(host)
print(f'url of host: {driver.current_url}')
print(f'WebDriver name: {driver.name}')
print("# open the tamp_host")
driver.get(temp_host)
print(f'url of temp host: {driver.current_url}')
time.sleep(2)
print("# back to original host")
driver.back()
time.sleep(2)
print(f'url of host: {driver.current_url}')
print("# forward to temp_host")
driver.forward()
time.sleep(2)
print(f'url of temp host: {driver.current_url}')
print("# back to original host then refresh")
driver.back()
driver.refresh()
time.sleep(2)
print(f'url of host: {driver.current_url}')
print("# get current_url, title")
first_url = driver.current_url
print(f'Title: {driver.title}\nFirst Page URL: {first_url}')
time.sleep(5)
print('-------------------------------------------------')
print("# get current_window_handle and save in a variable")
print("# click on New Tab button, this will open new tab")
print("# get window_handles")
print("# switch to new tab")
print("# get the current_url and title")
print("# verify that url is different from first url")
print("# close the tab with driver.close()")
print("# switch to main tab")
print("# get current_url and verify that it is the same as first url")
print("# close the whole browser (all tabs) -> driver.quit()")




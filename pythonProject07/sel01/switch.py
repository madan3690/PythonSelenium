from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver=webdriver.Chrome()
driver.get("https://www.amazon.in")
driver.maximize_window()
print(driver.title)

# driver.get("https://www.walmart.ca")
time.sleep(5)

driver.execute_script("window.open('https://www.fb.com','new_window')")
print(driver.title)
time.sleep(5)

driver.switch_to.window(driver.window_handles[1])
print(driver.title)
driver.switch_to.window(driver.window_handles[0])
print(driver.title)
driver.switch_to.new_window()
time.sleep(5)
driver.get("https://www.netflix.com")
print(driver.title)
driver.switch_to.window(driver.window_handles[1])
print(driver.title)
driver.switch_to.window(driver.window_handles[0])
print(driver.title)
driver.get_screenshot_as_png()
driver.close()
time.sleep(5)
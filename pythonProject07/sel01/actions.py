import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.amazon.ca")
driver.maximize_window()
actions=ActionChains(driver)
e=driver.find_element(By.XPATH,"//*[text()='Amazon Cash']")
actions.move_to_element(e).perform()
time.sleep(5)
actions.click(e).perform()
time.sleep(5)
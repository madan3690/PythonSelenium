import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



driver=webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://www.amazon.in")
driver.maximize_window()

element=WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH,"//*[text()='Gift Cards']")))
print(element.text)
driver.find_element(By.XPATH,"//*[text()='Gift Cards']").click()
time.sleep(20)

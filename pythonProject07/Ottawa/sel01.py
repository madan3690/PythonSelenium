import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver=webdriver.Chrome()
driver.get("https://www.amazon.in")
driver.maximize_window()

driver.find_element(By.XPATH,'//*[@id="twotabsearchtextbox"]').send_keys("Madan",Keys.ENTER)
time.sleep(2)
driver.switch_to.new_window()
time.sleep(2)
driver.get("https://www.netflix.com")
driver.save_screenshot("\\Screenshots")
time.sleep(2)
driver.switch_to.window(driver.window_handles[0])
driver.switch_to.frame(0)
driver.switch_to.default_content()
time.sleep(2)
driver.close()
time.sleep(2)
driver.quit()



import time
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome()
driver.get("http://www.dummypoint.com/Frame.html")
driver.switch_to.frame("f1")
driver.find_element(By.XPATH,"//button[text()='Promt Alert']").click()
time.sleep(3)
driver.switch_to.alert.accept()
actual = driver.find_element(By.XPATH,"//p[@id='demo']")
print(actual.text)
if actual.text == "Hello DummyPoint.com! This is the text from promt alert":
    print("text matches")
else:
    print("Text doesnot match")
driver.switch_to.default_content()
driver.switch_to.frame("f2")
driver.find_element(By.XPATH,"//button[text()='Promt Alert']").click()
time.sleep(5)

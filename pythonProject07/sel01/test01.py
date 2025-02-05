from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By


serv_obj=Service("C:/Drivers/chromedriver-win64/chromedriver.exe")

# driver = webdriver.Chrome(service=serv_obj)
driver = webdriver.Chrome()

driver.get("https://www.fb.com/")

driver.find_element(By.NAME,"email").send_keys("Madan")
driver.find_element(By.NAME,"login").click()

act_title=driver.title
print(act_title)
exp_title="Log into Facebook"

if act_title==exp_title:
    print("hooray")
else:
    print("halleluyah")


# driver.close()

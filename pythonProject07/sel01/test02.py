from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.fb.com")
# driver.maximize_window()
# driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("Madan")
# driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("Mohan")
# driver.find_element(By.CSS_SELECTOR,"input[data-testid=royal_email]").send_keys("Seetha")
# driver.find_element(By.CSS_SELECTOR,"input#email[data-testid=royal_email]").send_keys("2.0")
# driver.find_element(By.CSS_SELECTOR,"input.inputtext[data-testid=royal_pass]").send_keys("2.0")

driver.maximize_window()
driver.find_element(By.CSS_SELECTOR,"#email").send_keys("Madan")
driver.find_element(By.CSS_SELECTOR,".inputtext").send_keys("Mohan")
driver.find_element(By.CSS_SELECTOR,"[data-testid=royal_email]").send_keys("Seetha")
driver.find_element(By.CSS_SELECTOR,"#email[data-testid=royal_email]").send_keys("2.0")
driver.find_element(By.CSS_SELECTOR,".inputtext[data-testid=royal_pass]").send_keys("2.0")

text_msg=driver.find_element(By.XPATH,"//*[@id='u_0_5_hx']").text
print(text_msg)
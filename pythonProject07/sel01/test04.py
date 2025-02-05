from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



driver=webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://www.amazon.ca")

EC.presence_of_element_located(By.XPATH,"//*[text()='Deals Store']")
t=driver.find_element(By.XPATH,"//*[text()='Deals Store']/preceding-sibling::a[text()='New Releases']").text
print(t)
q=driver.find_element(By.XPATH,"//*[text()='Deals Store']/following-sibling::a[text()='Home']").text
print(q)
r=driver.find_elements(By.XPATH,"//*[text()='Deals Store']/parent::div/child::a")
print(len(r))
for i in r:
    print(i.text)
# print(r[3].text)


# //*[@id="nav-xshop"]/a[3]
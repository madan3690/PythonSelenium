import time

from selenium import webdriver
import openpyxl
from selenium.webdriver.common.by import By


def test_new_01():
    driver=webdriver.Chrome()
    driver.get("https://www.amazon.ca")
    driver.get("https://www.netflix.ca")
    driver.back()
    element=driver.find_element(By.XPATH,"//*[text()='Deals Store']")
    print()
    time.sleep(5)
    driver.forward()
    time.sleep(5)
    driver.refresh()
    time.sleep(5)
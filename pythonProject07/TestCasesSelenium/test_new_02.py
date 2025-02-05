import time

from selenium import webdriver
import openpyxl
from selenium.webdriver.common.by import By


def test_new_01():
    driver=webdriver.Chrome()
    driver.get("https://www.amazon.ca")
    driver.maximize_window()

    element=driver.find_element(By.XPATH,"//*[text()='Deals Store']")
    # print("\n")
    # print(element.is_displayed())
    #
    # time.sleep(5)
    # print(element.is_enabled())
    # time.sleep(5)
    # print("selected or what")
    # print(element.is_selected())
    # time.sleep(5)
    print("\n")
    print(element.text)
    elements=driver.find_elements(By.XPATH,"//*[text()='Deals Store']/parent::div/child::a")
    print(elements[0].text)
    print(len(elements))
    for ele in elements:
        print(ele.text)

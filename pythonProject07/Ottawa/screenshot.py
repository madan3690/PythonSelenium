import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver=webdriver.Chrome()
driver.get("https://www.amazon.in")
driver.maximize_window()
driver.save_screenshot("testtf01.png")


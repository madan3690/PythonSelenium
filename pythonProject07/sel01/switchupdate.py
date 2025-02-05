import time

from selenium import webdriver

try:
    driver = webdriver.Chrome()
    driver.get("https://www.netflix.ca")
    print(driver.title)
    driver.switch_to.new_window()
    driver.get("https://www.youtube.ca")
    print(driver.title)
    driver.switch_to.window(driver.window_handles[0])
    print(driver.title)
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    print(driver.title)
    time.sleep(1)
    driver.switch_to.frame(1)
    driver.switch_to.default_content()
    # driver.close()
    time.sleep(1)
    driver.switch_to.alert

    driver.switch_to.default_content()

except Exception as e:

    print("Exception hogaya "+str(e))
    print(e)



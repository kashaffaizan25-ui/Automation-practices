
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.google.com")
driver.find_element(By.ID,"L2AGLb").click()
time.sleep(10)
# driver.get("http://www.youtube.com")
# time.sleep(3)
# driver.back()
# time.sleep(3)
# driver.forward()
# time.sleep(3)
# driver.refresh()
# time.sleep(3)
# driver.quit()


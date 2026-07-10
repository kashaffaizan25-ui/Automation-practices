# from  selenium import webdriver
# import time
#
# from selenium.webdriver.common.by import By
#
# abc = webdriver.Chrome()
#
# abc.maximize_window()
# time.sleep(3)
# abc.get("http://www.facebook.com")
# time.sleep(4)
# abc.find_element(By.CLASS_NAME,"x1lliihq x6ikm8r x10wlt62 x1n2onr6 xlyipyv xuxw1ft").click()
# time.sleep(4)
# Email = abc.find_element (By.ID ,"_r_3_")
# time.sleep(4)
# Email.send_keys("kashaffaroox2@gmail.com")

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.saucedemo.com")
time.sleep(4)

username = driver.find_element(By.ID, "user-name")
password = driver .find_element( By .XPATH , "//input[@id = 'password']")
username.send_keys("kashaf@gmail.com")
password .send_keys("1223567")
time.sleep(6)










from selenium import webdriver
import time
from selenium.webdriver.common.by import By
abc = webdriver.Chrome()
abc.get("http://www.saucedemo.com")
abc.maximize_window()
username = abc.find_element (By.CSS_SELECTOR,"input")
username.send_keys("standard_user")
time.sleep(2)
password = abc.find_element(By.CSS_SELECTOR,"#password")
password.send_keys("secret_sauce")
time.sleep(2)
#login = abc.find_element(By.CSS_SELECTOR,".btn_action")
# when we have more btn or same name
# login = abc.find_element(By.CSS_SELECTOR,"input.btn_action")
login = abc.find_element(By.CSS_SELECTOR,"form > input[name='login-button']")
login.click()
time.sleep(5)


from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# for chrome size maximum
driver.maximize_window()
# mention the website link
driver.get("http://www.saucedemo.com")
# fir time
time.sleep(2)
# xpath locaters
#use relative xpath which is easy to find element , find by name
username = driver.find_element(By.XPATH,"//input[@name ='user-name']")
username.send_keys("standard_user")
time.sleep(2)
# find by id
password = driver .find_element( By .XPATH , "//input[@id = 'password']")
password .send_keys("secret_sauce")
time.sleep(2)
login = driver.find_element(By.XPATH,"//input[@id = 'login-button']")
login.click()
time.sleep(2)
# find by name to add to card
card = driver.find_element(By.XPATH, "//button[@name = 'add-to-cart-sauce-labs-bike-light']")
card.click()
time.sleep(2)
# fnd by text
product_name = driver.find_element(By .XPATH,"//div[text() = 'Sauce Labs Bolt T-Shirt']")
product_name.click()
time.sleep(2)
# for back the screen
driver.back()
# find element by partically text ( we also find by id , name and etc)
product = driver .find_element(By.XPATH , "//div[contains(text(),'Backpack')]")
product.click()
time.sleep(2)

driver.back()
# find element by using ( or method)
product_Sauce = driver.find_element(By.XPATH,"//div [text() = 'Sauce Labs Onesie' or text() = 'abc']")
product_Sauce.click()
time.sleep(2)

driver.back()
#find element by  using (and method)
all_product = driver.find_element(By.XPATH,"//div[text()= 'Test.allTheThings() T-Shirt (Red)' and"
                                           " @class = 'inventory_item_name ']")
all_product.click()
time.sleep(2)

driver.back()
# find link by using (link_ text)
link_product = driver.find_element(By.LINK_TEXT,"Sauce Labs Bike Light")
link_product.click()
time.sleep(2)

driver.back()
partial_name = driver.find_element(By.PARTIAL_LINK_TEXT,"Backpack")
partial_name.click()
time.sleep(3)











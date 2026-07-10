from selenium import webdriver
import time
from selenium.webdriver.common.by import By

car = webdriver.Chrome()
car.maximize_window()
car.get("https://dmytro-ch21.github.io/html/web-elements.html")

bmw_radio = car.find_element(By.ID,"radio2")
bmw_radio.click()
print ("option bmw is select:",bmw_radio.is_selected())

other_radio = car.find_element(By.ID,"radio5")
other_radio.click()
print ("option bmw is select:",other_radio.is_selected())

time.sleep(4)


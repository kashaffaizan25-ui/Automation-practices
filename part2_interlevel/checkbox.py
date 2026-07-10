from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# for chrome size maximum
driver.maximize_window()
# mention the website link
driver.get("https://dmytro-ch21.github.io/html/web-elements.html")

#fetch window title and print
print("window title:" ,driver.title)

 #
print ("url:" ,driver.current_url)

# check the box by simple method
# option_ford= driver.find_element(By.ID,"option1")
# if not option_ford.is_selected():
#     option_ford.click()
# option_bmw= driver.find_element(By.ID,"option2")
# if not option_bmw.is_selected():
#     option_bmw.click()

# checkbox by xpath:
option_car = driver.find_elements(By.XPATH,"//input [@type='checkbox']")
for option_car in option_car:
    option_car.click()

# print ("option bmw is select:",option_bmw.is_selected())
# print ("option ford is select:",option_ford.is_selected())

# fir time
time.sleep(5)



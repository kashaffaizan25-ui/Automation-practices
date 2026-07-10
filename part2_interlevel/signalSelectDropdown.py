from selenium import webdriver
import  time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

car = webdriver.Chrome()
car.maximize_window()
car.get("https://dmytro-ch21.github.io/html/web-elements.html")

dropdown = Select(car.find_element(By.ID,"carBrands"))

# Select options by visible text, value, and index
dropdown.select_by_visible_text("Mercedes")
print("Selected option:", dropdown.first_selected_option.text)


time.sleep(2)

dropdown.select_by_value("audi")
print("Selected option:", dropdown.first_selected_option.text)

time.sleep(2)

dropdown.select_by_index(1)  # Index starts from 0
print("Selected option:", dropdown.first_selected_option.text)


time.sleep(3)

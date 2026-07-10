
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
sauce = webdriver.Chrome()
sauce.maximize_window()
sauce.get("http://www.google.com")



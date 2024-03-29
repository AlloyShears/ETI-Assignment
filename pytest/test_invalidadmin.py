from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest
import time

driver = webdriver.Chrome()
driver.get("http://localhost:8000/admin/login/?next=/admin/")
elem = driver.find_element_by_name("username")
elem.send_keys("Kirby")

elem = driver.find_element_by_name("password")
elem.send_keys("Kirbyisthebest")
elem.send_keys(Keys.RETURN) #press enter key
time.sleep(2)

assert driver.current_url == 'http://localhost:8000/admin/login/?next=/admin/'


driver.close()
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest
import time

driver = webdriver.Chrome()
driver.get("http://localhost:8000/projects/")

elem = driver.find_element_by_name("/projects/1/")
elem.send_keys(Keys.RETURN) #press enter key
time.sleep(2)
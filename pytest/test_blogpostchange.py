from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest
import time

driver = webdriver.Chrome()
driver.get("http://localhost:8000/admin/login/?next=/admin/")
elem = driver.find_element_by_name("username")
elem.send_keys("aloys")

elem = driver.find_element_by_name("password")
elem.send_keys("10K88g00")
elem.send_keys(Keys.RETURN) #press enter key
time.sleep(2)


driver.get("http://localhost:8000/admin/blog/post/2/change/")
elem = driver.find_element_by_name("title")
elem.send_keys("Python is fun")

elem = driver.find_element_by_name("body")
elem.send_keys("Description of python test")
time.sleep(2)

from selenium.webdriver.support.ui import Select

elem = Select(driver.find_element_by_name("categories"))
elem.select_by_value('2')

elem = driver.find_element_by_name("_save") 
elem.click()

driver.get("http://localhost:8000/blog/")
assert len(driver.find_elements_by_id("blogs")) == original_blog_count + 1


driver.close()
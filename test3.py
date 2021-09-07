from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
file = open("path.txt")
PATH = file.read()

driver = webdriver.Chrome(PATH)
driver.get('https://unigen.herokuapp.com')

manual_button = driver.find_elements_by_class_name(
    "nav-link")[1].click()

driver.find_element_by_id(
    "input_taskID").send_keys("1234")

driver.find_element_by_id(
    "input_ba").send_keys("Some Person")

driver.find_element_by_id(
    "input_dev").send_keys("Francisco Salinas")

driver.find_element_by_id(
    "input_qa").send_keys("Selenium")

open_editor = driver.find_elements_by_class_name(
    "btn-alt")[0].click()

time.sleep(1)

driver.find_elements_by_class_name(
    "btn-default")[1].click()

driver.find_elements_by_tag_name(
    "textarea")[0].send_keys("This is an autofilled requirement.")

driver.find_elements_by_tag_name(
    "textarea")[1].send_keys("This is an autofilled test case.")

driver.find_elements_by_class_name(
    "btn-alt")[1].click()

driver.find_elements_by_class_name(
    "btn-default")[0].click()
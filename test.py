import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

file = open("path.txt")
PATH = file.read()
driver = webdriver.Chrome(PATH)
driver.get('http://localhost:8888/arrow-dash/play.html')

start_button = driver.find_element_by_id("start").click()

time = driver.find_element_by_id("time").text

global_page = driver.find_element_by_tag_name("body")

arrow_array = [Keys.ARROW_LEFT, Keys.ARROW_UP,
               Keys.ARROW_RIGHT, Keys.ARROW_DOWN]

while int(time) > 0:
    current_arrow = (re.search(
        "[0-3].*?", driver.find_elements_by_tag_name('img')[-1].get_attribute("src")))[0]
    global_page.send_keys(arrow_array[int(current_arrow)])

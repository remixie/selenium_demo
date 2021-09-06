from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
file = open("path.txt")
PATH = file.read()

print(PATH)
driver = webdriver.Chrome(PATH)
driver.get('https://forms.gle/1xKE9t5Mr75adPDDA')
time.sleep(0.5)

text_box = driver.find_elements_by_class_name(
    "quantumWizTextinputPaperinputInput")
text_box[0].send_keys("42")

scale_selection = driver.find_elements_by_class_name(
    "appsMaterialWizToggleRadiogroupOffRadio")[4].click()

radio_selection = driver.find_elements_by_class_name(
    "appsMaterialWizTogglePapercheckboxCheckbox")[0].click()

text_box[1].send_keys("Nope. I am Selenium.")

submit = driver.find_elements_by_class_name(
    "appsMaterialWizButtonPaperbuttonContent")[0].click()

from selenium import webdriver
import time
import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

# "return arguments[0].scrollIntoView(true);"

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/execute_script.html"
browser.get(link)
subx = browser.find_element_by_id("input_value")
x = calc(int(subx.text))
answer = browser.find_element_by_id("answer")
browser.execute_script("return arguments[0].scrollIntoView(true);", answer)
answer.send_keys(x)
robot_checkbox = browser.find_element_by_id("robotCheckbox")
browser.execute_script("return arguments[0].scrollIntoView(true);", robot_checkbox)
robot_checkbox.click()
robot_radio = browser.find_element_by_id("robotsRule")
browser.execute_script("return arguments[0].scrollIntoView(true);", robot_radio)
robot_radio.click()
button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()
time.sleep(10)
browser.quit()

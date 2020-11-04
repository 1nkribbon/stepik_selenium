import math
import time
from selenium import webdriver

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

try:
	link = "http://suninjuly.github.io/math.html"
	browser = webdriver.Chrome()
	browser.get(link)
	x_element = browser.find_element_by_id("input_value")
	x = x_element.text
	y = calc(x)
	answer_input = browser.find_element_by_id("answer")
	answer_input.send_keys(y)
	robo_check = browser.find_element_by_css_selector("[for='robotCheckbox']")
	robo_check.click()
	robo_rule = browser.find_element_by_css_selector("[for='robotsRule']")
	robo_rule.click()
	button = browser.find_element_by_css_selector("button.btn")
	button.click()
finally:
	time.sleep(10)
	browser.quit()

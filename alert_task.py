import time
import math
from selenium import webdriver

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

browser = webdriver.Chrome()

try:
	browser.get(link)
	first_button = browser.find_element_by_css_selector(".btn-primary")
	first_button.click()

	confirm1 = browser.switch_to.alert
	confirm1.accept()

	x = browser.find_element_by_id("input_value")
	answer = calc(int(x.text))
	answer_input = browser.find_element_by_id("answer")
	answer_input.send_keys(answer)

	button = browser.find_element_by_css_selector(".btn-primary")
	button.click()
finally:
	time.sleep(10)
	browser.quit()

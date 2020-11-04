import os
import time
from selenium import webdriver

link = "http://suninjuly.github.io/file_input.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)
	input_form = browser.find_elements_by_css_selector(".form-control")
	for element in input_form:
		element.send_keys("qwerty")
	file_input = browser.find_element_by_id("file")
	current_dir = os.path.abspath(os.path.dirname(__file__))
	file_path = os.path.join(current_dir, 'file.txt')
	file_input.send_keys(file_path)
	button = browser.find_element_by_css_selector(".btn-primary")
	button.click()
finally:
	time.sleep(10)
	browser.quit()

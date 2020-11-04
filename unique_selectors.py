from selenium import webdriver
import time

try:
	link = "http://suninjuly.github.io/registration1.html"
	browser = webdriver.Chrome()
	browser.get(link)
	input1 = browser.find_elements_by_tag_name("[required='']")
	for element in input1:
	    element.send_keys("awe")
	button = browser.find_element_by_css_selector("button.btn")
	button.click()
	time.sleep(1)
	welcome_text_elt = browser.find_element_by_tag_name("h1")
	welcome_text = welcome_text_elt.text
	assert "Congratulations! You have successfully registered!" == welcome_text
	
finally:
	time.sleep(5)
	browser.quit()

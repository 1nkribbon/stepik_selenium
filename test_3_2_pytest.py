from selenium import webdriver
def test_registration1():
	try:
		link = "http://suninjuly.github.io/registration1.html"
		browser = webdriver.Chrome()
		browser.get(link)
		input1 = browser.find_element_by_css_selector("[placeholder='Input your first name']")
		input2 = browser.find_element_by_css_selector("[placeholder='Input your last name']")
		input3 = browser.find_element_by_css_selector("[placeholder='Input your email']")
		input1.send_keys("form")
		input2.send_keys("form")
		input3.send_keys("form")
		button = browser.find_element_by_css_selector("button.btn")
		button.click()
		browser.implicitly_wait(5)
		welcome_text_elt = browser.find_element_by_tag_name("h1")
		welcome_text = welcome_text_elt.text
		assert "Congrat" in welcome_text
	finally:
		browser.quit()

def test_registration2():
	try:
		link = "http://suninjuly.github.io/registration2.html"
		browser = webdriver.Chrome()
		browser.get(link)
		input1 = browser.find_element_by_css_selector("[placeholder='Input your first name']")
		input2 = browser.find_element_by_css_selector("[placeholder='Input your last name']")
		input3 = browser.find_element_by_css_selector("[placeholder='Input your email']")
		input1.send_keys("form")
		input2.send_keys("form")
		input3.send_keys("form")
		button = browser.find_element_by_css_selector("button.btn")
		button.click()
		browser.implicitly_wait(5)
		welcome_text_elt = browser.find_element_by_tag_name("h1")
		welcome_text = welcome_text_elt.text
		assert "Congrat" in welcome_text
	finally:
		browser.quit()

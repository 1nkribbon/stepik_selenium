from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

#select = Select(browser.find_element_by_tag_name("select"))

link = "http://suninjuly.github.io/selects1.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)
	num1 = browser.find_element_by_id("num1")
	num2 = browser.find_element_by_id("num2")
	sumx = int(num1.text) + int(num2.text)
	select = Select(browser.find_element_by_tag_name("select"))
	select.select_by_value(str(sumx))
	button = browser.find_element_by_css_selector(".btn")
	button.click()
finally:
	time.sleep(10)
	browser.quit()

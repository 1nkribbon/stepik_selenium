import time
from selenium import webdriver

try:
	browser = webdriver.Chrome()
	browser.implicitly_wait(5)
	browser.get("http://suninjuly.github.io/cats.html")
	browser.find_element_by_id("button")
finally:
	time.sleep(10)
	browser.quit()

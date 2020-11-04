import time
import math
from selenium import webdriver

link = "http://suninjuly.github.io/get_attribute.html"

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

try:
	browser = webdriver.Chrome()
	browser.get(link)
	chest = browser.find_element_by_tag_name("img")
	chest_value = chest.get_attribute("valuex")
	x = calc(chest_value)
#	funcx = math.log1p(math.fabs(12*math.sin(int(chest_value))))
	answerx = browser.find_element_by_id("answer")
	answerx.send_keys(x)
	checkboxx = browser.find_element_by_id("robotCheckbox")
	checkboxx.click()
	radiobuttonx = browser.find_element_by_id("robotsRule")
	radiobuttonx.click()
	submitx = browser.find_element_by_css_selector(".btn-default")
	submitx.click()
finally:
	time.sleep(10)
	browser.quit()

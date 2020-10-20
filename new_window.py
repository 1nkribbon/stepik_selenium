# browser.switch_to.window(window_name) # переход на вкладку window_name
# new_window = browser.window_handles[1] # выбор вкладки [0:]. Здесь вторая вкладка
import time
import math
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)

	troll_button = browser.find_element_by_css_selector(".trollface")
	browser.execute_script("return arguments[0].scrollIntoView(true);", troll_button)
	troll_button.click()

	redirected = browser.window_handles[1]
	browser.switch_to.window(redirected)

	x = browser.find_element_by_id("input_value")
	answer = calc(int(x.text))

	answer_input = browser.find_element_by_id("answer")
	answer_input.send_keys(answer)

	submit_button = browser.find_element_by_css_selector(".btn")
	submit_button.click()
finally:
	time.sleep(10)
	browser.quit()

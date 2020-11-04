import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

try:
	browser.get("http://suninjuly.github.io/explicit_wait2.html")

	book_button = browser.find_element(By.ID, "book")
	browser.execute_script("return arguments[0].scrollIntoView(true);", book_button)
	price = WebDriverWait(browser, 12).until(
		EC.text_to_be_present_in_element((By.ID, "price"), "$100")
		)
	book_button.click()
	
	x = browser.find_element(By.ID, "input_value")
	answer = calc(int(x.text))
	answer_input = browser.find_element(By.ID, "answer")
	browser.execute_script("return arguments[0].scrollIntoView(true);", answer_input)
	answer_input.send_keys(answer)

	submit_button = browser.find_element(By.ID, "solve")
	browser.execute_script("return arguments[0].scrollIntoView(true);", submit_button)
	submit_button.click()
finally:
	time.sleep(10)
	browser.quit()
import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def browser():
	print("\nstart browser..")
	options = webdriver.ChromeOptions()
	options.add_experimental_option("excludeSwitches", ["enable-logging"])
	browser = webdriver.Chrome(options=options)
	yield browser
	print("\nquit browser..")
	browser.quit()

@pytest.mark.parametrize(
	"lesson", ["895", "896", "897", "898", "899", "903", "904", "905"])
def test_alien(browser, lesson):
	link = f"https://stepik.org/lesson/236{lesson}/step/1"
	browser.get(link)
	answer = math.log(int(time.time()))
	input_text = WebDriverWait(browser, 5).until(
		EC.presence_of_element_located((
			By.CSS_SELECTOR, "[placeholder='Напишите ваш ответ здесь...")))
	input_text.send_keys(str(answer))
	submit_btn = browser.find_element_by_css_selector(
		".submit-submission")
	submit_btn.click()
	alien_answer = WebDriverWait(browser, 5).until(
		EC.presence_of_element_located((
			By.CSS_SELECTOR, ".smart-hints__hint")))
	assert alien_answer.text == "Correct!", alien_answer.text

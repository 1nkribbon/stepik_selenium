import time
from selenium import webdriver

browser = webdriver.Chrome()

browser.execute_script("alert('Hello');")
time.sleep(5)
alert = browser.switch_to.alert
alert_text = alert.text
print(alert_text)
alert.accept()

browser.execute_script("confirm('Are you ready?');")
time.sleep(5)
confirm = browser.switch_to.alert
confirm_text = confirm.text
print(confirm_text)
confirm.accept()

browser.execute_script("prompt('password');")
time.sleep(5)
prompt = browser.switch_to.alert
prompt.send_keys("12345")
time.sleep(3)
prompt.accept()

time.sleep(10)
browser.quit()

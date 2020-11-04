from selenium import webdriver
import time

link = "http://selenium1py.pythonanywhere.com/"


class TestMainPage1():

    @classmethod
    def setup_class(self):
        print("\nstart browser for test suite 1 ..")
        time.sleep(5)
        self.browser = webdriver.Chrome()

    @classmethod
    def teardown_class(self):
        print("quit browser for test suite 1 ..")
        time.sleep(5)
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        print('start test link 1')
        time.sleep(5)
        self.browser.get(link)
        self.browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        print('start test basket 1')
        time.sleep(5)
        self.browser.get(link)
        self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")


class TestMainPage2():

    def setup_method(self):
        print("start browser for test 2..")
        time.sleep(5)
        self.browser = webdriver.Chrome()

    def teardown_method(self):
        print("quit browser for test 2..")
        time.sleep(5)
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        print('start test link 2')
        time.sleep(5)
        self.browser.get(link)
        self.browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        print('start test basket 2')
        time.sleep(5)
        self.browser.get(link)
        self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")
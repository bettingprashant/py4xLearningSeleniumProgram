import allure
from selenium import webdriver
import time
import pytest
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common import window
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestSelenium:

    def __init__(self):
        self.driver = None
    def open_browser(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument("--incognito")
        self.driver = webdriver.Chrome(self.chrome_options)
        self.driver.get("https://selectorshub.com/xpath-practice-page/")
        self.driver.maximize_window()
    @allure.title("JS")
    @allure.description("Verify JS")
    def test_js(self):
        title = self.driver.execute_script("return document.title") # This Title finding from the JS
    # driver.current_url  #webdriver finding the url via the API request.
        current_url = self.driver.execute_script("return document.URL")

        print(current_url)
        print(title)

        assert current_url == "https://selectorshub.com/xpath-practice-page/"
    def close_browser(self):
        time.sleep(3)
        self.driver.quit()

if __name__ == "__main__":
    test = TestSelenium()
    test.open_browser()
    test.test_js()
    test.close_browser()
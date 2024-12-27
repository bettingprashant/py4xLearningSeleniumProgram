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


@allure.title("JS")
@allure.description("Verify JS")
def test_verify_windows():

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://selectorshub.com/xpath-practice-page/")
    driver.maximize_window()
    title = driver.execute_script("return document.title") # This Title finding from the JS
    # driver.current_url  #webdriver finding the url via the API request.

    current_url = driver.execute_script("return document.URL")

    print(current_url)
    print(title)





    time.sleep(5)
    driver.quit()
import allure
from selenium import webdriver
import time
import pytest


from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

@allure.title("Exception Handle")
@allure.description("Verify Exception Handle")
def test_exception_handle():
    driver = webdriver.Chrome()
    driver.get("https://google.com")
    driver.maximize_window()

    try:

        textarea = driver.find_element(By.NAME,"q")
        driver.refresh()
        textarea.send_keys("The Testing Academy")
    except StaleElementReferenceException as see:
        print(see)
        print("stale element")


    time.sleep(5)
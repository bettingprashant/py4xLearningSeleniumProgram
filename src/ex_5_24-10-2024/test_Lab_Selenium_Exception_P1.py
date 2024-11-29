import allure
from selenium import webdriver
import time
import pytest


from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

@allure.title("Exception Handle")
@allure.description("Verify Exception Handle")
def test_exception_handle():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    driver.maximize_window()
    try:
        element = driver.find_element(By.ID,"this_id_doesnt_exist")
    except NoSuchElementException as nse:
        print(nse.msg)



    time.sleep(5)
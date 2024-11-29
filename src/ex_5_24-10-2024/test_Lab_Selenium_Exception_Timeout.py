import allure
from selenium import webdriver
import time
import pytest


from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

@allure.title("Timeout")
@allure.description("Verify Timeout")
def test_exception_handle():
    driver = webdriver.Chrome()
    driver.get("https://google.com")
    driver.get("https://google.com")

    # driver.maximize_window()

    try:
        WebDriverWait(driver=driver, timeout=10).until(EC.element_to_be_clickable(By.ID,"submit"))
        print("End of the Program")
    except TimeoutException as te:
        print(te)
        print("TimeoutException Occured !!, 10 Seconds Passed")
    finally:
        driver.quit()


    time.sleep(5)
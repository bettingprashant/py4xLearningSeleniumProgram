import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

from selenium.webdriver.common.by import By

@allure.title("Positive Testcase - App.vwo.com Signup Button Verification.")
@allure.description("Verify that Free Trial button is clicked, Navigated to next page")
def test_negative_vwo_free_trial_project3():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")

    anchor_tag_element = driver.find_element(By.PARTIAL_LINK_TEXT,"free trial")
    anchor_tag_element.click()
    assert driver.current_url == "https://vwo.com/free-trial/?utm_medium=website&utm_source=login-page&utm_campaign=mof_eg_loginpage"
    time.sleep(5)
    driver.quit()
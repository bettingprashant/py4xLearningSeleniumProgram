import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

from selenium.webdriver.common.by import By

@pytest.mark.negative
@allure.title("Negative Testcase - App.vwo.com - wrong Email, Password -> Error Message")
@allure.description("Verify that if email/pass is wrong, we will get a message")
def test_negative_vwo_login_project2():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    email_web_element = driver.find_element(By.ID,"login-username")
    email_web_element.send_keys("abc@gmail.com")

    password_web_element = driver.find_element(By.NAME,"password")
    password_web_element.send_keys("1234")

    submit_btn_web_element = driver.find_element(By.ID, "js-login-btn")
    submit_btn_web_element.click()
    time.sleep(3)

    error_message_web_element = driver.find_element(By.CLASS_NAME,"notification-box-description")
    print(error_message_web_element.text)
    assert error_message_web_element.text == "Your email, password, IP address or location did not match"
    time.sleep(5)
    driver.quit()
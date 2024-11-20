import allure
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.title("App.vwo.com- Explicit Wait")
@allure.description("Verify that App.vwo.com- Explicit Wait")
def test_5():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    email_web_element = driver.find_element(By.ID,"login-username")
    email_web_element.send_keys("abc@gmail.com")

    password_web_element = driver.find_element(By.NAME,"password")
    password_web_element.send_keys("1234")

    submit_btn_web_element = driver.find_element(By.ID, "js-login-btn")
    submit_btn_web_element.click()

    WebDriverWait(driver=driver, timeout=5).until(EC.visibility_of_element_located((By.CLASS_NAME,"notification-box-description")))

    error_message_web_element = driver.find_element(By.CLASS_NAME,"notification-box-description")
    print(error_message_web_element.text)
    assert error_message_web_element.text == "Your email, password, IP address or location did not match"
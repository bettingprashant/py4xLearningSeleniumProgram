import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

from selenium.webdriver.common.by import By

@allure.title("Registration Form")
@allure.description("Verify that New User should be created")
def test_user_registration():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/ui/index.php?route=account/register")
    first_name = driver.find_element(By.XPATH,"//input[@id='input-firstname']")
    first_name.send_keys("Prashant")
    last_name = driver.find_element(By.XPATH,"//input[@id='input-lastname']")
    last_name.send_keys("Raj")
    email_id = driver.find_element(By.XPATH,"//input[@id='input-email']")
    email_id.send_keys("pra@yopmail.com")
    telephone_no = driver.find_element(By.XPATH,"//input[@id='input-telephone']")
    telephone_no.send_keys("9876543210")
    password = driver.find_element(By.XPATH, "//input[@id='input-password']")
    password.send_keys("pass@1234")
    confirm_pass = driver.find_element(By.XPATH, "//input[@id='input-confirm']")
    confirm_pass.send_keys("pass@1234")
    privacy_policy = driver.find_element(By.XPATH,"//input[@type='checkbox']")
    privacy_policy.click()
    submit_button = driver.find_element(By.XPATH,"//input[@type='submit']")
    submit_button.click()
    # assert driver.current_url == "https://awesomeqa.com/ui/index.php?route=account/register"

    time.sleep(5)
